# Audit diagnostique comparatif — J+90 — stephane-lalut.com

## 1. En-tête

- **Date de l'audit** : 2026-08-22 (J+91 depuis la base de comparaison)
- **Base de comparaison** : `audits/diagnostic-2026-05-23.md` (J+0)
- **HEAD au moment de l'audit** : `b399315` — **244 commits** depuis `c8a44a3` (HEAD du J+0)
- **Périmètre** : comparatif et diagnostique pur. Aucune modification de fichier du site, aucun patch proposé. Le seul fichier écrit est le présent rapport.
- **Nœuds externes relus À LA SOURCE** (sans passer par une synthèse antérieure) : OpenAlex (API works + authors), DataCite (API dois), Zenodo (API records, 16 dépôts), ORCID (API pub v3.0), Wikidata (API wbgetentities + historique de révisions), OpenLibrary (API authors/works/search), Google Scholar (profil public), SSRN, GoatCounter.

### ⚠ Exclusion déclarée — le bilan à quatre points n'existe pas

La commande demandait un « bilan global comparatif J+0 / J+30 / J+60 / J+90 ».

**J+30 et J+60 n'ont jamais été produits.** Le répertoire `audits/` ne contient aucun
`diagnostic-compare-*.md` ; le gabarit `audits/prompts/diagnostic-compare-template.md`,
écrit le 2026-05-23 pour les trois échéances, n'a été exécuté aucune fois. Le workflow
qui portait les rappels (`audit-reminders-2026.yml`) a été supprimé le **2026-07-15**,
c'est-à-dire *avant* l'échéance J+60 — la suppression était planifiée, la reprise des
rappels hors GitHub ne l'a pas été.

Conséquence, dite plutôt que tue : **ce rapport est un comparatif à deux points, J+0 → J+90.**
Aucune trajectoire intermédiaire n'est reconstituable a posteriori, les instruments
concernés (Search Console, Bing AI Performance, GoatCounter) ne conservant pas
d'instantané daté côté dépôt. Ce qui est perdu l'est définitivement ; ce n'est pas
rattrapable par une lecture plus fine aujourd'hui.

---

## 2. Verdict opérationnel unique

> ### Défaut bloquant détecté : **NON** sur le site — **OUI** sur le graphe d'entité externe
>
> **Côté site** : les **7 items** du journal post-90 jours du J+0 sont **tous traités**. Aucune
> régression détectée sur les 7 dimensions d'origine. Le corpus est passé de 6 à 8 AWP
> (16 pages FR+EN), tous indexés et résolvables.
>
> **Côté graphe externe** : un défaut structurel **silencieux** est confirmé, que le
> dispositif de surveillance en place ne pouvait pas voir et n'a pas vu — **l'identité
> auteur OpenAlex est fragmentée en 9 entités distinctes** pour une seule personne.

### Point adjugé — le diagnostic du J+0 sur OpenAlex était faux dans sa cause

