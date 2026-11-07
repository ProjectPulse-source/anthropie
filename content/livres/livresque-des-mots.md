---
title: "Livresque des mots"
promo_slug: "livresque"  # clé D1/books.toml pour /ressources-offertes (guichet Kindle)
subtitle: "Anthologie inédite & éclectique de citations"  # page de titre de l'intérieur et couverture
pages: 680  # sync data/works.yaml (book-livresque-des-mots.pages) — broché, édition 2026 révisée (sommaire, Promenades, index des auteurs)
wikidata_qid: "Q140517745"  # item canonique (doublon Q138911600 fusionné) — alimente sameAs du Book
description: "Une anthologie qui refuse l'ordre alphabétique et thématique pour privilégier la surprise des rencontres. {citations} citations, {auteurs} voix, 25 siècles de génie humain, tissés en un fil d'Ariane subtil. Quarante ans de passion littéraire pour offrir non un classement, mais un voyage."
date: 2022-12-20
lastmod: 2026-11-01  # date de la derniere modification de contenu (fraicheur legere GEO-04 ; jamais enableGitInfo)
isbn: "978-2-9586347-0-4"
amazon_rating: 4.1       # note moyenne Amazon.fr (MAJ ~mensuelle, relecture Chrome)
amazon_rating_date: 2026-10-25  # date du relevé, affichée sous la note ; la mettre à jour avec elle
amazon_reviews: 89       # nb d'avis Amazon.fr ; omettre les 2 champs = pas d'étoiles sur /ressources-offertes
description_en: "An anthology that refuses alphabetical and thematic order in favour of the surprise of unexpected encounters. {citations} quotations, {auteurs} voices, 25 centuries of human genius woven along a subtle thread. Forty years of literary passion, offering not a classification but a journey."
price: "36"  # prix broché EUR — affiché sur la page + schema.org Offer
serie: "autres-ouvrages"
weight: 4
# Liens canoniques /dp/<ASIN broché 2958634701> — jamais de shortener amzn.eu/a.co
# (l'ancien CA réutilisait le shortener FR — corrigé 2026-06-04).
url_amazon_fr: "https://www.amazon.fr/dp/2958634701"
url_amazon_ca: "https://www.amazon.ca/dp/2958634701"
url_amazon_com: "https://www.amazon.com/dp/2958634701"
url_amazon_uk: "https://www.amazon.co.uk/dp/2958634701"
url_amazon_de: "https://www.amazon.de/dp/2958634701"
url_amazon_it: "https://www.amazon.it/dp/2958634701"
url_amazon_es: "https://www.amazon.es/dp/2958634701"
# Édition Kindle (ASIN B0CW994YWH) — bouton séparé par marché
url_amazon_fr_kindle: "https://www.amazon.fr/dp/B0CW994YWH"
url_amazon_ca_kindle: "https://www.amazon.ca/dp/B0CW994YWH"
url_amazon_com_kindle: "https://www.amazon.com/dp/B0CW994YWH"
url_amazon_uk_kindle: "https://www.amazon.co.uk/dp/B0CW994YWH"
url_amazon_de_kindle: "https://www.amazon.de/dp/B0CW994YWH"
url_amazon_it_kindle: "https://www.amazon.it/dp/B0CW994YWH"
url_amazon_es_kindle: "https://www.amazon.es/dp/B0CW994YWH"
# FAQ book-scoped (doctrine GEO-04). Chiffres canoniques : JAMAIS en dur —
# placeholders {citations}/{auteurs}/{siecles} résolus par desc-figures
# depuis data/works.yaml (corpus_stats), via l'ISBN de la page.
faq:
  - question: "Qu'est-ce qu'une anthologie de citations « sans classement » ?"
    answer: "Un recueil sans ordre thématique, alphabétique ni chronologique : {citations} citations et {auteurs} voix tissées pour que le sens naisse du voisinage — une réplique de cinéma à côté d'un moraliste, une chanson à côté d'un philosophe. Le recueil se lit comme un roman : on avance de page en page, et la rencontre qu'aucune recherche par mot-clé n'aurait produite fait le sel de la lecture."
  - question: "Combien de citations contient Livresque des mots ?"
    answer: "{citations} citations, {auteurs} voix, {siecles} siècles — aphorismes, extraits de romans, anecdotes littéraires, poésies, répliques choisies. Derrière la sélection, quarante ans de lectures et une curation d'auteur : une voix qui choisit."
  - question: "Livresque des mots a-t-il un index ?"
    answer: "Oui. L'édition brochée se clôt sur un index des auteurs qui renvoie à la page de chaque citation ; l'anthologie, elle, reste sans classement. Un fil pour flâner, un index pour retrouver. En version Kindle, la recherche plein texte ramène une citation, un auteur ou un mot."
  - question: "À qui offrir Livresque des mots ?"
    answer: "À l'amoureux de la langue et des formules, à l'écrivain en quête de compagnie, au lecteur qui aime ouvrir un livre au hasard. Une anthologie sans ordre imposé se prête naturellement au cadeau ; en version Kindle, le cadeau passe par un lien prépayé (mode d'emploi sur la page Offrir un livre Kindle)."
