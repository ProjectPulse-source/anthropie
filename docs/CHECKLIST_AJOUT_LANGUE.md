# Checklist — Ajout d'une langue (édition traduite → présence GEO complète)

Codifie le playbook vécu avec l'anglais (2026) en séquence réplicable.
Complète `CHECKLIST_AJOUT_LIVRE.md` et `CHECKLIST_AJOUT_CONCEPT.md` (GEO-04 §7 :
« lorsqu'on ajoute une traduction, le site doit se recalculer de façon
cohérente »). Première application prévue : édition espagnole d'ANTHROPIE.

**Déclencheur public** *(amendé 02/08 après contre-expertise)* : un **actif
linguistique réel et publiquement vérifiable** — édition avec ISBN et date
stable, AWP publié dans la langue, article substantiel, recension autorisée.
La mise en vente n'est pas le seul déclencheur légitime ; une langue sans
AUCUN actif vérifiable reste sans surface (doctrine anti-doorway).

**Trois états, jamais confondus** :
- **A — Préparation privée** (possible à tout moment) : terminologie,
  traduction, relecture native, cartographie des voisins, audit Hugo,
  brouillons, sondes de référence. Rien d'indexé publiquement.
- **B — Pré-ancrage public** (dès ISBN/DOI + date ferme + métadonnées
  stables + version réellement relue) : fiche produit, extrait, informations
  de citation, page de lancement minimale.
- **C — Déploiement complet** (à la publication) : page concept adaptée,
  AWP de référence, dépôt académique, maillage, mesure T+7/T+30.

**Principe** : l'ancrage d'un hook dans une langue se fait dans cet ordre —
**entité → actif → dépôt tiers → surfaces site → mesure**. Les pages
viennent en quatrième, pas en premier. Et l'unité d'analyse n'est pas la
langue mais la **communauté intellectuelle** : « l'espagnol » recouvre
l'Espagne, le Mexique, les Andes, le Cône Sud — des traditions distinctes.

---

## Phase 0 — Avant parution (coût quasi nul, à faire dès maintenant)

- [ ] **Wikidata** : label + description + alias du concept Q138827949 dans la
  langue (cf. protocole Laura). Règle absolue : la description dit
  « **hypothèse** » (hipótesis, Hypothese…), jamais « mécanisme » — la seule
  dérive constatée à ce jour est venue d'une traduction (ES/IT, corrigée).
- [ ] **Baseline sondes** (mode IA + SERP, connecté PUIS navigation privée),
  consignée dans `reports/geo_audit/` : qui occupe le MOT (ex. ES :
  « antropía » = sens anthropisation) et qui occupe le CONCEPT (ex. DE :
  Lessenich). Sans baseline, pas de mesure d'effet possible.
- [ ] **Cartographie des voisins natifs à affronter** — chaque communauté
  intellectuelle a ses voisins dominants : EN = cost-shifting (Kapp) ;
  DE = Externalisierungsgesellschaft (Lessenich). Pour l'ES, ordre d'entrée
  arbitré (02/08) : **1er cercle** vocabulaire général (externalización de
  costes, desplazamiento de cargas) ; **2e cercle** économie écologique
  (intercambio ecológicamente desigual, deuda ecológica, metabolismo
  social) ; **3e cercle** traditions latino-américaines (centro-periferia,
  CEPAL, dependencia, extractivismo) présentées comme **voisins et
  précédents partiels, jamais comme filiation** — un arrimage direct à la
  CEPAL exposerait à la critique de reconditionnement. La page concept se
  rend citable par la CONFRONTATION de ces voisins, pas par la traduction
  du texte français. Alimenter `reports/geo_audit/REGISTRE_COLLISIONS.md`.

## Phase 1 — Décision structurelle site (arbitrage auteur obligatoire)

- [ ] Ajouter une 3e/4e langue à Hugo est STRUCTUREL : `config/_default/hugo.toml`
  (bloc langue), menus, hreflang/x-default, `cross-language-banner.html`
  (conçu pour une paire fr↔en — à généraliser), `translation.url`.
  **Audit technique multilingue AVANT la première page** (interdit existant :
  ne pas toucher hreflang sans audit). Alternative dégradée acceptable au
  départ : fiche produit seule sous la langue existante la plus proche,
  comme l'EN a commencé.

## Phase 2 — Produit

- [ ] Fiche livre `.{lang}.md` : traduction du CONTENU par IA autorisée mais
  **relecture native obligatoire avant publication** (une fiche produit
  fautive détruit plus d'autorité qu'elle n'en crée).
- [ ] `data/works.yaml` : bloc `{lang}_edition` (modèle : `english_edition`
  de book-anthropie — ISBN, ASIN, pages, date, purchase_url) +
  `site_pages.{lang}` + `abstract_short.{lang}`.
- [ ] Liens Amazon `/dp/<ASIN>` canoniques par marché — jamais de shortener.

## Phase 3 — Ancrage définitionnel (le hook)

- [ ] Page concept ADAPTÉE, pas traduite : définition canonique validée par
  locuteur natif ; geste GEO-01 dans la langue (« le mot, ses usages, le
  concept » — l'auteur n'invente pas le mot) ; désambiguïsation des
  occupants LOCAUX du terme (pas la copie de la liste FR) ; confrontation
  des voisins natifs identifiés en Phase 0 ; FAQ sobres.
- [ ] Le hook qui s'ancre est la formulation EXACTE — si une traduction
  approximative s'ancre, c'est la déformation qui devient la vérité publique
  dans cette langue (boucle de gravure inversée). D'où : relecture native
  systématique de la définition et des FAQ, quel que soit le coût.

## Phase 4 — Dépôt tiers (le levier au meilleur rendement mesuré)

- [ ] AWP-01 traduit dans la langue → Zenodo (DOI propre, `isDerivedFrom` la
  version FR, communauté anthropie-working-papers) — réplique la structure
  FR/EN existante.
- [ ] SSRN (accepte les langues non anglaises) — le dépôt SSRN EN était le
  premier résultat observé le 01/08/2026 sur « anthropy » (recherche non
  personnalisée, géolocalisée US) : expérience réussie **à reproduire sous
  contrôle, plateforme par plateforme et langue par langue** — chaque dépôt
  doit avoir une fonction propre (audience disciplinaire, indexation locale,
  DOI, préservation) ; un doublon sans audience distincte fragmente les
  versions et les métriques.
- [ ] Infrastructure académique DE LA LANGUE si accessible (ES : Dialnet,
  SciELO, Redalyc ; DE : SSOAR ; etc.) — c'est l'équivalent local du
  pattern SSRN.

## Phase 5 — Registres et mesure (règle « l'état écrit suit l'acte »)

- [ ] `static/llms.txt` (section langue), `data/intent_matrix.yaml`
  (bloc adaptations), `scripts/check-geo-coverage.py` (étendre le miroir
  [5] à la langue), compteurs si besoin, `PROJECT_STATUS.md` (log).
- [ ] Sondes T+7 et T+30 contre la baseline de Phase 0 (double lecture
  connecté/privé, grille citation ET absorption).

## Interdits (rappel)

- Publier une traduction IA brute sans relecture native (définition, FAQ,
  descriptions Wikidata comprises).
- Créer une page dans une langue sans édition réelle.
- Trancher une translittération (ja/zh/ko/ru…) sans arbitrage auteur.
- Toucher hreflang/config langues sans audit préalable.
- Dupliquer la page concept FR « telle quelle » — chaque langue affronte
  SES voisins ou n'existe pas encore.
