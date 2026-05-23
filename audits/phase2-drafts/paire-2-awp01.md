# Paire 2 — AWP-01 (FR + EN)

> **Statut : DRAFT, à valider en revue. Aucune application au site.**

Cibles : `content/awp/awp-01.md` et `content/awp/awp-01.en.md`.

AWP-01 est le **texte fondateur** : la définition doit s'y imposer en
**autorité**. Règle applicable : *verbatim en position d'ouverture, paraphrase
éventuellement conservée plus loin comme reformulation.*

## Texte actuel

**FR — paragraphe d'ouverture** (`awp-01.md:36`) :
> L'anthropie est l'hypothèse selon laquelle tout ordre social local se construit en exportant son désordre vers d'autres lieux, d'autres temps ou d'autres groupes sociaux. Ce texte fondateur pose les principes du cadre anthropique.

**FR — FAQ** (`awp-01.md:19`) :
> L'anthropie est le principe selon lequel les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent. […]

**EN — paragraphe d'ouverture** (`awp-01.en.md:37`) :
> Anthropy is the hypothesis that every stable local social order is built by exporting its disorder to other places, other times, or other social groups. This founding text establishes the principles of the framework.

## Proposition

L'ouverture actuelle (« tout ordre social local se construit en exportant son
désordre ») est une **reformulation forte et spécifique**, utile à AWP-01.
Deux options :

- **Option A (verbatim en tête)** : insérer le verbatim canonique en première
  phrase via `{{< canonical-definition >}}`, puis enchaîner sur la
  reformulation actuelle comme développement :
  ```markdown
  {{< canonical-definition >}}

  Plus précisément&nbsp;: tout ordre social local se construit en exportant son désordre vers d'autres lieux, d'autres temps ou d'autres groupes sociaux. Ce texte fondateur pose les principes du cadre anthropique.
  ```
- **Option B (encart canonique après l'accroche)** : garder l'ouverture
  actuelle comme accroche, insérer `{{< canonical-definition >}}` juste après
  en encart d'autorité.

Pour l'EN : appliquer l'option retenue à l'identique (la 1ʳᵉ phrase EN actuelle
est une variante « every stable local social order is built by exporting… »,
à articuler avec le verbatim canonique EN « social systems displace disorder
rather than resolve it »).

## Arbitrage à trancher (REVUE)

1. Option A (verbatim en tête + reformulation comme précision) vs Option B
   (accroche + encart). A privilégie l'autorité canonique ; B préserve l'élan
   rédactionnel actuel.
2. La **FAQ** d'AWP-01 utilise « le principe selon lequel » : faut-il aussi
   l'aligner sur le verbatim, ou la laisser (le JSON-LD FAQPage cite la FAQ) ?
3. Cohérence avec l'`abstract`/`description` du front matter (qui sert le
   `citation_abstract` et le résumé visible) : la description ne doit pas être
   touchée sans décision séparée (impact métadonnées Scholar).

Recommandation provisoire : Option A pour le corps, FAQ laissée en l'état
(fonction conversationnelle distincte). À confirmer.
