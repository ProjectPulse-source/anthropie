# Plan d'architecture espagnole — audit et plan de modification arbitré

Audit read-only du 2026-08-03. **Aucun fichier du dépôt n'a été modifié.**
Répond à la commande de reprise (`REPRISE_PAGE_ES_2026-08-03.md` §8) et à
l'ordre de travail imposé (§3) : auditer d'abord, proposer ensuite, ne rien
toucher avant arbitrage.

---

## 1. Méthode et périmètre vérifié

Lus intégralement : `hugo.toml`, `menus.toml`, `params.toml`, `baseof.html`,
`head.html`, `header.html`, `footer.html`, `cross-language-banner.html`,
`how-to-cite.html`, `fr-typo.html`, `i18n/fr.toml`, `i18n/en.toml`,
`CHECKLIST_AJOUT_LANGUE.md`, `indexnow.yml`, `robots.txt`, `llms.txt`.
Mesurés par balayage : 26 layouts porteurs de conditionnels de langue,
20 fichiers `.en.md`, les mécanismes d'URL localisée, l'usage réel d'`i18n`.

---

## 2. Diagnostic

### 2.1. Ce qui est DÉJÀ correct pour N langues — à ne pas toucher

Quatre mécanismes structurants sont déjà génériques. C'est la bonne nouvelle
de l'audit, et elle réduit fortement le coût du chantier.

| Mécanisme | État | Preuve |
|---|---|---|
| **`hreflang`** | ✅ générique | `head.html` l. 14-27 boucle sur `.Translations` — il n'émet **que** les traductions réellement existantes, et rien du tout si la page n'est pas traduite. C'est exactement l'exigence non négociable, déjà satisfaite. |
| **`canonical`** | ✅ générique | `head.html` l. 32 : `.Permalink`. Auto-canonique par langue, jamais vers le français. |
| **Typographie française** | ✅ gardée | `fr-typo.html` l. 2 teste `site.Language.Lang == "fr"`. Conséquence concrète : **« ¿Qué es la antropía? » ne recevra pas l'espace fine française avant le `?`**, qui aurait été une faute en espagnol. Idem `french-typography.js`, chargé sous condition (`head.html` l. 84). |
| **Sitemap / IndexNow** | ✅ générique | Hugo produit un `<sitemapindex>` multilingue automatiquement ; `indexnow.yml` l. 78-81 **récurse déjà** l'index. Une langue ajoutée est prise en charge sans modification. |

**Le `x-default`** pointe vers le français quand une traduction FR existe
(`head.html` l. 19-25). Ce comportement reste juste avec trois langues.

### 2.2. Le mécanisme d'URL localisée est déjà éprouvé

L'anglais localise déjà ses URL par le champ `url:` en front matter :

```
content/livres/_index.en.md          → url: /en/books/
content/boucle-anthropique/_index.en.md → url: /en/anthropic-loop/
content/reversibilite-sociale/_index.en.md → url: /en/social-reversibility/
```

Conséquence directe : **`/es/que-es-la-antropia/` s'obtient sans rien casser**,
par `content/quest-ce-que-lanthropie/_index.es.md` + `url: /es/que-es-la-antropia/`.
Le groupe de traductions Hugo est formé par le chemin et le basename, avant
application du `url:`. Aucune `translationKey` n'est nécessaire.

### 2.3. Le défaut de classe : le site est câblé pour une PAIRE

**77 conditionnels binaires de langue, répartis dans 26 layouts.** Leur forme
canonique est toujours la même :

```go-html-template
{{- $isEn := eq .Lang "en" -}}   →   ... {{ if $isEn }}Books{{ else }}Livres{{ end }}
```

La branche `else` **est le français**. Ce n'est pas un défaut de propreté :
c'est le modèle de données. Ajouter `es` à la configuration produirait donc
mécaniquement des **pages espagnoles à chrome français** — précisément le
« retour silencieux vers le français » que vous interdisez.

Répartition (sites de décision par fichier) :

```
layouts/index.html                    28   ← home FR/EN
layouts/partials/head.html             9
layouts/partials/transmettre.html      5
layouts/livres/single.html             5
layouts/partials/header.html           3
layouts/awp/single.html                3
layouts/partials/livre-card.html       3
… 19 autres fichiers                  21
```