lang_repli: "/en/books/"  # pas de version anglaise (exclusion déclarée) : cible de l'onglet EN, partials/lang-cible.html
# Extrait « voix » (07/11/2026, à la demande de l'auteur) : scène verbatim de la dernière édition, vérifiée
# mot pour mot contre la source : broché HTML de l'édition 2026 (03-BROCHE-PDF, WEASY-2026-10-04-ED2026) ; quatre citations contiguës, confirmées par l'audit.
extrait_voix:
  source: "Quatre citations consécutives de l'édition 2026 · en exergue, l'avertissement du livre"
  paragraphes:
    - "La meilleure manière d'être revenu de bien des choses, c'est de n'y être jamais allé.<br><span class=\"book-voix__auteur\">— Louise-Victorine Ackermann</span>"
    - "Elle était revenue de bien des choses ce qui ne l'empêchait pas d'y retourner.<br><span class=\"book-voix__auteur\">— Natalie Clifford Barney</span>"
    - "Ce n'est pas que je sache bien employer mon temps mais c'est que je sais bien le perdre et soit dit sans me vanter c'est peut-être la première de toutes les sciences.<br><span class=\"book-voix__auteur\">— Duchesse de Choiseul</span>"
    - "Le regret qu'ont les hommes du mauvais emploi du temps qu'ils ont déjà vécu, ne les conduit pas toujours à faire de celui qui leur reste à vivre un meilleur usage.<br><span class=\"book-voix__auteur\">— Jean de La Bruyère</span>"
  ligne: "Elle était revenue de bien des choses ce qui ne l'empêchait pas d'y retourner."
  ligne_auteur: "Natalie Clifford Barney, dans le livre"
  chute: "Si vous ne voyez pas la couture, c'est qu'elle est réussie."
---

Une anthologie qui refuse l'ordre alphabétique.

{{< stat "citations" >}} citations. {{< stat "auteurs" >}} voix. 25 siècles. Aucun classement par thème, par auteur ou par lettre.

Le pari&nbsp;: que le voisinage des phrases produit du sens là où le classement le fige. Un fragment de Juvénal y côtoie un mot d'Albert Brie&nbsp;; un aphorisme du XVIIᵉ siècle se laisse rejoindre par une réplique de cinéma. À chaque page, des passerelles inattendues entre œuvres, époques et registres — aphorismes, extraits de romans, anecdotes littéraires, poésies, répliques choisies.

Ce que cherche cette anthologie n'est pas la commodité de la consultation thématique. C'est la résonance — la rencontre qui n'aurait pas dû avoir lieu et qui éclaire.

## Pour qui, pour quel besoin&nbsp;? {#pour-qui}

<div class="book-enbref">
<div>
<p class="book-enbref__t">Pour qui</p>

