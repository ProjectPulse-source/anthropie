# Import Wikidata — Alignement GEO 2026-07 — procédure pour Laura

**Dossier préparé le 2026-07-04, complété le 2026-07-06** (ajout du BLOC 7 : création de l'item du nouveau working paper AWP-07, publié le 05/07). Trois fichiers :

| Fichier | Rôle |
|---|---|
| `ETAT_ACTUEL.md` | Relevé factuel des items AVANT import — sert aussi de référence de rollback : toute valeur retirée par le batch y est consignée |
| `batch_quickstatements.txt` | Le batch à importer (format QuickStatements V1) — **40 commandes actives** (dont 1 création d'item), le reste est commenté |
| `README_LAURA.md` | Ce fichier |

## 1. Avant de commencer

- Il faut un compte Wikidata connecté (le tien). QuickStatements édite **sous ton nom**.
- Le batch ne contient **que** des corrections justifiées par un écart constaté (justification en commentaire au-dessus de chaque bloc). Rien d'autre ne doit être importé.
- ⚠️ Deux blocs en fin de fichier sont **volontairement commentés et ne doivent PAS être importés** (voir § 4).

## 2. Import pas-à-pas

1. Ouvrir **https://quickstatements.toolforge.org** → se connecter (bouton *Log in*, autorisation OAuth Wikidata).
2. Cliquer **New batch**.
3. Ouvrir `batch_quickstatements.txt` dans un éditeur de texte (Notepad++ ou VS Code — pas Word).
4. **Supprimer toutes les lignes commençant par `//`** (elles ne sont pas comprises par l'outil).
   - Notepad++ : Rechercher → Remplacer → mode « Expression régulière » → rechercher `^//.*\r?\n` → remplacer par (rien) → *Remplacer tout*.
   - Il doit rester exactement **40 lignes** : 7 commençant par `-`, 1 ligne `CREATE` seule, 14 lignes commençant par `LAST`, et 18 lignes commençant par `Q…`.
5. Coller ces 40 lignes dans la zone de texte de QuickStatements (onglet **V1 commands** — PAS l'onglet CSV).
6. Cliquer **Import V1 commands** → l'outil affiche la liste interprétée. Vérifier visuellement :
   - les lignes `-Q…` apparaissent comme **REMOVE** — il doit y en avoir exactement **7** : 2× Q139771993 (P356, P953), 1× Q138827344 (P1104), 1× Q138910896 (P1104), 3× Q138911733 (P212, P577, P5749) ;
   - la ligne `CREATE` apparaît comme **création d'un nouvel item** (« CREATE ») et les 14 lignes `LAST` qui la suivent lui sont rattachées — c'est le nouveau working paper AWP-07 « La boucle anthropique » ;
   - aucune ligne en erreur (rouge).
7. Cliquer **Run** (ou *Run in background* : plus fiable si la connexion est lente ; le batch reçoit alors un numéro et tourne côté serveur).
8. Attendre la fin : chaque ligne passe au vert (*done*). Les lignes en erreur restent listées — les copier et me les renvoyer telles quelles, ne pas improviser de correction.

**Ordre important** : dans chaque paire remove/add, la ligne `-` précède l'ajout — ne pas réordonner le fichier.

## 3. Vérifications post-import (5 minutes)

Ouvrir chaque item et contrôler :

| Item | À vérifier |
|---|---|
| [Q138827949](https://www.wikidata.org/wiki/Q138827949) | Description fr commence par « hypothèse selon laquelle… » (sans point final) ; en = « hypothesis that social systems displace disorder rather than resolve it » |
| [Q138909233](https://www.wikidata.org/wiki/Q138909233) | Description fr = « économiste, chercheur indépendant et essayiste » ; en = « French economist, independent researcher and essayist » |
| [Q139771993](https://www.wikidata.org/wiki/Q139771993) | Un SEUL DOI : `10.5281/ZENODO.19269487` (le …486 a disparu) ; le lien Zenodo pointe sur `records/19269487` |
| [Q138827344](https://www.wikidata.org/wiki/Q138827344) | Nombre de pages = 622 (une seule valeur) |
| [Q138910896](https://www.wikidata.org/wiki/Q138910896) | Nombre de pages = 224 (une seule valeur) |
| [Q138911733](https://www.wikidata.org/wiki/Q138911733) | Label « L'Odyssée des idées » (i minuscule) ; description « …(nouvelle édition 2026) » ; ISBN-13 = 978-2-9586347-4-2 **seul** ; date de publication = 2026 **seule** ; pages = 696 ; ASIN = 2958634744 **seul** ; titre (P1476) présent ; sous-titre (P1680) = « Culture, philosophie et science — de l'aube de l'humanité à l'intelligence artificielle » |
| **Nouvel item AWP-07** (le QID est attribué à la création — clique sur la ligne CREATE dans le journal du batch pour l'ouvrir) | Label FR « La boucle anthropique : déplacement, saturation, retour… » ; label EN « The anthropic loop: … » ; DOI **unique** = `10.5281/ZENODO.21200286` ; « fait partie de » (P361) = Anthropie Working Papers ; 3 liens P953 (Zenodo + les deux pages du site) ; date de publication 5 juillet 2026 ; auteur = Stéphane Lalut. **→ Renvoyer le QID créé (Qxxxxxxxx) à Stéphane** — il est nécessaire pour le registre du projet. |

En cas de doublon résiduel (ex. deux ISBN sur Q138911733) : c'est qu'une ligne REMOVE a échoué → supprimer l'ancienne valeur à la main dans l'interface Wikidata (crayon → *supprimer la déclaration*), en s'appuyant sur `ETAT_ACTUEL.md` pour identifier laquelle est l'ancienne.

## 4. Points d'arbitrage — état au 2026-07-04

1. **Sous-titre (P1680) de Q138911733 — ✅ TRANCHÉ le 04/07 par Stéphane : Option A** (sous-titre canonique porté par l'édition 2026) : « Culture, philosophie et science — de l'aube de l'humanité à l'intelligence artificielle ». La ligne est désormais **active dans le batch** (elle s'importe avec le reste). Note : l'ancien sous-titre long encore visible sur Amazon est un état transitoire (préservation des 159 avis, fusion de fiches en attente) — ignorer cette discordance, elle est connue et volontaire.
2. **⛔ Bloc OPTIONNEL langues tierces** (descriptions de/es/it du concept et de/es de la personne) : corrige des fautes réelles mais hors périmètre FR/EN du lot — reste commenté, à faire relire avant tout import.

## 5. Notes de traçabilité

- **Références perdues (assumé)** : les remove sur Q138910896 P1104 (1 réf.), Q138911733 P212 (2 réf.) et Q139771993 P356 (1 réf.) suppriment aussi les références attachées — elles sourçaient des valeurs périmées (ancienne édition / concept-DOI). L'état complet d'avant import est conservé dans `ETAT_ACTUEL.md`.
- **Ce batch remplace** le correctif différé `Wikidata/correction_pagination_anthropie_2026-05-29.qs` (repris à l'identique en BLOC 4) — l'archiver après import.
- **Rollback** : chaque édition QuickStatements est annulable individuellement via l'historique de l'item (*Voir l'historique* → *annuler*) ; `ETAT_ACTUEL.md` donne les valeurs d'origine exactes.
- **BLOC 7 (création AWP-07)** : pas d'état antérieur — l'item n'existait pas (vérifié le 06/07). En cas d'erreur sur une valeur, corriger la déclaration dans l'item créé ; ne **jamais** demander la suppression de l'item (une correction suffit toujours, et un item supprimé casserait les renvois).
- **Signalement hors Wikidata** (pour Stéphane, passage Zenodo § 1 de la worklist) : le record Zenodo 19269487 (AWP-05 FR) affiche une date de publication **2026-03-01** alors que site et Wikidata portent **2026-03-20** — à corriger côté Zenodo, rien à faire côté Wikidata.
