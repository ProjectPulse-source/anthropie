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

## Modèle d'une ressource de données — le dossier dette (acté par l'auteur, 2026-09-30)

**Le dossier dette publique est le modèle de structure et de méthode de toute ressource de données du site**
(décision de l'auteur, 30/09). Pages de référence : `/pourquoi-la-dette-publique-augmente/`,
`/cout-de-la-dette-publique/`, `/qui-paie-la-dette-publique/`, `/dette-publique-comparaison-internationale/` ; leurs
générateurs `scripts/update_dette_{dynamique,insee,monde}.py` et `generer_figures_qui_paie.py`. Arbitrages sources :
`D:\PRO\.claude\external-audits\ARBITRATIONS\` (PRO-20260930-061613, -092814, -103341 et les avis entrants du 30/09).
**Avant de créer ou de refondre une ressource, relire une page de référence et son générateur.**

**Vérifié par machine — bloquant** (`scripts/check-ressource-modele.py`, dans `check-all --ci`, donc avant tout
déploiement ; toute page dont le front matter déclare `donnees:`) : carte de partage propre (`og_image`) ; bloc
« Le résultat en une phrase » (`div.resultat-phrase`) ; bloc commun « Réutiliser cette page » ; balisage `Dataset`
(bloc `dataset:` du front matter, gabarit `schema-dataset-page.html`) ; JSON **et** CSV du jeu dans `static/` ;
appel au livre sans note Amazon (`avis="non"`) ; **vignette d'index** `static/images/vig-X.jpg` pour `og_image: images/og-X.jpg`.

**Présentation dans l'index `/ressources/`** (auteur, 01/10/2026 ; vaut pour toutes les ressources, y compris celles à
créer) : dans un bloc, les pages qui déclarent `donnees:` forment « le dossier » — grande grille, vignette sur fond
blanc, partie texte teintée (`--color-dossier-tint`) ; les autres pages du bloc suivent en cartes crème ; une page qui
déclare `ressource.encart: true` s'affiche en encart avec bouton (`ressource.bouton`) ; une page de données qui traite un
cas particulier du dossier déclare `ressource.prolongement: true` et s'affiche sous la grille, dans « Prolongements du
dossier » (option B, 01/10/2026 : elle garde `donnees:`, donc les critères bloquants). **Barre du dossier A+ v2
(auteur, 03/10/2026)** : cinq questions en onglets, puis « Prolongements » qui déplie toute page déclarant
`dossier_dette: prolongement` (libellé `dossier_dette_titre`, sous-titre `dossier_dette_role`) ; une telle page appelle
`{{< dossier-dette volet="prolongement" >}}`. Source de la page en gris dans l'en-tête ; tout changement de libellé se
remesure (bascule vers les libellés courts sous 968 px de barre). **Toutes les barres de dossier passent par un seul
organe** (auteur, 03/10/2026 : « pour chaque dossier, le même type d'architecture que pour Dette ») :
`partials/dossier-barre.html` dessine, les shortcodes préparent (`dossier-dette`, `enseignants-themes`, et `dossier`
pour tout autre bloc — onglets = pages du même `ressource.bloc`, libellés `onglet.long`/`court`/`long_en`, aucune barre
sous deux entrées). Une page neuve d'un bloc entre dans sa barre sans rien toucher d'autre que son front matter. Rien à déclarer dans l'index : le
tri se déduit des pages (`layouts/ressources/list.html`, partials `ressource-entree.html` et `ressource-encart.html`).
**Une nouvelle ressource de données fait produire sa vignette par le générateur de sa carte de partage**, dans le même
passage et avec le même dessin sur fond blanc (modèle : `carte()` de `scripts/og_dossier_dette.py`) ; sa sortie entre
dans le `git add` du workflow qui la régénère. ⚠ Les deux sous-titres d'un bloc mixte (« Le dossier, en N pages » /
« N questions du débat public », `i18n/*.toml`) sont rédigés pour le bloc Dette : un autre bloc mixte appellera des
sous-titres propres, à déclarer alors par bloc dans `content/ressources/_index*.md`.

**Discipline — écrite, non vérifiée par machine** (la session la tient, la contre-expertise la contrôle) :

1. **Architecture.** Une page = une découverte principale. Un dossier = des questions fondamentales en onglets
   (clés stables, numéro par l'ordre, libellés courts sur téléphone, sans défilement à 390 px) ; les cas
   particuliers en « Prolongements », jamais en onglet. Pas de page d'accueil de pure navigation.
2. **Hiérarchie de lecture : surprendre → montrer → expliquer → documenter.** Chapô (`chapo:`) qui donne la réponse ;
   figure signature en premier ; « le résultat en une phrase » dit ce que montre la figure juste au-dessus ; la
   preuve longue en `<details class="repli">` sur la même URL ; rien supprimé, aucune ancre publiée changée.
3. **Aucun chiffre saisi à la main.** Un générateur par jeu, un bloc `affichage`, des jetons (`{jeu.*}`, shortcode
   `*-val`). **Chaque qualificatif de la prose est une garde** dans le générateur (« a doublé », « près du double »,
   « comme l'Allemagne »…) : si la donnée le dément, arrêt. Au moins une garde **vue mordre** (mutation) à la
   création. **Jamais de commentaire figé autour d'un chiffre qui se met à jour** (erreur du 30/09 : « T2 2026, au
   cœur de la crise sanitaire »).
4. **Un contrôle indépendant de la méthode** quand une décomposition ou une identité est publiée (ex. : résidu
   flux-stock = témoin comptable) ; test décisif **avant** d'écrire la page — sans lui, pas de page.
   ⚠ **Un témoin se vérifie par l'algèbre puis par mutation** : celui du volet 1 ((ΔDette + B9) / PIB) était identique
   au résidu qu'il devait contrôler, donc incapable de rien rejeter, et a laissé passer un PIB en écus avant 1999
   (dette de 1995 à 57,5 % au lieu de 57,8 %) du 30/09 au 03/10/2026. Témoin retenu depuis : les ratios qu'Eurostat
   **publie** en % du PIB (`gov_10dd_edpt1`, PC_GDP), que le calcul n'utilise pas. Tout ratio se calcule sur le PIB
   de la notification (`gov_10dd_edpt1`, B1GQ, MIO_NAC), jamais sur `nama_10_gdp` en `CP_MEUR`.
5. **Figures** : SVG et PNG produits **ensemble ou pas du tout** ; titre, source et précaution imprimés dans l'image,
   fiches « Réutiliser » **lues dans le SVG** ; langage graphique du site (bleu = stock, orange = coût, gris = ce
   qui fait baisser).
6. **Données réutilisables** : JSON + CSV (UTF-8 avec BOM, format long si les tableaux diffèrent), `releve_le` à la
   racine, rien réécrit à données identiques ; licence CC BY 4.0 ; bouton CSV automatique dans « Réutiliser ».
7. **Dates** : le millésime des données (« Eurostat 2025 ») n'est jamais présenté comme une date de mise à jour.
8. **Écriture** : associations et non causes ; conditions explicites ; limites visibles (« Ce que ces données ne
   disent pas ») ; **vocabulaire unique d'une page à l'autre** (ex. : « taux implicite ») ; posture de chercheur
   (qui parle et d'où, noyau d'arbitrage de `D:\PRO`) ; le chiffre officiel prime visuellement sur toute simulation.
9. **Fin de page** : conclusion → livre (`appel-livre`, surtitre vrai via `sur=`, `avis="non"`) → sources →
   « Réutiliser » ; une carte de partage tirée des données et contrôlée (`og_dossier_dette.py`).
10. **Mise à jour** : workflow au calendrier de la source, sorties énumérées dans son `git add` ; tant que le module de
    mise à jour n'existe pas, un rendez-vous de rattrapage daté.
11. **Vérification avant commit** : build avec **lecture de `$?`** (jamais `--quiet | tail` seul) ; HTML construit relu
    (jetons résolus, JSON-LD valide) ; rendu 390 px sans débordement ; `check-all --ci` à 0 ; fiche D0 écrite.
12. **Contre-expertise** de la page construite avant ou juste après publication ; arbitrage écrit ; la
    littérature, si elle est citée, **teste** l'interprétation dans un bloc « Confrontation à la recherche » par
    page, jamais ne cautionne une mesure (arbitrage PRO-20260930-103341).
13. **Comparaison par sous-secteur public** (S1311 à S1314, entre pays ou dans le temps) : avant toute phrase,
    vérifier l'équivalence du **périmètre institutionnel** (un S1313 n'est pas le même objet selon qu'il existe ou
    non un S1312) et les **relations financières entre sous-secteurs** (dette détenue par un autre échelon :
    `gov_10dd_ggd`, dimension `sector2`) ; une série de transferts se coupe à chaque reclassement en impôt
    (ex. DGF → fraction de TVA). Plusieurs indicateurs qui ordonnent les pays différemment n'autorisent **aucun
    classement synthétique**. Même famille, entre **sources** : avant de rapprocher deux chiffres de sources
    différentes (Eurostat, Insee, OFGL, loi de finances), établir périmètre institutionnel, opération comptable,
    consolidation, date et dénominateur ; à défaut, **l'écart se documente, il ne se corrige jamais** (ex. : DGF
    votée ≠ contribution demandée ≠ DGF comptabilisée ; encours OFGL ≠ dette Maastricht). Cas fondateur : `/dette-publique-collectivites-locales/`, 01/10/2026 — la v1 comparait
    S1313 seul et concluait à tort que la France était le seul pays où la dette locale avait augmenté (arbitrage
    `D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261001-145721_arbitrage.md`).

## Couche pédagogique — `/enseignants/` (actée par l'auteur, 2026-09-30)

Une page d'**usage** pour les enseignants, qui transforme les ressources en activités sans les recopier ; les pages de
recherche ne portent **aucune** activité, seulement un lien discret (bloc « Réutiliser », FR, quatre volets dette).
Arbitrage : `D:\PRO\.claude\external-audits\ARBITRATIONS\ENTRANTE_2026-09-30_Dette_Pedagogie_arbitrage.md` ; fiche D0
dans la feuille de route GEO. **Le STOP des nouveaux ensembles est levé (auteur, 02/10/2026) : aucune exception à
demander, aucune fenêtre d'attente ; une page se met en ligne dès qu'elle est prête et contrôlée.**

1. **Fiches dynamiques.** Fiche élève et corrigé sont des sections imprimables de la page (`section.fiche`, bouton
   « Imprimer la fiche élève », `static/js/fiche-imprimer.js`, `assets/scss/_enseignants.scss`), nourries par les jetons
   des jeux (`dyn-val`, `monde-val`, `qp-val`, `dette-val`) : **aucun chiffre saisi**, aucun PDF figé ; un PDF, s'il
   existe un jour, est produit au build depuis ces sections.
2. **Neutralité.** Chaque question fait constater, calculer, comparer ou expliquer un mécanisme ; **aucune ne demande
   de trancher une politique**. C'est la condition d'une reprise par un site académique.
3. **Fidélité au programme.** Citer l'objectif officiel tel qu'il est écrit (Éduscol) ; ce qui le dépasse (r − g,
   solde primaire en Terminale) s'annonce comme approfondissement, jamais comme « le programme ».
4. **Chaque section contient une activité prête à l'emploi**, jamais une liste de liens. Français seulement : le
   programme de SES est français (exclusion déclarée).
5. **Exemplaire de consultation** : un bloc en **fin** de section, après les activités (le livre n'est jamais la
   contrepartie d'une activité), vers une page « un seul livre » de `/ressources-offertes/` — un fichier de contenu, même
   gabarit, même guichet, **stock commun**, aucune donnée collectée. **Aucun contrôle d'éligibilité** : il ne se construit
   que si une exigence externe ou un abus durable l'impose ; en cas d'abus, la marche suivante est le lien sur invitation
   (arbitrage `PRO-20260930-210901`).

6. **Exception — une activité peut porter sa propre figure** (auteur, 02/10/2026) quand aucune page de recherche n'a de
   figure sur le sujet : activité « Après une première année de licence », page `/enseignants/ecole-et-parcours/`. La page ne
   déclare pas `donnees:` pour autant ; la discipline du modèle de ressource vaut entière pour le jeu (générateur
   `scripts/generer_parcours_licence.py`, jetons `licence-val`, tableau `licence-tableau`, gardes de prose, témoins, JSON et CSV, SVG et PNG
   ensemble). Source sans API : tableurs du SIES archivés dans `scripts/sources_enseignants/` avec `SHA256SUMS`, que le
   générateur vérifie ; mise à jour annuelle à la main, en novembre (geste décrit en tête du générateur). La question de
   l'auteur titre le thème ; la fiche élève, qui s'imprime, garde un titre descriptif.
7. **Une page par thème, reliées par la barre `enseignants-themes`** (auteur, 02/10/2026 ; arbitrage
   `ENTRANTE_2026-10-02_Enseignants_Structure`). `/enseignants/` reste la page du thème dette : c'est l'adresse des
   courriels et des quatre pages du dossier. Un thème nouveau reçoit sa page fille (`content/enseignants/<theme>/_index.md`,
   une ligne dans le shortcode) si les deux déclencheurs de la règle « page propre » sont réunis ; une seule activité
   complète suffit, aucune page ni catégorie vide — sauf Littérature et Philosophie, annoncées grisées et sans lien dans le
   panneau « Autres disciplines » (auteur, 03/10/2026 ; pastille « Pour enseigner · SES ») ; chaque entrée grisée meurt avec
   la première page de sa discipline. **Dans `/ressources/`, un dossier par discipline** (auteur, 03/10/2026) : le bloc
   `enseigner` déclare `disciplines` ; les pages déclarent `ressource.discipline` et `ressource.theme` ; la carte SES ouvre
   `/enseignants/` (adresse des courriels ; `/enseignants/ses/` y renvoie), une discipline sans page s'affiche grisée
   (`layouts/partials/ressource-discipline.html`). Navigation nommée par ce que cherche l'enseignant (« École et
   parcours »), jamais par la formule de l'auteur, qui reste le titre. La barre réemploie les classes `dossier-dette*` ;
   elle ne porte aucune date. **Une ancre publiée ne se retire pas** : `#droit-a-l-erreur` reste portée par la barre de
   `/enseignants/` et renvoie à la page fille. Chaque thème a sa méthode et son encart d'exemplaire ; les façades
   enseignants du guichet déclarent `facade: "enseignants"` (pas de bloc « Faire circuler »). L'encart d'un livre à
   thèse dit que l'activité ne met pas cette thèse à l'épreuve. Avant publication : quatre impressions de fiche,
   arrivée par chaque ancre (titre visible sous les éléments collants), 390 px.
8. **Trois thèmes au 02/10/2026** : Dette publique (`/enseignants/`), École et parcours, Environnement
   (`/enseignants/environnement/`, `scripts/generer_empreinte_carbone.py`, Insee Première annuelle de mi-octobre).
   **Une série révisée ne se cite que depuis le fichier de sa dernière édition**, jamais depuis un résumé ni depuis
   deux éditions mêlées (l'empreinte 2023 valait 644 Mt dans l'édition 2024, 583 Mt dans celle de 2025). Deux
   conventions de comptabilité ne démontrent ni un déplacement ni l'effet d'une politique : la page l'écrit.

## Exemplaire de consultation sur les ressources (auteur, 2026-10-02)

Décision de l'auteur : toute ressource propose l'exemplaire de consultation du livre qu'elle concerne. Finalités :
volume sur la librairie en ligne par le guichet `/ressources-offertes/`, et crédibilité auprès des publics visés
(presse, enseignement, recherche, responsables publics, associations). **Deux organes, un seul texte de publics**
(`partials/consultation-publics.html`) :

- page qui porte un bloc d'achat : un bandeau avec bouton, en pied du bloc, **dans `appel-livre`**, automatique dès que le livre a une page au
  guichet (`consultation="non"` la retire) ;
- page sans bloc d'achat (notions, guides, corpus) : `{{< consultation slug="…" >}}` en fin de page ;
- pages des enseignants : `exemplaire`, avec leur façade (couche pédagogique, points 5 et 7).

Français seulement (exemplaires Amazon.fr). Le lien porte `?src=consultation-<page>` : l'origine des demandes se lit
dans la mesure d'audience. Aucun contrôle d'éligibilité, aucune donnée collectée ; un exemplaire attribué est un coût
du canal, jamais un résultat. Une page de ressource neuve reçoit l'un des deux organes ; `chercheur-independant` n'a
pas de livre lié (exclusion déclarée).

## Module de mise à jour des données (auteur, 2026-10-02)

« À chaque mise à jour d'une donnée que nous utilisons, la mise à jour et la réécriture des pages se déclenchent. »
**Un registre, un script, un workflow** :

- **`data/sources_maj.json`** : une ligne par source (producteur, pages, générateurs, jeu, sorties, fenêtre de parution,
  édition lue). Les générateurs des enseignants y lisent leur édition : **plus aucune année, aucun nom de fichier,
  aucune date de téléchargement en dur** dans un générateur ou une page.
- **`scripts/maj_sources.py`** : `etat` · `detecter` · `integrer` · `essai` · `sorties` · `controle`.
  `integrer` archive la pièce (empreinte dans `SHA256SUMS`), l'inscrit au registre, lance tous les générateurs
  concernés en `--check` puis en écriture ; un seul refus remet registre, empreintes et pièces dans leur état d'avant.
  `essai` est le témoin positif : chaque détecteur doit retrouver à la source l'édition déjà archivée.
- **`.github/workflows/maj-sources.yml`** : chaque jour, `integrer` ; chaque lundi, `essai` ; portes bloquantes
  (`check-all --ci`, build), commit des sorties **listées par le registre**, déploiement, un seul ticket ouvert en cas
  d'échec.

**Pour qu'une page se réécrive seule, sa prose ne contient que des jetons** : nombres, années, libellés d'édition,
dates, et jusqu'au nombre de cohortes en toutes lettres. Une phrase qui porte un chiffre saisi bloque la mise à jour,
ou pire, ment après elle. Quand une garde refuse une édition, c'est une phrase à réécrire, pas une garde à desserrer.

Ajouter une source en fichier : une ligne au registre, un détecteur dans `maj_sources.py`, son cas dans `essai`.
Une donnée citée ne vient jamais d'un résumé : le détecteur valide le **contenu** de la pièce (titre du tableau,
feuille attendue), jamais un code HTTP — la page d'une édition absente peut répondre 200.

Hors du module à ce jour, déclaré : les sources à API du dossier dette gardent leurs workflows `dette-*.yml` (elles
figurent au registre pour le tableau d'état) ; `generer_figures_qui_paie.py` se met à jour à la main.

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