Le J+0 écrivait : *« AWP-01 et AWP-06 absents de la fiche auteur OpenAlex (latence
d'indexation Crossref/DataCite, **hors contrôle du site**) »*, classé COHÉRENCE_EXTERNE,
à re-vérifier pendant la fenêtre.

Relecture à la source, 2026-08-22 :

1. **Les travaux ne sont pas absents.** Les 16 DOI Zenodo des 8 AWP (FR+EN) renvoient
   HTTP 200 sur `api.openalex.org/works/doi:…`. **Zéro absent.** Ce que la fiche auteur
   ne montrait pas, l'index le contenait — *l'absence de trace n'était pas l'absence du fait*.
2. **Ce n'est pas une latence.** 91 jours après, la répartition n'a pas convergé ; elle
   s'est aggravée, chaque nouveau dépôt créant une entité de plus.
3. **Ce n'est pas hors contrôle.** La cause est une **défaillance de désambiguïsation
   auteur chez OpenAlex**, corrigeable par réclamation ORCID côté OpenAlex.

**La qualification « latence » a coûté trois mois.** Elle a transformé un défaut actionnable
en attente passive, et la re-vérification prévue au § 6 du J+0 n'a pas eu lieu faute
d'échéance J+30/J+60 exécutée.

---

## 3. Tableau récapitulatif des écarts par dimension — J+0 → J+90

| Dim. | Objet | J+0 (23 mai) | J+90 (22 août) | Évolution |
|------|-------|--------------|----------------|-----------|
| **1** | robots / sitemap / canonical / hreflang / IndexNow | RAS | RAS | = |
| **2** | `citation_*` sur pages AWP | AWP-05 FR : concept DOI ≠ version DOI | `doi_zenodo`/`url_zenodo` alignés sur `19269487` | ✅ **corrigé** |
| **3** | JSON-LD Person `/a-propos/` | 8 `sameAs` live vs 9 source | 9 clés en source, SocArXiv commité | ✅ **corrigé** |
| **3 / 7** | `about = Anthropie` sur *Livresque des mots* | injecté inconditionnellement | conditionné `ne .Params.serie "autres-ouvrages"` (`layouts/livres/single.html:161`) | ✅ **corrigé** |
| **3** | JSON-LD `ItemList` sur `/livres/` | absent | présent (`layouts/livres/list.html:50-67`) | ✅ **corrigé** |
| **4** | Définition canonique single-source | `canonicalDefinition` lu par aucun template | partial dédié + **garde de build** qui casse la compilation si le verbatim dérive (`baseof.html:1-2`) | ✅ **corrigé, au-delà du demandé** |
| **4** | anthropie ≠ Anthropocène | absente de la page concept | section dédiée + entrée FAQ, **FR et EN** | ✅ **corrigé** |
| **5** | Titre AWP-06 | site court vs Zenodo/Wikidata complet | `subtitle` présent FR et EN | ✅ **corrigé** |
| **5** | Indexation OpenAlex | AWP-01/06 « absents », dit *latence* | **16/16 indexés, dispersés sur 9 entités auteur** | ⛔ **requalifié — AGGRAVÉ** |
| **6** | SSRN `11065608` | 403 anti-bot, non concluant | 403 anti-bot, non concluant | = (invérifiable depuis un runner) |
| **6** | PDF Zenodo | 12/12 HTTP 200 | 16/16 HTTP 200 | = (périmètre élargi) |
| — | **OpenLibrary — doublons LIT** | non instruit au J+0 | **NON fusionnés** : 2 fiches auteur, 2 œuvres *Livresque* | ⛔ **NOUVEAU — ouvert** |
| — | **Google Scholar** | profil listé en `sameAs` | **profil public, actif, 17 citations, h = 3** | ⚠ **NOUVEAU — décision caduque** |
| — | **Publication tierce indexée** | aucune | RFSE n° 36, `10.3917/rfse.036.0247` | ⚠ **NOUVEAU — à confirmer** |

---

## 4. Journal post-90 jours du J+0 — statut des 7 items

Vérification déterministe dans le dépôt, pas sur déclaration.

| # | Item | Statut | Preuve |
|---|------|--------|--------|
| 1 | Single-source de la définition canonique | **FAIT** | `layouts/partials/canonical-definition.html` + `hugo.toml:19` (EN) / `:48` (FR) ; **garde de build** `baseof.html:1-2` : la compilation échoue si `canonicalDefinition` FR perd le mot « déplacent » |
| 2 | Distinction anthropie ≠ Anthropocène | **FAIT** | `_index.md:88-90` + FAQ `:10-11` ; miroir EN `_index.en.md:99-105` + FAQ `:17-18` |
| 3 | Uniformiser le DOI exposé | **FAIT** | `content/awp/awp-05.md:12-13` → `19269487` (version DOI), aligné sur les 5 autres |
| 4 | 9ᵉ `sameAs` SocArXiv | **FAIT** | `data/author.toml:73-74` commité ; 9 clés présentes |
| 5 | Sous-titre AWP-06 | **FAIT** | `awp-06.md:3` et `awp-06.en.md:3` |
| 6 | `about = Anthropie` orphelin | **FAIT** | `layouts/livres/single.html:160-165`, condition `ne .Params.serie "autres-ouvrages"` |
| 7 | `ItemList` sur `/livres/` | **FAIT** | `layouts/livres/list.html:50-67` |

**7/7.** Aucun report, aucun abandon. L'item 1 a été traité au-dessus du niveau demandé :
la doctrine ne s'est pas contentée d'un partial, elle a ajouté une garde qui **casse le
build** — le seul mécanisme qui empêche la définition canonique de dériver en silence.

La clôture était **déjà journalisée** : `PROJECT_STATUS.md:1339`, entrée du **2026-06-15**,
« Clôture du journal post-90j de l'audit GEO ». La vérification ci-dessus ne la découvre donc
pas — elle la **corrobore dans le code**, ce qui est le seul moyen de distinguer un journal
juste d'un journal optimiste.

---

## 5. Indicateurs externes au jour de l'audit

### 5.1 OpenAlex — ⛔ le constat central

**9 entités auteur distinctes** pour une seule personne, réparties sur les 16 dépôts AWP :

| Entité OpenAlex | Nom porté | Travaux rattachés |
|---|---|---|
| **`A5130851063`** *(déclarée sur le site et sur Wikidata P10283)* | Stéphane Lalut | AWP-02/03/04/05 **FR** + RFSE |
| `A5133048122` | Stéphane Lalut | AWP-02/03/04 **EN** |
| `A5134537460` | **Stephane LALUT** | AWP-07 FR + EN |
| `A5143515672` | Stéphane Lalut | AWP-08 FR + EN |
| `A5130783250` | Stéphane Lalut | AWP-01 FR |
| `A5132995417` | Stéphane Lalut | AWP-01 EN |
| `A5133063046` | Stéphane Lalut | AWP-05 EN |
| `A5135611613` | Stéphane Lalut | AWP-06 FR |
| `A5135698507` | Stéphane Lalut | AWP-06 EN |

L'entité canonique — celle que le site expose en `sameAs`, celle que Wikidata déclare en
P10283, celle que le healthcheck mensuel interroge — porte **4 des 16 travaux du corpus**.

**Ce que la source dit, et qui disculpe le dépôt :**

- **Zenodo** : les **16** dépôts portent le **même** créateur `Lalut, Stéphane` et le **même**
  ORCID `0009-0002-1794-4895`. Aucune dérive de saisie.
- **DataCite** : l'ORCID est bien propagé, en `nameIdentifier` de scheme `ORCID`, sur tous
  les enregistrements contrôlés (AWP-01, 02, 06, 07), tous en état `findable`.
- **OpenAlex** : les 9 entités portent `orcid: None`. **La rupture est entre DataCite et
  OpenAlex**, pas en amont.

> **Hypothèse de cause, non vérifiée — à traiter comme telle.** Les `nameIdentifiers` DataCite
> exposent l'ORCID en forme **nue** (`0009-0002-1794-4895`), sans `schemeUri` ni forme URI
> `https://orcid.org/…`. C'est une cause plausible de non-appariement côté OpenAlex. Elle
> **n'est pas démontrée** et ne doit pas être écrite comme un fait : le seul constat établi
> est que l'ORCID est présent chez DataCite et absent chez OpenAlex.

**Métriques de la fiche canonique** : `works_count` 9 · `cited_by_count` **0** · `orcid` **absent** ·
`updated_date` 2026-08-08. Le `cited_by_count` à 0 chez OpenAlex, contre 17 citations chez
Google Scholar, ne se lit pas comme une contradiction : les deux ne comptent pas le même
périmètre de sources. Il se lit comme **une conséquence de plus de la fragmentation**.

### 5.2 Zenodo — 16 dépôts

| Dépôt | vues | téléch. | uniques | Dépôt | vues | téléch. | uniques |
|---|---:|---:|---:|---|---:|---:|---:|
| AWP-01 FR | 275 | 392 | 342 | AWP-01 EN | 182 | 348 | 322 |
| AWP-02 FR | 122 | 437 | 396 | AWP-02 EN | 82 | 442 | 401 |
| AWP-03 FR | 117 | 273 | 258 | AWP-03 EN | 178 | 323 | 298 |
| AWP-04 FR | 89 | 417 | 380 | AWP-04 EN | 152 | 414 | 384 |
| AWP-05 FR | 108 | 324 | 296 | AWP-05 EN | 153 | 356 | 335 |
| AWP-06 FR | 101 | 399 | 367 | AWP-06 EN | 140 | 251 | 224 |
| AWP-07 FR | 49 | 98 | 94 | AWP-07 EN | 47 | 333 | 307 |
| AWP-08 FR | 20 | 94 | 88 | AWP-08 EN | 47 | 77 | 67 |

**Total : 1 780 vues, 4 978 téléchargements, 4 559 uniques.**

> **Ce chiffre ne circule pas nu.** Sur 15 dépôts sur 16, les **téléchargements dépassent les
> vues**, souvent d'un facteur 3 à 5 (AWP-02 EN : 442 téléchargements pour 82 vues ; AWP-07 EN :
> 333 pour 47). Un lecteur humain voit la page avant de prendre le PDF. Ce profil est celui
> d'un **accès direct au fichier**, majoritairement automatisé — agrégateurs, moissonneurs,
> robots. **Couverture : preuve directe sur le compteur, aucune sur la qualification du
> trafic.** Ces valeurs relèvent de l'étage *éligibilité*, pas de l'étage *traction* ; les
> lire comme un lectorat serait une faute de niveau. Rappel du protocole : incident de
> comptage Zenodo du 2026-05-15, les valeurs absolues restent fragiles, seule la tendance
> trimestrielle est lisible.

