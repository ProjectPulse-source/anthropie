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

- [ ] `data/works.yaml` : entrée du livre (registre canonique — audité par
      `scripts/audit_works.py`).
- [ ] `static/llms.txt` : ajouter le livre (ISBN + Wikidata) à la main —
      la génération par template est un interdit acté.
- [ ] Compteur hero `layouts/index.html` : décider si le livre entre dans le
      décompte du **cadre anthropique stricto sensu** ; si oui, incrémenter
      en lettres dans les 2 blocs FR + EN.
- [ ] Maillage entrant : fiches `content/publications/*.md` concernées
      (`related_book`), pages offrir/ressources si pertinent.

## 3. Vérifications avant commit

- [ ] `hugo server` : JSON-LD `Book` complet (isbn, Offer avec le bon prix,
      sameAs Wikidata, image), og:image correcte (safe-zone WhatsApp),
      boutons Amazon Broché/Kindle par marché.
- [ ] `python scripts/check-corpus-counters.py` → exit 0.
- [ ] `python scripts/audit_works.py` → pas de warning nouveau.
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
