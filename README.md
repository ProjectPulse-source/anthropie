# stephane-lalut.com — Anthropie

Site officiel de **Stéphane Lalut**, économiste, chercheur indépendant et essayiste — [stephane-lalut.com](https://stephane-lalut.com).

L'**anthropie** est l'hypothèse selon laquelle les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent : tout ordre local se construit en exportant son désordre vers d'autres lieux, d'autres temps ou d'autres groupes sociaux. *(EN — Anthropy is the hypothesis that social systems displace disorder rather than resolve it.)*

## Points d'entrée

- [Qu'est-ce que l'anthropie ?](https://stephane-lalut.com/quest-ce-que-lanthropie/) — définition canonique, FAQ, les trois axes de transfert ([English version](https://stephane-lalut.com/en/quest-ce-que-lanthropie/))
- [Le Registre des coûts déportés](https://stephane-lalut.com/registre-des-couts-deportes/) — l'appareil documentaire du livre *ANTHROPIE* en consultation libre : 168 jalons historiques « ordre créé / dette déportée », des premiers outils aux algorithmes
- [Combien coûte la dette publique ?](https://stephane-lalut.com/cout-de-la-dette-publique/) — chiffres officiels INSEE/Eurostat actualisés ; données consolidées en accès libre : [dette_officielle.json](https://stephane-lalut.com/dette_officielle.json)
- [Série Anthropie Working Papers](https://stephane-lalut.com/serie-awp/) — huit working papers bilingues FR/EN (Zenodo, CC-BY 4.0, DOI)
- [Les livres](https://stephane-lalut.com/livres/) — *ANTHROPIE — Ordre ici. Dette ailleurs* (2025), *Dette Publique : Qui paie vraiment ?* (2025), *La Société du premier coup* (2026), et deux ouvrages hors corpus
- [Glossaire](https://stephane-lalut.com/glossaire/) — le vocabulaire opératoire du cadre, entrées ancrées
- [llms.txt](https://stephane-lalut.com/llms.txt) — synthèse du site à destination des systèmes d'IA

Identifiants de recherche : [ORCID 0009-0002-1794-4895](https://orcid.org/0009-0002-1794-4895) · [Wikidata Q138909233](https://www.wikidata.org/wiki/Q138909233) · [Zenodo](https://zenodo.org/communities/anthropie-working-papers) · [Google Scholar](https://scholar.google.com/citations?user=J4NqzwSfrHAC)

> L'ancien mini-site statique (2025) est conservé dans la branche [`backup-mini-site`](https://github.com/ProjectPulse-source/anthropie/tree/backup-mini-site) ; son contenu — dont le Registre — est intégré au site actuel.

## Technique

Site statique **Hugo Extended 0.147.0** — Sass natif Hugo, JavaScript vanilla, zéro dépendance npm. Déployé sur GitHub Pages via GitHub Actions (`.github/workflows/hugo.yml`) à chaque push sur `main`.

```bash
hugo server -D   # dev local (inclut drafts)
hugo --minify    # build de production -> ./public
```
