# Fusion Wikidata — dédoublonnage « Livresque des mots » (2026-07-16)

Laura — petit correctif suite à ton import du 09/07. En vérifiant l'item que tu
as créé (**Q140517745**, impeccable, merci !), j'ai découvert qu'il existait
**déjà** un item pour ce livre : **Q138911600** « Livresque des Mots ». Tu ne
l'as pas vu parce qu'il portait un « M » majuscule et un libellé différent — il
ne remontait pas à ta recherche. Il faut donc **fusionner les deux**.

> ⚠️ Une fusion **ne se fait pas** avec QuickStatements. Elle se fait avec l'outil
> **`Special:MergeItems`** (ou le gadget « Merge » présent dans le menu *Plus* de
> chaque item). C'est très rapide (2 min) une fois la pré-étape faite.

## Les deux items

| | **Q140517745** (à GARDER) | **Q138911600** (à fusionner dedans) |
|---|---|---|
| Libellé FR | Livresque des **mots** ✅ | Livresque des **Mots** (majuscule) |
| Description | anthologie éclectique… (2022 ; 3e éd. 2026) ✅ | « 4 680 citations, 1 380 auteurs » ❌ chiffres périmés |
| ISBN | ✅ | ✅ |
| ASIN / OpenLibrary / pages / sous-titre | ✅ tout | ❌ aucun |

→ On garde **Q140517745** comme item survivant (canonique), et **Q138911600**
devient une simple redirection vers lui.

> Note : d'habitude sur Wikidata on fusionne « vers le plus petit numéro ». Ici
> on fait **volontairement l'inverse**, parce que Q140517745 est le plus complet
> et le plus correct (libellé, description, identifiants). C'est assumé — si un
> message d'avertissement de l'outil le signale, tu peux passer outre.

## Étape 1 — Pré-requis (sinon la fusion échoue)

Les deux items ont des **descriptions différentes** en FR et en EN : l'outil de
fusion **refuse** de fusionner tant que ce conflit existe. Il faut donc d'abord
**vider les descriptions de Q138911600** (l'item qui va disparaître) :

1. Ouvrir **https://www.wikidata.org/wiki/Q138911600**
2. Cliquer le crayon ✏️ à côté de la **description française** → tout effacer →
   *publier*.
3. Idem pour la **description anglaise** (bascule la langue si besoin) → effacer →
   *publier*.

*(Les libellés, eux, n'ont pas besoin d'être touchés : la fusion transforme
automatiquement « Livresque des Mots » en alias sur l'item survivant.)*

## Étape 2 — Fusionner

Ouvrir ce lien (les deux cases sont déjà pré-remplies) :

**https://www.wikidata.org/wiki/Special:MergeItems?fromid=Q138911600&toid=Q140517745**

- **Item à fusionner (from)** : `Q138911600`
- **Item cible / survivant (to)** : `Q140517745`
- Cliquer **Merge / Fusionner**.

*(Si le lien pré-rempli n'affiche pas les valeurs, saisis-les à la main dans les
deux cases : `Q138911600` puis `Q140517745`.)*

## Étape 3 — Vérifications (2 min)

| Où | Ce qui doit être vrai |
|---|---|
| https://www.wikidata.org/wiki/Q138911600 | redirige maintenant vers Q140517745 |
| https://www.wikidata.org/wiki/Q140517745 | ISBN 978-2-9586347-0-4, ASIN 2958634701, OpenLibrary OL45424544W, 672 pages, sous-titre — **tous intacts** |
| « instance de » (P31) de Q140517745 | garder **Q47461344** (anthologie) + **Q571** (livre) ; si la fusion y a ajouté **Q7725634** et/ou **Q105420**, tu peux les **supprimer** (doublons) |

## Étape 4 — (optionnel, avis de Stéphane)

Les 3 autres livres figurent dans les « œuvres notables » (P800) de la fiche
auteur **Q138909233** ; « Livresque des mots » n'y est pas. Pour homogénéité, on
*pourrait* y ajouter **P800 = Q140517745**. À laisser à l'appréciation de
Stéphane (ce livre est hors corpus anthropie — mais P800 = œuvre de l'auteur, pas
lien au concept, donc c'est cohérent). Ne rien faire si doute.

## Puis

Un mot à Stéphane pour confirmer que la fusion est faite — il gèle alors
**Q140517745** comme QID canonique dans ses fichiers d'indexation.

---
*Préparé le 2026-07-16. Item survivant = Q140517745. Item absorbé = Q138911600.*
