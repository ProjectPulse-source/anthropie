# Reprise — architecture espagnole du site, puis page conceptuelle

Document de passation, arrêté le 2026-08-03, **révisé le jour même après
décision de l'auteur (SCIELO-04)**. Écrit pour être lu par une session
neuve : état, décision d'architecture, arbitrages qui s'imposent, pièges,
commande de reprise, et **règle d'arbitrage des consignes futures**.

---

## 1. Objet du prochain fil

**Deux temps, dans cet ordre :**

1. **Ouvrir une architecture espagnole propre et extensible** — troisième
   langue Hugo complète, décision de l'auteur (§3). La première tâche est un
   **audit + plan de modification arbitré**, sans toucher à la production.
2. Puis créer **« ¿Qué es la antropía? »**, la page conceptuelle.

C'est le **point 2 sur 4** du Pareto arrêté le 03/08 (voir §4). Le point 1
(vague chercheurs, 24/08) ne dépend pas de ce fil et reste prioritaire.

---

## 2. État acquis — à ne pas refaire

**Le concept existe en trois langues, citable, avec DOI et licence :**

| Langue | AWP-01 | Page site |
|---|---|---|
| Français | `10.5281/zenodo.19266862` | `/quest-ce-que-lanthropie/` |
| Anglais | `10.5281/zenodo.19431208` | `/en/quest-ce-que-lanthropie/` |
| **Espagnol** | **`10.5281/zenodo.21766184`** (publié le 03/08) | **aucune — c'est l'objet du fil** |

- **Zenodo** : 17 records, **0 bloquant** (`scripts/zenodo_audit_complet.py`).
- **Wikidata** : batch espagnol prêt pour Laura —
  `Downloads\QS_WIKIDATA_AWP01_ES_2026-08-03.txt` + sa note. Convention :
  **un seul item par AWP**, versions en `P953` qualifié `P407` (es = Q1321).
- **Dépôts** : SocArXiv AWP-01 EN en modération ; MPRA lot d'avril bloqué,
  relance envoyée ; SSRN 6 papiers / 105 téléchargements — **on s'arrête là**.
- **Site** : au plateau en FR/EN. On n'ajoute plus de pages *sauf* celle-ci.

---

## 3. Le verrou technique — TRANCHÉ PAR L'AUTEUR LE 03/08

**Décision : option A — troisième langue Hugo complète.** La page isolée est
écartée.

> *Motif de l'auteur : « Je compte publier plusieurs traductions espagnoles —
> working papers, puis livres. Une page isolée pourrait convenir à un contenu
> exceptionnel sans suite prévue ; ici, elle créerait une dette technique dès
> la deuxième publication. »*

**Mais une architecture complète ≠ un site traduit.** Le modèle retenu est un
**corpus espagnol sélectif** :

- une racine `/es/` **minimale** ;
- la page conceptuelle « ¿Qué es la antropía? » ;
- les pages des **AWP effectivement traduits** (aujourd'hui : AWP-01) ;
- ultérieurement, les livres disponibles en espagnol ;
- **aucun miroir automatique** des articles, recensions, actualités ou pages
  institutionnelles françaises.

**Exigence explicite sur le multilingue** : le sélecteur de langue et les
`hreflang` doivent refléter **uniquement les traductions réellement
disponibles, page par page**. Ni triplette FR-EN-ES affichée artificiellement
partout, ni retour silencieux vers le français. C'est le point le plus
délicat de l'implémentation : le bandeau `cross-language-banner.html` est
aujourd'hui conçu **pour une paire**, et `head.html` (l. 13-25) émet les
alternates de façon systématique.

Interdit hérité, toujours valable (`08_ENGLISH_STRATEGY.md` §7.7) :
**ne pas renommer les URL EN existantes ni casser leur câblage hreflang** —
positions acquises et mesurées.

**Ordre de travail imposé par l'auteur** : auditer l'architecture Hugo
existante et **proposer un plan de modification arbitré AVANT tout
changement** — configuration des langues, structure des contenus, menus,
sélecteur, `hreflang`, canonical, sitemap, traductions d'interface (i18n),
contrôles de sortie. **Ne toucher ni aux contenus ni à la production tant que
ce plan n'est pas validé.**

---

## 4. Arbitrages déjà rendus — ils s'imposent au prochain fil

Issus de deux contre-expertises externes (`SCIELO-01.txt`, `SCIELO-02.txt`),
vérifiées à la source et acceptées :

1. **Internationalisation asymétrique** *(version arrêtée par l'auteur le
   03/08)* : FR = langue de production et de légitimation principale ·
   EN = langue-pont internationale · **ES = langue d'implantation et de
   publication sélective** · autres langues = principalement diffusion des
   *livres*, **avec exceptions ponctuelles** si un texte structurant le
   justifie.
2. **Ne pas traduire ses institutions**, seulement son contenu et ses points
   d'accès. Pas d'article espagnol réécrit, pas de soumission à des revues
   hispanophones, pas de comité éditorial, pas de campagne académique.
3. **Présence minimale viable par langue** : texte canonique + page
   conceptuelle + métadonnées/citation + quelques relais ciblés. La couche
   suivante ne s'ouvre que **sur signal** (citations, demandes, invitations,
   ventes) — *on ne construit pas l'écosystème en espérant un public.*
