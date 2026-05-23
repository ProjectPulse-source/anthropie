# Paire 1 — Accueil (FR + EN)

> **Statut : DRAFT, à valider en revue. Aucune application au site.**

## Localisation réelle

La définition de l'accueil est dans **`layouts/index.html`**, paragraphe
`.hero__lede` (lignes 16-20), et NON dans `content/_index.md`. Le shortcode
markdown n'est donc pas l'outil ici — il faut le **partial**.

## Texte actuel (paraphrase mêlée à la présentation du site)

**FR** (`layouts/index.html:19`) :
> L'anthropie est l'hypothèse selon laquelle les systèmes sociaux ne suppriment pas le désordre&nbsp;: ils le déplacent dans l'espace, dans le temps, ou entre groupes sociaux. Ce site rassemble un corpus de recherche qui la met à l'épreuve&nbsp;: six *Anthropie Working Papers*, deux livres, des publications et des ressources conçues pour être lues, citées et discutées.

**EN** (`layouts/index.html:17`) :
> Anthropy is the hypothesis that social systems displace disorder rather than resolve it — in space, in time, or between social groups. This site gathers a research corpus devoted to testing this hypothesis: six *Anthropy Working Papers*, two books, publications and resources designed to be read, cited and discussed.

Observation : la 1ʳᵉ phrase EN est **déjà identique au verbatim canonique**
(« social systems displace disorder rather than resolve it »). La 1ʳᵉ phrase
FR en est une **variante développée** (« ne suppriment pas le désordre : ils
le déplacent dans l'espace, dans le temps, ou entre groupes sociaux »).

## Proposition

La phrase d'attaque a une **fonction rhétorique** (accroche + enchaînement
immédiat sur la présentation du corpus). Règle applicable : *conserver la
paraphrase comme accroche, injecter le verbatim en encart adjacent.*

Proposition concrète : conserver le `.hero__lede` tel quel, et ajouter
**immédiatement après le hero** (ou sous le lede) un encart canonique rendu
par le partial :

```go-html-template
<p class="hero__canonical">{{ partial "canonical-definition.html" . }}</p>
```

(le partial rend lui-même un `<p class="canonical-definition">` ; on peut
soit l'envelopper, soit l'appeler nu et styler `.canonical-definition` dans
le hero.)

## Arbitrage à trancher (REVUE)

1. **Où placer l'encart** : sous le `.hero__lede` dans `.hero-main`, ou en
   bande pleine largeur sous la section hero ? (impact visuel fort sur la home)
2. **Marquage** : `<p>` simple stylé, `<blockquote>`, ou `<div>` dédié ?
3. **Redondance FR/EN** : en EN, la 1ʳᵉ phrase du lede EST déjà le verbatim ;
   un encart canonique juste après serait une **répétition**. Faut-il
   l'encart seulement en FR (où le lede diverge), et s'en passer en EN ? Ou
   reformuler le lede EN pour éviter la répétition ?
4. **Alternative minimaliste** : remplacer seulement la 1ʳᵉ phrase FR du lede
   par le verbatim canonique (alignement strict) et garder la suite — sans
   encart séparé. Plus sobre, mais fait perdre la nuance « dans l'espace,
   dans le temps, ou entre groupes sociaux ».

Recommandation provisoire : option 4 en FR (aligner la 1ʳᵉ phrase sur le
verbatim, conserver la 2ᵉ moitié du lede), statu quo en EN (déjà canonique).
À confirmer en revue.
