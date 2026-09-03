# Wikidata — navette du 2026-09-03 (UNE ligne, un seul Run) : l'identifiant Goodreads sur l'item auteur

Laura — rien à créer, rien à corriger : on **ajoute une déclaration** sur
`Q138909233` (Stéphane Lalut), qui en porte déjà 17.

| Item | Propriété | Valeur | Référence |
|---|---|---|---|
| **Q138909233** | `P2963` — Goodreads author ID | `23088054` | https://www.goodreads.com/author/show/23088054.St_phane_Lalut · consulté 2026-09-03 |

## Comment faire — UN CLIC

1. Ouvrir le lien du fichier **`deeplink.txt`** : il charge la commande dans
   QuickStatements (connectée à ton compte).
2. **Vérifier le preview** : une seule ligne, un **ajout de déclaration `P2963`**
   avec sa référence. Si l'outil annonce autre chose — une modification d'une
   déclaration existante, ou plus d'une ligne — ne pas lancer et me le dire.
3. **Run**, puis me confirmer.

Repli si le lien ne s'ouvre pas — coller `batch_quickstatements.txt` en mode
Import V1, en retirant les lignes `//`.

## Pourquoi maintenant

Open Library a posé le 1ᵉʳ septembre trois identifiants sur la fiche auteur
`OL16378291A` : `wikidata`, `viaf`, `goodreads`. Les deux premiers avaient déjà
leur réciproque sur Wikidata (`P648` et `P214`) ; **le troisième n'en a pas**.
Depuis le 01/09, Open Library déclare donc un lien vers Goodreads que Wikidata
ne confirme pas. Cette ligne referme l'arc.

Vérifié à la source le 03/09 avant d'écrire le lot :

- `Special:EntityData/Q138909233.json` → 17 propriétés, **`P2963` absente**.
- `https://www.goodreads.com/author/show/23088054` → HTTP 200 après redirection
  vers le slug canonique `23088054.St_phane_Lalut`, titre
  « Stéphane Lalut (Author of L'odyssée des idées) ». L'identifiant résout bien
  sur la bonne personne.
- `openlibrary.org/authors/OL16378291A.json` → `remote_ids.goodreads = "23088054"`,
  révision 4.

Forme de la référence identique aux navettes précédentes (`S854` = URL consultée,
`S813` = date de consultation), comme pour les `P648` corrigés le 26/08.

## Ce qui reste ouvert sur ce graphe, et qui n'est PAS dans ce lot

- **`P268` (BnF)** : toujours impossible — les notices BnF de *La Société du premier
  coup* et de la nouvelle édition de l'*Odyssée* n'existent pas encore. Rien à poser
  tant que le dépôt légal n'a pas produit les notices.
- **`P8383` (Goodreads work ID)** sur les items livres : possible, non fait ici. Il
  faudrait relever un identifiant d'œuvre par livre sur Goodreads (les identifiants
  visibles sur la page auteur sont des identifiants d'**édition**, pas d'œuvre).
  À noter au passage : la page auteur montre **deux** entrées « La Société du premier
  coup » et **deux** « L'Odyssée des idées » — la fusion des éditions côté Goodreads
  est incomplète, à traiter là-bas avant d'en tirer un identifiant vers Wikidata.

Merci !
