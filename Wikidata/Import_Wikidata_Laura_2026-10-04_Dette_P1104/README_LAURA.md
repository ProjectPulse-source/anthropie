# Wikidata, *Dette Publique : Qui paie vraiment ?* (Q138910896) : nombre de pages

> ⏳ **PRÉPARÉ le 2026-10-04**, sur demande de l'auteur (« corrige Wikidata »). Bloc ✅ à poser après exécution
> et relecture à l'API.

Une correction sur l'item du livre, sans création d'item.

## Pourquoi

| Propriété | Sur Wikidata (lecture API du 04/10) | Valeur juste | Preuve |
|---|---|---|---|
| P1104 nombre de pages | 224 (sans référence) | **225** | fiche amazon.fr du broché (https://www.amazon.fr/dp/2958634736), « Nombre de pages de l'édition imprimée : 225 pages », lue le 04/10/2026 ; PDF imprimé de 225 pages |

Le 224 venait du registre du site (`data/works.yaml`, renseigné le 30/05/2026), faux depuis l'origine ; le site
est corrigé (commit `448bab8`, en ligne le 04/10). La lecture de l'item avant modification est dans ce dossier :
`lecture_api_2026-10-04_avant.json` (un seul P1104, `+224`, sans référence ni qualificatif : le retrait ne perd
rien).

## Le geste

Lien direct : `deeplink.txt`. Il retire 224 et pose 225, avec la page amazon.fr en référence (S854) et la date de
consultation (S813, 04/10/2026). Détail lisible : `batch_quickstatements.txt`.

## Après exécution : relecture et écriture en retour

1. Relire l'item à l'API (`wbgetentities`, pas la page HTML), poser le JSON ici (`readback_api_<date>.json`) :
   un seul P1104, `+225`, avec sa référence.
2. Côté site, rien à changer : `data/works.yaml` et la fiche portent déjà 225. Relancer
   `python scripts/check-wikidata-registre.py` et `python scripts/check-fiches-registre.py` à 0, puis ouvrir ce
   fichier sur un bloc ✅ (QID, révision, sortie des deux scripts).
