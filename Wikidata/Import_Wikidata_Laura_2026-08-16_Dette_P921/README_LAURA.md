# Wikidata — navette du 2026-08-16 (1 commande, un seul Run)

> ✅ **FAIT le 2026-08-16**, exécuté par Laura le jour même. **Readback API** :
> `Q138910896` → `P921` porte désormais **3 valeurs** — `Q138827949` (anthropie),
> `Q3024789` (dette de l'État, générique) et **`Q3024794`** (dette publique de la
> France), toutes trois au rang normal ; **12 propriétés au total** sur l'item,
> donc **aucun effet de bord**. Aucun reste sur ce dossier.

Laura — une seule ligne à exécuter.

## Ce qu'on ajoute, et pourquoi

L'item du livre *Dette Publique : Qui paie vraiment ?* (**Q138910896**) déclarait
son sujet principal (`P921`) comme *anthropie* + **`Q3024789`** — « dette de
l'État », l'item **générique, tous pays confondus**.

Il lui manquait le nœud **précis** : **`Q3024794`, « dette publique de la
France »** — celui qui porte les liens vers les articles Wikipédia (fr, de),
l'identifiant Google Knowledge Graph, et vers lequel converge toute résolution
d'entité quand quelqu'un — ou un modèle — interroge la dette publique française.

| | |
|---|---|
| Item à enrichir | **Q138910896** (*Dette Publique : Qui paie vraiment ?*) |
| Propriété | **P921** (sujet principal) |
| Valeur à ajouter | **Q3024794** (dette publique de la France) |
| Valeurs déjà présentes, à conserver | Q138827949 (anthropie), Q3024789 (générique) |

## Comment faire — UN CLIC

1. Ouvrir le lien du fichier **`deeplink.txt`** : il charge la commande dans
   QuickStatements.
2. Vérifier d'être connectée, puis **Run**.

Repli si le lien ne s'ouvre pas — coller ce bloc dans QuickStatements (format V1,
séparateur tabulation) :

```
Q138910896	P921	Q3024794
```

## Surface jumelle, le même jour

La page [`/cout-de-la-dette-publique/`](https://stephane-lalut.com/cout-de-la-dette-publique/)
a commencé à émettre un JSON-LD `Dataset` (compilation INSEE/Eurostat sous
licence CC BY 4.0) dont le champ `about` pointe **le même `Q3024794`**. Les deux
surfaces désignent donc le même nœud : c'était l'objet du geste.

## Périmètre — ce qu'on ne fait PAS, et pourquoi

Wikidata **n'est pas un annuaire de liens**. On rattache les **œuvres** (le livre,
via son sujet), jamais les pages du site :

- ajouter `stephane-lalut.com` en `P973` sur un item de sujet comme `Q3024794`
  serait de l'auto-référencement — révoqué, et à juste titre : la source des
  chiffres est l'INSEE, pas nous ;
- ajouter un lien externe à l'article Wikipédia depuis le site lui-même relève du
  conflit d'intérêts ;
- **créer un item Wikidata pour le jeu de données : écarté** — notoriété
  contestable, et un item de plus à maintenir pour un retour nul.
