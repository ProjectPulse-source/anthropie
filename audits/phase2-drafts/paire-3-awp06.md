# Paire 3 — AWP-06 (FR + EN)

> **Statut : DRAFT, à valider en revue. Aucune application au site.**

Cibles : `content/awp/awp-06.md` et `content/awp/awp-06.en.md`.

AWP-06 est une **application spécialisée** (infrastructures numériques). Règle
applicable : *conserver la paraphrase comme reformulation contextuelle,
injecter le verbatim via {{< canonical-definition >}} à un endroit approprié.*

## Texte actuel

**FR — paragraphe d'ouverture** (`awp-06.md:36`) :
> L'anthropie désigne le mécanisme par lequel les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent. Cet article examine les infrastructures numériques contemporaines — data centers, IA générative, chaînes matérielles, territoires d'accueil, dispositifs de garantie publique — comme régime structuré de déplacement&nbsp;: le service numérique n'a pas allégé la matière, il a appris à la faire travailler ailleurs.

**EN — paragraphe d'ouverture** (`awp-06.en.md:36`) :
> Existing analyses of digital infrastructures often treat materialist critique, opacity studies, and environmental footprint accounting as separate approaches, thereby missing the broader regime that connects them. This paper applies the framework of anthropy — the hypothesis that social systems displace disorder rather than resolve it — to contemporary digital infrastructures: […]

Observation : l'ouverture **FR** commence par une paraphrase (« désigne le
mécanisme par lequel… ») très proche du verbatim. L'ouverture **EN** insère
**déjà** le verbatim canonique en incise (« — the hypothesis that social
systems displace disorder rather than resolve it — »). Les deux langues ne
sont donc pas symétriques.

## Proposition

- **FR** : remplacer la 1ʳᵉ phrase paraphrasée par le verbatim canonique via
  `{{< canonical-definition >}}` en tête, puis enchaîner sur la spécialisation
  numérique :
  ```markdown
  {{< canonical-definition >}}

  Cet article examine les infrastructures numériques contemporaines — data centers, IA générative, chaînes matérielles, territoires d'accueil, dispositifs de garantie publique — comme régime structuré de déplacement&nbsp;: le service numérique n'a pas allégé la matière, il a appris à la faire travailler ailleurs.
  ```
- **EN** : l'ouverture EN intègre déjà le verbatim en incise. Option : la
  laisser (le verbatim y est présent et fonctionnel), OU restructurer pour
  ouvrir explicitement sur `{{< canonical-definition >}}` puis le constat sur
  les approches compartimentées. Risque de la restructuration : casser la
  logique « approches séparées → régime unificateur » propre à l'abstract EN.

## Arbitrage à trancher (REVUE)

1. Asymétrie FR/EN : faut-il harmoniser les deux ouvertures (verbatim en tête
   des deux), ou respecter la structure propre à chaque langue (FR remanié, EN
   laissé car le verbatim y est déjà) ?
2. L'ouverture FR sert aussi de base au `description`/`abstract` front matter
   (citation_abstract) — vérifier l'impact métadonnées avant d'aligner la
   description.
3. Position du verbatim : tout en tête, ou après la phrase de cadrage « Cet
   article examine… » ?

Recommandation provisoire : FR → verbatim en tête + spécialisation ;
EN → statu quo (verbatim déjà présent en incise). À confirmer.
