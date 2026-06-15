# Drafts Phase 2 — single-source de la définition canonique

Trois paires FR/EN à traiter, idéalement en sessions séparées avec
arbitrage par page.

## Règle de décision (rappel)

- Page concept : verbatim via {{< canonical-definition >}} (déjà en place
  depuis post-diag-05)
- Pages où une paraphrase rhétorique a une fonction : conserver la
  paraphrase, injecter le verbatim en encart adjacent ou immédiatement
  après
- Pages où la définition doit s'imposer en autorité (AWP-01) : verbatim
  en position d'ouverture, paraphrase éventuellement conservée plus loin
  comme reformulation

## État des paires

- [x] Paire 1 — Accueil (appliqué 2026-06-15) : FR aligné sur le verbatim inline (`layouts/index.html:19`) ; EN inchangé (1ʳᵉ phrase du lede = déjà le verbatim canonique).
- [x] Paire 2 — AWP-01 FR + EN (appliqué 2026-06-15) : `{{< canonical-definition >}}` en tête + reformulation rétrogradée en « Plus précisément / More precisely ».
- [x] Paire 3 — AWP-06 (appliqué 2026-06-15) : FR `{{< canonical-definition >}}` en tête + spécialisation numérique ; EN inchangé (verbatim déjà présent en incise).

## Note d'architecture importante (découverte au draft)

Contrairement à l'hypothèse initiale, la définition de l'**accueil** ne vit
**pas** dans `content/_index.md` (qui ne porte que `hero_lead`/`hero_statement`),
mais dans le template `layouts/index.html` (paragraphe `.hero__lede`, lignes
16-20). Le shortcode `{{< canonical-definition >}}` (markdown) n'y est donc
**pas applicable**. La Phase 2 pour l'accueil passera par le **partial**
`{{ partial "canonical-definition.html" . }}` appelé directement dans le
template, OU par la conservation de la paraphrase actuelle. Voir
`paire-1-accueil.md` pour l'arbitrage.

Le partial `canonical-definition.html` est déjà conçu pour recevoir une Page
en contexte (il lit `.Site.Params.canonicalDefinition`, résolu par langue) :
il fonctionne aussi bien appelé depuis un template que via le shortcode.
