# Project Status — stephane-lalut.com

## Bilan 2026-05-13 — Chantier diffusion clos

Synthèse des 4 axes de diffusion exécutés en mai 2026 ; le chantier est désormais clos pour la durée de la fenêtre GEO/diffusion 90 jours.

1. **Wikidata** : Phase A + B + C exécutées (lots `Lalut-Anthropie-PhaseA/B/C-2026-05-12/13`). 6 items AWP créés (`Q139771989` à `Q139771994`). Correction DOI Option B effectuée (12 suppressions manuelles). Script Python d'automatisation v1.0 dans `Wikidata/scripts/` (fetchers Zenodo/Crossref/OpenLibrary + generators awp/article/book + validators garde-fous P9934/P407).

2. **SocArXiv** : 6 AWPs déposés sur `osf.io/ymkpj`. DOIs SocArXiv liés en P953 sur les 6 items AWP Wikidata. Profil OSF `ymkpj` rattaché à `Q138909233` (Stéphane Lalut) via P973.

3. **OpenLibrary** : 4 fiches livre + page auteur enrichie. Author ID `OL16378291A`. Work IDs : Livresque `OL45424544W`, L'Odyssée `OL45424562W`, ANTHROPIE `OL45424565W`, Dette Publique `OL45424600W`. Batch 16 (P648 OpenLibrary IDs) transmis à Laura. 2 doublons OpenLibrary à fusionner après obtention du statut LIT (~1 semaine).

4. **Externe** : BnF dépôt légal régularisé, Bing Webmaster Tools configuré (import Google Search Console + sitemap), GitHub Actions IndexNow + Wayback Machine opérationnels (commit `ab86532`).

**Phrase de pilotage maintenue** : *« la prochaine preuve viendra des tiers ».*

**Statut final** : chantier diffusion clos. Aucune action structurelle prévue pendant les 90 jours GEO/diffusion. Actions résiduelles passives :
- Laura exécute le batch 16 OpenLibrary (~24h)
- Stéphane fusionne les 2 doublons OpenLibrary après obtention du statut LIT (~1-2 semaines)
- Surveillance Bing Webmaster Tools « AI Performance » + log mensuel Wayback Machine (`Wayback/archive-log.md`)

## Mise à jour 2026-05-13 — Workflows IndexNow + Wayback Machine

- **`.github/workflows/indexnow.yml`** : notification temps réel à Bing/Yandex
  après chaque push touchant `content/**`, `data/**`, `layouts/**`, ou la config.
  Sécurité supplémentaire : run hebdomadaire le lundi.
  La clé IndexNow est détectée dynamiquement depuis `static/<key>.txt`.

- **`.github/workflows/wayback-archive.yml`** : archivage mensuel (1er du mois,
  6h UTC) de toutes les URLs du sitemap sur Wayback Machine. Log cumulatif
  committé dans `Wayback/archive-log.md`.

Les deux workflows sont indépendants. IndexNow se déclenche à chaque push
significatif (notification immédiate). Wayback s'exécute mensuellement
(archivage long terme).

**Status** : workflows créés, non encore poussés en production. Stéphane
valide visuellement les YAML avant push manuel.

**Premier test recommandé** : déclencher manuellement chaque workflow via
l'onglet Actions du repo GitHub après push, pour vérifier que la chaîne
complète fonctionne sans attendre le prochain push naturel ou le 1er du mois.


> **À lire avant** : toute intervention sur le site, technique 
> ou éditoriale. Décrit l'état architectural, les doctrines 
> en place, les chantiers en cours et les chantiers reportés.
> Dernière mise à jour : 2026-08-02.
> **Règle de fraîcheur** : l'état écrit suit l'acte — toute session qui
> exécute met à jour ce log ET les statuts des registres/backlogs touchés
> dans la même session. Un statut périmé vaut défaut : il provoque la
> re-exécution de l'acquis ou l'abandon de travaux crus « déjà faits ».

## 0. Log chronologique

### 2026-08-01/02 — Contrôle visibilité EN, sync registres, arbitrages GEO-01/02/03

**Contrôle GEO EN (01/08, mode IA Google + WebSearch neutre)** : le concept
est VISIBLE en anglais — « The Socioeconomic Hypothesis » (Lalut) en section 2
du mode IA EN sur « anthropy » ; requête conceptuelle sans le mot entièrement
construite sur l'hypothèse ; **SSRN 6543618 n°1 hors personnalisation** (le
dépôt SSRN est devenu le premier actif EN). Nuance auteur : « Anthropy » nue
en navigation privée FR = entités commerciales seules (bataille de fréquence
de corpus — ne se corrige pas on-site). **Verdict : plateau on-site, maillage
auto-génératif par inférence de requêtes REJETÉ** (anti-doorway, moratoire,
non-cannibalisation). Topo : `Downloads/TOPO_GEO_EN_2026-08-01.md`.

