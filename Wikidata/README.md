# Wikidata/ — inventaire structuré pour le maillage Wikidata

> ## ⚠ À lire avant tout geste Wikidata (état au 2026-08-16)
>
> **Ce dossier est versionné depuis le 2026-08-16.** Il a vécu quatre mois en
> **un seul exemplaire, sur un seul disque**, sans historique ni redondance —
> alors qu'il porte l'intégralité de la navette Wikidata. C'était le vrai risque,
> et c'est ce que le suivi git corrige : historique, diff, copie distante.
>
> **Deux étages, à ne pas confondre :**
>
> | Étage | Fichiers | Nature |
> |---|---|---|
> | **Inventaire** | `00_`…`16_`, `_*-prompt*.txt`, `scripts/` | **Régénérable** depuis l'état du repo. Une photo, pas une archive. |
> | **Registre** | `Import_Wikidata_Laura_<date>_<sujet>/`, `Fusion_*`, `2026-07_GEO_alignement/` | **Historique, non régénérable.** C'est le registre primaire de ce qui a été exécuté. |
>
> `CHANGELOG.md` n'est **ni l'un ni l'autre** : c'est un récit. Il a décroché du
> 13/05 au 16/08 sans que la traçabilité en souffre — vérification faite, les
> 9 QID de `data/works.yaml` sont tous documentés par les dossiers datés. Un récit
> qui double une source finit par en diverger : en cas de contradiction, **les
> dossiers datés font foi.**
>
> ### La règle, née du seul manque réellement mesuré
>
> **Tout geste Wikidata laisse un dossier daté — même s'il tient en une commande.**
>
> La convention a lâché exactement quand le travail est passé du lot préparé au
> deep-link d'une ligne collé en session : les items du 15/08 (`Q141072263` et ses
> recensions) n'ont laissé aucune trace ici. Conséquence mesurée le 16/08 :
> `works.yaml` déclarait encore `wikidata: "" # todo — item à créer` pour un livre
> **dont l'item existait depuis la veille**, et la fiche n'avait donc aucun
> `sameAs`. Ce n'était pas un défaut de journal, mais d'**écriture en retour**.
>
> Un dossier daté contient au minimum : `README_LAURA.md` (ce qu'on ajoute, à quel
> item, pourquoi) et `deeplink.txt`. Une fois exécuté, il ouvre sur un bloc
> **✅ + readback API** — jamais « fait » sans relecture. Modèle le plus récent :
> `Import_Wikidata_Laura_2026-08-16_Dette_P921/`.
>
> ### Boucler : trois surfaces, jamais une seule
>
> Un QID obtenu n'existe pour le site que s'il redescend jusqu'à la page :
> **item Wikidata → `data/works.yaml` → front matter `wikidata_qid` de la fiche**
> → `sameAs` du JSON-LD. `python scripts/check-fiches-registre.py` couvre le
> dernier maillon (registre → fiche, livres **et AWP**) ; **le premier — Wikidata →
> registre — est couvert depuis le 2026-09-02 par `python scripts/check-wikidata-registre.py`** :
> requête inverse depuis le nœud auteur (`haswbstatement:P50=Q138909233`), comparée aux
> QID déclarés au registre, dans les deux sens (absent du registre ; inexistant, redirigé
> ou sans P50). Témoin positif le jour de son écriture : **10 écarts, 0 faux positif** —
> les 8 AWP, la série et une recension vivaient sur Wikidata depuis des mois sans que le
> site le sache. **Le bloc ✅ d'un dossier daté cite désormais trois choses** : le QID
> rendu, le commit qui l'a écrit en retour dans `data/works.yaml` (et la fiche), et la
> sortie à 0 de ce script. Un diff des QID cités dans les fichiers du dossier avait
> d'abord été envisagé, et **écarté par la mesure** : les fichiers du dossier
> citent 70 QID dont l'essentiel est du vocabulaire et jusqu'à un exemple factice
> (`Q1234567`) — un diff QID produirait 61 faux positifs, soit l'inverse d'un
> garde-fou.
>
> ### Périmètre — ce qu'on ne fait pas
>
> Wikidata n'est **pas un annuaire de liens** : on rattache les **œuvres**, jamais
> les pages du site. Poser `stephane-lalut.com` en `P973` sur un item de sujet, ou
> ajouter un lien externe à un article Wikipédia depuis le site, serait de
> l'auto-référencement — révoqué, et à juste titre.

