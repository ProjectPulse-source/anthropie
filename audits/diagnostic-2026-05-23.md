# Audit diagnostique — stephane-lalut.com

## 1. En-tête

- **Date de l'audit** : 2026-05-23
- **Commit de référence du prompt** : `3975b24` (mai 2026, ouverture du gel 90 jours)
- **HEAD local au moment de l'audit** : `c8a44a3` — soit 4 commits éditoriaux d'alignement AWP-06 par-dessus le commit de référence (boucle anthropique home + page théorique, chaîne de boucles, sommaires livres, page Livresque). Tous documentés dans `PROJECT_STATUS.md` § 0 comme interventions validées de la fenêtre d'alignement. Aucune modification structurelle (routing, JSON-LD, `citation_*`, hreflang, sitemap, canonical) selon le log ; le présent audit le confirme.
- **État de l'arbre de travail** : `data/author.toml` est **modifié non commité** (ajout d'une 9ᵉ entrée `sameAs` SocArXiv). Le site live reflète la version déployée à 8 `sameAs` — voir Dimension 3.
- **Nœuds externes consultés (snapshot 2026-05-23)** : Zenodo (API records + résolution DOI), DataCite/doi.org (résolution), OpenAlex (API author `A5130851063`), Wikidata (`Q138909233`, items AWP `Q139771989`…`Q139771994`), ORCID, IdRef, Academia, OSF/SocArXiv. Google Scholar et SSRN : voir réserve anti-bot en Dimension 6.
- **Périmètre** : diagnostic pur, lecture seule. Aucun fichier du site modifié. Le seul fichier écrit est le présent rapport.

---

## 2. Verdict opérationnel unique

> ### Défaut bloquant détecté : **NON**
>
> Aucun défaut ne justifie de rompre la fenêtre 90 jours pour intervenir maintenant. Les 12 pages AWP (FR+EN) sont indexables, citables, dotées de métadonnées Google Scholar complètes et d'un graphe JSON-LD correctement noué ; tous les DOI exposés résolvent ; tous les PDF Zenodo répondent en HTTP 200 ; robots/sitemap/hreflang/canonical/IndexNow sont conformes.
>
> **La phase GEO/diffusion 90 jours peut se poursuivre sans intervention.**

### Point adjugé (un seul candidat « bloquant » examiné et écarté)

Le cas **AWP-05 FR** a fait l'objet de deux lectures contradictoires en cours d'audit ; il est tranché ici par test de résolution direct :

- Front matter `content/awp/awp-05.md` : `doi_zenodo`/`url_zenodo` = `…19269486`, mais `pdf_url` = `…19269487`. La page live `/awp/awp-05/` propage cette divergence (citation_doi et lien Zenodo sur `486`, PDF sur `487`).
- Le chemin nu `https://zenodo.org/records/19269486` renvoie 404 — ce qui pouvait laisser croire à un DOI cassé.
- **Mais** l'API Zenodo confirme : `19269486` est le **concept DOI** (`conceptrecid`/`conceptdoi`) du record `19269487` (version, titre « Penser hors les murs »). La résolution `https://doi.org/10.5281/zenodo.19269486` → `302` → `https://zenodo.org/doi/…19269486` → **HTTP 200**, page vivante pointant sur la dernière version. Corroboré par OpenAlex qui liste les deux DOI du même travail.
- **Conclusion** : le DOI de citation de l'AWP-05 FR **n'est pas cassé** ; la citation est possible. L'écart est une **incohérence interne** (concept DOI côté citation vs version DOI côté PDF, alors que les 5 autres AWP FR exposent uniformément leur version DOI). Gravité **AMÉLIORABLE**, non bloquant. Voir Dimension 2 et journal post-90j.

---

## 3. Tableau récapitulatif des écarts par dimension

