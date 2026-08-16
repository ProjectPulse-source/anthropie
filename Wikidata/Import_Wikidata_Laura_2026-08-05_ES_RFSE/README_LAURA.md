# Wikidata — navette du 2026-08-05 (2 blocs, un seul Run)

> ✅ **TOUT FAIT le 2026-08-05** (exécuté par Laura le jour même) : item créé
> = **Q140892752** — readback API complet 23/23 conforme (labels/descriptions,
> P50 Q138909233 rang 4 sourcé, DOI, P1433 Q3428732, 6 P2093, P953 Cairn) ;
> Q139771989 : label + description ES posés, P953 espagnol sur le concept
> 21766183 vérifié. Aucun reste sur ce dossier.

Laura — deux mises à jour dans un même batch :

1. **AWP-01 passe en espagnol** : la traduction espagnole du premier working
   paper est publiée sur Zenodo. On ajoute à l'item existant **Q139771989**
   son libellé + sa description en espagnol, et le lien texte intégral
   espagnol (qualifié langue = espagnol).
2. **Première publication en revue à comité de lecture** : la recension de
   *Chasseurs d'États* (Benjamin Lemoine) par Stéphane est parue dans la
   **Revue française de socio-économie** 2026/1 (n° 36), dans un bloc
   « Comptes rendus d'ouvrages » co-signé par 7 recenseurs. On crée l'item
   de ce bloc (c'est l'objet bibliographique qui porte le DOI).

| | |
|---|---|
| Item existant à enrichir | **Q139771989** (AWP-01) |
| Zenodo ES (concept, résout vers la dernière version) | https://zenodo.org/records/21766183 |
| Item à créer | « Comptes rendus d'ouvrages », RFSE 2026/1 (n° 36), p. 247-265 |
| Revue | **Q3428732** (Revue française de socio-économie) |
| DOI du bloc | **10.3917/rfse.036.0247** |
| Auteur | Stéphane Lalut (**Q138909233**), 4e sur 7 ; les 6 autres en « author name string » |

## Comment faire — UN CLIC

1. Ouvrir le lien du fichier **`deeplink.txt`** : il charge le batch dans
   QuickStatements → **Run** (connectée à ton compte).
   *(Alternative : coller `batch_quickstatements.txt` en mode Import V1, en
   retirant les lignes `//`.)*
2. **Noter le QID créé** (bloc 2) et l'envoyer à Stéphane.

## Notes (pourquoi c'est fait comme ça)

- Le lien Zenodo espagnol pointe le **record de concept** (21766183), pas une
  version datée : il résoudra toujours vers la dernière version du texte.
- Ce batch **remplace** celui du 03/08 (`QS_WIKIDATA_AWP01_ES_2026-08-03.txt`)
  qui figeait une version corrigée depuis — ne pas l'exécuter.
- Pas de « main subject » sur l'item RFSE : le bloc recense 7 ouvrages
  différents, et l'ouvrage recensé par Stéphane n'a pas d'item Wikidata.
- Les co-recenseurs restent en « author name string » (P2093) : on ne vérifie
  pas leurs éventuels items — seul Stéphane est lié en P50.

Merci !
