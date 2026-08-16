# Changelog — Wikidata/

## v3.1 — 2026-08-16 (rattachement du livre *Dette Publique* au nœud français)

- **Lot exécuté par Laura, relu par l'API** : `Q138910896` `P921` **`Q3024794`**
  (*dette publique de la France*). Deep-link QuickStatements, une seule commande.
- **Motif** : l'item du livre portait `P921` = anthropie (`Q138827949`) +
  `Q3024789` (*dette de l'État*, générique tous pays) — donc **pas** le nœud
  précis, celui qui porte les sitelinks frwiki/dewiki et l'identifiant Google
  Knowledge Graph, et où atterrit la résolution d'entité sur la dette française.
- **Readback** : `P921` = 3 valeurs, rang normal, **12 propriétés au total** —
  aucun effet de bord.
- **Cohérence de surface** : le même jour, la page `/cout-de-la-dette-publique/`
  a commencé à émettre un JSON-LD `Dataset` dont le `about` pointe **le même
  `Q3024794`**. Les deux surfaces désignent désormais le même nœud.
- **Périmètre rappelé, pour ne pas se tromper de geste** : Wikidata n'est pas un
  annuaire de liens. On rattache les **œuvres**, jamais les pages ; ajouter le
  site en `P973` sur un item de sujet — ou un lien externe sur l'article
  Wikipédia — serait de l'auto-référencement, et serait révoqué. **Item Wikidata
  pour le jeu de données : écarté** (notoriété contestable, accrétion à
  maintenir).

> ⚠ **Ce fichier n'est PAS le registre — mesure du 2026-08-16.** Il a décroché au
> 13/05 et j'ai d'abord cru à un trou de traçabilité. Vérification faite, c'est
> faux : **les 9 QID de `data/works.yaml` sont tous documentés dans `Wikidata/`**,
> par les dossiers datés (`Import_Wikidata_Laura_2026-07-*`, `_2026-08-05_ES_RFSE`,
> `Fusion_Livresque_2026-07-16`, `2026-07_GEO_alignement`). **Le registre primaire,
> ce sont les dossiers datés ; ce CHANGELOG n'en est que le récit**, et un récit
> qui double une source finit toujours par en diverger.
>
> **Le vrai manque est ailleurs, et il est nommé** : les gestes exécutés depuis une
> session par simple deep-link — création de `Q141072263` + recensions
> `Q141072264-66` le 15/08, et le `P921` du 16/08 — **n'ont laissé aucun dossier**.
> La convention a lâché au moment où le travail est passé du lot préparé au lien
> d'une ligne. D'où la règle désormais explicite dans `README.md` : **tout geste
> Wikidata laisse un dossier daté, même s'il tient en une commande.**
>
> Conséquence mesurée du même manque : `Q141072263` existait depuis le 15/08 et
> `works.yaml` disait encore `wikidata: "" # todo — item à créer` ; la fiche
> n'avait donc **aucun `sameAs`**. Corrigé le 16/08 (registre + fiche), readback
> API à l'appui. Ce n'était pas un défaut de journal : un défaut d'**écriture en
> retour**.

## v3.0 — 2026-05-13 (Automatisation : script Python de génération)

- **Création du dispositif Python d'automatisation** dans `Wikidata/scripts/`.
- **Architecture modulaire** : fetchers (Zenodo, Crossref, OpenLibrary),
  generators (awp, article, book), validators (garde-fous intégrés).
- **Validations intégrées** reproduisant les 8 erreurs accumulées dans Phase A+B+C :
  P9934 hors scope, P407 sur P356, formats DOI/ISBN, contrainte unicité P356.
- **Workflow semi-automatisé** : Stéphane déclenche, le script génère, validation
  humaine obligatoire, transmission à Laura, exécution QuickStatements.
- **Aucune communication automatique avec Wikidata.** Préservation du contrôle
  qualité humain à chaque étape.
- **Coût marginal d'une nouvelle publication** : ~10 min de validation (vs ~1h
  composition manuelle de batch).
- **Aucun commit automatique.** Repo `Wikidata/scripts/` reste untracked tant que
  Stéphane n'a pas validé l'ensemble du dispositif après premier test réel.

## v2.5 — 2026-05-11 (SocArXiv : AWP-06 déposé, profil OSF résolu)

