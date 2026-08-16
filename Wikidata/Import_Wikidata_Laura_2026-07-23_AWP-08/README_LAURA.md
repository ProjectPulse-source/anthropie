# Wikidata — nouvel item AWP-08 (2026-07-23)

> ✅ **TOUT FAIT le 2026-07-24** : item créé = **Q140680750** (propriétés
> conformes) + rétro-liens passés (série↔AWP-08, auteur↔AWP-08, rattrapage
> série↔AWP-07 Q140446195) — vérifié par readback API : la série a ses 8 AWP.
> **SEUL RESTE (hors ce dossier)** : la **fusion Livresque** Q138911600 →
> Q140517745 (gadget *Merge*, consigne dans
> `Wikidata/Fusion_Livresque_2026-07-16/README_LAURA.md` ; re-vérifié 24/07 :
> doublon toujours vivant).

Laura — un nouvel working paper est publié aujourd'hui, à créer sur Wikidata,
au même patron que les AWP précédents (un item par AWP, article scientifique,
rattaché à la série).

| | |
|---|---|
| Titre FR | **La réversibilité sociale comme dimension de l'inégalité — Repli, mémoire institutionnelle et agenda de mesure** |
| Titre EN | Social Reversibility as a Dimension of Inequality — Fallback, Institutional Memory, and a Measurement Agenda |
| Auteur | Stéphane Lalut (**Q138909233**) |
| Série | Anthropie Working Papers (**Q139040913**), n° 8 |
| DOI (FR, canonique) | **10.5281/zenodo.21506320** |
| Zenodo EN (isDerivedFrom) | 10.5281/zenodo.21507249 |
| Publication | 2026-07-23 · Licence CC-BY 4.0 |
| Pages site | https://stephane-lalut.com/awp/awp-08/ · /en/awp/awp-08/ |

## Comment faire — UN CLIC

1. Ouvrir le lien du fichier **`deeplink.txt`** (dossier joint) : il ouvre
   QuickStatements avec le batch déjà chargé → **Run**.
   *(Alternative : coller `batch_quickstatements.txt` en mode Import, en
   retirant les lignes `//`.)*
2. **Noter le QID créé** et l'envoyer à Stéphane.
3. **Rétro-liens** (2 lignes, mode Import, remplacer NEW_QID par le QID créé) :
   ```
   Q139040913	P527	NEW_QID
   Q138909233	P800	NEW_QID
   ```

> L'item est FR-canonique (comme les AWP précédents) : le DOI FR en P356,
> l'édition anglaise via les liens texte intégral qualifiés (P953 + P407
> anglais). Ne pas créer d'item séparé pour l'édition EN.

Merci !
