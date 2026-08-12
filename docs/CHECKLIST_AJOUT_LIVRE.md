# Checklist — Ajout d'un nouveau livre

> Miroir de `CHECKLIST_AJOUT_AWP.md` pour la section `content/livres/`.
> Créée suite à l'audit GEO-03 du 2026-07-08 (industrialisation de
> l'indexation des œuvres à venir). À réviser après chaque publication.

## 0. Prérequis produit (hors dépôt)

- [ ] ASIN broché + ASIN Kindle actés et inscrits au **catalogue canonique**
      (source unique ASIN/ISBN — ne jamais improviser un identifiant).
- [ ] Prix broché acté (jamais de prix inventé : le champ `price` alimente
      l'`Offer` schema.org affiché à Google).
- [ ] Couverture finale disponible : **un seul fichier**
      `assets/images/livres/<slug>.jpg` (le remplacer suffit à propager).
      Spec GEO du fichier :
      - portrait **2:3, 1000 × 1500 px** (gabarit des 4 couvertures en place),
        JPEG, poids indicatif ≤ 250 KB — l'original est publié tel quel à
        l'URL stable `/images/livres/<slug>.jpg` (référencée par works.yaml
        et les registres externes) ;
      - nom = **slug exact** de la fiche (`.File.ContentBaseName`) ;
      - édition anglaise réelle : variante `assets/images/livres/<slug>.en.jpg`
        (repli automatique sur la couverture FR si absente) ;
      - la couverture est propagée automatiquement : JSON-LD `Book.image`
        (ImageObject avec dims réelles + crédit), **og:image de la fiche**
        (aperçu = la couverture ; `og_image` en front matter = opt-out),
        cartes /livres/, emblème home, pages ressources. Rien à câbler.
      - `data/works.yaml` : renseigner `image_url` avec l'URL stable
        (consommée par les registres externes — Wikidata, OpenLibrary…).

## 1. Fiche `content/livres/<slug>.md`

Front matter — modèle : `anthropie-ordre-ici-dette-ailleurs.md` :

- [ ] `title`, `date`, `description` (+ `description_en`)
- [ ] `price: "NN"` — prix broché EUR réel
- [ ] `isbn` (broché), `pages`, `serie`
- [ ] `wikidata_qid` dès que l'item Wikidata existe (alimente `sameAs` du Book)
- [ ] Liens Amazon **canoniques `/dp/<ASIN>`** par marché :
      `url_amazon_fr|es|com|uk|de|it|ca` + variantes `_kindle`.
      **Jamais de shortener** (`amzn.eu`, `a.co`) — collisions avérées en 2026-06.
