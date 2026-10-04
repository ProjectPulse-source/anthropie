# Wikidata — passe complète du 4 octobre 2026 (un seul Run)

> ⏳ **PRÉPARÉ le 2026-10-04** (demande de l'auteur : « passe complète sur Wikidata »). Page transmise à Laura :
> https://claude.ai/artifact/Hcu1uLhcGy4B2hrpzr8yqb (privée : à partager depuis son menu ; lien et lot de la page
> vérifiés identiques, à l'octet, à `deeplink.txt` et `batch_quickstatements.txt`). Bloc ✅ à poser après exécution
> et relecture à l'API.
> Remplace le lien du dossier `Import_Wikidata_Laura_2026-10-04_Dette_P1104` (son contenu est le bloc 1 ci-dessous).

Lien direct : `deeplink.txt` (37 lignes, décodé et comparé ligne à ligne au lot). Détail lisible :
`batch_quickstatements.txt`. Lecture des deux items modifiés avant le geste : `lecture_api_2026-10-04_avant.json`
(Q138910896 révision 2539728601, P1104 = +224 ; Q140517745 révision 2546908838, P1104 = +694).

## Ce que fait le lot

| Bloc | Item | Geste | Preuve |
|---|---|---|---|
| 1 | *Dette Publique : Qui paie vraiment ?* Q138910896 | P1104 224 → **225** | amazon.fr (2958634736) le 04/10, PDF imprimé de 225 p. ; site corrigé (`448bab8`) |
| 2 | *Livresque des mots* Q140517745 | P1104 694 → **680** | amazon.fr (2958634701) le 04/10 : édition 2026 révisée ; registre v1.22 (`3b77474`) |
| 3 | *Un président peut-il tenir ses promesses ?* | **création** (livre) : titre, sous-titre, auteur, essai, sujet (président de la République française), français, France, 22/09/2026, ISBN, 286 p., ASIN, site | amazon.fr (2958634787) le 04/10 : 286 p., 22 septembre 2026, ISBN 978-2958634780 ; site corrigé à 286 (`5edab4d`) ; aucun item ne porte l'ISBN (témoin : l'ISBN de *Dette publique* retrouve Q138910896) |
| 4 | « Variable d'ajustement de la République ? », *Revue Projet* n° 412 | **création** (article) : titre Crossref, revue Q3407167, juin 2026, n° 412, p. 78-81, DOI, auteur, texte en ligne | Crossref `10.3917/pro.412.0078` (type journal-article) ; aucun item ne porte ce DOI (témoin : DOI RFSE → Q140892752) |

Choix déclarés : l'article est un `article` (Q191067), non un `article scientifique` — la *Revue Projet* est une
revue de réflexion, pas une revue à comité de lecture ; le titre est celui de Crossref (la revue en ligne affiche
« Commune » en rubrique, l'auteur écrit « La commune, variable d'ajustement de la République ? »).

## Ce qui n'entre pas — et pourquoi

| Œuvres | Décision | Motif |
|---|---|---|
| 5 articles acceptés, 4 en évaluation | **pas encore** | non publiés : ils entreront à la parution, avec leur DOI |
| 2 billets du blog Mediapart | **non** | autopublication |
| 13 articles de presse et de revues en ligne sans DOI (*En attendant Nadeau*, *Nonfiction*, *La Vie des idées*, *Terrestres*, *Le Temps*, *Alternatives économiques*, *La Grande Conversation*) | **non, recommandé** | la navette n'a créé jusqu'ici que des articles à DOI ; treize notices d'un même auteur en un lot liraient comme de l'autopromotion, au risque d'une suppression qui coûterait plus de crédibilité que le gain |
| Ressources du site (dossier dette, collectivités, enseignants, pouvoirs du président, registre des coûts déportés, méthode du corpus Livresque) | **non** | Wikidata rattache des **œuvres**, jamais les pages d'un site (règle du README de la navette) |
| Jeux de données du dossier dette (JSON, CSV) | **pas en l'état** | éligibles seulement déposés avec un DOI (Zenodo, comme les AWP) ; décision d'auteur |

## Après exécution

1. Relire à l'API (`wbgetentities`) les deux items modifiés et les deux items créés ; poser le JSON ici
   (`readback_api_<date>.json`) : un seul P1104 par livre (+225, +680) ; les créations avec toutes leurs déclarations.
2. Écriture en retour : `wikidata:` des deux nouvelles œuvres dans `data/works.yaml` (`book-promesses-2027`,
   `art-projet-municipales-2026-06`) et `wikidata_qid` sur leurs fiches ; `check-wikidata-registre.py` et
   `check-fiches-registre.py` à 0 ; bloc ✅ (QID, révisions, sortie des deux scripts).
