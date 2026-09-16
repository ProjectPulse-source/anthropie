# Wikidata — recension RFSE (Lemoine, *Chasseurs d'États*) : DOI propre et lien mort

> ⏳ **PRÊT À ENVOYER le 16/09. Envoi à Laura : geste auteur.** Aucune écriture faite : ce bloc devient
> ✅ + readback API après exécution, jamais « fait » sans relecture.

## Pourquoi

Cairn a restructuré le numéro RFSE 2026/1 (n° 36). Il n'y a plus de page « Comptes rendus d'ouvrages » :
`-page-247` affiche « Page non trouvée », le sommaire liste 7 comptes rendus `247a` à `247g`, chacun
avec son DOI. Vérifié le 16/09 :

| Source | Constat |
|---|---|
| Crossref | `10.3917/rfse.036.0247` = bloc, 7 recenseurs · `…0247a`-`…0247g` = les 7 recensions · `…0247d` = « Benjamin Lemoine, Chasseurs d'États… », Stéphane Lalut, p. 247d-265d · `…0247h` → 404 |
| Cairn (navigateur) | page `-page-247d` : `citation_doi` `10.3917/rfse.036.0247d`, « Par Stéphane Lalut », pages 247d à 265d |
| Wikidata (API) | `haswbstatement:P356=10.3917/RFSE.036.0247D` → **0 item** ; témoin `P356=10.3917/RFSE.036.0247` → Q140892752 (la recherche répond) |

⚠ Le résolveur DOI de Cairn (`v4.reseaucairn.info`) répondait 503 pour les deux DOI le 16/09, y
compris en navigateur : panne côté éditeur, sans effet sur ce lot.

## Ce que fait le lot — `batch_quickstatements.txt` (lien direct : `deeplink.txt`)

**Q141072266** — la recension seule (P31 compte rendu, P50 Stéphane Lalut) :

| Geste | Propriété | Valeur |
|---|---|---|
| ajout | P356 DOI | `10.3917/RFSE.036.0247D` (majuscules, forme stockée par Wikidata), réf. page 247d + date de consultation |
| ajout | P304 pages | `247d-265d`, même référence |
| ajout | P433 numéro | `36` (comme le bloc) |
| ajout | P361 partie de | Q140892752 (le bloc) |
| **retrait** | P953 texte intégral | `…-page-247` (page morte) |
| ajout | P953 texte intégral | `…-page-247d` |

**Q140892752** — le bloc : **retrait** de P953 `…-page-247` (page morte). Le DOI commun reste (il
existe toujours chez Crossref), ainsi que ses références datées du 05/08.

## Après exécution — readback et écriture en retour

1. Relire les deux items à l'API (`wbgetentities`, pas la page HTML) et poser le JSON dans ce dossier
   (`readback_api_<date>.json`).
2. Vérifier : `haswbstatement:P356=10.3917/RFSE.036.0247D` → Q141072266.
3. Côté site, rien à changer dans le registre (déjà `doi_review` et `wikidata_review`) ; relancer
   `python scripts/check-wikidata-registre.py` et `python scripts/check-fiches-registre.py` à 0.