À l'inverse, la couche `i18n/` existe mais est **vestigiale** : 9 clés,
9 appels. L'infrastructure propre est là, elle n'a simplement jamais été
utilisée.

### 2.4. Trois pièges concrets, par ordre de gravité

**① `footer.html` — quatre 404 silencieux sur CHAQUE page espagnole.**
Le pied de page construit ses liens par `relLangURL` :

```go-html-template
<a href="{{ "/quest-ce-que-lanthropie/" | relLangURL }}">
<a href="{{ "/serie-awp/" | relLangURL }}">
<a href="{{ "/publications/" | relLangURL }}">
<a href="{{ "/glossaire/" | relLangURL }}">
<a href="{{ "/contact/" | relLangURL }}">
```

Sur une page ES, `relLangURL` produit `/es/publications/`, `/es/glossaire/`,
`/es/contact/` — **qui n'existeront pas** (corpus sélectif) — et
`/es/quest-ce-que-lanthropie/`, qui n'existera pas non plus **puisque le slug
espagnol est localisé**. Quatre liens morts, sur toutes les pages, sans aucun
signal. C'est l'item le plus dangereux du chantier.

**② `header.html` — le sélecteur promet des traductions inexistantes.**

```go-html-template
{{ if .IsTranslated }}…{{ else }}<a href="/en/">EN</a>{{ end }}
```

Une page non traduite propose quand même l'autre langue, vers sa page
d'accueil. Avec trois langues, la fausse promesse est doublée. Le sélecteur
doit être reconstruit sur `.Translations` **sans branche de repli**.

**③ Le champ `translation:` est une PAIRE, pas un graphe.**

```yaml
translation:
  doi: "10.5281/zenodo.19431208"
  url: "/en/awp/awp-01/"
  title: "What is anthropy? Principles of a hypothesis"
```

Champs **singuliers**. AWP-01 aura trois versions (FR `19266862`,
EN `19431208`, ES `21775366` v2). Deux consommateurs sont concernés :
`cross-language-banner.html` et le JSON-LD `workTranslation` /
`translationOfWork` de `head.html` (l. 214-218). Le schéma ne sait pas
exprimer un triplet.

Accessoirement, `cross-language-banner.html` est binaire **avec du texte
anglais en dur** : une page AWP espagnole afficherait le bloc *« Original
French version »* en anglais.

### 2.5. Point où je contredis la contre-expertise

`SCIELO-03.txt` §6.1 recommande :

```yaml
languages:
  es:
    contentDir: content/es
```

**À rejeter.** Le dépôt entier repose sur la convention par suffixe : 20
fichiers `.en.md` côte à côte, `check-geo-coverage.py` (l. 76-84) qui filtre
sur `.en.md`, `check-corpus-counters.py`, `CHECKLIST_AJOUT_AWP.md` §1 qui
l'impose explicitement. Passer en `contentDir` obligerait à **déplacer tous
les fichiers anglais**, donc à toucher les positions acquises — interdit
hérité (`08_ENGLISH_STRATEGY.md` §7.7). Le suffixe `.es.md` donne exactement
le même résultat pour zéro déplacement. La contre-expertise l'avait d'ailleurs
assortie de la réserve « à adapter à votre configuration actuelle ».

---

## 3. L'arbitrage architectural

> **Ouvrir l'espagnol n'est pas un problème de configuration, c'est un
> problème de généralisation du chrome.** La configuration prend dix lignes.
> Ce qui coûte, c'est de faire passer les gabarits d'un modèle « FR sinon EN »
> à un modèle « N langues ».

Trois voies possibles :

| Voie | Contenu | Verdict |
|---|---|---|
| **A. Ternaire imbriqué** | `cond $isEs … (cond $isEn … …)` sur les 77 sites | ❌ **NO-GO.** Surcouche : le coût croît en N², et la quatrième langue serait pire. C'est exactement le « couche N+1 » proscrit. |
| **B. Refactor i18n intégral** | Les 77 sites → clés `i18n` | Correct mais disproportionné : touche `livres/`, `publications/`, `index.html` — des gabarits **jamais rendus en espagnol**, donc risque de régression sur FR/EN acquis pour zéro bénéfice. |
| **C. Refactor du chemin ES seul + gate de sortie** | ~13 layouts effectivement traversés par une page ES → `i18n` ; les autres restent binaires ; un contrôle sur le HTML généré prouve la complétude | ✅ **Recommandé.** Traite la classe là où elle mord, laisse le reste intact, et remplace la promesse par une mesure. |