4. **Deux gates avant tout dépôt** : conformité ET valeur marginale.
   *Éligible mais sans valeur marginale = NO-GO.* SciELO Preprints = NO-GO
   définitif (refuse tout texte déjà public ailleurs) ; revues hispanophones
   = NO-GO stratégique ; SSRN = fit incertain, dépôt AWP-07 annulé.
5. **Le Pareto** : (1) vague chercheurs 24/08 · (2) **cette page** ·
   (3) dix contacts hispanophones ciblés · (4) traduction espagnole du livre.

---

## 5. Inputs obligatoires — lire avant d'écrire une ligne

- **`reports/geo_audit/REGISTRE_COLLISIONS.md`** — section « antropía / ES »,
  très fournie (marque OEPM ANTROPÍA de Vocento, rubrique éditoriale
  `elcorreo.com/antropia/`, Revista *Anthropía* PUCP, verdict RAE, Battaner).
  **C'est l'input n°1 de la page.**
- **`docs/CHECKLIST_AJOUT_LANGUE.md`** — la séquence (états A/B/C) et la
  Phase 0.
- **`content/quest-ce-que-lanthropie/_index.en.md`** — le modèle de ce que
  fait une page concept : geste GEO-01, désambiguïsations, FAQ, objections.
- Le record Zenodo ES (`21766184`) — pour le **verbatim et les mots-clés
  exacts**, à ne jamais reformuler.

---

## 6. Contenu attendu (arbitré le 03/08)

Une seule URL réunissant : la **définition canonique** ; le problème auquel
l'anthropie répond ; les **trois axes** (spatial, temporel, social) ; la
relation aux coûts sociaux, à l'externalisation et à l'entropie ; le lien
vers **AWP-01 ES** ; la **citation prête à copier** ; une présentation du
livre *ANTHROPIE* à venir en espagnol.

**Trois exigences non négociables :**

- **Verbatim canonique espagnol identique partout** :
  *« La antropía es la hipótesis según la cual los sistemas sociales
  desplazan el desorden en lugar de resolverlo. »* — c'est la forme
  contrôlée par `zenodo_audit_complet.py`. Ne pas la reformuler.
- **Geste GEO-01 en espagnol** : le mot, ses usages, le concept.
  *L'auteur n'invente pas le mot* — il en fixe un usage opératoire.
- **Adapter, pas traduire** : la page espagnole doit affronter **ses**
  voisins (Stiegler — déjà démarqué en FR/EN, l'espagnol traduit cette
  démarcation ; l'occupation éditoriale Vocento ; le sens
  « anthropisation »), pas recopier la liste française.

⚠ **Piège hispanophone spécifique** : la CEPAL, *centro-periferia*, la
*teoría de la dependencia* sont des **voisins et précédents partiels**,
jamais une filiation. Un arrimage direct exposerait à la critique de
reconditionnement — arbitrage rendu le 02/08.

---

## 7. Pièges techniques rencontrés dans ce fil (transposables)

- **Un contrôle qu'on n'éprouve pas ment.** Mon détecteur SSRN interrogeait
  `doi.org` : 403 anti-bot → il annonçait **6 papiers absents alors qu'ils
  étaient tous en ligne**. Corrigé par l'API Crossref. Toujours éprouver un
  détecteur contre un cas connu-vrai.
- **Le formulaire d'édition d'œuvre OpenLibrary** et **l'upload SocArXiv**
  résistent à l'automatisation (sélecteur de fichier natif). Le formulaire
  *auteur* d'OpenLibrary, lui, fonctionne.
- **Le nom du fichier déposé est public** (OSF affiche
  `AWP06_Digital_Infrastructures_EN.pdf`). Ne jamais déposer un `_tmp_…`.
