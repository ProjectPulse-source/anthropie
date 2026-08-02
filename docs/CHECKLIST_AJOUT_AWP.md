# Checklist — Ajout d'un nouvel AWP

Procédure compacte pour ajouter un *Anthropie Working Paper* (AWP-NN) sur le site, sans rater de surface dépendante. À suivre dans l'ordre.

## 1. Dépôt Zenodo FR et EN

Dépôt FR sur la communauté Zenodo `anthropie-working-papers`, licence CC-BY 4.0. Dépôt EN en second pour obtenir un DOI EN distinct. Lier les deux dépôts via `isDerivedFrom` (FR canonique, EN traduction). Récupérer les deux DOIs `10.5281/zenodo.XXXXXXX` et les URLs `https://zenodo.org/records/XXXXXXX`.

### 1 bis. Les 8 métadonnées Zenodo à ne jamais oublier

**Pourquoi cette liste existe** : l'audit du 2026-08-02 a trouvé qu'AWP-08, déposé le 23/07, était sorti **sans ORCID et hors de la communauté de la série** — donc invisible depuis la vitrine Zenodo et non rattaché au profil auteur. Personne ne l'avait vu pendant dix jours. Les dépôts se font vite et à la main ; c'est là que se creusent les trous.

À vérifier sur **chacun des deux records** (FR et EN) :

1. **Verbatim canonique de la définition** en ouverture de la description — FR : « L'anthropie est l'hypothèse selon laquelle les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent. » ; EN : « Anthropy is the hypothesis that social systems displace disorder rather than resolve it. » *(Le verbatim en incise dans le corps est accepté — conformité actée, commit `e6c6b8a`. Ne jamais employer de variante : « reroute », « reroutes », « shifts »… — un cas corrigé sur AWP-03 EN le 02/08.)*
2. **ORCID** `0009-0002-1794-4895` **et** affiliation `Independent Researcher` sur le creator.
3. **Licence** CC-BY-4.0.
4. **Langue** déclarée, cohérente avec la version (fr / en).
5. **Mots-clés** renseignés.
6. **Communauté** `anthropie-working-papers`.
7. **`isDescribedBy`** vers la page du site correspondante, **en https**.
8. **Liaison de traduction réciproque** : la version EN porte `isDerivedFrom` → DOI FR, la version FR porte `isSourceOf` → DOI EN. *(Zenodo refuse `isTranslationOf`/`hasTranslation` de DataCite 4.6 — vérifié le 02/08.)*

### 1 ter. Contrôle automatisé — obligatoire avant de clore l'ajout

Ajouter la nouvelle paire dans la liste `PAIRS` de `scripts/zenodo_audit_complet.py`, puis lancer :

```bash
python scripts/zenodo_audit_complet.py
```

Le script vérifie les 8 points ci-dessus plus la présence du fichier PDF, et distingue **BLOQUANT** (à corriger) de **info** (champ décoratif, ex. `version`). **Ne pas clore l'ajout tant que le compte de bloquants n'est pas à 0.**

Outils de correction si l'audit signale un trou : `scripts/zenodo_fix_verbatim.py` (verbatim manquant) et `scripts/zenodo_link_translations.py` (liaison de traduction).

### 1 quater. Dépôts sur les plateformes tierces — RÈGLE D'ÉCHELONNEMENT

Zenodo mis à part (dépôt propre, sans modération), **toute plateforme à modération — SSRN, MPRA, SocArXiv — se traite un dépôt à la fois** :

1. Déposer **un seul** papier.
2. Surveiller : `python scripts/check_deposits_status.py` (détecte SSRN via Crossref, MPRA via le code HTTP, OSF via son API — aucun mot de passe requis).
3. **Attendre l'acceptation** avant de poser le suivant. Compter quelques jours à deux semaines.
4. Poser un rappel (RDV Outlook) plutôt que de surveiller à la main.

**Pourquoi c'est une règle et pas un conseil** : le 07/04/2026, cinq AWP ont été déposés sur MPRA en dix-huit minutes. Ils sont restés bloqués **118 jours** sans message ni rejet. Un dépôt isolé, le 08/05, a été accepté en **sept jours**. Le dépôt groupé par un déposant récent est lu comme un signal de spam.