**Justification du choix C.** L'opérateur réflexif s'applique : le défaut est
bien de classe (77 instances), mais la mesure préventive proportionnée n'est
pas de refactorer les 77 — c'est de refactorer les ~30 qui sont sur le chemin
espagnol **et d'installer le contrôle qui empêche la classe de se reformer**.
Le jour où `/es/libros/` s'ouvrira, le gate signalera lui-même les gabarits
`livres/` restés binaires. La complétude n'est pas promise, elle est mesurée.

**Corollaire sur la home.** `layouts/index.html` (28 conditionnels, contenu
éditorial FR/EN : les trois axes, la vitrine AWP-06, le corpus) **ne doit pas
être touché**. Hugo cherche `layouts/index.es.html` avant `layouts/index.html`.
Le portail espagnol minimal vit dans son propre fichier. Zéro régression sur
la home française et anglaise.

---

## 4. Décisions qui vous reviennent

### D1 — Le sélecteur de langue perd son lien de repli

Aujourd'hui, une page française non traduite affiche quand même « EN », qui
renvoie à `/en/`. Votre exigence l'interdit. Le supprimer **change le
comportement de pages FR et EN existantes** : sur les pages non traduites, un
lien disparaît.

- **Avantage** : conforme à l'exigence, aucune fausse promesse, cohérent sur
  trois langues. Ne touche **ni les URL ni le câblage `hreflang`** — l'interdit
  hérité est respecté.