### 5.3 Google Scholar — ⚠ le profil existe et il compte

`J4NqzwSfrHAC` — profil **public**, HTTP 200, libellé « anthropie ».

| | Toutes | Depuis |
|---|---:|---:|
| Citations | **17** | 17 |
| indice h | **3** | 3 |
| indice i10 | 0 | 0 |

**12 travaux listés**, dont 5 cités : *What is anthropy ?* (5) · *3.3 million years…* (4) ·
*ANTHROPY — Order here* (4) · *Public Debt and Anthropy* (2) · *Energy Transition, or
Anthropic Transfer ?* (2).

> **Qualification obligatoire — et l'appareil la portait déjà.** `data/works.yaml` mesure
> lui-même, par travail, un champ `citation_pattern` dont les valeurs au dernier relevé sont
> sans ambiguïté : AWP-01 « **auto-circulation présumée** (cité par AWP-02 à 06) »,
> `citations_observed: 4` ; AWP-02 « **auto-circulation confirmée** 2026-05-08 (cité par
> AWP-03/04/05) », `citations_observed: 3` ; AWP-03 et AWP-04 « auto-circulation présumée »,
> 2 et 1. **Le dépôt établissait déjà que ces citations sont internes** — il n'y a rien à
> re-découvrir sur ce périmètre.
>
> Ce qui n'est **pas** instruit, c'est l'**écart** : le relevé interne totalise une dizaine de
> citations au printemps, Google Scholar en affiche **17** aujourd'hui, dont 4 sur l'ouvrage
> *ANTHROPY* qui n'entre pas dans le registre AWP. **Le constat exact est donc : ~10 citations
> documentées comme auto-circulation, un delta d'environ 7 non instruit.** C'est ce delta —
> et lui seul — qui peut porter un signal de traction. Un h de 3 avec i10 à 0 reste par
> ailleurs **compatible avec un graphe entièrement interne**. Hypothèse à instruire, jamais
> une correction de l'objet.

