# Wikidata — navette du 2026-09-03, **3ᵉ lot** (4 lignes, un seul Run) : Babelio

Laura — rien à créer. On ajoute l'identifiant Babelio de l'auteur, et celui de
**trois** livres sur six. Les trois autres attendent, pour la raison dite plus bas.

| Item | Propriété | Valeur | Fiche Babelio |
|---|---|---|---|
| **Q138909233** Stéphane Lalut | `P3630` auteur | `636238` | /auteur/Stephane-Lalut/636238 |
| **Q138827344** ANTHROPIE | `P3631` œuvre | `1922333` | /livres/Lalut-ANTHROPIE…/1922333 |
| **Q138910896** Dette Publique | `P3631` œuvre | `1947782` | /livres/Lalut-Dette-Publique…/1947782 |
| **Q141072263** La Société du premier coup | `P3631` œuvre | `2105689` | /livres/Lalut-LA-SOCIT-DU-PREMIER-COUP…/2105689 |

La valeur est le **nombre seul** : les deux propriétés imposent `\d+`, et la
*formatter URL* de Wikidata est `babelio.com/auteur/wd/$1` — le fragment de titre
dans l'URL réelle ne fait pas partie de l'identifiant.

## Comment faire — UN CLIC

1. Ouvrir le lien du fichier **`deeplink.txt`**.
2. **Vérifier le preview** : quatre **ajouts de déclaration**, un `P3630` et trois
   `P3631`, chacun avec sa référence. Si une ligne annonce autre chose, ne pas
   lancer et me le dire.
3. **Run**, puis me confirmer.

Repli : coller `batch_quickstatements.txt` en mode Import V1, sans les lignes `//`.

## ⛔ Pourquoi l'Odyssée et Livresque ne sont pas dans ce lot

Les deux ont **deux fiches Babelio vivantes**, et dans les deux cas c'est l'ancienne
qui porte la réception :

| Livre | Fiche ancienne | Fiche récente |
|---|---|---|
| L'Odyssée des idées | `1626056` — « De l'aube de l'humanité à l'ère numérique », **plusieurs pages de critiques** | `2105688` — « Culture générale, histoire, philosophie… », neuve |
| Livresque des mots | `1472366` — « Anthologie éclectique de citations », **29 critiques, 20 citations** | `1648633` — « Anthologie inédite & éclectique… », le titre actuel |

Poser `P3631` maintenant reviendrait à graver dans Wikidata la moitié d'un livre —
et probablement la moitié vide. C'est exactement ce qui a été refusé le matin même
sur Goodreads, pour la même raison, avant que la réunion des éditions ne rende les
identifiants stables. **Ces deux lignes viendront quand Babelio aura fusionné.**

## Ce qui a été contrôlé, et ce qui ne peut pas l'être

⚠ **Aucune fiche Babelio n'a pu être relue à la source.** Le site rend **403** à toute
requête directe, refuse la récupération de page, et oppose une vérification anti-robot
dans le navigateur — qui n'est pas franchie. Les identifiants de ce lot viennent des
**URL relevées par l'auteur dans son propre navigateur** le 03/09. C'est une preuve
plus faible que celle du lot Goodreads du même jour, où chaque rattachement avait été
vérifié contre l'ISBN porté par l'item. **Dit, pas tu.**

📌 Corollaire de méthode, vérifié aux dépens du dossier : **la liste fournie par
l'auteur n'est pas un recensement.** Elle donnait une fiche Livresque ; il y en a deux.
L'écart a été trouvé par une recherche indépendante, pas par la liste. Avant d'ajouter
`P3631` à un sixième livre, refaire cette recherche croisée — ne jamais déduire d'une
seule énumération qu'elle est complète.

## Ce que Babelio apporte, et ce qu'il n'apporte pas

Mesuré le 03/09 dans `babelio.com/robots.txt` : Babelio **interdit l'intégralité des
robots d'IA** — `GPTBot`, `ChatGPT-User`, `OAI-SearchBot`, `CCBot`, `Google-Extended`,
`PerplexityBot`, `anthropic-ai`, `Claude-Web`, `ClaudeBot`, `Applebot-Extended`,
`FacebookBot`, `Bytespider`, `meta-externalagent`. Comparaison faite le même jour :
Goodreads ne bloque que `GPTBot` et `CCBot`, donc laisse passer les robots de
**recherche** (`OAI-SearchBot`, `PerplexityBot`, `ClaudeBot`).

**Conséquence à ne pas confondre** : cet arc n'apporte **rien** en visibilité IA — aucun
modèle ne lira jamais une page Babelio. Il vaut pour deux autres choses : la complétude
de l'item Wikidata, qui est lu par tous ces robots ; et le référencement classique, car
Babelio reste indexable par Google et Bing. Ne pas le porter au crédit du GEO.

Merci !
