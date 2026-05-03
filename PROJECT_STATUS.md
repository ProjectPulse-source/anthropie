# Project Status — stephane-lalut.com

> **À lire avant** : toute intervention sur le site, technique 
> ou éditoriale. Décrit l'état architectural, les doctrines 
> en place, les chantiers en cours et les chantiers reportés.
> Dernière mise à jour : mai 2026 (post bascule GEO/diffusion).

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