**Corollaire** : ne jamais rattraper un retard en déposant en lot. C'est ce qui recrée le blocage qu'on cherche à résorber.

## 2. Création des fichiers content

Convention multilingue Hugo **par suffixe** (pas par sous-dossier) :

- `content/awp/awp-NN.md` — version FR
- `content/awp/awp-NN.en.md` — version EN

Ne pas créer de bundle `content/awp/awp-NN/index.md`. Le repo utilise le format flat avec suffixe `.en.md`, cohérent avec `defaultContentLanguageInSubdir = false`.

## 3. Frontmatter minimal

S'aligner sur un AWP existant (par exemple `awp-05.md`) pour la complétude. Champs requis : `title`, `date`, `doi_zenodo`, `url_zenodo`, `pdf_url`, `abstract`, `citation_pdf_url`, `jel_codes`, `keywords[_en]`, `faq[]`, `translation.{doi,url,title,is_canonical}`, `related[]`, `related_book` (si pertinent).

## 4. Mise à jour `data/works.yaml`

Nouvelle entrée AWP avec `type: awp`, `series_number: N`, `canonical_title.{fr,en}`, `publication_date_fr`, `publication_date_en`, blocs `deposits.{zenodo_fr,zenodo_en,ssrn_en,mpra_en}`, `site_pages.{fr,en}`. Conserver l'ordre chronologique des entrées.

## 5. Rendu local Hugo + vérifications

Lancer `hugo server` et vérifier sur les deux URLs FR et EN : balises `<meta name="citation_*">` présentes, lien hreflang, JSON-LD `ScholarlyArticle` et `FAQPage` valides (extension Schema Markup Validator ou copier-coller dans schema.org/validator).

## 6. Linter cohérence corpus

Exécuter `python scripts/check-corpus-counters.py`. Doit sortir code 0 (aucune divergence). Si le linter détecte un chiffre dur obsolète (par exemple `cinq Anthropie Working Papers` quand on passe à 6) : corriger les occurrences listées avant commit.

## 7. Mise à jour du hero index (FR + EN)

Le hero de `layouts/index.html` (lignes 18-22) affiche `X Anthropie Working Papers, deux livres` en FR et `X Anthropy Working Papers, two books` en EN, où **X est écrit en lettres** (`cinq`, `six`, `seven`/`sept`, etc.). À chaque ajout d'AWP, incrémenter X dans **les deux blocs** (`if eq .Lang "en"` et `else`).

Le compteur livres reste `deux` / `two` : il désigne le **cadre anthropique** stricto sensu (livres ANTHROPIE + Dette Publique), pas le corpus livres total (qui inclut *Livresque des mots*, antérieur et hors série).

## 8. Maillage avec `/publications/`

Si le nouvel AWP **prolonge** une recension ou un article déjà publié dans `content/publications/*.md` : ajouter `awp-NN` au champ `related: [...]` du frontmatter de la fiche concernée. Préserver l'ordre chronologique croissant (`awp-01`, `awp-04`, `awp-06` plutôt que `awp-06`, `awp-01`).

Le libellé visible humain est généré par i18n : clé `pub_related_label` (`"Prolonge :"` FR / `"Extends:"` EN). Le champ `related:` se rend automatiquement.

## 9. Build production + vérification HTTP

`hugo --minify`. Si déploiement GitHub Pages : push sur `main` déclenche le workflow `.github/workflows/hugo.yml`. Après quelques minutes, vérifier HTTP 200 sur :

- `https://stephane-lalut.com/awp/awp-NN/`
- `https://stephane-lalut.com/en/awp/awp-NN/`
- `https://stephane-lalut.com/` (hero compteur mis à jour)
- `https://stephane-lalut.com/en/` (idem)

## 10. Note convention bilinguisme publications

Aucune traduction `.en.md` n'est créée pour les fiches `content/publications/*.md`. Choix éditorial : les fiches publication restent en FR (langue de la revue source) sur les deux versions du site. La page `/en/publications/` rend les fiches FR via fallback multilingue Hugo. Ne pas créer de `*.en.md` dans `content/publications/` sauf décision éditoriale explicite.