**Sync registres avec l'édition anglaise du 21/07 (3 commits)** :
**9d106f2** `works.yaml` v1.10 (bloc `english_edition`, `site_pages.en`,
`abstract_short.en`) + `intent_matrix.yaml` (condition doctrine remplie) ;
**10cb115** `llms.txt` (AWP-08 manquant, « eight », édition EN) ;
**912bf1d** `check-geo-coverage.py` section [5] miroir EN (12/12 ok).
Hors dépôt : `08_ENGLISH_STRATEGY.md` interdit n°1 annoté caduc (ANTHROPIE
seul) ; `12_IMPLEMENTATION_BACKLOG.md` statuts rafraîchis et sourcés (B8/C1/
C2/C4/C6/D1/D4 = faits ; C5 seul incertain ; C7 échéance 24/08) ;
fiche T1 `reports/geo_audit/T1_SONDES_EN_2026-09-15.md` (5 sondes, double
lecture connecté/privé + instrumentation).

**Arbitrage GEO-03 (02/08, investigation externe)** : déploiement France
effectif le **22/07** (AI Mode généralisé, AIO sélectif) — le re-test
« ~23/09 » est fusionné dans T1 15/09. Guide Google màj 10/07 : RAG sur
ranking classique + query fan-out (pas de canal IA séparé) ; « no special
schema.org markup needed » → **gel de tout schema motivé par l'IA** ;
éligibilité snippets = condition d'inclusion (vérifié : 0 nosnippet sur le
site). Search Console : rapports « Search generative AI » + toggle (défaut =
inclus) à surveiller. Attente clics : **−30/−50 % de CTR** sur requêtes
couvertes — piloter aux impressions/absorption, pas aux clics. Recherche
2026 : réécritures « citables » agressives peuvent dégrader le retrieval
(anti-surcouche corroboré) ; viser l'absorption (densité de preuves
extractibles). GEO-01/02/03 : arbitrages rendus, notes closes.

**Rattrapage log — vague « nasse » de juillet (post-09/07, cf. git log)** :
mailles P0/P1 (fd041d7, 1692057), `/communs-negatifs/` (8d9492c),
`/chercheur-independant/` (d5b0e4e), `/livresque/methode-et-corpus/`
(affbc96), **linter `scripts/check-geo-coverage.py`** (318f703), **AWP-08**
FR+EN (04456c9, 23/07), **édition anglaise ANTHROPY** sur le site
(c67176e, 21/07), mailles EN (c2b1623, 1b6ba69), og:image par entité
(f6fb13a, cc43dbe). Wikidata : import fait, état vérifié par API le 01/08
(af4ba03). Obsolètes dans l'entrée du 09/07 : « baseline avant le 23/09 »
(lancement advenu le 22/07) ; T0 requêtes = fait le 09/07.

### 2026-08-02 (suite) — Multilingue : sondes ES/DE, dossier Wikidata, checklist langue

Sondes mode IA : ES = « antropía » occupé par le sens anthropisation, concept
absent ; DE = requête conceptuelle résolue vers **Lessenich /
Externalisierungsgesellschaft** (mêmes trois axes) — gate antériorité OK
(AWP-07 le démarque déjà). Verdict : aucune page ES/DE/JA sans produit ;
levier = entité Wikidata. Dossier de contre-expertise
`Downloads/WIKIDATA_LANGUES_Q138827949_2026-08-02.md` (corrections ES/DE/IT
dont dérive « mécanisme »→« hypothèse », ajouts it/pt/ja/zh/ru + ar/ko
recommandés ; import via Laura après arbitrage auteur). **Édition ES
d'ANTHROPIE annoncée par l'auteur (semaines à venir)** →
`docs/CHECKLIST_AJOUT_LANGUE.md` créée (séquence entité → produit → dépôt
tiers → surfaces → mesure, codifie le playbook EN ; contre-analyse GEO-04).