- **AWP-06 (Digital Infrastructures) déposé sur SocArXiv** : DOI `10.31235/osf.io/z6x38_v1`, accepté par modération. URL preprint : `https://osf.io/preprints/socarxiv/z6x38_v1`. C'est le premier dépôt OSF de Stéphane, ouvre la voie aux 5 autres.
- **OSF User ID résolu** : `ymkpj`. URL profil : `https://osf.io/ymkpj/`.
- **Batch `15_quickstatements_socarxiv_filled.qs` mis à jour** : 2 placeholders sur 13 pré-remplis (`<OSF_USER_ID>` et `<OSF_DOI_AWP_06>`). 11 placeholders restants : 5 DOIs SocArXiv AWP-01 à AWP-05 (à substituer au fur et à mesure des dépôts), 6 QIDs Wikidata AWP-01 à AWP-06 (à substituer après Phase B Laura).
- **`data/author.toml`** : 9ème entrée `sameAs` ajoutée (`https://osf.io/ymkpj/`). Non commitée tant que les autres dépôts SocArXiv ne sont pas terminés.
- **Cinétique de dépôt restant** : 1 dépôt tous les 2-3 jours, ordre AWP-01 → AWP-02 → AWP-03 → AWP-04 → AWP-05, total 10-15 jours.
- **Aucun commit.** Dossier `Wikidata/` reste `untracked`.

## v2.4 — 2026-05-11 (intégration SocArXiv — préparation)

