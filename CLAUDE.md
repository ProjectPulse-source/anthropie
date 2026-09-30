# CLAUDE.md

## Stack

Static site for **stephane-lalut.com** (Stéphane Lalut, économiste). Hugo Extended **0.147.0**, Sass natif Hugo, vanilla JS, **zéro dépendance npm**. Déployé sur GitHub Pages via `.github/workflows/hugo.yml` à chaque push sur `main`. *(Le domaine anthropie.fr n'a jamais été détenu — aftermarket Premium GoDaddy, dossier clos 2026-06-04 : ne jamais le référencer comme site vivant.)*

## Layouts & partials clés

Section `awp` : quatre sorties par working paper — `single.html` plus **BibTeX / RIS / EndNote**, déclarées en `outputFormats` dans `hugo.toml`. L'URL `/awp/` redirige vers `/serie-awp/` par `aliases` ; les pages individuelles restent en `/awp/awp-01/`.

Section `publications` : cartes via `partials/publication-card.html`, gabarit unique **160×107** que réemploie le mur presse de `/a-propos/` (`partials/presse-wall.html`) — une seule règle y sert donc les deux pages.

⚠ `assets/js/hero-flowfield.js` existe dans le dépôt mais n'est plus chargé (canvas supprimé lors du redesign home).

## CSS

Point d'entrée `assets/scss/main.scss`. Les paramètres de design exposés à Hugo (taille H1 hero, gabarit emblème livre) vivent sous `[params.design]` dans `hugo.toml` — modifier là plutôt qu'en dur dans le SCSS quand la valeur est référencée par un template.

## Ajout d'un nouvel AWP

Procédure compacte documentée dans [`docs/CHECKLIST_AJOUT_AWP.md`](docs/CHECKLIST_AJOUT_AWP.md). Points sensibles à retenir :

1. **Convention multilingue par suffixe** : créer `content/awp/awp-NN.md` (FR) + `content/awp/awp-NN.en.md` (EN). Pas de bundle `content/awp/awp-NN/index.md`.
2. **Hero index à mettre à jour manuellement** : `layouts/index.html` lignes 18-22 contient le compteur AWP écrit en lettres (FR et EN). À incrémenter à chaque ajout.
3. **Linter de cohérence** : `python scripts/check-corpus-counters.py` doit sortir 0 avant commit. Détecte les chiffres durs obsolètes (`cinq Anthropie Working Papers` quand on passe à 6, etc.).
3 ter. **Doctrine du dépôt échelonné** (décision auteur, 2026-08-02) — vaut pour SSRN, MPRA, SocArXiv et toute plateforme à modération : **jamais plus de 1 à 2 dépôts à la fois**. On dépose, on surveille avec `python scripts/check_deposits_status.py`, et **on ne pose le suivant qu'une fois le précédent ACCEPTÉ**. Preuve : 5 dépôts MPRA en 18 minutes le 07/04/2026 sont restés bloqués 118 jours, alors qu'un dépôt isolé le 08/05 a été accepté en 7 jours. Ne jamais rattraper un retard en déposant en lot — c'est ce qui crée le blocage qu'on cherche à résorber.
3 bis. **Audit Zenodo** : `python scripts/zenodo_audit_complet.py` doit sortir **0 bloquant** (ajouter la nouvelle paire dans `PAIRS` d'abord). Vérifie verbatim canonique, ORCID, licence, langue, mots-clés, communauté, `isDescribedBy` https et liaison de traduction réciproque. Motif : AWP-08 était sorti sans ORCID ni communauté (détecté et corrigé le 2026-08-02) — les dépôts manuels sont l'endroit où se creusent les trous.
4. **Maillage publications** : si l'AWP prolonge une fiche `content/publications/*.md`, ajouter `awp-NN` au champ `related:` du frontmatter, ordre chronologique croissant.
5. **Pas de traduction `.en.md` pour `content/publications/`** : choix éditorial, fallback multilingue Hugo.

## Méthodologie de patch

Ce dépôt suit la doctrine cross-projets définie dans
`~/.claude/CLAUDE.md` (lue par Claude Code à chaque session).

Avant tout patch substantiel, lecture obligatoire dans cet ordre :

1. `PROJECT_STATUS.md`
2. ce fichier (`CLAUDE.md`) pour les conventions locales

Contextualisations propres à ce repo :

- **Un seul geste avant commit : `python scripts/check-all.py --reseau`** (runner des contrôles
  ci-dessous ; `--ci` = les trois hors réseau, exécutés en porte bloquante par `hugo.yml` avant
  déploiement depuis le 2026-09-02).
- Linter cohérence corpus : `scripts/check-corpus-counters.py`
- Linter couverture GEO (FR + miroir EN) : `scripts/check-geo-coverage.py`
- Parité registre ↔ fiches (livres, AWP) : `scripts/check-fiches-registre.py` ;
  parité Wikidata ↔ registre (deux sens) : `scripts/check-wikidata-registre.py` ;
  sondage inverse des autres nœuds (Crossref, OpenLibrary, site, listes manuelles) :
  `scripts/sondage-noeuds-externes.py`, condition de mort en tête du fichier.
- Linter encodage console : `scripts/check-console-encoding.py` — un `print()`
  contenant « ✓ », « → » ou un emoji fait sortir **1** un script sain sous
  console Windows cp1252, ce qui est indiscernable d'un vrai échec. Le cookie
  `# -*- coding: utf-8 -*-` ne protège pas : il déclare l'encodage de la source,
  pas celui de `stdout`.
- Checklist d'ajout d'AWP : `docs/CHECKLIST_AJOUT_AWP.md`
- Convention multilingue Hugo : suffixe `.en.md` (pas sous-dossier
  `content/en/`)
- Source unique d'identité auteur : `data/author.toml`
- **Navette Wikidata : `Wikidata/`** — versionnée depuis le 2026-08-16 (elle a
  vécu quatre mois en un seul exemplaire sur un seul disque). **Lire son
  `README.md` avant tout geste Wikidata** : les dossiers `Import_..._<date>_<sujet>/`
  sont le **registre primaire** (historique, non régénérable) ; les fichiers
  `00_`…`16_` ne sont qu'un inventaire régénérable ; `CHANGELOG.md` est un récit
  et ne fait pas foi. Règle : **tout geste laisse un dossier daté, même en une
  commande**, et se clôt par un readback API. Chaîne à boucler jusqu'au bout —
  item → `data/works.yaml` → `wikidata_qid` de la fiche → `sameAs` du JSON-LD ;
  le dernier maillon est couvert par `check-fiches-registre.py` (livres **et AWP**),
  le premier par `check-wikidata-registre.py` depuis le 2026-09-02 — requête inverse
  depuis le nœud auteur, deux sens ; 10 écarts trouvés le jour même, 0 faux positif
  (un diff des QID cités dans le dossier avait été mesuré puis écarté : 61 faux
  positifs sur 70). Le bloc ✅ d'un dossier daté cite le QID, le commit d'écriture
  en retour et la sortie du script.
- Instruments Zenodo : `scripts/zenodo_inventory.py` (recherche du corpus),
  `scripts/zenodo_stats.py` et `zenodo_stats_full.py` (vues et téléchargements).
  Audit des balises Google Scholar sur le site en ligne : `audit_scholar.sh`.
  Tous versionnés le 2026-08-16, même motif que `Wikidata/`.

**Règle de fraîcheur d'état (« l'état écrit suit l'acte »)** : toute session
qui exécute un travail met à jour, dans la même session, (1) le log § 0 de
`PROJECT_STATUS.md`, (2) le statut des backlogs et registres touchés
(`data/works.yaml`, `reports/**/12_IMPLEMENTATION_BACKLOG.md`, fiches de
mission), (3) `static/llms.txt` si un fait qu'il énonce a changé. Symétrique :
avant de reprendre un backlog ou une consigne, vérifier ses statuts contre le
git log — un statut périmé provoque soit la re-exécution d'un acquis, soit
l'abandon d'un travail cru fait. Constat fondateur (arbitrages GEO-01→03,
2026-08-02) : la péremption d'état était l'unique défaut récurrent du
système, retrouvé dans le backlog, works.yaml, llms.txt et la mémoire.
Complément (contre-expertise 02/08) : **l'état interne suit l'acte ;
l'état externe expire** — tout relevé d'observation externe (SERP, mode IA,
concurrent, plateforme) porte sa date, son contexte (pays/langue/connexion/
moteur/requête exacte) et une durée de validité ; passé ce délai, il
redevient une hypothèse à re-vérifier, pas un fait. Registre des collisions
de nom/concept : `reports/geo_audit/REGISTRE_COLLISIONS.md` (hors dépôt) —
input obligatoire de toute nouvelle langue ou surface.

## Architecture des ressources — une question, une section (actée 2026-09-30)

Décisions complètes et motifs : registre en fin de
`D:\PRO\06_PROMOTION\ARBITRAGE_CONTRE_EXPERTISE_GEO-PLUS_2026-09-29.md` ; exécution et étapes :
`D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`. **Lire les deux avant de créer une page ou
une section de ressource.** Trois règles en tiennent lieu de rappel :

1. **Une question se traite en section d'une page mère**, jamais par une URL par formulation. Une
   page propre ne naît que si deux déclencheurs sont réunis, dont un observable (demande mesurée,
   matière documentaire propre, cycle de mise à jour distinct).
2. **Tout titre-question porte une ancre figée** : `## La question ? {#identifiant}`. Contrôle
   **bloquant** : `scripts/check-ancres-questions.py` (dans `check-all --ci`). Un titre déjà publié
   garde l'identifiant qu'il a aujourd'hui.
3. **Avant publication, la fiche de mesure D0** est écrite dans la feuille de route : résultat au plus
   près de la finalité, diagnostics, état initial, dates. ⚠ **Aucun contrôle ne la vérifie** : c'est
   une discipline de session, pas un verrou.

## Règle de surface — « la présence vient du dépôt » (actée 2026-08-11)

Défaut récurrent, six occurrences en deux jours, toujours la même forme : **une donnée
existe quelque part et la surface qui la consomme ne la reçoit pas — sans erreur, sans
warning, sans trace.** Un livre publié absent du mur `/a-propos/` ; `pages` manquant sur
une fiche, donc pas de pagination sur deux pages ; `subtitle` manquant, donc pas de hook ;
deux QID Wikidata connus de `works.yaml` mais jamais déclarés en fiche, donc pas de
`sameAs` ; un compteur de corpus périmé ; une page traduite qui ne le disait pas. Aucune
n'a été trouvée par l'appareil : toutes par l'auteur, en regardant le site.

Trois règles en découlent, à appliquer à **toute** surface qui agrège ou reflète du contenu :

1. **La présence vient du dépôt, l'éditorial du front matter.** Un gabarit n'énumère
   jamais à la main ce que `content/` sait déjà. Le front matter ne porte que ce qui ne
   se déduit pas (une ligne éditoriale, une étiquette), en **table de surcharges indexée
   par slug**, avec repli. Toute valeur dérivable (pagination, titre, URL, couverture,
   traduction) se **dérive** — la recopier, c'est programmer sa dérive.
2. **Une exclusion peut être légitime ; le silence, jamais.** Quand une liste manuelle se
   justifie (ex. `$order` de `/ressources-offertes/`, où l'on retire un livre sans stock),
   elle porte un `warnf` sur ce qu'elle omet. Idem pour un champ éditorial absent : la
   tuile s'affiche **et** le build avertit — ne jamais faire disparaître l'objet.
3. **Le registre est la source, la fiche doit le refléter.** `scripts/check-fiches-registre.py`
   compare fiches et `data/works.yaml` (QID, pagination, ISBN) et signale « le registre le
   sait, la fiche ne le dit pas ». À lancer avant commit, comme les autres linters.
   Symétrique depuis le 2026-09-02 : `scripts/check-wikidata-registre.py` signale « Wikidata le
   sait, le registre ne le dit pas » — la classe qui a laissé 8 AWP quatre mois sur Wikidata
   sans `sameAs`. Un contrôle qui part du registre ne peut pas la voir ; il faut partir du nœud.

⚠ Un `warnf` **ne survit pas à `hugo --quiet`** (faux négatif observé le 11/08 en testant
la première garde). La CI utilise `hugo --minify` sans `--quiet` : ne pas changer cela.
Et un garde-fou se **teste par mutation réelle puis restauration**, jamais par relecture
du code.

## Figures de données — constantes, et une règle de méthode

La charte graphique complète (couleurs sémantiques, grille, étiquetage, jalons, bandes, cartouche,
contrôles) est une **constante de l'auteur** arrêtée le 2026-09-28 : mémoire
`feedback_langage_graphique_figures`. Elle s'applique aux deux générateurs de ce dépôt
(`update_dette_insee.py`, `generer_figures_qui_paie.py`) sans être rediscutée figure par figure.
Trois points en tiennent lieu de rappel : **deux couleurs de données au maximum** et la même
grandeur toujours de la même couleur ; **toute étiquette centrée sur le point qu'elle désigne** ;
**le libellé d'une bande d'événement se pose sous elle, en deux lignes** — période, puis intitulé.

⚠ **Une teinte nouvelle passe `validate_palette.js` avant d'être appliquée.** Le bleu marine du site
(`#1B2A4E`) y échoue comme couleur de données : chroma trop faible, il lit gris. C'est ainsi que le
bleu profond `#184f95` a été retenu — sur mesure, non par goût.

### Avant de corriger une mise en page, MESURER

Le 2026-09-28, trois correctifs CSS successifs ont été livrés et déployés contre un défaut supposé
— un retour à la ligne de la barre du dossier — qui **n'existait pas** : trente secondes dans le
navigateur (`window.innerWidth`, `getComputedStyle(...).gridTemplateAreas`) ont montré une grille à
une seule rangée et un simple désalignement optique. **Une propriété calculée vaut mieux que trois
hypothèses.** Quand un symptôme visuel résiste à une correction, la suivante ne s'écrit pas : on
relève d'abord la valeur calculée, ou l'on demande la capture d'inspecteur.

## Conventions de contenu

### Typographie française — règle de site (auteur, 2026-09-20)

**La ponctuation haute et les unités ne se séparent jamais de ce qui précède.** Espace
insécable (`&nbsp;` dans les `.md`) devant `;` `:` `!` `?` `»`, après `«`, et entre un
nombre et son unité (`19&nbsp;€`, `117,5&nbsp;%`). Sans elle, le navigateur rejette le
signe seul en début de ligne : le « € » passe à la ligne suivante sans son montant, sur
le chiffre même que la page met en avant.

**Portée étendue par l'auteur le 2026-09-28 : « les symboles, les chiffres, la ponctuation
doivent être insécables QUEL QUE SOIT LE SUPPORT ».** La règle ne s'arrête donc pas au HTML
produit au build : elle vaut aussi pour ce qu'un script écrit dans la page après coup.

**TROIS** organes, un seul énoncé — et c'est le troisième qui manquait :

- **Le corps des pages** est écrit avec des `&nbsp;` dans la source, et contrôlé par
  `scripts/check-typo-fr.py` — **bloquant** dans `check-all.py --ci`, donc au déploiement.
  `--corriger` applique ; un chemin en argument ne traite que ce fichier.
- **Les gabarits** passent leurs libellés par `partials/fr-typo.html`, qui pose les fines
  insécables, traite les guillemets et les unités, et termine par `safeHTML`.
- **Le texte injecté par un script**, que les deux premiers ne voient pas : `static/js/french-typography.js`
  porte depuis le 28/09 la règle **nombre ↔ unité** et **nombre ↔ milliers**, qui n'existait que
  dans les deux autres. ⚠ Ce script ne passe qu'**une fois, au chargement** : un contenu réécrit
  ensuite (compteur, valeur rafraîchie) doit poser ses insécables **lui-même, à la source**.

**Incident fondateur (auteur, 28/09, sur Android)** : le compteur de dette écrivait
`fmt.format(x) + " €"` — une espace **ordinaire**. Le « € » partait seul à la ligne, sans son
montant, sur le chiffre le plus visible du site. Deux organes portaient la règle, le troisième
l'ignorait, et aucun contrôle ne regardait de ce côté. Le séparateur de milliers rendu par
`Intl.NumberFormat` varie en outre selon la plateforme : il est désormais normalisé en ` `.

⚠ **Rendre un champ de front matter avec `{{ . }}` échappe ses `&nbsp;` en `&amp;nbsp;`** —
l'entité s'affiche alors en toutes lettres au lecteur. Tout sous-titre ou description venant
du front matter passe par `fr-typo.html`. Défaut mesuré le 2026-09-20 sur dix pages, dont
l'accueil ; il restait encore `layouts/livres/single.html` (bloc « autres livres ») au moment
de l'écriture.

La règle précédente tenait en une ligne et n'était outillée nulle part : **426 fautes**
s'étaient accumulées dans 23 fichiers sans que rien ne le signale. Une règle de forme non
contrôlée dérive, parce que la faute est invisible à la relecture et ne se voit qu'à la
coupure de ligne, chez le lecteur.
- `unsafe = true` dans le renderer Goldmark : HTML inline autorisé dans le markdown.
- Tout nouveau working paper doit fournir `doi_zenodo` + `url_zenodo` + `pdf_url` (Zenodo community `anthropie-working-papers`) et un pendant `.en.md` avec `translation` croisé.