**Contre-expertise externe (ChatGPT) intégrée le 02/08** — verdicts amendés
et actés : moratoire on-site devient CONDITIONNEL (pages dérivées de
requêtes interdites ; nouvelle page = objet autonome + besoin observé +
lacune réelle) ; déclencheur langue assoupli (« actif public vérifiable »,
3 états privé/pré-ancrage/déploiement — checklist amendée) ; sur-affirmation
« SSRN n°1 mondial » corrigée (résultat daté/localisé, réplication sous
contrôle) ; « chaque langue a son Kapp » → chaque COMMUNAUTÉ intellectuelle
(ES : entrer par externalización de costes puis economía ecológica, CEPAL en
voisin, jamais en filiation) ; Wikidata GO RESTREINT (corrections ES/DE/IT,
labels latins par défaut ja/zh/ru/pt, AR/KO suspendus — addendum du dossier
Downloads) ; règle complétée « l'état interne suit l'acte, l'état externe
expire » (CLAUDE.md). **DÉCOUVERTE VÉRIFIÉE : collision de concept avec
anthropie.org** (« L'Anthropie », édifice 12 couches, anonyme, CC0, GitHub
créé 29/04/2026, 0 star, empreinte recherche quasi nulle au 02/08) →
`reports/geo_audit/REGISTRE_COLLISIONS.md` créé (9 entrées), sonde S6 de
veille ajoutée au T1, signature composée adoptée (« Anthropie — l'hypothèse
du déplacement du désordre, formulée par Stéphane Lalut »). Grille de
reprise en 4 niveaux (hébergement/mention/citation/application) intégrée
au T1 — les mesures d'août prouvent la récupération machine, pas encore
l'usage autonome par des tiers : c'est l'objectif des échéances 24/08+.

### 2026-07-09 — Rounds GEO-03/GEO-04 : indexation réparée, site-graphe ancré, lot 1 exécuté

Missions `_Consignes_GEO-03/04/05.txt` (audits + GO auteur item par item).