- [ ] `related_awp: []` — mapping chapitres → AWP (graphe de navigation)
- [ ] `reviews: []` le cas échéant (author/quote/date/url/source ;
      pas d'`aggregateRating` importé — interdit acté)
- [ ] **Pas de pendant `.en.md`** (décision actée 2026-07-04). À réviser
      uniquement quand une **édition anglaise** existera comme produit réel
      (ASIN propre, `inLanguage: en`).

## 2. Registres et surfaces à synchroniser

- [ ] **Notes Amazon (`amazon_rating`/`amazon_reviews`) — rien à inscrire, mais
      savoir** : la routine mensuelle (rappel Outlook du 10) dérive sa liste de
      **toutes** les fiches `content/livres/*.md` porteuses d'un ASIN — jamais
      d'une liste figée ; un nouveau livre est donc relevé d'office dès le mois
      suivant. Les 2 champs restent **absents** tant que la preuve sociale n'est
      pas matérielle (décision auteur, ordre de grandeur ≥ 10 avis — garde anti
      « preuve sociale inversée » : champs absents = pas d'étoiles affichées).
      *(Trou du 2026-08-12 : Premier coup présent sur /ressources-offertes/
      depuis le 10/08, absent de la routine figée à 4 livres — corrigé en
      dérivant la liste du dépôt.)*
- [ ] `data/works.yaml` : entrée du livre (registre canonique — audité par
      `scripts/audit_works.py`).
- [ ] **Inscription périphérie→centre (OBLIGATOIRE, quelle que soit la
      langue ou le sujet du livre)** : déclarer le ou les **sujets d'entrée
      périphériques** du livre (dette, écologie, IA, citations, culture
      générale…) et poser le **fil remontant** vers le cadre (lien vers la
      page concept ou l'AWP pertinent dans le corps de la fiche). La fiche
      doit valoir par son sujet propre ; l'anthropie est le fil, jamais une
      étiquette plaquée.
- [ ] `data/intent_matrix.yaml` : entrée du livre (sujets d'entrée, cercles
      de requêtes, statuts couverte/enrichissement/différée — lire la
      doctrine en tête du fichier : aucune page ne se crée depuis la matrice).
- [ ] `static/llms.txt` : ajouter le livre (ISBN + Wikidata) à la main —
      la génération par template est un interdit acté.
- [ ] Si `faq[]` ajoutée à la fiche : questions **book-scoped** uniquement
      (jamais une question définitionnelle déjà possédée par une page pont)
      et **aucun chiffre canonique en dur** dans les `answer` (source
      unique `works.yaml` corpus_stats).
- [ ] Compteur hero `layouts/index.html` : décider si le livre entre dans le
      décompte du **cadre anthropique stricto sensu** ; si oui, incrémenter
      en lettres dans les 2 blocs FR + EN.
- [ ] **Mur « Auteur » de `/a-propos/` — la tuile apparaît TOUTE SEULE**
      (depuis le 2026-08-11 : présence lue dans `content/livres/`, groupée par
      `serie`, triée par `weight`). Il ne reste qu'à écrire l'**éditorial**
      dans `wall_lignes` de `content/a-propos/_index.md` **et** `_index.en.md` :
      - `line` (attendu) — HOOK, une loi contre-intuitive qui agrippe le lecteur
        qualifié et filtre l'autre, puis RAISON DE CLIQUER. Jamais de définition
        de genre en tête. **Test de survie : la ligne ne doit pas fonctionner
        sur un autre livre.** Absente → le livre s'affiche quand même et
        `hugo --minify` émet un `WARN auteur-wall :` (visible dans le log CI ;
        ⚠ `--quiet` l'étouffe, ne pas l'utiliser pour ce contrôle) ;
      - `meta` (facultatif) — **ne rien écrire** pour une pagination simple :
        elle est dérivée de `pages` de la fiche. Ne le poser que pour un rang
        d'édition (« 3ᵉ édition »). Jamais d'année (décision auteur 2026-08-09).
      *Motif : ce mur itérait sur une liste manuelle et « La Société du premier
      coup » y est restée invisible le lendemain de sa parution, sans erreur ni
      trace. La présence vient du dépôt, l'éditorial du front matter.*
- [ ] Maillage entrant : fiches `content/publications/*.md` concernées
      (`related_book`), pages offrir/ressources si pertinent.

## 3. Vérifications avant commit

- [ ] `hugo server` : JSON-LD `Book` complet (isbn, Offer avec le bon prix,
      sameAs Wikidata, image), og:image correcte (safe-zone WhatsApp),
      boutons Amazon Broché/Kindle par marché.
- [ ] `python scripts/check-corpus-counters.py` → exit 0.
- [ ] `python scripts/audit_works.py` → pas de warning nouveau.
- [ ] `python scripts/check-fiches-registre.py` → exit 0 (parité fiche ↔ `works.yaml` :
      QID Wikidata, pagination, ISBN — attrape « le registre le sait, la fiche ne le dit pas »).
- [ ] `hugo --minify` → build OK.

## 4. Indexation (après merge sur `main`)

Automatique : déploiement Pages → workflow **IndexNow** (Bing/Yandex/Naver/
Seznam ; l'index Bing alimente Copilot et ChatGPT Search) → sitemap à jour
(Google découvre naturellement en 3-7 jours) → archivage Wayback mensuel.

- [ ] Vérifier dans le log GitHub Actions du run IndexNow le **nombre
      d'URLs de pages extraites** (le vert seul ne prouve rien).
- [ ] Accélération Google (facultative, manuelle) : Search Console →
      inspection d'URL → « Demander une indexation » sur la fiche FR
      (24-48 h au lieu de 3-7 j). Google ne supporte ni IndexNow ni
      d'API d'indexation pour ce type de contenu — il n'y a rien de plus
      à automatiser côté Google.

## 5. Nœuds externes (différables, mais à tracer)

- [ ] Item Wikidata du livre (scripts `Wikidata/scripts/`, import Laura).
- [ ] Fiche OpenLibrary (author `OL16378291A`).
- [ ] Dépôt légal BnF (broché).