| Dim. | Objet | Constat | Gravité |
|------|-------|---------|---------|
| **1** | robots / sitemap / canonical / noindex / hreflang / IndexNow | Tous conformes (live = source). x-default présent, sitemaps FR+EN, clé IndexNow servie. | — (RAS) |
| **2** | `citation_*` sur 12 pages AWP | Complètes et exactes sur 11 pages. AWP-05 FR : `citation_doi` = concept DOI `19269486` ≠ version DOI `19269487` du `citation_pdf_url`. Les deux résolvent. | AMÉLIORABLE |
| **3** | JSON-LD ScholarlyArticle / serie-awp | ScholarlyArticle complet (author, datePublished, DOI, isPartOf, inLanguage) ; ItemList + CreativeWorkSeries présents, `@id #series` noué avec `isPartOf` des AWP. | — (RAS) |
| **3** | JSON-LD Person `/a-propos/` | 8 `sameAs` en live vs 9 en source (SocArXiv ajouté mais non commité/déployé). Transitoire et volontaire. | COHÉRENCE_EXTERNE |
| **3 / 7** | JSON-LD Book *Livresque des mots* | `about = DefinedTerm Anthropie` injecté inconditionnellement (`layouts/livres/single.html:53`) sur un ouvrage hors corpus → orphelin sémantique mineur. | AMÉLIORABLE |
| **3** | Page `/livres/` | Pas de JSON-LD `ItemList` des ouvrages. | AMÉLIORABLE |
| **4** | Définition canonique | Verbatim uniquement sur la page concept ; paraphrasée sur accueil / AWP-01 / AWP-06. `canonicalDefinition` (`params.toml:2`) n'est lu par aucun template → pas de single-source. | AMÉLIORABLE |
| **4** | Distinction anthropie ≠ **Anthropocène** | Absente de la page concept (le terme n'apparaît que dans AWP-02). | AMÉLIORABLE |
| **4** | Distinction anthropie ≠ **entropie** | Présente, section dédiée. | — (RAS) |
| **5** | Cohérence AWP-01 / AWP-06 | Site ↔ Zenodo ↔ Wikidata concordants (titre/date/DOI/auteur). AWP-06 : titre site court vs titre Zenodo/Wikidata avec sous-titre. | AMÉLIORABLE |
| **5** | Indexation OpenAlex | AWP-01 et AWP-06 absents de la fiche auteur OpenAlex (latence d'indexation Crossref/DataCite, hors contrôle du site). | COHÉRENCE_EXTERNE |
| **6** | Liens profils auteur | ORCID, Zenodo, OpenAlex, Wikidata, IdRef, SocArXiv, Academia, Google Scholar : HTTP 200 / redirections propres. SSRN : 403 (anti-bot probable, non concluant). | NON_APPLICABLE (SSRN) |
| **6** | PDF Zenodo des 12 AWP | Tous HTTP 200. | — (RAS) |
| **6** | Liens d'achat livres (Amazon) | Présents et fonctionnels (shortlinks `amzn.eu`/`a.co`, popover JS, couvertures 200). | — (RAS) |
| **7** | Fiches livres | 2 livres anthropiques complets et bien maillés (`related_awp`, JSON-LD Book + Wikidata). | — (RAS) |

---

## 4. Détails par dimension

### Dimension 1 — Indexabilité et hygiène d'exploration — **RAS**
`robots.txt` live identique à `static/robots.txt` : `Allow: /` (incl. GPTBot, ClaudeBot), aucun `Disallow: /`, 3 sitemaps déclarés. `sitemap.xml` = index pointant sur `/fr/sitemap.xml` (29 URL) et `/en/sitemap.xml` (14 URL). Canonical auto-référentiel correct sur home, `/serie-awp/`, `/awp/awp-01/`, `/quest-ce-que-lanthropie/`, `/a-propos/` et leurs équivalents `/en/`. Aucun `noindex` sur les pages publiques testées. `hreflang` réciproque FR↔EN avec `x-default` → FR. Clé IndexNow `cb6e6e95…txt` servie en texte brut (HTTP 200). Généré par `layouts/partials/head.html:10-27`.

### Dimension 2 — Métadonnées académiques sur pages AWP — **1 écart AMÉLIORABLE**
Balises générées par `head.html:67-80`. Sur les 12 pages : `citation_title` non vide, `citation_author = "Lalut, Stéphane"`, `citation_publication_date` au format `YYYY/MM/DD`, `citation_language` correct (fr/en), `citation_abstract_html_url` = URL canonique de la page, `citation_pdf_url` sur un PDF Zenodo. Seul écart : **AWP-05 FR** expose le concept DOI `19269486` en `citation_doi` alors que `citation_pdf_url` porte la version `19269487` (cf. point adjugé § 2). Les 5 autres AWP FR exposent uniformément leur version DOI. Recommandation différée : aligner `doi_zenodo`/`url_zenodo` de `content/awp/awp-05.md:12-13` sur `19269487` pour uniformité (ou, choix éditorial inverse, basculer les 6 sur leur concept DOI). Aucune urgence : citation résolvable en l'état.

### Dimension 3 — Graphe d'entités JSON-LD — **3 écarts AMÉLIORABLE / COHÉRENCE**
- **ScholarlyArticle** (`head.html:122-167`) sur `/awp/awp-01/` et `/awp/awp-06/` : `author` (Person + ORCID en `identifier`/`sameAs`), `datePublished`, `identifier` = bon DOI, `isPartOf` CreativeWorkSeries `@id …/serie-awp/#series`, `inLanguage`, plus `about` DefinedTerm Anthropie → Wikidata `Q138827949`, `license` CC-BY-4.0, `workTranslation` croisé. Conforme.
- **`/serie-awp/`** : `ItemList` (6 items) + `CreativeWorkSeries` `@id …#series` `hasPart` 6 articles. Le `@id` est exactement celui pointé par `isPartOf` des AWP → graphe noué.
- **Person `/a-propos/`** : 8 `sameAs` en live (ORCID, Zenodo, OpenAlex, Google Scholar, Academia, Wikidata, SSRN, IdRef). Le 9ᵉ (SocArXiv `osf.io/ymkpj`) figure dans `data/author.toml:71-75` mais **non commité** → écart 8/9 transitoire et volontaire, à résorber par un commit + déploiement (action de fin de fenêtre, pas urgente).
- **Book** : `/livres/anthropie-…/` (ISBN 978-2-9586347-2-8, Wikidata Q138827344) et `/livres/dette-publique-…/` (ISBN 978-2-9586347-3-5, Wikidata Q138910896) complets. *Livresque des mots* (ISBN 978-2-9586347-0-4) : Book correct mais `about = Anthropie` injecté sans condition de série → **orphelin sémantique** (ouvrage hors corpus). `/livres/` (liste) : aucun JSON-LD ItemList (opportunité).

### Dimension 4 — Définition canonique et cohérence textuelle — **2 écarts AMÉLIORABLE**
Chaîne canonique (`config/_default/params.toml:2`, `canonicalDefinition`) : « *L'anthropie est l'hypothèse selon laquelle les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent.* »
- **Présence/identité** : verbatim uniquement sur `/quest-ce-que-lanthropie/`. Accueil, AWP-01 et AWP-06 emploient des paraphrases distinctes (« ne suppriment pas le désordre : ils le déplacent… », « désigne le mécanisme par lequel… », « est le principe selon lequel… »). Symptôme de **classe** et non d'incident : `canonicalDefinition` n'est lu par aucun template (`layouts/`), donc aucun single-source de la définition — contrairement à `data/author.toml` pour l'identité. → AMÉLIORABLE (cohérence rédactionnelle / SEO sémantique). Mesure proportionnée pour la phase post-90j : exposer `canonicalDefinition` via un partial réutilisable, comme l'identité auteur.
- **anthropie ≠ Anthropocène** : distinction **absente** de la page concept (le terme « Anthropocène » n'apparaît que dans AWP-02). → AMÉLIORABLE (risque de confusion lexicale non levé à l'endroit canonique).
- **anthropie ≠ entropie** : **présente** (section « Anthropie et entropie », `_index.md:59-65`). Conforme.

### Dimension 5 — Cohérence inter-nœuds (AWP-01 & AWP-06) — **AMÉLIORABLE / COHÉRENCE_EXTERNE**
- **AWP-01** : Site FR/EN ↔ Zenodo (19266862 / 19431208) ↔ Wikidata `Q139771989` concordants sur titre, date, DOI, auteur, abstract. Absent d'OpenAlex.
- **AWP-06** : date, DOI, auteur concordants partout. **Écart de titre** : le site affiche le titre court (sans sous-titre) ; Zenodo et Wikidata `Q139771994` portent le titre complet « … : data centers, IA et déplacement du désordre ». Même œuvre, identification non ambiguë via DOI → AMÉLIORABLE. Absent d'OpenAlex.
- **OpenAlex** : la fiche auteur `A5130851063` ne liste qu'AWP-02/03/04/05 (chacun en doublon concept+version DOI, artefact Zenodo standard). AWP-01 et AWP-06 non encore indexés → **COHÉRENCE_EXTERNE**, latence d'indexation hors contrôle du site, à re-vérifier pendant la fenêtre.

### Dimension 6 — État des liens externes critiques — **RAS bloquant**
Profils : ORCID, Zenodo (308 normal → records), OpenAlex, Google Scholar, Academia, Wikidata, IdRef, SocArXiv → HTTP 200 / redirections propres. **SSRN** `author=11065608` → 403 : anti-bot probable, **non concluant** (à vérifier manuellement depuis un navigateur), pas classé « cassé ». Les 12 PDF Zenodo des AWP → HTTP 200. Liens d'achat Amazon (popover JS, shortlinks `amzn.eu`/`a.co`) et couvertures → fonctionnels. Le « 404 » du chemin `records/19269486` est traité en § 2 (concept DOI, résolution valide).

### Dimension 7 — Critères pages livres — **RAS bloquant**
Les deux ouvrages anthropiques (ANTHROPIE, Dette Publique) : titre, ISBN, argument éditorial, sommaire structuré, liens d'achat 7 marchés, JSON-LD Book + sameAs Wikidata, maillage texte + `related_awp` (rendu via `layouts/partials/book-related-awp.html`). *Livresque des mots* correctement traité comme hors corpus (`serie autres-ouvrages`, pas de `related_awp`), seul résidu : le `about = Anthropie` (déjà compté en Dim. 3).

---

## 5. Journal post-90 jours (AMÉLIORABLE, sans proposition de patch)

À reprendre après la fenêtre, par ordre de valeur GEO décroissante :

1. **Single-source de la définition canonique** — `canonicalDefinition` (`params.toml`) n'est consommé par aucun template ; harmoniser accueil / AWP / page concept sur la formulation de référence via un partial réutilisable (symptôme de classe, pas incident isolé).
2. **Distinction anthropie ≠ Anthropocène** à ajouter sur la page concept (`content/quest-ce-que-lanthropie/_index.md`), au même rang que la distinction anthropie ≠ entropie déjà présente.
3. **Uniformiser le DOI exposé des AWP** — trancher concept DOI vs version DOI pour les 6 AWP ; aujourd'hui AWP-05 FR est le seul à citer son concept DOI (`content/awp/awp-05.md:12-13`).
4. **Commit + déploiement du 9ᵉ `sameAs` SocArXiv** (`data/author.toml`) pour aligner le live sur la source.
5. **Titre AWP-06** — décider si le sous-titre « : data centers, IA et déplacement du désordre » doit figurer sur la page site comme sur Zenodo/Wikidata.
6. **`about = Anthropie` orphelin** sur *Livresque des mots* — conditionner l'injection `about` à l'appartenance au corpus anthropique (`layouts/livres/single.html:53`).
7. **JSON-LD ItemList sur `/livres/`** — enrichissement de la page liste.

---

## 6. Pistes d'observation pour les 90 jours

Indicateurs externes à surveiller (sans intervention sur le code) :

- **OpenAlex** : apparition d'AWP-01 et AWP-06 dans la fiche auteur `A5130851063` (signal d'indexation Crossref/DataCite aboutie).
- **Téléchargements Zenodo par AWP** : suivi `unique_downloads` (cf. décision reportée sur le compteur `/serie-awp/`, rappel programmé au 2026-06-22).
- **Search Console / Bing Webmaster « AI Performance »** : requêtes d'entrée, impressions sur « anthropie », confusion éventuelle avec « Anthropocène » (corrobore la priorité n°2 du journal).
- **GoatCounter** : pages d'entrée, part des pages AWP vs home, profondeur de parcours.
- **Mentions externes** : citations Google Scholar, backlinks `.edu`, reprises, items Wikidata enrichis par des tiers.
- **SSRN** : vérifier manuellement (hors crawl) que la page auteur `11065608` reste publique (403 constaté en audit = anti-bot, non concluant).

---

*Rapport diagnostique terminal. Aucune action appliquée. Conforme à la doctrine de gel 90 jours (`PROJECT_STATUS.md` § 7) : seul un défaut bloquant aurait justifié une intervention immédiate ; aucun n'a été détecté.*