**GEO-03 (commis le 09/07, poussé sur GO)** : `fix(indexnow)` **2f3dae2** — le
workflow soumettait les **2 sitemaps XML** au lieu des pages depuis le passage
multilingue (la racine est un sitemapindex, IndexNow n'expanse pas) ; récursion
+ garde-fou <10 URLs = échec explicite. `docs(geo)` **d1785c6** checklists
ajout livre/publication. `fix(seo)` **b250cdf** aliases
`/en/what-is-anthropy/` (+ racine) — répare le **backlink Wikidata Q138827949
P973** qui pointait un 404 depuis mai. ⚠ push bloqué : les jetons git/gh
n'ont pas le scope `workflow` — `gh auth refresh -s workflow` requis.

**GEO-04 (doctrine)** : `data/intent_matrix.yaml` (matrice d'intentions 5
cercles, statuts, en-tête anti-doorway dur — AUCUNE page ne se crée depuis ce
fichier), `docs/CHECKLIST_AJOUT_CONCEPT.md`, hooks checklists (**1098329**).
Décision d'architecture : works.yaml reste le registre canonique unique —
aucun des 10 fichiers YAML parallèles suggérés n'est créé. Rapport complet :
`reports/geo_audit/GEO04_KNOWLEDGE_GRAPH_PROPAGATION.md` (local, gitignoré).

**Lot 1 site-graphe (GO _Consignes_GEO-05, 6 commits atomiques)** :
① **1b73852** nœud `DefinedTerm #concept` émis sur la page concept FR+EN —
le sommet était référencé par AWP/livres/série mais défini nulle part ;
② **6cc3beb** FAQ rendues sur les 4 fiches livres (book-scoped strict : la
question « qui paie la dette publique ? » reste la propriété exclusive de la
page pont) + `schema-faqpage` résout les placeholders `{citations}` via
desc-figures ; ③ **4aeb00c** chiffres canoniques page offrir via source
unique (shortcode stat : fallback `stats_isbn` + séparateur nommé `nbsp`) ;
④ **750c7d3** bloc « Du même auteur » (BEM `.book-others`) ; ⑤ **5f76680**
EN : « Order here. Debt elsewhere. » + « a quotation anthology in the
lineage of the commonplace book » sur /en/books/ ; ⑥ **a387298** fraîcheur
légère : `lastmod` manuel aux dates git réelles (concept, AWP-01/02/05/06,
fiches livres) + `dateModified` JSON-LD conditionnel (`ne .Lastmod .Date`).
**Jamais `enableGitInfo`** (checkout CI shallow = fake-freshness globale).
⑦ BreadcrumbList **différé** (bénéfice quasi nul à 2 niveaux, décision auteur).

Restent (hors dépôt ou à la demande) : run manuel IndexNow post-push (lire le
nombre d'URLs au log), baseline GoatCounter clics amazon-outbound avant le
23/09 (lancement AI Overviews France), T0 requêtes Google FR distinct des 18
prompts assistants, item Wikidata Livresque à créer, lecture intent_matrix
par la routine GEO trimestrielle (arbitrage auteur).

### 2026-07-04 — MODIFICATION DURABLE DE LA RÈGLE : levée anticipée du gel structurel

Décision explicite de l'auteur (session GEO du 04/07) : le gel structurel 90 j
(échéance initiale ~2026-08-12) est **levé de manière anticipée et la règle est
modifiée durablement**. Nouveau régime :

- les interventions sur le site se font **à la demande de l'auteur**, validées
  par diff avant commit (méthodologie inchangée) — plus de fenêtre calendaire ;
- la doctrine de fond demeure : **diffusion > optimisation**, conversion par
  autorité, pas de contenu creux, quota de pages maîtrisé, protocole de mesure
  (`reports/geo_audit/GEO_PROTOCOLE_MESURE.md`) inchangé ;
- conséquence immédiate : la « rafale » planifiée pour le 12-26 août est
  **publiée ce jour** (2 pages-ponts + 2 pages offrir + GoatCounter events).

Contexte : audit GEO complet + méta-analyse croisée du 04/07 (13 + 8 livrables,
`reports/geo_audit/` et `reports/geo_authority_conversion_audit/`), 16 commits
de phase 1/1-bis/GEO-01/QEA déployés le même jour, passe Zenodo (verbatim +
dates) exécutée, dossier Wikidata prêt pour import.

### 2026-06-15 — Clôture du journal post-90j de l'audit GEO (harmonisation définition + DOI AWP-05)

Round demandé par l'auteur : « faire toutes les améliorations nécessaires pour
améliorer la visibilité GEO », sur la base de `audits/diagnostic-2026-05-23.md`.
Gel 90 j **explicitement levé** pour ces items (la worklist GEO différée du
journal post-90j *est* l'objet de la demande). Périmètre **non structurel** :
routing, hreflang, sitemap, canonical, JSON-LD machine = intacts ; seuls du
contenu/wording et un DOI de citation sont touchés.

**Re-audit read-only préalable (clé) :** l'audit du 23/05 (`c8a44a3`) était
largement périmé. **5 des 7 items du journal avaient déjà été traités** entre
`c8a44a3` et `fd9c353` : distinction Anthropocène (page concept), 9ᵉ `sameAs`
SocArXiv (`data/author.toml`), sous-titre AWP-06 propagé en `citation_title`/
`headline`, `about=Anthropie` conditionné à `serie != autres-ouvrages`
(`livres/single.html:77`), `ItemList` sur `/livres/` (`livres/list.html`).
Seuls 2 chantiers restaient réellement ouverts.

**Correctifs appliqués (2 commits atomiques) :**

- **`feat(geo)` `e6c6b8a`** — single-source du **verbatim** de la définition
  canonique (`canonicalDefinition` de `params.toml`/`hugo.toml`) sur les
  surfaces à plus forte autorité : accueil FR (`layouts/index.html:19`, 1ʳᵉ
  phrase du lede alignée sur le verbatim, nuance spatial/temporel/social
  conservée, symétrie avec le lede EN déjà canonique) ; AWP-01 FR+EN et AWP-06
  FR via `{{< canonical-definition >}}` en ouverture (paraphrase rétrogradée
  en « Plus précisément / More precisely »). AWP-06 EN inchangé (verbatim déjà
  en incise). Drafts `audits/phase2-drafts/` marqués appliqués. Closes l'item
  n°1 (priorité GEO du journal). Build OK, verbatim rendu vérifié sur 4 surfaces.

- **`content(awp)` `53c1c65`** — uniformisation du DOI exposé d'**AWP-05**
  (seul des 6 à exposer son **concept** DOI `…19269486` au lieu du **version**
  DOI `…19269487` de son `pdf_url` et des 5 autres). Aligné sur la convention
  « version DOI » du 29/05 — sens qui *rentre* dans la convention, jamais
  l'inverse (bascule version→concept toujours interdite). `awp-05.md`
  (doi_zenodo + url_zenodo) et `awp-05.en.md` (translation.doi cross-link).
  Version DOI vérifiée via `api.zenodo.org`. Closes l'item n°3.

**Journal post-90j de `audits/diagnostic-2026-05-23.md` : intégralement clos**
(5 items déjà faits + 2 ce jour). Reprise du gel jusqu'à l'échéance
~2026-08-12. Les indicateurs externes du § 6 de l'audit restent à surveiller
sans intervention (OpenAlex, téléchargements Zenodo, AI Performance).

### 2026-06-04/05 — Liens Amazon canoniques + purge anthropie.fr (correctif bloquant hors-gel)

Round `_Commandes-158` (audit READ_ONLY puis patch sur GO explicite). Deux défauts
bloquants avérés corrigés, gel 90 j respecté (même classe que l'intervention du 29/05).

- **`fix(livres)` `4341fd7`** : les 21 liens Amazon des 3 fiches livres étaient des
  **shorteners** (`amzn.eu/d/…`, `a.co/…`) avec **collisions avérées** (Dette DE/IT
  pointaient le shortener d'un autre livre ; Livresque CA = lien FR). Remplacés par
  les **URL canoniques `/dp/<ASIN>`** + **boutons séparés Broché / Kindle par marché**
  (`url_amazon_<mkt>` / `url_amazon_<mkt>_kindle`, partial `amazon-button.html`).
  L'`Offer.url` du JSON-LD devient canonique. ASIN vérifiés contre les données de
  compte KDP ; **vérifié en production** : 0 shortener, 5/5 liens échantillonnés
  résolvent vers le bon livre (dont les ex-collisions .it/.ca et les Kindle .es).
  Prérequis posé pour les tags **Amazon Attribution** (câblage prévu septembre 2026).
- **`docs` `c2a77a2`** : purge des mentions « site pour anthropie.fr »
  (CLAUDE.md/AGENTS.md/README → stephane-lalut.com). **Dossier domaine CLOS** :
  anthropie.fr n'a jamais été détenu (aftermarket Premium GoDaddy) — aucun rachat,
  aucune redirection. La production n'émettait aucune référence (vérifié :
  sitemap/canonical/llms.txt = 0 hit). Les mentions historiques exactes
  (§ correctif `/presse/` ci-dessous, docs/memo) sont conservées.

### 2026-05-29 — Audit GEO/SEO/sécurité + 4 correctifs ciblés (intervention hors-gel, non structurelle)

Audit read-only en 5 lots (GEO/IA, maillage, SEO, performance, sécurité) demandé par l'auteur. Verdict : **0 défaut bloquant** ; le gel 90 jours n'est donc pas rompu sur le fond. 4 commits atomiques appliqués sur des défauts *utiles* (non structurels) — routing, JSON-LD, `citation_*`, hreflang, canonical : **intacts**.

**Correctifs (commits `0e4d026`, `60b1db8`, `75920d9`, `44fb770`) :**

- **`/presse/`** (`fix(seo)`) : page orpheline (0 lien entrant), indexable et au sitemap, au contenu vacant et à l'e-mail `contact@anthropie.fr` **non délivrable** (domaine `anthropie.fr` sans enregistrement MX, vérifié par DNS ; le domaine vivant est `stephane-lalut.com`/OVH). Passée en `noindex` + sortie du sitemap (`_build.list: never`, `render: always`). **Mécanisme `noindex` créé** dans `head.html` (flag front matter `noindex: true` → `<meta name="robots" content="noindex, follow">`) — n'existait nulle part auparavant. E-mail mort remplacé par un lien vers `/contact/` (formulaire Formspree). *Étape B à la main de l'auteur : remplir le kit presse, retirer les 2 blocs front matter, ajouter le lien colonne « Ressources » du footer.*

- **`scripts/audit_works.py`** (`fix(audit)`) : faux positifs `citation_*`. `hugo --minify` retire les guillemets d'attribut (`name=citation_title`) que la regex exigeait → 12 pages AWP conformes signalées à tort. Les 11 balises `citation_*` + le JSON-LD ScholarlyArticle sont bien présents (vérifié sur le live). Warnings : **18 → 6** (reste = DOI SSRN externes, attendus).

- **CI** (`fix(ci)` + `chore(ci)`) : actions GitHub épinglées au **SHA** (étaient en tag mutable `@v4/@v3/@v7`) sur les 6 workflows, SHA résolus via l'API GitHub — durcissement supply-chain (reco OpenSSF, post-incident *tj-actions* 2025) sur des workflows à droits `pages:write`/`id-token:write`/`contents:write`. À rafraîchir au J+90 (rappel déjà outillé). Healthcheck mensuel : 403 anti-bot Academia rendu non bloquant (évite un faux positif/issue chaque mois) + casse URL alignée sur `author.toml`.

**Laissés volontairement (test de suppression) :** subsetting polices, image LCP home en CDN Amazon, CSP `<meta>`, bascule DOI version→concept. Sur ce dernier point : les DOIs Zenodo exposés sont les **DOI de version** (ex. AWP-01 …862) ; le DOI concept (…861) existe à −1 et résout aussi — **ne pas « corriger » version→concept** sans décision éditoriale (casserait l'historique Scholar). Vérifié via `api.zenodo.org`.

**Modifications structurelles : aucune.** Seul le sitemap perd `/presse/` (page non stratégique). Reprise du gel après ces commits.

### 2026-05-12 — Chaîne de boucles sur la home (4e patch, conclusion alignement AWP-06)

Quatrième et dernier commit de la fenêtre éditoriale d'alignement avec AWP-06 et la campagne de diffusion S9-S10 2026. Ajout d'une animation SVG cyclique (24 s desktop / 30 s mobile) qui suit littéralement le contour des cercles externes Spatial et Social sur la home, avec croisement en X au centre du cercle Temporel — overlay décoratif en background derrière les cercles HTML existants.

**Justification doctrinale :** cohérence de grammaire visuelle (boucle anthropique) avec la page théorique, différenciation par le rythme (24 s desktop / 30 s mobile vs 16 s page théorique) et par la composition (4 lignes droites tangentes + 2 grands arcs contournant les sphères externes, croisement Temporel en X — vs lemniscate asymétrique simple en page théorique). Chaque page doit signifier seule pour des publics multiples (chercheurs, journalistes, éditeurs) qui ne suivent pas un parcours linéaire.

**Périmètre :**

- Assets : `static/img/figures/chaine-boucles-desktop.svg` (viewBox 1000×543, path `M…L…A…L…L…A…L…Z`, N=2295, K=1148) et `chaine-boucles-mobile.svg` (viewBox 360×900, path L+A équivalent vertical, N=2172, K=1086). Animation SMIL `stroke-dashoffset` + comet `animateMotion` synchronisés (K = N/2 exact). `prefers-reduced-motion` respecté sur les 2 SVG. Pas de texte dans les SVG (les textes des trois axes restent en HTML pour SEO et accessibilité).
- Partial nouveau : `layouts/partials/figures/chaine-boucles.html`, bascule responsive via `<picture><source media="(max-width:768px)">`, `aria-hidden="true"` (overlay décoratif).
- SCSS composant nouveau : `assets/scss/_figure-chaine-boucles.scss`. Desktop : `position:absolute; top:-135px; height:540px` (débord vertical pour arcs dépassant la rangée des sphères, total 540px = 270 sphères + 135 haut + 135 bas). Mobile (`@media max-width:768px`) : `height:auto; bottom:0` (overlay couvrant l'ensemble du triad-wrapper). Importé après `figure-boucle-anthropique` dans `main.scss`.
- Intégration home (`layouts/index.html`) : ajout d'un wrapper `.axes-overlay-wrapper` autour de la grille `.axis-grid` existante. `.axis-grid` reçoit `position:relative; z-index:1` (additif, les cercles HTML passent devant l'overlay z-index:0). Aucune modification du markup ni des textes des trois cercles.

**Modifications structurelles : aucune.** Routing, JSON-LD, `citation_*`, schema.org, hreflang, sitemap, canonical : intacts. Cercles HTML et leurs textes (Spatial / Temporel / Social, directions, body) : intacts.

**Reprise du gel :** dernière intervention de la fenêtre d'alignement AWP-06. Le gel 90 jours reprend strictement après ce commit. Échéance approximative : 2026-08-12. Aucune intervention non bloquante prévue d'ici là.

### 2026-05-12 — Boucle anthropique : home + page théorique (alignement AWP-06)

Le gel 90 jours initié au commit 3975b24 (mai 2026) est interrompu pour une intervention éditoriale ciblée, explicitement validée par l'auteur, dont l'objectif est l'alignement du site avec AWP-06 avant la campagne de diffusion académique septembre-octobre 2026.

**Périmètre exact :**

- Home (`layouts/index.html`) : ajout d'un bloc texte « Une frontière contemporaine — L'attention comme réceptacle » sous la section des trois axes, avec lien sortant vers AWP-06 (`{{ "/awp/awp-06/" | relLangURL }}`). Bilingue FR + EN inline. Aucune illustration ajoutée sur la home.
- Page « Qu'est-ce que l'anthropie ? » (FR `content/quest-ce-que-lanthropie/_index.md` + EN `_index.en.md`) : ajout d'un paragraphe théorique (extériorisation cognitive + retour anthropique) inséré entre la section des trois axes et la section « Anthropie et entropie », suivi de la figure « La boucle anthropique » via shortcode.
- Assets SVG nouveaux (4) dans `static/img/figures/` : variantes FR par défaut + variantes `-en`, `boucle-anthropique-desktop[-en].svg` (lemniscate horizontale animée SMIL, viewBox 900×440) et `boucle-anthropique-mobile[-en].svg` (lemniscate verticale animée SMIL, viewBox 360×720). Comète + queue à 7 niveaux d'opacité sur les 4. `prefers-reduced-motion` respecté sur les 4.
- Partial nouveau bilingue : `layouts/partials/figures/boucle-anthropique.html`, double bascule langue (`.Lang`) + viewport (`<picture><source media="(max-width:768px)">`).
- Shortcode markdown nouveau : `layouts/shortcodes/boucle-anthropique.html` wrappant le partial avec contexte `.Page`.
- Composant SCSS nouveau : `assets/scss/_figure-boucle-anthropique.scss`, figure alignée sur la largeur du gabarit texte en desktop, full-bleed en mobile (`@media (max-width: 768px)`), caption serif italique plafonnée à 720 px. Importé après `page-common` dans `main.scss`.
- Bloc home « frontière contemporaine » : règles SCSS ajoutées dans `_home.scss` section 2 bis (tokens existants `--font-sans/serif`, `--fs-micro/h2/body/small`, `--color-text-*`, `--color-accent[-hover]` ; pas de nouveaux tokens introduits).

**Modifications structurelles : aucune.** Routing, JSON-LD, métadonnées `citation_*`, schema.org, hreflang, sitemap, balises canonical : intacts. Aucune classe BEM existante modifiée hors `_home.scss`.

**AWP : aucun modifié.** Le concept de boucle techno-cognitive introduit ici est inscrit dans le livre ANTHROPIE (622 p., ISBN 978-2-9586347-2-8) et préparé dans AWP-02 (migration des modalités vers le temporel et le cognitif) et AWP-06 (quatre registres couplés énergie/matière/territoire/attention). Un AWP-07 dédié pourra formaliser le concept lors d'une campagne de diffusion ultérieure distincte.

**Reprise du gel :** la phase GEO/diffusion reprend après ce commit. Aucune autre intervention non bloquante prévue avant la fin de la fenêtre 90 jours (échéance approximative ~2026-08-12).

## 1. État de phase

**Depuis le 2026-07-04** : le gel calendaire est levé (voir log § 0) — le site
est en régime « interventions à la demande, validées par diff », avec pour
priorité d'énergie la **diffusion** (campagne académique, AWP-07, nœuds
externes), pas l'optimisation on-site.

*(Historique : phase active GEO/diffusion 90 jours de mai à juillet 2026 ;
la phase de construction infrastructurelle initiale est close.)*

L'audit de bascule a livré le verdict OUI sans correction obligatoire.
Les 3 recommandations triviales (R1+R2+R3) ont été appliquées dans 
un mini-commit polish.

## 2. Architecture finale (état au commit polish)

### Source unique de vérité
- `data/author.toml` : 8 identifiants sameAs (ORCID, Zenodo community, 
  OpenAlex, Google Scholar, Academia, Wikidata, SSRN, IdRef)
- Consommé par 9 surfaces (5 JSON-LD machine + 4 visibles humain)
- 0 ORCID hardcodé dans `layouts/` ni `config/`

### Identité auteur
- Statut unifié : "Économiste — Chercheur indépendant et essayiste"
- Bilinguisme JSON-LD Person + eyebrow accueil (FR/EN selon `.Lang`)
- Cohérence sur 16 positions du site

### Vignettes /publications/
- Tout le corpus (10 fiches) en bloc typographique
- Alternance navy/crème stricte par compteur logoIndex
- Champ `source_type` : 5 catégories (Revue, Magazine, Quotidien, 
  Journal, Portail) + Académique réservée

### Pattern technique critique
- Schema.org : toujours `dict→jsonify→safeJS`, jamais de concaténation
- BEM SCSS : sélecteurs descendants explicites depuis modifier 
  (jamais `&__xxx` qui produit `.parent--mod__xxx`)

## 3. Wikidata Q138909233

7 P-propriétés renseignées par Laura :
- P269 IdRef ID : 283054085
- P1960 Google Scholar : J4NqzwSfrHAC
- P10283 OpenAlex ID : A5130851063
- P496 ORCID iD : 0009-0002-1794-4895
- P3781 SSRN author ID : 11065608
- P5023 Academia.edu profile URL
- P9934 Zenodo communities ID : anthropie-working-papers

Note : la communauté Zenodo `anthropie-working-papers` est 
**rattachée au Concept Q138827949** (anthropy), pas au Person. 
Sémantiquement plus juste : c'est une communauté de concept, 
pas d'auteur.

## 4. Doctrine éditoriale

### Identifiants visibles humains
- Surfaces sobres (footer, credibility-strip) : labels courts 
  (ORCID, Google Scholar, Zenodo)
- Surfaces académiques (badge AWP, meta-strip série) : labelLong 
  ("ORCID 0009-0002-1794-4895") ou logo image SVG
- Pages individuelles AWP : badge image SVG (convention preprints)

### Statut auteur dans le contenu
- Énumérations narratives : "économiste, chercheur indépendant 
  et essayiste"
- AWP-05 : 2 occurrences génériques de "chercheur indépendant" 
  préservées (emploi catégoriel, non auto-référentiel)

## 5. Chantiers en cours (90 jours)

### Phase 1 — Diffusion académique ciblée
- Plan de citations internes pour AWP-06 + template mail chercheurs
- 15-20 cibles francophones/anglophones identifiées
- Vagues 3-5 mails/semaine maximum
- Suivi signaux externes : citations Scholar, backlinks .edu, 
  reprises, mentions

### Phase 2 — Pages-ponts (limitées)
- 2-3 pages-ponts maximum sur 90 jours
- Créées en réaction aux signaux externes (ex. si chercheur 
  demande positionnement vs Polanyi → page Polanyi)
- Format : nœuds de graphe 900-1500 mots, pas articles longs

### Phase 3 — Chantier édition (post-90j)
- Ouvrira après premiers retours diffusion
- Préparation troisième livre lié au cadre anthropique
- Site déjà testé comme tremplin éditorial réplicable

## 6. Chantiers reportés / à activer si signal

- **Catégorie "Académique"** dans NOTES_PUBLICATIONS.md : à activer 
  quand une vraie revue peer-reviewed publie une fiche 
  (ex. Droit et Société). Décision : reclasser ou non Lectures 
  et Revue de la régulation rétroactivement.
- **isIdenticalTo SSRN** sur AWP-02/03/04/05 EN : action externe 
  en attente d'APPROVED SSRN. Script `scripts/zenodo_add_ssrn_links.py` 
  prêt à relancer.
- **Densification Wikidata** des 4 items existants (claims < 8) : 
  impact GEO fort mais hors site lui-même. Via Laura.
- **knowsAbout EN** dans data/author.toml : actuellement français 
  unique. Néologisme "anthropie" volontaire en français. Marginal.
- **Refactor description/canonicalDefinition** doublons entre 
  params.toml et hugo.toml [params] : nettoyage cosmétique, 
  hors enjeu.

## 7. Méta-règles d'engagement

### Discipline pendant les 90 jours
- Pas de retour structurel sur le site sauf défaut bloquant
- Énergie transférée vers diffusion, pas captée par optimisation
- Pages-ponts en réaction à signaux externes, pas en anticipation
- Si tentation de revenir au code : relire la phrase de pilotage

### Phrase de pilotage
> "Le site est suffisamment robuste ; la prochaine preuve ne 
> viendra plus du code, mais des tiers."

### Anti-pattern à éviter
- Multiplier les sessions techniques pendant les 90 jours
- Créer 10+ pages-ponts d'un coup (dilution conceptuelle)
- Confondre GEO architecture avec diffusion réelle
- Chercher une nouvelle validation infrastructurelle après chaque 
  arbitrage

## 8. Référence aux fichiers de doctrine spécialisés

- `NOTES_PUBLICATIONS.md` : règles publications (front matter, 
  taxonomie source_type, règle d'or SCSS BEM)
- `data/author.toml` : source unique identité auteur

---

*Ce fichier est versionné dans le repo. Toute évolution majeure 
(fin des 90 jours, ouverture chantier édition, refactor structurel)
doit faire l'objet d'une mise à jour explicite avec préfixe 
`docs:` dans le message de commit.*