- **Inconvénient** : léger appauvrissement de la navigation sur les pages
  monolingues (l'utilisateur ne peut plus sauter vers l'accueil de l'autre
  langue depuis n'importe quelle page).
- **Recommandation** : **supprimer**. L'alternative — règle stricte pour ES,
  repli conservé pour FR/EN — produirait un comportement à deux vitesses,
  invérifiable et impossible à documenter.

### D2 — Migrer `translation:` (paire) vers une liste

- **Avantage** : le graphe FR↔EN↔ES devient exprimable, le JSON-LD
  `workTranslation` redevient complet pour Google Scholar, et la quatrième
  langue ne coûtera rien. Opération **mécanique et unique** : 16 fichiers AWP
  + 2 consommateurs, en une passe.
- **Inconvénient** : touche le front matter des fichiers `.en.md` (pas leurs
  URL, pas leur `hreflang`). Un oubli sur un fichier casserait un bandeau —
  détectable au build.
- **Alternative moins chère** : garder la paire ; ES pointe vers FR, FR ne
  pointe que vers EN. Le graphe reste incomplet côté schema.org, et la dette
  ressurgit au premier AWP-02 ES.
- **Recommandation** : **migrer maintenant**. C'est exactement le motif qui a
  fait rejeter la page isolée (§3 du dossier de reprise) : la dette technique
  apparaît à la deuxième publication.

### D3 — Portée du refactor i18n

- **Recommandation** : **voie C** — les ~13 layouts du chemin espagnol
  seulement, complétude prouvée par le gate de sortie.
- **Alternative** : voie B (les 26 layouts). Plus homogène, mais elle modifie
  des gabarits de production FR/EN sans qu'aucune page espagnole ne les
  emprunte.

---

## 5. Plan d'exécution en lots

### Lot 0 — Le contrôle AVANT la config *(inversion volontaire de l'ordre SCIELO-03)*

`SCIELO-03.txt` §11 place le contrôle de sortie en Gate 4. Je propose de
l'écrire **en premier**, pour la raison consignée au §7 du dossier de reprise :
*un contrôle qu'on n'éprouve pas ment* — le détecteur SSRN annonçait six
papiers absents alors qu'ils étaient tous en ligne.

Écrire `scripts/check-lang-output.py`, qui **build dans un répertoire jetable**
et inspecte le HTML généré (jamais la configuration) :

1. tout lien interne émis depuis `/es/**` résout-il vers un fichier généré ?
   *(c'est le piège ① qui devient impossible)* ;
2. le chrome d'une page ES contient-il un marqueur FR ou EN
   (`Livres`, `Books`, `Comment citer`, `How to cite`, `Tous droits réservés`…) ;
3. réciprocité `hreflang` : chaque page d'un groupe émet-elle le même ensemble,
   y compris elle-même ;
4. `<html lang="es">`, `<title>`/`description` espagnols, canonical auto-référente ;
5. présence dans le sitemap.

**Puis l'éprouver contre un cas connu-vrai** : injecter délibérément un libellé
français et un lien mort dans un stub ES, vérifier que le contrôle les voit,
retirer l'injection. Sans cette étape, le contrôle n'est pas un contrôle.

### Lot 1 — Configuration *(≈ 15 lignes)*

- `[languages.es]` : `weight = 3`, `languageCode = "es"`, `languageName = "Español"`.
  Code générique `es` — pas de variante régionale (`es-ES`/`es-419`), conforme
  à la recommandation Google citée en `SCIELO-03` §6.1.
- `[languages.es.params]` : `description` + `canonicalDefinition` portant le
  **verbatim canonique espagnol**
  *« La antropía es la hipótesis según la cual los sistemas sociales desplazan
  el desorden en lugar de resolverlo. »*
- **Garde de build ES**, en miroir de la garde française existante
  (`baseof.html` l. 1-3, qui fait échouer le build si le verbatim FR perd le
  mot « déplacent ») : le build échoue si le verbatim ES perd « desplazan ».
  C'est le même invariant que contrôle `zenodo_audit_complet.py`, appliqué au
  site. Coût : 3 lignes.
- Menu espagnol : **3 entrées** — `Inicio` · `¿Qué es la antropía?` ·
  `Working Papers`. **Pas de `Contacto`** tant qu'aucune page de contact
  espagnole n'existe (le menu ne doit pas promettre ce qui n'existe pas).

### Lot 2 — Généralisation du chrome

`footer.html` (liens conditionnés à l'**existence réelle de la page** via
`site.GetPage`, au lieu de `relLangURL` — supprime la classe, pas l'instance) ·
`header.html` (sélecteur strict sur `.Translations`, sans repli) ·
`i18n/es.toml` + extension de `fr.toml`/`en.toml` · `cross-language-banner.html`
(généralisé, rendu dans la langue de la page) · `how-to-cite.html` ·
`awp/single.html` · `serie-awp/list.html` · `awp-card.html` ·
`related-awp.html` · `awp-in-press.html` · `transmettre.html` ·
`_default/list.html` · `schema-creativeworkseries.html` + `schema-website.html`
(URL de concept et de série par langue).

Migration `translation:` → liste si **D2** est validée.

### Lot 3 — Squelettes, non publiés

`layouts/index.es.html` (portail minimal, fichier neuf) ·
`content/_index.es.md` · `content/quest-ce-que-lanthropie/_index.es.md`
(`url: /es/que-es-la-antropia/`) · `content/awp/awp-01.es.md`
(DOI **v2** `10.5281/zenodo.21775366`) · `content/serie-awp/_index.es.md`
(deux ensembles : *Disponibles en español* / *En francés e inglés*).

Structure seule, textes en attente. **Gate : le contrôle du Lot 0 doit sortir
zéro défaut avant d'injecter la moindre ligne de contenu.**

### Lot 4 — Contenu *(second temps du fil)*

La page « ¿Qué es la antropía? ». Entrée n°1 :
`reports/geo_audit/REGISTRE_COLLISIONS.md`, section antropía/ES. Règle :
**adapter, pas traduire** — affronter les voisins hispanophones (marque OEPM
ANTROPÍA de Vocento, rubrique `elcorreo.com/antropia/`, *Anthropía* PUCP, sens
« anthropisation », démarcation Stiegler traduite), **pas** recopier la liste
française. CEPAL / *centro-periferia* / *dependencia* : voisins et précédents
partiels, **jamais une filiation** (arbitrage du 02/08).

### Lot 5 — Registres *(règle « l'état écrit suit l'acte »)*

`static/llms.txt` (section ES, en miroir de la section English l. 69-79) ·
`scripts/check-geo-coverage.py` (étendre le miroir [5] à l'espagnol) ·
`data/works.yaml` · `PROJECT_STATUS.md` § log · `docs/CHECKLIST_AJOUT_LANGUE.md`
(Phase 1 passe de « à faire » à « fait, voici comment »).

---

## 6. Ce que ce plan ne crée PAS

Conforme au corpus sélectif (§3 du dossier, `SCIELO-03` §4) :
`/es/libros/` (tant qu'aucune édition espagnole n'est réelle) ·
`/es/publicaciones/` · `/es/glosario/` · `/es/contacto/` · `/es/prensa/` ·
`/es/sobre-mi/` · aucune traduction des recensions · aucune rubrique
d'actualités · **aucun miroir automatique**.

`layouts/index.html`, `layouts/livres/**`, `layouts/publications/**`,
`layouts/presse/**`, `layouts/a-propos/**` : **non modifiés**.

---

## 7. Ce que je n'ai pas pu vérifier sans construire

Le groupement des traductions par Hugo **quand le `url:` diffère d'une langue
à l'autre** ne peut pas être prouvé par lecture seule. Le cas anglais le rend
très probable (`/en/books/` coexiste avec `/livres/` et le pied de page émet
bien un lien « Version française »), mais **ce n'est pas une preuve** : je ne
l'affirmerai qu'après le premier build du Lot 0. Si Hugo ne groupait pas, le
recours est `translationKey: quest-ce-que-lanthropie` — une ligne, sans effet
sur les URL.

---

## 8. Ordre de grandeur

| Lot | Fichiers | Nature |
|---|---|---|
| 0 — contrôle éprouvé | 1 nouveau | script |
| 1 — configuration | 2 | ~18 lignes |
| 2 — chrome | ~13 modifiés, 1 nouveau | refactor |
| 3 — squelettes | 5 nouveaux | structure |
| 4 — contenu | 1 | rédaction |
| 5 — registres | 5 | mise à jour |

Aucun fichier `.en.md` ne change d'URL. Aucun `hreflang` existant n'est
supprimé. Le seul changement de comportement sur les pages FR/EN est celui de
la décision **D1**, s'il est validé.

---

# 9. AMENDEMENT — après contre-expertise `SCIELO-05.txt` (2026-08-03)

Les trois décisions sont arbitrées. **D1 = option 1. D3 = voie C. D2 = migration,
mais selon un modèle que la contre-expertise corrige — et que je corrige à mon
tour sur deux points.**

## 9.1. D2 — le champ `translation:` ne doit pas être migré, il doit disparaître

Ma proposition initiale (§4, D2) était fautive : je proposais de migrer un champ
redondant vers une **liste** redondante, sans lui appliquer le test de
suppression. Vérification faite dans le dépôt, tout ce que réclament les deux
consommateurs est **déjà porté par la page sœur** :

| Champ de `translation:` | Déjà disponible | Verdict |
|---|---|---|
| `doi` | `doi_zenodo` de la traduction | redondant |
| `title` | `.Title` de la traduction | redondant |
| `url` | `.Permalink` de la traduction | redondant |
| `is_canonical` | — | **seul irréductible** |

**Modèle retenu** : suppression du bloc `translation:` ; `cross-language-banner.html`
et le JSON-LD `workTranslation`/`translationOfWork` reconstruisent le groupe
depuis `.AllTranslations` et les métadonnées propres de chaque page.

**Deux corrections apportées à `SCIELO-05` :**

1. **Pas de `work_id`.** Le dépôt porte déjà trois identifiants stables de
   l'œuvre : `awp_number: "AWP-01"` en front matter, le basename dont Hugo
   dérive le groupe de traductions, et les slugs nus de `related:`. Un quatrième
   identifiant échouerait au test de suppression que la contre-expertise vient
   elle-même d'appliquer à la liste.
2. **`is_original: true` sur le seul fichier de langue source**, plutôt que
   `original_language: fr` recopié sur les trois fichiers. Une ligne, un fichier,
   zéro duplication ; les consommateurs balaient `.AllTranslations`. Cela redresse
   au passage une incohérence actuelle : `is_canonical: true` vit dans le bloc
   `translation:` du fichier **anglais**, où il ne décrit pas la page mais sa
   cible — propriété écrite à l'envers.

**Conséquence fonctionnelle assumée** : une traduction n'est annoncée que
**quand sa page existe**. AWP-01 ES a son DOI depuis le 03/08 mais pas de page :
la page française ne l'annoncera qu'au Lot 3. Ce n'est pas une régression — c'est
la doctrine « pas de promesse sans actif » qui devient structurelle.

## 9.2. D3 — les cinq conditions, une simplification, un couplage

Les cinq conditions supplémentaires sont acceptées. La **condition 4** corrige un
défaut réel du §5 Lot 0 ci-dessus, qui prévoyait d'injecter un défaut dans un stub
puis de « retirer l'injection » — c'est-à-dire de modifier un fichier de production
en comptant sur la mémoire de l'opérateur pour revenir en arrière. **Fixtures en
répertoire temporaire uniquement.**

**Simplification** : 0A (baseline) et 0B (gate) sont le même outil — build, parse
du HTML, extraction d'invariants. **Un seul script à deux modes**, `--snapshot` et
`--check`, plutôt que deux dispositifs. La condition 5 (non-régression FR/EN) est
alors obtenue gratuitement au lieu d'être un sixième contrôle.

**Couplage non nommé jusqu'ici** : D2 ne touche pas que des bandeaux — il **change
le JSON-LD émis sur les pages anglaises**, qui portent des positions acquises et
mesurées. `workTranslation` passe de `url | absURL` à `.Permalink` ; le résultat
*devrait* être identique. La baseline 0A n'est donc pas un confort méthodologique :
**c'est la condition qui rend D2 exécutable**. L'ordre 0A → … → Lot 2 n'est pas
négociable et ne sera pas contourné si le Lot 2 s'avère long.

## 9.3. Ordre d'exécution arrêté

```
0A  snapshot des invariants FR/EN (URL, canonical, hreflang, DOI, JSON-LD,
    liens internes, sélecteurs) — AVANT toute modification
0B  gate --check, éprouvé contre des fixtures corrompues en répertoire temporaire
1   configuration ES (+ garde de build sur le verbatim canonique espagnol)
2   généralisation du chrome + suppression du champ translation:
    → gate --check après chaque lot ; ARRÊT IMMÉDIAT au premier invariant violé
3   squelettes non publiés
4   contenu espagnol
5   registres — seulement après build réussi ET inspection humaine des 4 pages
```

Gate **bloquant** (exit ≠ 0), à la différence de `check-geo-coverage.py` qui est
délibérément informatif. Découverte automatique de `/es/**`, jamais de liste
écrite à la main.

---

# 10. PLAN ARRÊTÉ — après panel de développement interne (2026-08-03)

**Ce chapitre remplace le §5 et le §9.3.** Quatre sièges convoqués : conception,
adversarial/sécurité, efficience/mission, et un quatrième siège **GEO
hispanophone** — dimension absente des six contre-expertises, qui étaient
purement techniques.

## 10.1. Le défaut que six contre-expertises ont traversé sans le voir

**`head.html` n'est générique que sur `hreflang`.** Tout ce qui l'entoure est
écrit `cond (eq .Lang "en") X Y` — « si anglais, sinon FRANÇAIS ». Les
contre-expertises ont audité la ligne 14 et se sont arrêtées là.

| `head.html` | Ce qu'une page ES émettrait |
|---|---|
| **l. 207-209** | **`about` → l'`@id` du concept FRANÇAIS** |
| l. 151 | `DefinedTerm` espagnol **jamais émis** (test sur deux `RelPermalink` en dur) |
| l. 37 | `og:locale` = `fr_FR` |
| l. 204-205 | `isPartOf` → série française |
| `hugo.toml` l. 46-48 | `canonicalDefinition` **française** par repli silencieux |

La ligne 207-209 est le cœur : **l'AWP espagnol déclarerait porter sur le concept
français** — le signal « la version espagnole est dérivée, citez le français ».
Une page dont le texte visible est espagnol et la carte d'identité machine
française.

## 10.2. Quatre angles morts vérifiés par lecture directe

1. **`scripts/check-corpus-counters.py` l. 144-146** — `awp-01.es.md` correspond
   au glob `awp-*.md` et ne finit pas par `.en.md` : **compté français**.
   `truth_fr` passe à 9, tout « huit working papers » du contenu FR devient une
   erreur, et CLAUDE.md exige « 0 avant commit ». **Blocage de lot 1**, pas de
   lot 5. Même modèle binaire dans `check-geo-coverage.py` l. 81.
2. **`.github/workflows/indexnow.yml` l. 9-15** — déclenché sur `config/**` ET
   `layouts/**`. Pousser le lot 1 seul crée `/es/` (Hugo génère la home de chaque
   langue déclarée), rendue par `layouts/index.html` dont toutes les branches
   `else` sont françaises, entrée au sitemap, **soumise à Bing/Yandex/Naver**,
   avec les homes FR et EN portant `hreflang="es"` vers elle. **Une soumission ne
   se rétracte pas.**
3. **`related-awp.html` l. 13** — `Site.GetPage "/awp/awp-02"` renvoie nil côté
   ES : `<aside>` et `<h2>` rendus autour d'un `<ul>` vide. HTML valide, zéro 404,
   page cassée, invisible à tout gate.
4. **`cross-language-banner.html`** — deux branches, **texte anglais en dur dans
   les deux**. Une page espagnole afficherait un bandeau anglais.

## 10.3. Divergences tranchées

**① Le gate : `diff -r` remplace le script à contrats.** `diff -r pre post` sur
deux builds ne *représente* rien — il compare des octets. Le doublon
`hreflang="en"`, le double lien « Version française », la disparition du JSON-LD
glossaire : invisibles à un dict Python `{lang: url}`, triviaux dans un diff
textuel. Condition : **épingler le build des deux côtés** — `--minify`,
`--baseURL https://stephane-lalut.com/`, environnement production (le CI écrase
le baseURL de `hugo.toml` et minifie ; `hugo.IsProduction` conditionne du
balisage). **C1 et C3 tombent. C2 se réduit à deux lignes** (`public/es/*.html`
non vide, au compte exact). La direction du JSON-LD se vérifie par **lecture
humaine du diff**, pas par contrat : aucune machine ne juge « le français est
l'original ».

**② D2 REPORTÉ — contredit ce qui avait été validé avec SCIELO-05 et SCIELO-06.**
Fait nouveau : `translation:` est lu en **quatre endroits** (`awp/single.html`
l. 88, 141, 174 + le bandeau). Le supprimer des 16 fichiers sans refondre ces
gabarits ferait disparaître le lien FR↔EN sur 16 pages en production. Et la
polarité s'inverse (`is_canonical` sur la traduction → `is_original` sur
l'original) : une erreur de sens publie « l'anglais est l'original du français »
sur huit AWP, en JSON-LD valide. Coût du report, mesuré : la page FR d'AWP-01 ne
déclare pas `workTranslation` vers l'espagnol. C'est tout — `hreflang` et le
sélecteur couvrent la réciprocité. **D2 n'est pas nécessaire aux pages
espagnoles et porte le seul risque irréversible-en-publication du chantier.**
Reporté au 2e AWP ES, en commit isolé.

**③ Périmètre : TROIS pages.** `/es/serie-awp/` tombe — liste à un élément, et
contradiction non résolue : si ce n'est pas une traduction de `/serie-awp/`, la
déclarer comme telle promet une équivalence fausse à `hreflang` ; ne pas la
déclarer la prive de `hreflang` et d'`x-default`. Son information — « 1 de 8
disponible en español ; los demás, en francés e inglés » — tient en un paragraphe
sur `/es/`. Une URL de moins en concurrence sur « antropía ».

**④ L'ordre.** Trois sièges convergent : la seule chose vraiment irréversible du
dossier n'est pas technique — **une baseline de sondes prise après la mise en
ligne est perdue à jamais**, et `reports/geo_audit/T0_REQUETES_GOOGLE_ES.md`
n'existe pas.

## 10.4. Trois faits qui périment le dossier de reprise

- **Le DOI à graver est le DOI de CONCEPT `10.5281/zenodo.21766183`**, pas la
  version `21775366`. C'est déjà celui que le record FR référence, et déjà la
  doctrine du projet (commit `27f4241` : « le registre suit le CONCEPT pour les
  œuvres versionnées »). Le §2 ci-dessus porte encore `21766184` : trois numéros
  circulent, un seul doit être gravé.
- **Wikidata Q138827949 déclare `P31 → Q17737 « théorie »`** — contredit la règle
  absolue du projet sur la couche que les machines lisent en premier. Défaut
  trilingue. La description ES ne nomme pas Lalut, contrairement à FR et EN.
- **Aucun agrégateur hispanophone ne moissonne Zenodo.** Dialnet, Redalyc,
  Latindex, LA Referencia, Recolecta : fermés sans revue ni dépôt institutionnel.
  La découverte espagnole passera par des infrastructures **génériques** —
  OpenAlex (AWP-01 FR et EN déjà présents), OpenAIRE, BASE, CORE, Scholar.
  MPRA est le seul levier disciplinaire hispanophone réel, mais la **doctrine du
  dépôt échelonné** l'interdit tant que la file n'est pas vide.
- Mots-clés Zenodo ES en castillan péninsulaire (« costes ») pour une audience
  majoritairement américaine (« costos »), et **zéro code JEL** — donc inexistant
  pour le circuit économique, y compris celui qu'on viserait via MPRA.

## 10.5. Arbitrages éditoriaux rendus par l'auteur

- **La page ES sera plus longue et plus argumentative que ses sœurs.** Section
  Stiegler placée immédiatement après la définition, citant la source primaire
  espagnole (*Bifurcar*, trad. Paláu, DOI `10.22395/csye.v12n23a13`, p. 311).
  **Précision de l'auteur (04/08)** : cette section reste une démarcation
  **courte et probatoire** — elle établit la distinction et cite la source, puis
  cède la place au **développement positif du concept**. Elle ne devient pas une
  discussion de Stiegler : le lecteur vient chercher la définition de l'auteur,
  pas l'histoire du mot. La longueur supplémentaire de la page ES va au concept,
  pas au voisin.
  Motif : le risque n°1 en espagnol n'est pas l'absence, c'est **l'absorption** —
  qu'un moteur fusionne l'antropía de Lalut avec celle de Stiegler, présent
  depuis 2023 dans une revue colombienne indexée. La dissymétrie de format répond
  à une dissymétrie réelle de l'appareil (AWP-07 non traduit).
- **`related-awp` sur la page ES : repli sur FR/EN avec marquage de langue
  explicite en espagnol** — « (en francés) », « (en inglés) » + `hreflang`.
  Jamais de bloc vide, jamais de cul-de-sac.

## 10.6. Séquence arrêtée

```
PHASE 0 — hors dépôt, aucun risque, PASSE DEVANT TOUT
   T0_REQUETES_GOOGLE_ES.md : requêtes figées AVANT mise en ligne,
     double géolocalisation Espagne + Amérique latine (proxies Webshare) ;
     une sonde espagnole passée depuis la France ne mesure qu'un artefact
   Wikidata : retirer P31 « théorie » · nommer Lalut dans la description ES ·
     P1889 → Q2707809 (antropización) · P973 ES après mise en ligne seulement
   Zenodo ES : codes JEL, doublet costes/costos, isDescribedBy, mots-clés
   Brouillon de la page conceptuelle → relecture native : CHEMIN CRITIQUE

PHASE 1 — local, non poussé
   build de référence épinglé  →  /tmp/pre
   config ES + menus ES (3 entrées) + garde de build sur le verbatim ES
   PATCH check-corpus-counters.py et check-geo-coverage.py (bloquants)

PHASE 2 — le vrai lot : head.html de binaire à trilingue
   about / isPartOf / DefinedTerm / og:locale / canonicalDefinition ES
   footer (existence de page, jamais relLangURL) · header (sélecteur strict)
   cross-language-banner (3 branches) · related-awp (repli marqué)
   how-to-cite · awp/single · i18n/es.toml · layouts/index.es.html

PHASE 3 — contenu espagnol relu par un natif

PHASE 4 — contrôle : build épinglé → /tmp/post ; diff -r
   le diff ne doit montrer QUE des ajouts sous /es/** et les hreflang attendus
   public/es/*.html non vide et au compte exact
   lecture humaine du diff JSON-LD
   ARRÊT au premier écart inexpliqué

PHASE 5 — push unique, puis registres (llms.txt section Español, PROJECT_STATUS,
   checklists) — après build réussi ET inspection des pages en ligne
```

**Porte humaine, plus contraignante qu'anticipé** : rien ne part sur `main` avant
que le contenu espagnol existe et soit relu — sinon `indexnow.yml` soumet une
page française déclarée espagnole. Alternative si un push intermédiaire s'impose :
lot 1 avec `/es/` exclu de la sortie, et le diff **prouve** son absence du
sitemapindex.
