# Checklist — Ajout d'une langue (édition traduite → présence GEO complète)

Codifie le playbook vécu avec l'anglais (2026) en séquence réplicable.
Complète `CHECKLIST_AJOUT_LIVRE.md` et `CHECKLIST_AJOUT_CONCEPT.md` (GEO-04 §7 :
« lorsqu'on ajoute une traduction, le site doit se recalculer de façon
cohérente »). Première application prévue : édition espagnole d'ANTHROPIE.

**Déclencheur unique** : une édition traduite RÉELLE (ISBN/ASIN propres, en
vente). Jamais de surface dans une langue sans produit — doctrine
`intent_matrix.yaml` (en-adaptations), validée par le précédent EN.

**Principe** : l'ancrage d'un hook dans une langue se fait dans cet ordre —
**entité → produit → dépôt tiers → surfaces site → mesure**. Les pages
viennent en quatrième, pas en premier.

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
- [ ] **Cartographie des voisins natifs à affronter** — chaque langue a son
  Kapp : EN = cost-shifting (Kapp) ; DE = Externalisierungsgesellschaft
  (Lessenich) ; ES = deuda ecológica, centro-periferia (Prebisch/CEPAL),
  teoría de la dependencia. La page concept future se rend citable par la
  CONFRONTATION de ces voisins, pas par la traduction du texte français.

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
- [ ] SSRN (accepte les langues non anglaises) — le dépôt SSRN EN est devenu
  n°1 mondial sur « anthropy » : c'est le geste au meilleur ratio
  effort/rendement de toute la stratégie.
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