Pour l'amoureux de la langue et des formules, le lecteur qui aime ouvrir un livre au hasard — et pour le cadeau&nbsp;: une anthologie sans ordre imposé se prête naturellement à être offerte.

</div>
<div>
<p class="book-enbref__t">Le livre sert à</p>

- citer juste&nbsp;: pour l'édition 2026, le texte et la paternité de chaque citation ont été réexaminés, et la ligne d'auteur dit quand la paternité reste discutée ([la méthode, et vingt cas célèbres](/citations-celebres-verifiees/))&nbsp;;
- retrouver une citation et son auteur, par l'index des auteurs de l'édition brochée ou par la recherche de la version Kindle&nbsp;;
- trouver une formule pour un discours, une dédicace ou une carte, ou simplement lire au hasard.

**Ce qu'il n'est pas**&nbsp;: un dictionnaire thématique. Les citations ne sont pas classées&nbsp;; on y entre par l'index, par la recherche ou par le hasard.

</div>
</div>

## Sans classement, à lire comme un roman

«&nbsp;Anthologie de citations sans classement&nbsp;»&nbsp;: la formule décrit exactement le parti pris de *Livresque des mots* — {{< stat "citations" >}} citations, {{< stat "auteurs" >}} voix, sans ordre thématique, alphabétique ni chronologique. Le recueil se lit comme un roman&nbsp;: on avance de page en page, et le sens naît du voisinage. Qu'y trouve-t-on qu'on ne trouve ni dans les recueils classés ni sur les sites de citations&nbsp;? La rencontre qu'aucune recherche par mot-clé n'aurait produite — une réplique de cinéma à côté d'un moraliste, une chanson à côté d'un philosophe — et une curation d'auteur&nbsp;: quarante ans de lectures, une voix qui choisit. Pour retrouver une voix, l'édition brochée se clôt sur un index des auteurs qui renvoie à la page de chaque citation&nbsp;: un fil pour flâner, un index pour retrouver. Les chiffres exacts du corpus, leur histoire d'une édition à l'autre et la méthode de sélection sont détaillés sur la page [Méthode et corpus](/livresque/methode-et-corpus/).

## Offrir ce livre

Un objet littéraire qui se prête au cadeau&nbsp;: à qui et pourquoi, sur la page [Offrir un livre de culture générale](/offrir-un-livre-de-culture-generale/). En version Kindle, le cadeau passe par un lien prépayé — [mode d'emploi](/offrir-un-livre-kindle/).

## Au fil des pages

<div class="book-citations">

> Esclaves maintenant de plaisirs corrupteurs, / Que leur faut-il&nbsp;? du pain et des gladiateurs.
>
> — Juvénal

> Il n'y a point de plus cruelle tyrannie que celle que l'on exerce à l'ombre des lois et avec les couleurs de la justice.
>
> — Montesquieu

> Les fausses opinions ressemblent à la fausse monnaie qui est frappée d'abord par de grands coupables et dépensée ensuite par d'honnêtes gens qui perpétuent le crime sans savoir ce qu'ils font.
>
> — Joseph de Maistre

> Je forme une entreprise qui n'eut jamais d'exemple et dont l'exécution n'aura point d'imitateur. Je veux montrer à mes semblables un homme dans toute la vérité de la nature&nbsp;; et cet homme ce sera moi. Moi seul.
>
> — Jean-Jacques Rousseau, *Les Confessions* (incipit)

> Le poète s'interroge, le philosophe se regarde. Les poètes ont cent fois plus de bon sens que les philosophes. En cherchant le beau, ils rencontrent plus de vérités que les philosophes n'en trouvent en cherchant le vrai.
>
> — Joseph Joubert

> Quelques-uns donnent sans compter&nbsp;; le reste compte sans donner.
>
> — Albert Brie

</div>

---

Troisième édition, 2026, avec sommaire et index des auteurs, chaque citation réexaminée. Version papier pour la flânerie, version Kindle pour la recherche plein texte et l'index cliquable.
