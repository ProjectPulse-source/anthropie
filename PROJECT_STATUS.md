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
> Dernière mise à jour : mai 2026 (post bascule GEO/diffusion).

## 0. Log chronologique

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

**AWP : aucun modifié.** Le concept de boucle techno-cognitive introduit ici est inscrit dans le livre ANTHROPIE (606 p., ISBN 978-2-9586347-2-8) et préparé dans AWP-02 (migration des modalités vers le temporel et le cognitif) et AWP-06 (quatre registres couplés énergie/matière/territoire/attention). Un AWP-07 dédié pourra formaliser le concept lors d'une campagne de diffusion ultérieure distincte.

**Reprise du gel :** la phase GEO/diffusion reprend après ce commit. Aucune autre intervention non bloquante prévue avant la fin de la fenêtre 90 jours (échéance approximative ~2026-08-12).

## 1. État de phase

Le site est en **phase active GEO/diffusion 90 jours** (depuis mai 2026).

La phase de construction infrastructurelle est **close**. Aucune 
nouvelle session technique structurelle n'est prévue pendant les 
90 jours sauf défaut bloquant détecté.

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