- **PowerShell 5.1** : `.ps1` en ASCII pur, corps accentués lus depuis un
  fichier UTF-8. Le hook anti-push **misfire sur les heredocs bash** →
  écrire un script fichier.
- **MEMORY.md** approche sa limite de lecture : compacté à 17,2 Ko le 03/08.
  Surveiller.

---

## 8. COMMANDE DE REPRISE — à coller telle quelle

```
Nouveau fil : ouvrir l'architecture espagnole du site, puis créer la page
conceptuelle « ¿Qué es la antropía? ».

Avant toute chose, lis dans cet ordre :
1. Downloads\REPRISE_PAGE_ES_2026-08-03.md (ce document : état, décision
   d'architecture, arbitrages qui s'imposent, pièges, règle d'arbitrage)
2. reports/geo_audit/REGISTRE_COLLISIONS.md — section antropía/ES
3. docs/CHECKLIST_AJOUT_LANGUE.md
4. content/quest-ce-que-lanthropie/_index.en.md (le modèle de page concept)
5. PROJECT_STATUS.md § log 2026-08-03

DÉCISION DÉJÀ PRISE, ne pas la rouvrir : troisième langue Hugo complète
(pas de page isolée), mais corpus espagnol SÉLECTIF — racine /es/ minimale,
page conceptuelle, AWP réellement traduits, livres ES plus tard, AUCUN
miroir automatique des articles, recensions, actualités ou pages
institutionnelles.

TA PREMIÈRE TÂCHE : auditer l'architecture Hugo existante et me proposer un
PLAN DE MODIFICATION, sans rien modifier. Le plan doit couvrir :
config des langues · structure des contenus · menus · sélecteur de langue
(conçu aujourd'hui pour une paire) · hreflang et x-default · canonical ·
sitemap · traductions d'interface (i18n) · contrôles de sortie.

Exigence non négociable : le sélecteur et les hreflang ne doivent refléter
que les traductions RÉELLEMENT disponibles page par page — pas de triplette
FR-EN-ES artificielle, pas de retour silencieux vers le français.

Ne touche ni aux contenus ni à la production avant que j'aie arbitré ce plan.

Garde-fous : ne casse ni les URL EN ni leur câblage hreflang (positions
acquises) ; verbatim canonique ES identique partout ; adapter et non
traduire ; diff avant commit ; jamais de push automatique.
```

---

## 9. RÈGLE D'ARBITRAGE DES CONSIGNES FUTURES

**Une consigne nouvelle ne périme pas automatiquement un arbitrage rendu.**

Ce fil a produit cinq arbitrages (§4) fondés sur des faits vérifiés et deux
contre-expertises. Si une consigne future les contredit, la conduite est :

1. **Ne pas obéir en silence** et ne pas refuser non plus : **dire la
   contradiction**, en une ou deux phrases, en citant l'arbitrage concerné et
   ce sur quoi il reposait.
2. **Distinguer trois cas** :
   - *fait nouveau* (une plateforme change sa politique, une mesure
     infirme la précédente) → l'arbitrage tombe, on refait le raisonnement ;
   - *changement d'objectif de l'auteur* → l'arbitrage tombe : il servait
     l'ancien objectif, il ne vaut pas contre le nouveau ;
   - *simple oubli du fil précédent* → rappeler l'arbitrage et demander
     confirmation avant d'agir.
3. **L'auteur tranche toujours.** S'il réaffirme après avoir entendu la
   contradiction, c'est sa décision : exécuter pleinement, sans y revenir.

Ce qu'il ne faut pas faire : rejouer une piste déjà fermée sans le dire.
Le cas SciELO l'a montré — j'ai proposé les revues hispanophones juste après
avoir retiré le dépôt SciELO, réintroduisant le biais que je venais de
corriger. **La contre-expertise l'a vu, pas moi.**

---

## 10. Ce qui reste en attente, hors ce fil

- **Push** : 6 commits locaux non poussés au 03/08.
- **06/08** SocArXiv (AWP-02 si AWP-01 accepté) · **08/08** MPRA ·
  **17/08** OpenLibrary (statut librarian) · **24/08** vague chercheurs ·
  **15/09** relevé T1.
- Wikidata ES : batch prêt, à transmettre à Laura.
- Semantic Scholar : 16 URLs prêtes, jamais soumises (compte à créer).
- OpenLibrary : 2 doublons à fusionner dès le statut accordé ; description
  d'ANTHROPIE à saisir à la main.
- AWP-06 sur SocArXiv : **aucune licence déclarée** — à passer en CC-BY 4.0.
