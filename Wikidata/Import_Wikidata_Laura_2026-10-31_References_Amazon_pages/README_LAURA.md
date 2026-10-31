# Lot Wikidata du 31/10/2026 — référence Amazon des nombres de pages (P1104)

**Pour Laura** : ouvrir le lien de `deeplink.txt` dans QuickStatements, connecté au compte habituel, et lancer. Six
lignes, trois livres.

## Rapprochement fait avant le lot (31/10)

Pour chacun des sept livres qui portent un nombre de pages sur Wikidata, trois relevés indépendants :

| Livre | Item | Wikidata (P1104) | PDF intérieur en vente (pages comptées) | Amazon, « nombre de pages de l'édition imprimée » (navigateur, 31/10) | Référence avant le lot |
|---|---|---|---|---|---|
| *Anthropie* | Q138827344 | 630 | 630 | 630 (amazon.fr) | Amazon, 23/10 |
| *Anthropy* | Q140645013 | 644 | 644 | 644 (amazon.fr et amazon.com) | **aucune** |
| *Dette publique* | Q138910896 | 225 | 225 | 225 | Amazon, 04/10 |
| *L'Odyssée des idées* | Q138911733 | 682 | 682 | 682 | **aucune** |
| *La Société du premier coup* | Q141072263 | 140 | 140 | 140 | **aucune** |
| *Un président peut-il tenir ses promesses ?* | Q141640333 | 286 | 286 | 286 | Amazon, 04/10 |
| *Livresque des mots* | Q140517745 | 680 | 680 | 680 | Amazon, 04/10 |

Les sept valeurs concordent. Les quatre références existantes restent justes (même nombre affiché aujourd'hui) : on ne
les touche pas. Le lot ajoute la référence aux trois déclarations qui n'en ont pas. Pour *Anthropy*, l'écart du 23/10
(Amazon affichait 632) est résorbé : Amazon affiche 644.

PDF comptés : `03_LIVRES\anthropie\LIVRABLES_KDP\FR_ANTHROPIE_Broche_INTERIEUR_630p_finale-n47-20261022.pdf`,
`…\EN_ANTHROPY_Broche_INTERIEUR_644p_revision-20261023.pdf`, `03_LIVRES\dette-publique\03_LIVRABLES\Dette_INTERIEUR_broche_225p_edition-20261017.pdf`,
`03_LIVRES\odyssee\03_LIVRABLES\odyssee_broche_interieur.pdf`, `03_LIVRES\premier-coup\03_LIVRABLES\PREMIER_COUP_BROCHE_FINAL.pdf`,
`03_LIVRES\promesses-2027\03_LIVRABLES\KDP_MAJ_2026-09-28\FR_PROMESSES-2027_Broche_INTERIEUR_286p_2026-09-28.pdf`,
`03_LIVRES\livresque\03-BROCHE-PDF\LIVRESQUE DES MOTS - 16,99x24,4 - WEASY-2026-10-04-ED2026.pdf`.

## Forme du lot

Retrait de la déclaration, puis recréation avec sa référence (S854 page Amazon du broché, S813 date de consultation).
C'est le modèle qui a écrit le 04/10 et le 23/10 ; le 23/10, « ajouter une référence à la déclaration existante »
s'était terminé en vert **sans rien écrire**. *Anthropy* prend la page amazon.com, comme son entrée de `data/works.yaml`.

## Après exécution

Relire les trois items par l'API (`wbgetclaims`, `property=P1104`) : un seul P1104 par item, valeur inchangée, une
référence S854 + S813. Consigner la révision ici, puis `python scripts/check-wikidata-registre.py`.

## ✅ Exécuté le 31/10/2026 (23:09 UTC, Laura) — relu par l'API le 01/11

Relecture `wbgetclaims` (`rb_Q141072263.json`, `rb_Q138911733.json`, `rb_Q140645013.json`) : un seul P1104 par item,
valeur inchangée, une référence S854 + S813 `+2026-10-31` :

- Q141072263 *Premier coup* : `+140`, `https://www.amazon.fr/dp/2958634760`, révision 2563187160 ;
- Q138911733 *Odyssée* : `+682`, `https://www.amazon.fr/dp/2958634744`, révision 2563187173 ;
- Q140645013 *Anthropy* : `+644`, `https://www.amazon.com/dp/2958634752`, révision 2563187189.

Séquence retrait → création → référence sur chaque item. `check-wikidata-registre.py` : parité OK (23 items). Les sept
nombres de pages du catalogue portent désormais une référence Amazon. Aucune écriture en retour dans le site : les
valeurs n'ont pas changé.