### 5.4 Wikidata — pas d'enrichissement tiers substantiel

Les 6 items AWP `Q139771989`…`Q139771994` portent chacun 8 propriétés
(P31, P50, P356, P361, P407, P577, P921, P953). L'item auteur `Q138909233` en porte 17.
Les items des travaux plus récents existent : `Q140446195` (AWP-07), `Q140680750` (AWP-08),
`Q140517745` (*Livresque des mots*), `Q141072263` (*La Société du premier coup*).
P800 de l'item auteur liste **15 œuvres notables**.

**Historique des révisions** : les modifications de la période sont le fait de
`Laura Moreau` via QuickStatements (ajout du label et de la description **espagnols** sur
`Q139771989` le 2026-08-05, correction concept DOI → version DOI sur `Q139771993` le
2026-07-06 — répercussion propre du même arbitrage que l'item 3 du journal) et de `KrBot`
(maintenance). Une seule édition par un tiers non identifié au dossier : `MS Sakib` sur
l'item auteur, 2026-07-26.

**Conclusion : aucun enrichissement tiers substantiel en 90 jours.** Attendu à ce stade ; se
consigne, ne déclenche rien.

### 5.5 OpenLibrary — ⛔ les doublons LIT ne sont pas fusionnés

| Fiche auteur | Nom | Œuvres |
|---|---|---|
| **`OL16378291A`** *(déclarée en Wikidata P648, surveillée par le healthcheck)* | Stéphane Lalut | 7 |
| **`OL16378292A`** | Stéphane Lalut | 1 — *Livresque des mots — Anthologie inédite & éclectique de citations* |

L'item du J+90 — *« fusion des deux doublons LIT (statut Super-Librarian) »* — est
**NON FAIT**. Les deux fiches auteur coexistent toujours ; la seconde ne porte que
*Livresque*, tandis que la première porte déjà `OL45424544W` (*LIVRESQUE DES MOTS*) :
**la même œuvre existe donc en deux exemplaires sous deux auteurs différents.**

**Deux doublons d'œuvres**, sur la fiche `OL16378291A` — ce sont les « 2 doublons » que
`PROJECT_STATUS.md:11` annonçait à fusionner « après obtention du statut LIT (~1 semaine) » :

| Doublon | À CONSERVER | À FUSIONNER DEDANS |
|---|---|---|
| *Anthropie — Ordre ici. Dette ailleurs.* | `OL45424565W` *(canonique, `PROJECT_STATUS.md:11`)* | `OL45424564W` |
| *Dette Publique* | `OL45424600W` *(canonique, `PROJECT_STATUS.md:11`)* | `OL45424599W` (*: Qui paie vraiment ?*) |

Le point ouvert est donc **plus large que son intitulé** : ce ne sont pas seulement « deux
doublons d'œuvres », c'est **une fiche auteur en double par-dessus**, laquelle porte un
troisième exemplaire de *Livresque* face au `OL45424544W` déjà canonique. Les délais annoncés
en mai — « ~1 semaine », « ~1-2 semaines » — courent depuis **treize semaines**.

> **Nuance qui change le geste à faire.** D'après le relevé de la session du **2026-08-15**
> (non revérifiable depuis ce poste, donc rapporté et non attesté), une demande de fusion a
> été **envoyée** à `openlibrary@archive.org` couvrant exactement ces objets. Sept jours plus
> tard, **la source ne montre aucun changement**. Le geste dû n'est donc pas « demander la
> fusion » — c'est **relancer, ou obtenir le statut Super-Librarian et fusionner soi-même**.
> *Un courrier envoyé n'est pas un résultat obtenu* : sans contrôle à la source, l'envoi se
> serait confondu avec la réalisation, et le point serait resté clos à tort.

### 5.6 ORCID — le nœud sain du graphe

`0009-0002-1794-4895` : **36 travaux**, sources mêlées DataCite, Crossref et saisie auteur.
C'est **le seul nœud du graphe qui agrège correctement l'ensemble** : les 8 AWP (FR+EN),
les dépôts SSRN (`10.2139/ssrn.6615059`, `.6615278`, `.6615305`, `.6615438`, `.6735581`),
SocArXiv (`10.31235/osf.io/z6x38_v1`), les ISBN des ouvrages, les recensions OpenEdition
(`10.4000/162f0`, `10.4000/16ihm`), les tribunes, **et une version espagnole d'AWP-01**
(`10.5281/zenodo.21775366` / `.21766184`) qui n'apparaît nulle part ailleurs dans le
périmètre audité.

**Conséquence opérationnelle** : ORCID est complet et OpenAlex est fragmenté. Le levier de
réparation part donc du nœud sain vers le nœud cassé, jamais l'inverse.

### 5.7 Instruments non lisibles depuis ce poste — déclarés, pas tus

| Instrument | État | Motif |
|---|---|---|
| **Search Console** | non lu | authentification interactive ; lecture manuelle requise |
| **Bing Webmaster « AI Performance »** | non lu | idem |
| **GoatCounter** (`lalut.goatcounter.com`) | non lu | tableau privé — HTTP 303 vers connexion, API `/api/v0/stats/hits` → **401** |
| **SSRN** (`11065608`) | non concluant | HTTP **403** anti-bot, identique au J+0 — *ne pas classer « cassé »* |
| **Backlinks `.edu`, mentions presse** | non instruit | recherche manuelle, hors périmètre déterministe |

Les trois premiers portent précisément les questions du J+90 restées sans réponse :
requêtes d'entrée, impressions « anthropie », confusion « Anthropocène », CTR de la page
concept, pages d'entrée, profondeur de parcours, part AWP vs home. **Ces questions restent
entières.**

---

## 6. Anomalies nouvelles depuis le 23 mai

### A1 — ⛔ Identité auteur OpenAlex fragmentée en 9 entités

Voir § 5.1. **Gravité : ÉLEVÉE.** Défaut *silencieux* : il ne casse rien, ne produit aucune
erreur, et se contente de diviser par 4 la surface de l'auteur sur l'index académique le plus
moissonné par les moteurs génératifs. Chaque nouveau dépôt aggrave l'écart.

### A2 — ⛔ Doublons OpenLibrary non résorbés, et plus larges qu'annoncé

Voir § 5.5. **Gravité : MOYENNE.**

### A3 — ⚠ La décision « Google Scholar différé » est caduque — c'est la CHECKLIST qui a vieilli, pas le dossier

Le J+90 devait *« décider sur Google Scholar (création différée tant que circulation interne
non stabilisée — réévaluer) »*. **Le profil est créé, public, actif, et déclaré en quatre
endroits** : `data/author.toml:43`, Wikidata `P1960 = J4NqzwSfrHAC`, `PROJECT_STATUS.md:1492`,
et la table `NODES` du healthcheck mensuel.

**Attribution exacte de la faute, parce que soupçonner le mauvais document coûte autant que
ne rien soupçonner** : le dossier de pilotage n'a jamais été faux. `PROJECT_STATUS.md`
enregistre l'identifiant Scholar depuis le lot Wikidata de mai, et `data/works.yaml` porte
même la qualification d'auto-circulation. **C'est la checklist du J+90 qui a vieilli** — figée
au 23 mai, elle a transporté pendant trois mois une décision *« à rendre »* sur un objet
*déjà en production*, sans qu'aucun mécanisme ne la confronte à l'état réel.

**Ce n'est pas un cas isolé — c'est la moitié de la checklist.** Sur les **quatre** décisions
que le J+90 portait, **deux étaient déjà rendues** avant même d'être posées :

| Décision inscrite au J+90 | État réel, et depuis quand |
|---|---|
| « Décision sur Google Scholar — création différée » | Profil créé et déclaré au dossier **depuis le lot Wikidata de mai** |
| « Sortie de la phase 90 jours » | Gel levé par décision explicite de l'auteur le **2026-07-04** (`PROJECT_STATUS.md:1315`, état de phase `:1452`) |

**Gravité : MOYENNE**, et elle porte sur la classe, pas sur le cas : *une liste de contrôle
figée fabrique des faux positifs éternels.* Une checklist écrite le 23 mai pour être ouverte
le 22 août est, par construction, une **référence figée** — elle ne peut que vieillir, et rien
dans sa forme ne la confronte à l'état réel au moment où on l'exécute. C'est exactement la
classe de défauts qui ne se signale pas au moment où elle casse : ici, elle a fait *travailler*
sur deux questions mortes, ce qui est le coût symétrique de la méfiance — du vrai temps dépensé
à re-décider du déjà-décidé.

**Correctif de forme, applicable à la prochaine échéance** : une checklist d'audit différé
n'énonce pas des **décisions à rendre**, elle énonce des **questions à poser à l'état**
(« la phase est-elle close, et où est-ce écrit ? »). La première forme périme ; la seconde non.

### A4 — ⚠ Publication tierce indexée, non reflétée par le site

`10.3917/rfse.036.0247` — « Comptes rendus d'ouvrages », *Revue française de socio-économie*
n° 36, pp. 247-265, 2026-08-04. Crossref (**source primaire**, pas seulement OpenAlex) liste
**Stéphane Lalut** parmi 7 auteurs. Corroboré par le profil Google Scholar, qui porte aussi
*Valéry Ridde, La financiarisation de la santé au Sénégal* et *Arnaud Kaba, La main et
l'esprit* ; et par `data/works.yaml`, qui journalise déjà des recensions (Nonfiction) et une
tribune (*La Grande Conversation*, Terra Nova).

**Ce que l'audit établit** : la publication existe, elle est indexée, et l'attribution vient
du fournisseur, pas d'un artefact d'agrégateur.
**Ce que l'audit n'établit pas** : que ce soit bien l'auteur. Aucun ORCID n'accompagne
l'attribution chez Crossref. → **DÉCISION AUTEUR** (§ 7.5).

### A5 — ⚠ Le healthcheck vérifie la vie, pas la justesse

`healthcheck-external-nodes.yml` interroge 10 nœuds une fois par mois et n'alerte que sur le
code HTTP. Pendant les 90 jours :

- `OpenLibrary auteur` → **200** à chaque passage, pendant que la fiche double subsistait ;
- `OpenAlex auteur` → **200** à chaque passage, pendant que l'identité se fragmentait de 4 à 9 entités ;
- `Google Scholar` → **200** à chaque passage, sans jamais signaler que l'objet dont on
  « différait la création » existait.

> **Le contrôle partageait le filtre de ce qu'il contrôlait.** Il interroge exactement les
> URL déclarées par le dépôt, et une URL déclarée répond toujours — par construction. La
> question qu'il ne pose jamais est : *qu'est-ce qui n'entre jamais dans ce contrôle ?*
> Réponse mesurée : les 5 entités OpenAlex qui n'étaient pas dans `NODES`, et la fiche
> OpenLibrary qui n'y était pas non plus. **Un contrôle sans témoin positif est réputé
> ABSENT** ; celui-ci a rendu 100 % de verts en laissant passer les deux seuls défauts
> externes de la période.

### A6 — ⚠ `PROJECT_STATUS.md` nommait DEUX mauvaises propriétés Wikidata

Bloc « ## 3. Wikidata Q138909233 », `PROJECT_STATUS.md:1495-1496` :

| Écrit | Ce que la propriété est réellement | Propriété correcte, portée par l'item |
|---|---|---|
| `P3781 SSRN author ID` | **P3781 = `has active ingredient`** | **P3747** = SSRN author ID |
| `P5023 Academia.edu profile URL` | **P5023 = `activity policy in this place`** | **P5715** = Academia.edu profile URL |

**Le nœud vivant est juste** — `Q138909233` porte bien P3747 et P5715 — **seul l'état écrit
était faux**, sur deux lignes voisines. Gravité : FAIBLE en conséquence, mais ce n'est pas un
incident isolé : deux erreurs adjacentes dans le même bloc indiquent qu'il a été rédigé **de
mémoire plutôt que relu sur l'item**. C'est la forme canonique du défaut silencieux — un état
déclaré qui diverge de l'état réel sans rien casser, jusqu'au jour où quelqu'un s'y fie pour agir.

**Capillarité — surfaces contrôlées, une ligne chacune** :

- `PROJECT_STATUS.md` → **propagé** (corrigé, 2 lignes) ;
- `Wikidata/2026-07_GEO_alignement/ETAT_ACTUEL.md` → **sans objet**, porte déjà `P3747` ;
- `Wikidata/Import_Wikidata_Laura_2026-07-06/ETAT_ACTUEL.md` → **sans objet**, porte déjà `P3747` ;
- reste de l'arbre `D:\PRO` → **balayé**, `P3781` n'y apparaît nulle part ailleurs ;
- mémoire de session hors dépôt (`reference_graphe_entite_auteur`) → **propagé**, elle
  écrivait « P3747 Scopus » ;
- item Wikidata vivant → **sans objet**, jamais atteint par le défaut.

> **Corrigé dans la session, hors périmètre du présent audit** : la correction fait l'objet
> d'un **commit séparé**, précisément pour que ce rapport reste ce qu'il annonce — lecture
> seule. La solution étant connue et disponible, la reporter n'aurait eu aucun motif recevable.

---

## 7. Les quatre décisions propres au J+90

### 7.1 Sortie de la phase 90 jours — **SANS OBJET : elle a été prononcée le 2026-07-04**

Il n'y a rien à décider. `PROJECT_STATUS.md:1315` journalise une *« MODIFICATION DURABLE DE
LA RÈGLE : levée anticipée du gel structurel »* — décision explicite de l'auteur en session
GEO du **04/07**, sept semaines avant cette échéance — et `PROJECT_STATUS.md:1452` la porte
en état de phase : *« Depuis le 2026-07-04 : le gel calendaire est levé […] régime
interventions à la demande, validées par diff »*. Le journal post-90 jours avait lui-même
été clos plus tôt encore, le **2026-06-15** (`PROJECT_STATUS.md:1339`).

**Prononcer aujourd'hui une sortie déjà prononcée aurait reproduit exactement le défaut que
ce rapport diagnostique en A3.** Le dossier de pilotage était à jour ; c'est la checklist du
J+90 qui portait la décision comme pendante.

**Ce qui reste vrai et utile**, une fois l'item vidé de sa question : le **bilan** — c'est
ce rapport — et une **réserve à inscrire dans l'état**. La santé constatée porte sur **le
site**. Elle ne porte pas sur le **graphe d'entité**, où deux défauts restent ouverts (A1, A2)
et où la surveillance en place a démontré son inefficacité (A5).

### 7.2 Refonte du prompt projet « SITE INTERNET » — **la leçon d'usage est disponible**

Le retour d'usage des 90 jours ne porte pas sur la forme du prompt mais sur **ce que le
gabarit ne demandait pas** :

1. **Le gabarit ne demandait aucune vérification d'identité entre nœuds.** Il demandait
   « OpenAlex : nombre de works listés, présence d'AWP-01 et AWP-06 » — une question de
   **présence sur une fiche**, à laquelle « absent » est une réponse valide et trompeuse.
   La bonne question était : *chaque travail est-il rattaché à la MÊME entité auteur ?*
   Formulation à retenir : **partir du travail vers l'auteur, jamais de l'auteur vers le travail.**
2. **Le gabarit acceptait « latence » comme conclusion.** Aucune échéance n'était attachée
   à cette qualification, donc rien ne l'a jamais périmée. Toute qualification de type
   « attendre » doit désormais porter **une date de péremption et un test de sortie**.
3. **Le gabarit ne se lisait pas lui-même.** Il prévoyait trois exécutions ; aucune trace
   n'était prévue pour constater qu'elles n'avaient pas eu lieu.

→ Rédaction **différée à une session dédiée**, motif déclaré : la refonte du prompt est un
arbitrage de méthode, pas un correctif ; la traiter dans le même geste que l'audit
mélangerait la mesure et l'instrument.

### 7.3 Google Scholar — **décision SANS OBJET, à retirer du dossier**

Le profil existe, il est public, il porte 17 citations et un h de 3. La décision inscrite
(« création différée ») décrivait un état faux. **À supprimer des points ouverts**, et à
remplacer par un point de mesure : *dépouiller la liste « Cité par » pour établir la part
d'autocitation* — sans quoi le 17 restera un chiffre nu (§ 5.3).

### 7.4 `healthcheck-external-nodes.yml` — **GARDER, mais la présomption est inversée**

Test de suppression appliqué, présomption inversée : ce n'est pas à qui veut le supprimer de
prouver son inutilité, c'est à qui veut le garder de prouver son **utilité présente**.

**Ce qu'il apporte** : coût quasi nul (1 exécution/mois), aucune maintenance sur la période,
détection réelle d'une disparition de nœud — panne franche, irréversible côté graphe, et
qui ne se signalerait autrement jamais. Il a par ailleurs **documenté son propre angle mort**
dans ses commentaires (exclusions SSRN et IdRef, avec le raisonnement complet sur le HTTP 000
depuis les runners) : c'est un contrôle qui dit ce qu'il ne couvre pas.

**Ce qu'il n'apporte pas** : aucune garantie de justesse (A5).

→ **Conservé.** Il satisfait l'exception : conséquence externe grave et difficilement
réversible, et son intensité est proportionnée. **Condition de mort écrite** : il disparaît
le jour où il aura passé **douze mois consécutifs sans qu'aucun de ses passages ne change
d'état** — ce prédicat, et pas une date, vaut décision de suppression.

⚠ **Il ne doit PAS être étendu** pour couvrir A1 ou A2. Un contrôle qui compare des identités
serait un nouveau dispositif permanent, et le défaut qu'il viserait est **ponctuel et
réparable une fois** : on répare, on ne surveille pas. La vérification d'identité de graphe
relève de l'audit périodique — geste humain, cadence trimestrielle — pas d'un cron.

### 7.5 Ce qui remonte à l'auteur — 3 gestes, aucun automatisable

| # | Geste | Pourquoi l'auteur, et pas moi |
|---|---|---|
| **G1** | **Réclamer les 9 entités OpenAlex** sous l'ORCID `0009-0002-1794-4895` et demander leur fusion sur `A5130851063` | Compte externe, action irréversible côté tiers |
| **G2** | **RELANCER** la demande de fusion OpenLibrary du 15/08 restée sans effet, ou fusionner soi-même : fiche auteur `OL16378292A` → `OL16378291A` ; œuvres `OL45424564W` → `OL45424565W` et `OL45424599W` → `OL45424600W` | Requiert le statut Super-Librarian — droit attaché à la personne |
| **G3** | **Confirmer ou infirmer** la recension RFSE `10.3917/rfse.036.0247` | Fait biographique : nul ne peut le vérifier à la place de l'auteur |

Si G3 est **confirmé**, deux conséquences suivent, à traiter dans la session qui reçoit la
réponse : l'ajouter à `data/works.yaml` et à la page publications ; et vérifier que la
recension est bien rattachée à l'ORCID chez Crossref — c'est aujourd'hui la seule
publication du corpus qui n'y est pas attachée côté fournisseur.

---

## 8. Recommandations pour la fenêtre suivante

**Peut continuer en l'état** — le site. Les 7 dimensions du J+0 sont saines, la définition
canonique est protégée par une garde de build, le corpus a doublé sans régression
structurelle. Aucune intervention de fond n'est motivée.

**Mérite une action** — le graphe externe, par gravité décroissante :

1. **A1**, OpenAlex, gravité ÉLEVÉE → G1. Coût faible, effet large, et le défaut s'aggrave à chaque dépôt.
2. **A2**, OpenLibrary, gravité MOYENNE → G2.
3. **A3**, état écrit périmé sur Google Scholar → correction du dossier de pilotage, coût nul.
4. **§ 5.3**, dépouillement « Cité par » → transforme un chiffre nu en mesure de traction, ou l'infirme.

**Peut être abandonné comme non pertinent :**

- La **surveillance de « l'apparition d'AWP-01 et AWP-06 chez OpenAlex »** (§ 6 du J+0) :
  la question était mal posée, ils y sont depuis le début. Elle est remplacée par A1.
- La **décision « création Google Scholar »** et la **« sortie de la phase 90 jours »** :
  sans objet toutes les deux, rendues respectivement en mai et le 04/07 (§ 7.1 et § 7.3).
- Toute **reconstitution de J+30 et J+60** : les instruments ne conservent pas d'historique
  exploitable ; ce serait fabriquer une trajectoire au lieu de la mesurer.

**Ce qui reste entier et non instruit** : Search Console, Bing AI Performance, GoatCounter,
SSRN, backlinks `.edu` et mentions presse (§ 5.7). Ce ne sont pas des résultats nuls, ce sont
des **cellules non lues** — la distinction est celle du § 2 du protocole de mesure, et la
confondre reviendrait à conclure d'un instrument sur ce qu'il ne regarde pas.

---

*Rapport diagnostique comparatif terminal. Aucune action appliquée sur le site.
Toutes les valeurs externes ont été relues à la source le 2026-08-22, sans intermédiaire
d'une synthèse antérieure.*