- **Création du batch additif `15_quickstatements_socarxiv_filled.qs`** : enrichissement de Q138909233 avec le profil OSF (P973), et ajout du DOI SocArXiv comme P356 supplémentaire sur chaque item AWP. Sourcing total par AWP après ce batch : 4 plateformes (Zenodo FR + Zenodo EN + SSRN + SocArXiv).
- **Mise à jour de `data/author.toml`** : ajout de SocArXiv au `sameAs` JSON-LD via un nouveau bloc `[[author.sameAs]]` (cohérent avec la convention TOML réelle du fichier, blocs nommés plutôt qu'array de strings). Tableau de sameAs porté de 8 à 9 entrées. Modification untracked tant que `<OSF_USER_ID>` n'est pas substitué.
- **Cinétique** : ce batch s'exécute APRÈS Phase B Wikidata (les QIDs réels des AWPs sont nécessaires). Substitution partielle tolérée — possibilité d'exécuter en vagues au fur et à mesure des dépôts SocArXiv.
- **Placeholders explicites** : 13 placeholders dans le batch 15_, à substituer par Stéphane (`<OSF_USER_ID>`, 6 × `<OSF_DOI_AWP_XX>`) et par Laura (6 × `<Q-AWP-XX>` après Phase B).
- **Aucun commit.** Dossier `Wikidata/` reste `untracked`. `data/author.toml` modifié reste également non commité tant que substitution incomplète.

## v2.3 — 2026-05-11 (résolution finale par omission/reconduction)

- **5 dernières décisions résolues** par validation utilisateur 2026-05-11 — toutes par omission ou reconduction, aucun Q-ID inventé :
  - #5 self-published : Q3504054 supprimé (3 lignes P123 retirées dans `11_` §A.3/§A.4/§A.5)
  - #6 publication series : Q1711593 supprimé (1 ligne P31 retirée dans `11_` §A.6) ; P31=Q13442814 actuel reconduit, bloc commentaire reformulé
  - #7 economic essay : Q62482 supprimé (1 ligne P136 retirée dans `11_` §A.3)
  - #8 independent research : Q161732 supprimé (1 ligne P921 retirée dans `12_` §B.5)
  - #9 longue durée : Q1339645 supprimé (1 ligne P921 retirée dans `12_` §B.2). Q1812879 également confirmé non pertinent (ne pas introduire)
  - #12 Google Scholar : P1960 confirmé actif et standard. P4985 = TMDB person ID, écarté.
- **Total : 7 déclarations QS supprimées** (5 dans `11_` : 3×P123 Q3504054 + 1×P136 Q62482 + 1×P31 Q1711593 ; 2 dans `12_` : 1×P921 Q1339645 + 1×P921 Q161732) + 1 commentaire orphelin nettoyé.
- **Décompte final** : 0 `[À VÉRIFIER]` Wikidata externe restant. Batch QS prêt pour exécution Laura selon cinétique maillage v1 §13.
- `14_remaining_decisions_for_laura.md` : tableau de tête actualisé, sections #5/#6/#7/#8/#9/#12 réécrites en mode RÉSOLU, synthèse d'exécution reset à 0 min effort Laura.
- `00_inventory_audit.md` §6.9 ajoutée + en-tête v2.3.
- **Aucun commit.** Dossier `Wikidata/` reste `untracked`.

## v2.2 — 2026-05-11 (4 substitutions supplémentaires validées par l'utilisateur)

- **4 substitutions appliquées** dans `11_quickstatements_phase_A_filled.qs` et `wikidata_maillage_lalut_v1.md` :
  - #2 public finance : Q161157 → **Q274490**
  - #3 ecological economics : Q1062148 → **Q1049066**
  - #4 social sciences : Q21201 → **Q34749**
  - #11 Academia.edu profile property : P6079 → **P5715** (1ʳᵉ correction P-ID de la série)
- Re-confirmation : Q1322603 → Q22661177 déjà appliquée en v2.1 (0 occurrence résiduelle).
- 8 marqueurs `[À VÉRIFIER]` supprimés (3 dans `11_`, 5 dans le maillage).
- `14_remaining_decisions_for_laura.md` : tableau de tête + sections #2/#3/#4/#11 + synthèse mis à jour. Restant pour Laura : **6 items** (vs 9 après v2.1). Effort estimé : ~5-10 min.
- `00_inventory_audit.md` §6.8 ajoutée + en-tête v2.2.
- **Note croisée** : `09_wikidata_existing_state.yaml` mentionne P5023 sur Q138909233 pour Academia ; possible typo du prompt initial pour P5715. À vérifier Laura.
- **Aucun commit.** Dossier `Wikidata/` reste `untracked`.

## v2.1 — 2026-05-11 (décisions structurantes résolues + correction critique)

- **3 décisions structurantes résolues** via web_search Anthropic :
  - #1 given name « Stéphane » : Q937131 → Q3501543
  - #10 Zenodo repository : Q1322603 → Q22661177
  - #13 Amazon URL : remplacé par P5749 ASIN (doctrine Wikidata sur identifiants dédiés)
- **Correction critique #14** : ma recommandation v1 de supprimer P31=Q3331189 sur Q138911733 était fausse — la contrainte de propriété P5749 exige cette valeur. Conserver Q3331189, ajouter Q47461344 et Q571 en complément.
- **Décision #6 (publication series) confirmée non-résolue** après recherche web : aucun Q-ID concept standard identifié. Recommandation par défaut : ne pas toucher au P31 actuel (Q13442814).
- Application sur Q138911733 (L'Odyssée des Idées) : déclaration P5749 = `295863471X` ajoutée, sourcing URL Amazon FR.
- `14_remaining_decisions_for_laura.md` : tableau de tête mis à jour, sections #6 et #13 réécrites, synthèse d'exécution recalibrée (effort Laura ~10-15 min vs 15-25 min initial).
- `00_inventory_audit.md` §6.7 ajoutée.
- **Aucun commit.** Dossier `Wikidata/` reste `untracked`.

## v1.3 — 2026-05-11 (corrections Q-IDs après web_search Anthropic)

- **7 corrections Q-IDs Wikidata** appliquées dans les batches QuickStatements (11_, 12_, 13_) et dans `wikidata_maillage_lalut_v1.md` :
  - Q22954024 → Q3024789 (government debt)
  - Q42213 → Q45003 (entropy)
  - Q12739 → Q795757 (energy transition)
  - Q1066186 → Q671224 (data center)
  - Q161172 → Q1554076 (political ecology)
  - Q1149875 → Q41719 (hypothesis)
  - Q17737 et Q11660 confirmés corrects (suppression marqueurs `[À VÉRIFIER]`)
- **Bonus** : Q137571914 (AI data center) ajouté en commentaire sur §B.6 (AWP-06) comme alternative plus précise à Q671224 — décision Laura.
- **Création `14_remaining_decisions_for_laura.md`** : isole les 13 `[À VÉRIFIER]` Wikidata externes restants (10 Q-IDs ambigus + 3 P-IDs à arbitrer) avec contexte d'usage, alternatives connues, et recommandations neutres.
- `00_inventory_audit.md` §6.6 ajoutée pour traçabilité des corrections.
- **Aucun commit.** Dossier `Wikidata/` reste `untracked`.

## v1.2 — 2026-05-11 (même jour, données L'Odyssée fournies par utilisateur)

- **Données partielles L'Odyssée des Idées (Q138911733) intégrées** depuis
  fourniture utilisateur :
  - URL Amazon FR : `https://www.amazon.fr/Lodyssée-idées-philosophie-lintelligence-artificielle/dp/295863471X`
  - ISBN-13 : `978-2958634711` (confirme la valeur existante sur Wikidata)
  - ISBN-10 / ASIN papier : `295863471X`
- `03_books.yaml` : L'Odyssée déplacée de `books_mentioned_in_external_doc_but_not_in_repo` vers une entrée régulière `books[]` avec métadonnées partielles + `source_external` explicite.
- `08_external_links.yaml` : nouvelle entrée `book-lodyssee-des-idees` avec URL Amazon.
- `09_wikidata_existing_state.yaml` : champ `external_data_provided_by_user` ajouté sur Q138911733 + recommandation P953 / P856 (à arbitrer Laura).
- `11_quickstatements_phase_A_filled.qs` §A.5 : P50 author maintenant sourcé sur l'URL Amazon (source primaire vérifiable) plutôt que sur stephane-lalut.com (pas de page) ; renforcement P212 ISBN avec source URL Amazon.
- `00_inventory_audit.md` §5 item 4 : reflet de la fourniture utilisateur, anti-pattern slug-URL explicité.
- **Anti-pattern respecté** : le sous-titre suggéré par le slug Amazon (`philosophie-lintelligence-artificielle`) n'a PAS été recopié comme titre canonique.

## v1.1 — 2026-05-11 (même jour, après découverte du maillage)

- **Découverte du maillage stratégique** `wikidata_maillage_lalut_v1.md`
  dans `Wikidata/` (570 lignes, v1.0 Mai 2026).
- **Réécriture en miroir exact** des 3 batches QuickStatements :
  - `11_quickstatements_phase_A_filled.qs` ← maillage v1 §A.1-A.6
  - `12_quickstatements_phase_B_filled.qs` ← maillage v1 §B.1-B.6 (avec préalable §B.0 recherche doublons)
  - `13_quickstatements_phase_C_filled.qs` ← maillage v1 §C.1-C.3
- **Substitutions repo appliquées** (6 valeurs confirmables) :
  URL EN concept (slug `what-is-anthropy`), ASIN livre 1, ISBN livre 2, pages
  livre 1, DOIs AWPs, dates publication AWPs.
- **Erreur du maillage v1 corrigée** : URL EN série AWP (`/en/awp-series/`
  proposée → `/en/serie-awp/` réel, cf. `hugo.toml` ligne 27-29).
- **Q-IDs/P-IDs Wikidata externes** restent `[À VÉRIFIER]` (~19 marqueurs)
  — Laura valide depuis Wikidata.
- `00_inventory_audit.md` mis à jour : sources +1, incohérences +1 (entre
  maillage et repo), §6.5 nouveau (état des `[À VÉRIFIER]`), §9 cinétique
  Laura issue du maillage v1 § 13.

## v1.0 — 2026-05-11

- Génération initiale via `_wikidata-prompt.txt`.
- Sources consultées :
  - `data/author.toml` (8 sameAs, identité auteur)
  - `data/works.yaml` v1.2 (33 œuvres : 6 AWP + 3 livres + 10 articles publiés + 9 accepted_pending + 5 in_review)
  - `data/awp_short_titles.yaml`
  - `content/awp/awp-NN.md` (FR, 6 fichiers)
  - `content/awp/awp-NN.en.md` (EN, 6 fichiers)
  - `content/livres/*.md` (3 livres présents)
  - `content/publications/*.md` (11 fiches articles)
  - `content/quest-ce-que-lanthropie/_index.md` + `_index.en.md`
  - `content/serie-awp/_index.md` + `_index.en.md`
  - `content/glossaire/_index.md` (18 entrées)
  - `config/_default/hugo.toml` + `params.toml`
  - `PROJECT_STATUS.md` (phase architecturale stable, doctrine 90j diffusion)
- Champs remplis : voir `00_inventory_audit.md` § Résumé exécutif.
- Champs `null` : voir `00_inventory_audit.md` § Tableau des données manquantes.
- Incohérences détectées : voir `00_inventory_audit.md` § Tableau des incohérences.
- **Pas de commit Git.** Décision humaine en aval.
