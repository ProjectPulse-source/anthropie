# Wikidata — recensions *Lectures* : items créés le 2026-08-15 (dossier reconstruit le 2026-09-02)

> ✅ **FAIT le 2026-08-15 (01h53 Paris), exécuté par Laura** — QuickStatements, même lot
> que le livre `Q141072263` (*La Société du premier coup*). **Ce dossier n'existait pas** :
> la trace a été reconstruite le 2026-09-02 à partir de l'historique et des données de
> l'API (`readback_api_2026-09-02.txt`). Rien à exécuter ici. Aucun reste côté Wikidata.

## Ce qui a été créé

| Item | Œuvre (`data/works.yaml`) | DOI | Date de publication |
|---|---|---|---|
| **Q141072264** | `art-lectures-kaba-2026-04` — recension de *La main et l'esprit* (Arnaud Kaba) | `10.4000/162F0` | 2026-04-14 |
| **Q141072265** | `art-lectures-ridde-2026-05` — recension de *La financiarisation de la santé au Sénégal* (Valéry Ridde) | `10.4000/16IHM` | 2026-07-03 |

Structure identique sur les deux items, conforme au modèle RFSE (`Q140892752`) :
labels et descriptions fr/en, `P31` Q637866 (compte rendu), `P50` Q138909233, `P407` Q150,
`P1433` **Q28587733** (*Lectures*, ISSN 2116-5289, OpenEdition), `P577`, `P356`, `P953`
(texte intégral OpenEdition), `P1476` (titre). Aucun doublon : la recherche
`haswbstatement:P356=<DOI>` ne renvoie que ces deux items.

## Ce que le 02/09 a corrigé — l'écriture en retour

`data/works.yaml` déclarait encore ces deux entrées **sans QID** dix-huit jours après la
création (le 16/08, la même classe de défaut avait été corrigée pour le livre seul). Une
session du 02/09 a d'abord proposé de **créer** les items en se fiant au registre ; la
vérification à la source (recherche par DOI) a montré qu'ils existaient. C'est exactement
la classe décrite en tête du `README.md` de ce dossier : le registre n'est pas la source.

Écriture en retour faite le 02/09 : `wikidata:` posé sur les deux entrées de `works.yaml`
(v1.15). **Bout de chaîne, exclusion déclarée** : les fiches `content/publications/*.md`
ne portent pas de `wikidata_qid` et aucun gabarit ne l'émettrait (`schema-itemlist.html`
n'ajoute que `identifier` depuis `doi_zenodo`) ; pour les articles, la chaîne s'arrête donc
au registre. Faire porter un `sameAs` par item de l'`ItemList` `/publications/` est un
point ouvert nommé, non traité.

## Optionnel, non fait

`P50` et `P356` sont **sans référence** sur ces deux items (le modèle RFSE en portait une :
`S854` URL + `S813` date). Un item de compte rendu porteur de son DOI se source lui-même ;
ajouter les références est possible en une ligne QuickStatements par item, sans urgence.