**Objectif.** Fournir un inventaire exhaustif et sourcé des données structurées
du site `stephane-lalut.com`, prêt à alimenter le maillage Wikidata géré par
Laura, et notamment à finaliser le fichier `wikidata_maillage_lalut_v1.md`
(batches QuickStatements).

**Date de génération.** 2026-05-11 (v1.2 — données L'Odyssée intégrées depuis fourniture utilisateur).

**Convention de versioning.** Chaque régénération bumpe une version dans
`CHANGELOG.md`. Le contenu du dossier est régénérable depuis l'état du repo.

**Point d'entrée.** Lire d'abord `00_inventory_audit.md` qui fait l'inventaire
des sources consultées, des champs manquants (`null`) avec leur
`expected_source`, et des incohérences détectées entre sources.

## Structure

| Fichier | Contenu |
|---|---|
| `00_inventory_audit.md` | Audit complet : sources, champs `null`, incohérences |
| `01_author.yaml` | Identité Stéphane Lalut (Q138909233) |
| `02_concept_anthropie.yaml` | Concept anthropie (Q138827949) + 18 entrées glossaire |
| `03_books.yaml` | 3 livres (Q138827344, Q138910896, Livresque sans QID) |
| `04_awp_series.yaml` | Série AWP (Q139040913) |
| `05_awps.yaml` | AWP-01 à AWP-06 (FR + EN) exhaustifs |
| `06_articles.yaml` | 10+1 publiés / 8 acceptés / 5 in_review |
| `07_site_mapping.yaml` | URL site ↔ QID Wikidata |
| `08_external_links.yaml` | Liens externes structurés (sameAs, Zenodo, SSRN, MPRA, Amazon, DOIs) |
| `09_wikidata_existing_state.yaml` | État Wikidata existant (depuis prompt utilisateur) |
| `10_wikidata_target_completion.md` | Différence état actuel ↔ état cible |
| `11_quickstatements_phase_A_filled.qs` | Phase A : compléter les 6 items existants |
| `12_quickstatements_phase_B_filled.qs` | Phase B : CREATE les 6 AWPs |
| `13_quickstatements_phase_C_filled.qs` | Phase C : rétro-liens (placeholders à compléter post-B) |
| `wikidata_maillage_lalut_v1.md` | **Maillage stratégique de référence** (v1.0 Mai 2026, 570 lignes) — source des batches QS, conventions, cinétique Laura, checklists pré/post-batch |
| `CHANGELOG.md` | Historique de génération |

## Règles

- **Aucune invention** : tout champ rempli porte une `source_file` (idéalement
  `source_line`).
- **`null` ≠ `""`** : `null` = donnée absente du repo (avec `expected_source`) ;
  `""` = donnée explicitement vide à la source.
- **Aucun web fetch** : tout vient du repo local.
- **Pas de commit automatique** : ce dossier reste sous décision humaine.

## À ne pas faire

- Ne pas modifier manuellement ces fichiers. Régénérer via
  `_wikidata-prompt.txt` à la racine du repo.
- Ne pas committer le dossier sans relecture humaine de
  `00_inventory_audit.md`.
- Ne pas exécuter Phase C avant Phase B (les QIDs AWP sont nécessaires).
- **Respecter la cinétique du maillage v1 § 13** : ≥ 48 h entre Phase A et
  Phase B, ≥ 72 h entre Phase B et Phase C. Fractionner Phase B en 3
  sous-batches (J+3, J+7, J+10) pour éviter pattern de mass-editing.
