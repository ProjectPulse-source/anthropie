# Project Status — stephane-lalut.com

## Bilan 2026-05-13 — Chantier diffusion clos

Synthèse des 4 axes de diffusion exécutés en mai 2026 ; le chantier est désormais clos pour la durée de la fenêtre GEO/diffusion 90 jours.

1. **Wikidata** : Phase A + B + C exécutées (lots `Lalut-Anthropie-PhaseA/B/C-2026-05-12/13`). 6 items AWP créés (`Q139771989` à `Q139771994`). Correction DOI Option B effectuée (12 suppressions manuelles). Script Python d'automatisation v1.0 dans `Wikidata/scripts/` (fetchers Zenodo/Crossref/OpenLibrary + generators awp/article/book + validators garde-fous P9934/P407).

2. **SocArXiv** : 6 AWPs déposés sur `osf.io/ymkpj`. DOIs SocArXiv liés en P953 sur les 6 items AWP Wikidata. Profil OSF `ymkpj` rattaché à `Q138909233` (Stéphane Lalut) via P973.

3. **OpenLibrary** : 4 fiches livre + page auteur enrichie. Author ID `OL16378291A`. Work IDs : Livresque `OL45424544W`, L'Odyssée `OL45424562W`, ANTHROPIE `OL45424565W`, Dette Publique `OL45424600W`. Batch 16 (P648 OpenLibrary IDs) transmis à Laura. 2 doublons OpenLibrary à fusionner après obtention du statut LIT (~1 semaine).

4. **Externe** : BnF dépôt légal régularisé, Bing Webmaster Tools configuré (import Google Search Console + sitemap), GitHub Actions IndexNow + Wayback Machine opérationnels (commit `ab86532`).

**Phrase de pilotage maintenue** : *« la prochaine preuve viendra des tiers ».*

**Statut final** : chantier diffusion clos. Aucune action structurelle prévue pendant les 90 jours GEO/diffusion. Actions résiduelles passives :
- Laura exécute le batch 16 OpenLibrary (~24h)
- Stéphane fusionne les 2 doublons OpenLibrary après obtention du statut LIT (~1-2 semaines)
- Surveillance Bing Webmaster Tools « AI Performance » + log mensuel Wayback Machine (`Wayback/archive-log.md`)

## Mise à jour 2026-05-13 — Workflows IndexNow + Wayback Machine

- **`.github/workflows/indexnow.yml`** : notification temps réel à Bing/Yandex
  après chaque push touchant `content/**`, `data/**`, `layouts/**`, ou la config.
  Sécurité supplémentaire : run hebdomadaire le lundi.
  La clé IndexNow est détectée dynamiquement depuis `static/<key>.txt`.

- **`.github/workflows/wayback-archive.yml`** : archivage mensuel (1er du mois,
  6h UTC) de toutes les URLs du sitemap sur Wayback Machine. Log cumulatif
  committé dans `Wayback/archive-log.md`.

Les deux workflows sont indépendants. IndexNow se déclenche à chaque push
significatif (notification immédiate). Wayback s'exécute mensuellement
(archivage long terme).

**Status** : workflows créés, non encore poussés en production. Stéphane
valide visuellement les YAML avant push manuel.

**Premier test recommandé** : déclencher manuellement chaque workflow via
l'onglet Actions du repo GitHub après push, pour vérifier que la chaîne
complète fonctionne sans attendre le prochain push naturel ou le 1er du mois.


> **À lire avant** : toute intervention sur le site, technique 
> ou éditoriale. Décrit l'état architectural, les doctrines 
> en place, les chantiers en cours et les chantiers reportés.
> Dernière mise à jour : 2026-08-15 (soir).
> **Règle de fraîcheur** : l'état écrit suit l'acte — toute session qui
> exécute met à jour ce log ET les statuts des registres/backlogs touchés
> dans la même session. Un statut périmé vaut défaut : il provoque la
> re-exécution de l'acquis ou l'abandon de travaux crus « déjà faits ».

## 0. Log chronologique

### 2026-08-15 (jour, 2) — Adaptation EN `/en/register-of-deported-costs/` + push auteur (mandat explicite du tour)

**Adaptation, pas traduction** (doctrine intent_matrix) : la page EN présente le Registre
(grille, 7 âges aux noms canoniques de la fiche EN, trajectoire spatial→social→cognitif,
« What the Register does not say »), donne **3 exemples adaptés** (outils, Néolithique,
marchés 2024) et renvoie pour le registre complet à l'édition EN *ANTHROPY* (632 p., qui
contient l'épilogue *Register of deported costs*) et à la version FR en ligne. **Les 165
jalons FR restent exclusifs à la page FR — jamais de traduction mécanique du corpus.**
Nom canonique retenu : « Register of Deported Costs » (= épilogue de la fiche EN publiée).
7 FAQ EN (JSON-LD validé), 0 cannibalisation avec /en/quest-ce-que-lanthropie/.

Maillage EN : fiche livre EN (`ressources_livre` + lien Contents + lastmod), page concept
EN (« Three pages extend the framework »), glossaire EN (entrée + désambiguïsation croisée
coupled-cost-registers), llms.txt § English, intent_matrix (en-adaptations). Au passage,
le titre du bloc « Ressources et données du livre » passé en **i18n** (`book_resources`
FR/EN) — il était en dur en français dans `layouts/livres/single.html` et serait apparu
en français sur la fiche EN.

Vérifié : build 0, YAML 0, compteurs 0, couverture GEO 0 signal (EN maille reconnue,
fraîche), hreflang ×3 sur la page FR, les deux sitemaps. **Push auteur exécuté ce tour
(mandat explicite « Push »)** — IndexNow part au push. Chaîne QR dette re-vérifiée en
ligne : compagnon github.io = redirection vivante vers /cout-de-la-dette-publique/?src=compteur-qr.

### 2026-08-15 (jour) — Maille `/registre-des-couts-deportes/` : rapatriement de l'ancien mini-site GitHub (commande auteur)

**Commande auteur** : refaire pour la page GitHub `ProjectPulse-source/anthropie` ce qui a été
fait pour le compteur dette — rapatrier dans le site, au design du site, « en autant de
réponses claires » pour le GEO grand public. Constat d'audit : le dépôt GitHub **est** le
dépôt du site (même remote) ; l'ancien mini-site (2025) ne survit que dans la branche
`backup-mini-site` et n'est plus servi nulle part. Son actif unique jamais rapatrié : le
**Registre des coûts déportés** (165 jalons rédigés « ordre créé / dette déportée » ; le
livre en compte 168).

**Livré :**
- `data/registre_couts_deportes.json` — 165 jalons **dérivés par script** (session, one-shot)
  depuis l'ancien `index.html`, typographie FR appliquée (insécables), affectation aux
  **7 âges du livre publié** (Sommaire de la fiche = vérité ; l'ancien mini-site portait un
  découpage antérieur, non repris) par bornes chronologiques. Répartition : 8/7/33/18/32/32/35.
  Le JSON est désormais la source maintenue ; `_meta` documente la provenance.
- Nouvelle maille `/registre-des-couts-deportes/` : réponse directe, grille de lecture,
  trajectoire spatial→social→cognitif (postface), registre complet rendu par le shortcode
  `registre-ages` (`<details>` ancrés par jalon, compteurs dérivés au build — **aucun nombre
  en dur**), section « Ce que le Registre ne dit pas », 7 FAQ (JSON-LD FAQPage validé).
  Anti-cannibalisation tenue : zéro FAQ définitionnelle anthropie/dette.
- Maillage : fiche livre ANTHROPIE (`ressources_livre` + lien Sommaire + lastmod), page
  concept (lien « histoire longue » + lastmod), glossaire (entrée « Registre des coûts
  déportés » + désambiguïsation croisée avec « registres de coûts couplés » AWP-06),
  `llms.txt`, `intent_matrix` v1.2 (2 requêtes couvertes, exemption commande-auteur
  documentée), NASSE_GEO_ETENDUE.md (cluster 4, gates passées), README du dépôt réécrit
  (la page GitHub devient un nœud du maillage : présentation + points d'entrée + note
  branche backup).
- Vérifié : build 0, `check-corpus-counters` 0, `check-geo-coverage` 0 signal (maille
  reconnue, fraîche, maillée), 165 `<details>`/ancres uniques, page dans `fr/sitemap.xml`,
  203 insécables posés dans le corps.

**Écartés (readback)** : Wikidata (graphe auteur clos 15/08 — rien à rouvrir, aucune
notabilité pour une page) ; ItemList JSON-LD des 165 jalons (poids ~50 Ko sans rich result) ;
redirections des anciennes URLs `*.html` (mortes depuis la bascule Hugo, aucun QR connu —
à la différence du compteur) ; miroir EN (candidat noté, doctrine « adapter, pas traduire »,
décision auteur). **Écart connu** : 165 jalons en ligne vs 168 au livre — les 3 manquants
n'étaient pas dans l'ancienne page ; à compléter un jour depuis le PDF broché si souhaité
(édition directe du JSON).

**Push auteur dû** (s'ajoute à la file : site d'abord, puis compagnon dette). IndexNow
partira seul au push (`content/**`).

### 2026-08-15 (nuit, 3) — Retours auteur `Modifs_Site.txt` appliqués (`27cee45`)

Ressource unique de la fiche livre **remontée avant les Working Papers** et reformulée
(le QR mis en avant — le double lien signalé avait déjà disparu au push précédent) ;
formules « honnêteté » supprimées (« louche lorsqu'on s'en réclame » — auteur) ; le
paradoxe budgets-en-hausse / services-dégradés rendu **causal et exact** : effet Baumol
(un service fait de personnes suit les salaires, pas la productivité) + besoins croissant
plus vite que le PIB (vieillissement, progrès médical, judiciarisation) → un budget stable
couvre chaque année moins de la demande, sans baisser ; la dette ne crée pas l'écart,
elle **pince la marge de rattrapage**. Corps + FAQ 5 alignés. Redirection QR **ratifiée
par l'auteur**. Push auteur dû.

### 2026-08-15 (nuit, 2) — Rapatriement du compteur sur la page ; compagnon → REDIRECTION (décision auteur)

**Décision auteur** (renversement PARTIEL de l'arbitrage externe 022215, signalé, non
effacé : le compagnon perd son rôle d'« annexe interactive » — design obsolète, hors
site). Exécuté (site `c82c21d`, compagnon `3f47597`, **2 push auteur dus : site
D'ABORD, compagnon ensuite**) :
- **Compteur animé rapatrié** sur `/cout-de-la-dette-publique/` : bloc `live` dans le
  JSON (ancre, fin de trimestre ISO, croissance annuelle calculée sur 4 trimestres —
  gardes 0-15 %), rendu en data-attributes, JS inline sans AUCUN nombre en dur,
  étiquette « extrapolation mécanique… ni observation ni prévision » (formulation du
  réviseur 033932), sans-JS = rien de cassé (hidden). Vérifié en navigateur : compteur
  en marche (≈ +6 400 €/s), mathématique contrôlée. Pas de fetch INSEE côté navigateur
  (choix assumé : cohérence compteur/ligne officielle ; l'« API automatisée » = le
  pipeline + PR).
- **Chaîne causale 4 maillons** pour non-spécialistes ajoutée sous le bloc (emprunt →
  stock → prix moyen → intérêts → qui paiera).
- **Tous les renvois site → compagnon retirés** (partial, page, fiche livre — la
  ressource fiche pointe la page et mentionne le QR).
- **Compagnon = page de redirection** (meta refresh + JS + lien) vers
  `/cout-de-la-dette-publique/?src=compteur-qr` (param = mesure des arrivées QR),
  canonical vers la page, noindex ; **l'URL github.io reste vivante À VIE** (QR imprimé
  dans les EPUB vendus — interdiction de renommer/supprimer dépôt ou compte, README à
  jour) ; le nœud healthcheck la surveille.

### 2026-08-15 (soir) — Chantier dette EXÉCUTÉ : B-minimal + page coût + pipeline + compagnon réparé — EN ATTENTE DES 2 PUSH AUTEUR

**GO auteur reçu** (chiffres automatiques + courbes croisées + « incontournable GEO »). Panel
interne convoqué (3 sièges) avant implémentation ; synthèse d'arbitre : variante **PR** (jamais
de publication sans merge humain), page satellite plutôt que section, une seule courbe (le
ciseau — pas de courbe « services publics » fabriquée), équivalences à millésime unique.
⚠ Constat de données qui corrige la demande : la corrélation « dette↑ → santé/éducation↓ »
est FAUSSE dans les agrégats (santé 8,1→8,9 % PIB ; éducation stable) — le récit publié est
le ciseau (coût qui baisse pendant que l'encours monte, retournement 2022) + équivalences de
masses 2024 + section « ce que les données ne montrent pas ».

**Livré (5 commits site `9761b7b`→`0b9774e`, build + linters verts, rendu vérifié en navigateur) :**
- `scripts/update_dette_insee.py` — INSEE SDMX (010777616/608) + Eurostat (D41PAY, COFOG) ;
  gardes : bandes, ancres consolidées, delta vs committé, non-régression, écriture atomique,
  exit 1 sans écriture (témoin positif : mutation réelle exercée) ; produit
  `data/dette_officielle.json` (bloc `affichage` FR précalculé + équivalences 2024) +
  endpoint public `/dette_officielle.json` + `static/img/ciseau-dette-interets.svg`.
- Bloc chiffré au build sur la page pont (partial `dette-chiffres` : errorf si absent, warnf
  si périmé >290 j — la garde vit dans le BUILD) ; placeholders `{dette.*}` dans
  `desc-figures` (couvre le JSON-LD FAQPage) ; shortcode `dette-val` — AUCUN chiffre en dur.
- **Nouvelle page `/cout-de-la-dette-publique/`** (propriété « combien coûte » ; « qui paie »
  reste EXCLUSIF au pont) : ciseau SVG 2 panneaux, équivalences (intérêts 2024 = 7,2× les
  tribunaux GF0303, > poste GF03 entier, 40 % de GF09, 23 % de GF07), 5 FAQ chiffrées par
  placeholders, honnêteté explicite (pic ratio = T1 2021, pas aujourd'hui). intent_matrix +
  llms.txt à jour (exemption « réaction/anticipation » signalée : le signal = commande auteur).
- Fiche livre : bloc « Ressources et données du livre » (frontmatter `ressources_livre`).
- `.github/workflows/dette-insee.yml` : cron mensuel → fetch+gardes → build gate → **PR**
  (merge humain = publication) ; issue si échec ; condition de décroissance en tête.
- **Compagnon** (clone `D:\PRO\90_SAS\EN_COURS\dette-publique-france`, 3 commits `42620d4`→`9108b35`) :
  JSON de repli régénéré (était 2 docs concaténés, illisible), ancre d'extrapolation recalée
  (T1 2026, +5,7 %/an observé), idbank faux 001694056 + clé fictive supprimés, **titre du
  livre corrigé (« Dette Souveraine » ×5 → vrai titre)**, **bouton Amazon réparé (était
  `href='#'`)** → `/dp/2958634736`, og:image existante, backlinks vers pont/coût/fiche,
  pipeline propre supprimé (condition de mort : les données viennent du site). Rendu vérifié
  en navigateur : `[INSEE Live] Source : insee-live — période : 2026-Q1`.

**✅ Porte ⓪ FRANCHIE — contre-expertise contenu `033932` ARBITRÉE, CORRIGÉE et CLOSE
le 15/08 soir** (réponse ChatGPT ; canal Perplexity non rendu, compensé par
auto-vérifications à la source : D41REC 3,9 Md€ → brut/net marginal ; TR 1 561,6 Md€).
Verdict « publiable après corrections ciblées », **toutes appliquées** (commits site
`0958455`, compagnon `60b1479`) : **taux apparent** ajouté (le chaînon stock→charge :
6,5 % en 1996 → 1,2 % creux 2020 → 2,0 % en 2025, série publiée dans le JSON) ; double
base **+124 %/2020 et +80 %/2019** ; **intérêts/recettes 4,3 %** (2025) ; clause COFOG
GF0303 vs mission Justice ; hiérarchie observation→mécanisme→lecture (« peut être lue »,
plus d'« anesthésiait » causal) ; « pic historique » → « maximum de la série disponible »
(révision-résistant) ; absorbeurs élargis ; compagnon : « premier poste budgétaire de
l'État » RETIRÉ (faux en APU). Écartés conformes : dette/habitant, projection, zone euro.
Arbitrage : `ARBITRATIONS\anthropie-site-20260815-033932_arbitrage.md`.

**✅ Portes ① et ② FRANCHIES le 15/08 (nuit) — les deux push exécutés par l'auteur, LIVE
VÉRIFIÉ** : page 200 + bloc stylé (contrôle visuel), endpoint `/dette_officielle.json` 200,
SVG 200, JSON compagnon valide en ligne (2026-T1), IndexNow notifié automatiquement.
Ligne healthcheck du compagnon AJOUTÉE au workflow (commit suivant). **RESTENT : ③ 2FA
sur le compte ProjectPulse-source (geste auteur) ; ④ merges des futures PR de données
(~4/an) ; arbitrage d'emplacement du clone compagnon (aujourd'hui `D:\PRO\90_SAS\EN_COURS\`,
le sas — à migrer vers un emplacement pérenne ou à re-cloner à la demande).**

### 2026-08-15 — Rattachement compteur de dette : architecture B-minimal ARBITRÉE, en attente de GO auteur

**Saisine auteur** : rattacher le compteur `ProjectPulse-source/dette-publique-france`
(GitHub Pages, cible du QR imprimé dans l'EPUB *Dette publique*) au site, avec l'idée de
faire de la fiche livre « un incontournable GEO ». Audit gate 0 (lecture seule) puis
contre-expertise externe `anthropie-site-20260815-022215` (REASONING_AUDIT, cycle complet
CLOS le jour même). **Aucune modification du site ni du compteur dans cette session.**

**Décision retenue** (détail : `.claude/external-audits/ARBITRATIONS/anthropie-site-20260815-022215_arbitrage.md`) :
un seul actif citationnel — `/qui-paie-la-dette-publique/` reçoit un bloc chiffré compact
**au build** (période INSEE, montant, % PIB, source, date de relevé) ; compteur = preuve
visuelle (6 gestes de durcissement puis STOP — son JSON de repli est corrompu, données
2025-T2, cron disparu, 0 lien retour) ; fiche livre = conversion (bloc « ressources »,
jamais de FAQ informationnelle — garde-fou GEO-04 intact). Page « en chiffres » NON
ouverte (critère durci : réponse non substituable). Pas de sous-domaine pour le SEO.
INSEE 2026-T1 vérifié à la source : **3 536,1 Md€ / 117,5 % du PIB** (idbanks 010777616/608).

**Faits neufs vérifiés (sources primaires, 15/08)** : les bots de search sont
`OAI-SearchBot`/`Claude-SearchBot` (pas GPTBot/ClaudeBot) ; Google **rend le JS** — mais
le contenu essentiel ne doit jamais en dépendre (invariant multi-canaux) ; **rich result
FAQ retiré de Google Search le 15/06/2026** (les FAQ du site gardent leur valeur
lecteur/LLM, l'argument rich result est mort) ; `llms.txt` officiellement neutre pour
Google. → mémoire `reference_geo_crawlers_et_faq_2026`.

**EN ATTENTE AUTEUR** : ① GO chantier site (B-minimal) ; ② GO chantier compteur (6 gestes) ;
③ emplacement du clone local (`D:\anthropie\dette-publique-france`, hors `D:\PRO`).

### 2026-08-13 — Maintien souverain d'ANTHROPY EN à 1,99 USD ; consignations US/CA révoquées

Décision auteur : « Je conserve ANTHROPY à 1,99 USD pour l'instant. » Conséquences
au registre des prix (dépôt Ads) : la vitrine $1.99 relue le 12/08 à 21:55Z était
l'état réel — ratifié —, pas un retard de propagation. `promo_scheduled_end` passe
à `null` (fenêtre ouverte, fin à la prochaine déclaration) et les
`normal_price_observed_return` US et CA du 12/08 sont **révoqués** (CA par
déduction PRIMARY_CONVERSION, à confirmer). À re-consigner au vrai retour à 12,99.
⚠ Signalé à la session Ads via le registre : (1) les enchères US se restaurent
automatiquement le 13/08 alors que la promo continue — cohérence à arbitrer ;
(2) le Countdown UK du 21-27/08 exige la stabilité du prix .co.uk avant le 20/08 —
vérifier que le maintien USD ne s'y propage pas par conversion.

### 2026-08-12 (nuit) — AWP-07 déposé sur MPRA ; correctif Search Console images

1. **MPRA : AWP-07 déposé — paper #130468, in review** (mandat auteur explicite,
   dépôt TEST espacé pour sonder le blocage referee du 04/08). Formulaire complet :
   titre + sous-titre canoniques, abstract Zenodo intégral, 12 mots-clés, JEL
   B41/B52/D62/Q57, bibliographie complète extraite du PDF (References est un champ
   OBLIGATOIRE MPRA), PDF 220 kB. Vue « Manage deposits » relevée au passage :
   AWP-01..05 Under Review (AWP-01 modifié le 02/08), AWP-06 Live Archive.
   Registre + `scripts/check_deposits_status.py` mis à jour ; contrôle J+14 posé
   au calendrier (26/08). Règle maintenue : AWP-08 seulement après ACCEPTATION.
2. **Search Console (mail Google du 12/08)** : champs `license` et
   `acquireLicensePage` manquants sur les ImageObject — ajoutés au JSON-LD des
   couvertures (layouts/livres/single.html) ; `license` pointe la nouvelle section
   « Droits d'utilisation des images » (#droits-images) de /transparence-contacts/,
   `acquireLicensePage` pointe /contact/. Vérifié dans le build.
3. Hors dépôt site, même session : prix Kindle consignés dans le registre Ads
   (Anthropie/Dette constat fiche + US/CA déclaration auteur ; Livresque consigné
   à 21:43Z après résolution de la contradiction : la vitrine 5,00 € était un
   affichage **Prime Reading** — prix réservé aux clients Prime, PAS le prix
   catalogue ; KDP vérifié à 12,99 par l'auteur. ⚠ Fait commercial nouveau pour
   la session Ads : Amazon a fait entrer Livresque en Prime Reading) ; collector
   documentaire relancé (PID 24720) ; rappel fin promo Premier coup créé (17/08).

### 2026-08-12 (soir) — Notes Amazon dépôt-dérivées ; contrôles SSRN/OSF/MPRA consignés

1. **Notes Amazon rafraîchies** (commit `352a04a`) : Odyssée 4,4/162 · Livresque
   4,1/87 · Dette 4,2/27 · Anthropie 4,4/22. **Trou détecté par l'auteur** : la
   routine relisait une liste figée de 4 livres ; le Premier coup — sur
   `/ressources-offertes/` depuis le 10/08 — n'était pas relevé. Règle actée :
   la liste se **dérive de `content/livres/*.md`** (anciens mis à jour, nouveaux
   relevés d'office). Relevé Premier coup : **5,0/2 — non affiché** (2 avis =
   preuve non matérielle ; champs absents = pas d'étoiles, garde en place).
   Procédure inscrite : mémoire de routine + `docs/CHECKLIST_AJOUT_LIVRE.md` § 2.
2. **SSRN — contrôle clos** (page auteur relue en direct le 12/08) : 6 papiers,
   108 téléchargements, AWP-07/08 absents. AWP-07 n'a jamais été déposé sur
   SSRN → rien à « accepter » → pas de dépôt AWP-08. La file réelle d'AWP-07/08
   est MPRA (après déblocage) ; grille du 03/08 défavorable à SSRN de toute façon.
3. **MPRA** : relance envoyée le 02/08 12:43 (vérifié dans les Envoyés) ; aucune
   réponse à J+10. Prochaine décision auteur : 2e relance vs attente.
4. **OSF** : transition consignée au registre (fin créations 16/11/2026,
   projets read-only 19/02/2027 ; preprints et DOI persistent — z6x38 non
   menacé). Action unique avant novembre : vérifier l'absence de projets actifs
   sur ymkpj.
5. Monitoring `anthropie-monitoring` : les échecs du 06/08 sont résolus (runs
   verts le 12/08).

### 2026-08-12 (suite) — Arbitrages auteur : related_book, rattrapage intent_matrix, registre resynchronisé

Trois gestes sur décision auteur, dans la foulée de l'ajout EAN du matin :

1. **`related_book: livresque-des-mots`** ajouté à la fiche EAN « Parler sans
   savoir à qui » (l'essai sur le quant-à-soi du livre éclaire l'anthologie).
2. **`data/intent_matrix.yaml` v1.1 — rattrapage** : la règle d'inscription du
   § 0 était restée sans exécution depuis la création de la matrice (aucune
   publication inscrite). Nouvelle entité `publications-presse` : 18 inscriptions
   chronologiques (objet au vocabulaire `presse_objets`, sujets d'entrée
   périphériques, fil remontant AWP + livre). Le fil est un miroir du front
   matter des fiches — source de vérité — à répercuter dans le même commit.
3. **`data/works.yaml` : 5 `related_works` resynchronisés** sur les fiches
   (terrestres, fressoz, carton-malm, vuillemey, grande-conversation) : le
   maillage des fiches avait été enrichi à la parution d'AWP-06/AWP-07
   (checklist § 1.4), le registre n'avait jamais suivi — même classe
   « état déclaré ≠ état réel » que les compteurs du matin.

### 2026-08-12 — Publication EAN « Parler sans savoir à qui » (hors-série États du livre)

**Saisine** : ajout au site de la publication du 2026-08-11 — essai original (non
recension) pour le hors-série n°9 d'En attendant Nadeau, « États du livre ».
Exécution par la checklist `docs/CHECKLIST_AJOUT_PUBLICATION.md` :

- Fiche `content/publications/en-attendant-nadeau-parler-sans-savoir-a-qui.md`
  (logo, noindex + hors sitemap, chapo FR/EN, fil remontant `related: [awp-06]` —
  même maillage IA/numérique que les fiches EAN Welgryn et Neel-Chavez).
  Pas de `related_book` : l'essai ne recense ni n'éclaire un livre du catalogue.
- `data/works.yaml` : entrée `art-ean-parler-2026-08`, registre v1.13,
  `meta.last_updated` 2026-08-12 ; total_works 38 → 40 (le compte déclaré était
  déjà en retard d'une unité avant l'ajout — recalé sur les 40 entrées réelles :
  27 articles + 8 AWP + 5 livres).
- Murs presse `/a-propos/` FR + EN : `presse_objets` « Livre et algorithmes » /
  « Books and algorithms ».
- `static/llms.txt` : aucun changement requis (la section publications liste les
  revues, EAN y figure déjà ; aucune énumération par article).
- `data/intent_matrix.yaml` : non modifiée — constat : aucune publication n'y est
  inscrite par slug malgré la doctrine d'inscription ; suivi de la pratique
  établie, écart signalé à l'auteur.
- Au passage (classe « état déclaré ≠ état réel ») : les compteurs de section en
  commentaire de `works.yaml` avaient dérivé (« PUBLIÉS (10) » pour 12 entrées,
  articles publiés restés sous « EN ATTENTE ») — compteurs durs retirés des
  en-têtes, le champ `status` de chaque entrée fait foi.

### 2026-08-11 (nuit) — `/doctor` : le `CLAUDE.md` violait la règle de surface qu'il énonce

**Saisine** : `/doctor` (santé de l'installation Claude Code). Résultat de l'appareil
lui-même : **rien à réparer**. Installation npm unique (`D:\npm-global`), pas de résidu
natif ni de `~/.claude/local`, cinq fichiers de configuration qui parsent, quatre
définitions d'agents valides et sans collision de nom, version `2.1.227` = dernière
publiée, `defaultMode: auto` déjà actif au scope utilisateur et non masqué par le projet.
Aucune extension inutilisée à désinstaller : `panel` 28 usages, `capture-kiosque` 0 mais
installée le 26/07 pour un besoin épisodique (gardée), aucun plugin, aucun serveur MCP
local. Fenêtre : 50 transcripts, 13/07 → 11/08.

**Le vrai défaut est éditorial, et c'est le nôtre.** Trois blocs de `CLAUDE.md`
recopiaient ce que le dépôt sait déjà — et avaient **dérivé sans bruit** :
« AWP-01..05 » quand il y en a huit ; six sections `content/` listées quand il y en a
vingt-six ; quinze partials SCSS énumérés quand `main.scss` en importe vingt-et-un ;
sept partials cités sur trente-trois. Quatre énoncés faux dans le fichier que **toute**
session lit avant d'agir.

**C'est exactement la « règle de surface » du 11/08 au matin, appliquée à
l'instruction au lieu du gabarit.** La règle dit : *« Toute valeur dérivable se dérive —
la recopier, c'est programmer sa dérive. »* Elle a été écrite pour les gabarits Hugo.
Le `CLAUDE.md` qui la porte était lui-même une liste recopiée. Le défaut n'a pas été
trouvé par un linter : il l'a été en confrontant le fichier au dépôt, c'est-à-dire
exactement comme les six occurrences fondatrices l'avaient été — en regardant.
**Portée à retenir : la règle vaut pour la documentation d'instruction, pas seulement
pour le code de rendu.** Un `check-corpus-counters.py` ne regarde pas `CLAUDE.md`.

**Correctifs appliqués** (aucun commit, diff laissé à la revue) :

- `CLAUDE.md` — les trois énumérations dérivables remplacées par des pointeurs
  (`layouts/partials/`, `assets/scss/main.scss`, « lire un fichier existant »). Conservé
  verbatim tout ce qui ne se dérive pas : le gotcha `hero-flowfield.js` (promu en ⚠, il
  est désormais le point de la section), la convention `[params.design]`, le gabarit
  160×107, le lien `faq` → `schema-faqpage.html`. −14 lignes / +6, ≈ 755 tokens résidents
  par session.
- `CLAUDE.md` § Méthodologie de patch — retrait du renvoi n° 3 vers `.claude/rules/` :
  **ce répertoire n'a jamais existé dans ce dépôt.** Chaque session partait en lecture à
  vide. Le renvoi reste dans `~/.claude/CLAUDE.md`, qui est chargé dans tous les projets.
- `.claude/settings.local.json` (gitignoré) — 99 → 88 règles. Retirés : quatre
  blancs-seings (`Bash(python *)`, `Bash(PYTHONIOENCODING=utf-8 python *)`, un wrapper
  `sh -c`, un `rm -f` destructif pré-approuvé sur `02-DATA_RAW/`) et sept règles mortes
  ou malformées (deux blobs `curl`+`python -c` de 769 et 485 caractères, une parenthèse
  non fermée, trois cibles absentes du dépôt **et** de l'historique git — vérifié).
  Sauvegarde pré-édition dans le scratchpad de session.

**Suite immédiate — deux gates étaient rouges en permanence sous Windows.** Le retrait du
blanc-seing `Bash(PYTHONIOENCODING=utf-8 python *)` a rendu visible ce qu'il masquait :
`scripts/check-corpus-counters.py` **sortait 1 sur corpus sain**, parce que
`UnicodeEncodeError` se déclenche en imprimant la ligne de *succès* (« ✓ », hors cp1252).
Le gate que `CLAUDE.md` déclare bloquant avant commit ne pouvait donc jamais rendre 0 sur
cette machine — et son échec est **indiscernable d'une divergence réelle** pour qui ne lit
que le code de sortie, ce que la consigne demande précisément de faire. Son docstring
annonçait « Encodage UTF-8 forcé pour Windows » : **état déclaré ≠ état réel**, règle
d'audit n° 7, dans le gate lui-même. Même défaut sur `scripts/audit_works.py`, en pire :
il meurt ligne 566 (« 📖 Lecture de… »), **avant tout appel réseau** — il n'a donc jamais
pu tourner sous Windows autrement que préfixé.

*Correctif* : garde `sys.stdout.reconfigure(encoding="utf-8")` en tête des deux fichiers
(+21 lignes, additions pures). **Vérifié par la sortie, pas par relecture** :
`check-corpus-counters` rend 0 de bout en bout avec le ✓ affiché ; `audit_works` bascule
`cp1252 → utf-8` à l'import et imprime les huit glyphes qui le tuaient. Les trois linters
sûrs sortent 0.

*Ce que le challenge a évité* — trois fois de suite, l'analyse initiale était fausse :
(1) le premier scanner comptait `# -*- coding: utf-8 -*-` comme une garde, alors que ce
cookie déclare l'encodage de la **source** et ne protège rien : deux fichiers classés
« protégés » ne l'étaient pas ; (2) le deuxième comptait les caractères **n'importe où**
dans le fichier — commentaires, docstrings, écritures en UTF-8 incluses — et annonçait
9 fichiers à corriger ; (3) l'analyse AST, restreinte aux littéraux atteignant réellement
`print()`, ramène le périmètre à **4, dont 2 suivis**. `audit_geo_v2.py` et ses 1372
occurrences n'imprime rien de fautif : il aurait été patché pour rien. **Mesurer la sortie
plutôt que lire le code n'a pas seulement corrigé le diagnostic, il a divisé le patch
par cinq.**

*Restent 2 fichiers non suivis*, laissés intacts (fichiers de travail) :
`scripts/check_dates_coherence.py` (2 `print()` fautifs) et `scripts/fix_dates_en.py`
(3) — ce dernier étant un mutateur de contenu, il n'a été ni exécuté ni modifié.

*Arbitrage tranché (auteur, même session) : le linter est installé.*
`scripts/check-console-encoding.py` — analyse AST, ni exécution ni réseau. Il ne signale
un fichier que s'il cumule **(1)** un littéral hors cp1252 atteignant `print()` **et**
**(2)** l'absence de reconfiguration réelle de `sys.stdout` : sans la condition (2) il
crierait sur les fichiers réparés. Le cookie `coding:` est délibérément exclu des motifs
de garde — c'est ce qui avait produit le faux négatif initial. Portée assumée comme
**borne inférieure** : l'analyse statique voit les littéraux, pas un caractère arrivant
par variable. Enregistré dans `CLAUDE.md` (un linter que personne ne lance est mort).

*Testé par mutation réelle, jamais par relecture* — les deux mutations sont détectées et
aucune ne survit : (A) script fautif ajouté dans `scripts/` → exit 1, fichier nommé, puis
supprimé ; (B) garde retirée d'un vrai fichier déjà réparé → exit 1, fichier nommé, puis
restauré avec **SHA-256 identique avant/après** (`ac3e81c9…4c5cd2ad`). Les 4 linters
sortent 0 sous console cp1252 sans préfixe. 2 scripts non suivis également réparés
(`check_dates_coherence.py`, `fix_dates_en.py` — enjeu accru sur le second, qui modifie
du front matter : un crash en cours d'impression laisserait une passe partiellement
appliquée sans compte rendu).

**Règle de conduite actée par l'auteur, appliquée à elle-même dans la foulée.** Le build
de déploiement remontait un avertissement : cinq actions GitHub épinglées ciblent Node 20,
déprécié, et GitHub les force provisoirement sur Node 24. J'avais classé cela « pas à
traiter ce soir ». **Arbitrage auteur : non.** Un défaut identifié dont la correction est
connue et disponible se traite dans la session même — et en priorité quand il appartient
à la classe qui *ne se signale pas au moment où elle casse* (dépréciation, sursis
fournisseur, garde qui ne garde rien, état déclaré ≠ état réel). Ces défauts ne coûtent
rien tant qu'ils dorment, puis coûtent une panne qu'on ne rattache pas à sa cause et qui
en déclenche d'autres. Inscrit dans `~/.claude/CLAUDE.md` (portée transverse à tous les
projets) et en mémoire `feedback_pas_de_report_solution_disponible`.

*Exécution* — 5 pins relevés dans 4 workflows : `checkout` v4→v7.0.1,
`configure-pages` v4→v6.0.0, `upload-pages-artifact` v3→v5.0.0, `deploy-pages` v4→v5.0.0,
`github-script` v7→v9.0.0. Les ruptures ont été qualifiées **contre l'usage réel du
dépôt**, pas contre le changelog en général : v6 de `checkout` change la persistance des
identifiants et v7 bloque les PR de fork sur `pull_request_target`/`workflow_run` — aucun
workflow ici n'est concerné ; la rupture v5 de `configure-pages` ne touche que l'entrée
`static_site_generator: next`, non utilisée. Seule rupture réellement dangereuse :
**`upload-pages-artifact` v4 exclut les fichiers cachés de l'artefact** — écarté par la
mesure, un build local montre que `public/` n'en contient aucun (sinon il aurait fallu
`include-hidden-files: true`, et la perte aurait été silencieuse).

*Défaut attrapé par le contrôle des pins* : le SHA retenu pour `github-script` n'était pas
un commit. La ref `v9.0.0` est un **tag annoté** — `.object.sha` renvoie l'objet-tag, pas
le commit visé. Dans un `uses:`, cela casse au runtime avec un message opaque. Les cinq
pins sont désormais vérifiés un par un via `repos/<action>/commits/<sha>`. **À refaire
systématiquement lors d'un repin : résoudre le tag, ne jamais recopier `.object.sha`.**

**Point de vigilance non traité** : `memory/MEMORY.md` (index de 207 fiches) est devenu
le plus lourd fichier chargé à chaque session, ≈ 4 360 tokens estimés — devant les deux
`CLAUDE.md` réunis. Rien de cassé, mais c'est le premier poste à examiner si le contexte
se tend.

### 2026-08-11 (soir) — Dossier GEO EXPERIENCE : aucun outil installé, une doctrine de la note actée

**Saisine** : `GEO EXPERIENCE/GEO_Experience-01..04.txt` (hors dépôt, gitignoré) —
audit de six dépôts GEO (GEO-optim/GEO, geo-citation-lab, elmohq/elmo,
Auriti-Labs/geo-optimizer-skill, Cognitic-Labs/geoskills, oneglanse), en vue
d'outillage et de veille.

**Verdict, après 4 navettes arbitrées : AUCUNE INSTALLATION.** Motifs, dans l'ordre
de force : (1) **OneGlanse = NO-GO doctrinal** — il automate les interfaces web
consommateur authentifiées (Camoufox, sessions ChatGPT/Gemini/Perplexity/Claude), ce
que la règle non négociable n°1 d'`external-audits` interdit ; la question ne se
discute pas sur ses mérites techniques. (2) **Redondance** — l'appareil existant
(`GEO_PROTOCOLE_MESURE.md`, 18 prompts, `intent_matrix.yaml`, `GEO_QUERY_MATRIX.csv`,
`audit_geo_v2.py`, `check-geo-coverage.py`) couvre déjà ce que ces outils apportent ;
Citation Lab se réduit à trois concepts (source sélectionnée / contenu absorbé /
entité exposée), soit un paragraphe de protocole, pas une installation. (3) **Le coût
réel n'est pas l'API mais la lecture humaine** — 18 × N répétitions × N moteurs, et
l'absorption ne se code pas, elle se lit. (4) **Le protocole § 3 interdit déjà à toute
métrique de volume de déclencher une action** : un score mieux mesuré déciderait
toujours de rien.

**Défaut réel trouvé, et c'est le seul acquis du dossier** : le score T0 « 5-6/18 »
circulait **sans sa couverture** — un moteur sur cinq interrogé, 19 cellules sur 90,
soit 21 %. Le symétrique exact existait dans l'appareil éditorial : `MODULE_RETRO-LAB`
présentait « 18,0 → 18,2 » comme *la preuve par la mesure* qu'une passe améliore la
note, sur un instrument qui n'a jamais déclaré sa matérialité. **Même défaut, deux
appareils.**

**Acte — doctrine de la note, arbitrée par l'auteur (9 amendements), appliquée des
deux côtés** : une note ne circule jamais nue ; quatre objets à ne jamais fondre en un
seul (granularité de la grille · **couverture pondérée**, preuve directe vs inférence ·
**fiabilité empirique**, méthode déclarée a priori mais valeur estimée sur les
réplications observées · **seuil de matérialité** fixé a priori) ; « bande de seuil »
requalifiée en **zone de revue décisionnelle**, qui ne déclenche une notation
complémentaire que si une décision dépend réellement du franchissement ; la réplication
estime l'incertitude, elle **ne crée pas de matérialité** ; une divergence
interne/externe déclenche une **investigation de calibration**, jamais une moyenne
silencieuse ni un verdict automatique de défaut de grille ; **trois étages** —
Conformité / Note / Traction, la traction n'autorisant **jamais à elle seule** une
correction de l'objet, seulement une hypothèse à instruire.

**Fichiers touchés** — `MODULE_RETRO-LAB` **v1.4** (invariant 9, § Trois étages, 2
lignes au gate d'entrée, contrôle bloquant ② à six, garde-fou anti-invariant imaginaire,
requalification 18,0 → 18,2 en **non-dégradation**) ; v1.3 archivée avec empreinte —
`_ARCHIVE_MODULES\MODULE_RETRO-LAB_v1.3_2026-08-07.md`, SHA-256 `6FB8AD94…13DD38`
(**première révision du control plane restituable à l'identique** ; l'exigence de
versionnement du § Versionnement reste entière). `GEO_PROTOCOLE_MESURE.md` **§ 6**
(doctrine transposée ; **±3/18 requalifié en seuil de matérialité**, ce n'était pas un
seuil de bruit) et `GEO_PROMPTS_T0.md` (résultat réécrit par moteur avec couverture).
Ces deux derniers vivent dans `reports/` — **gitignoré**, donc hors commit.

**Priorité qui en découle pour T1 (octobre)** : *finir la couverture avant de raffiner
l'instrument.* Compléter ChatGPT, Copilot et Claude sur les 18 intentions vaut plus que
toute réplication statistique sur Perplexity. Six variables à relever en plus du ✔/✘
(coût nul, même lecture) : source trouvée · citée · entité mentionnée · **concept repris**
· concurrent dominant · **collision sémantique**. Motif : c'est la colonne « concurrent
cité » — jamais le score — qui a produit le seul résultat actionnable de T0 (prompt 7,
« dette technologique » capté par « dette technique » au sens logiciel). Et **archiver
les réponses brutes** : seul coût de non-exécution irrécupérable du dossier.

**Passage unique d'Auriti — EXÉCUTÉ le 11/08, test de valeur marginale RÉUSSI (une
trouvaille réelle sur treize recommandations).** Exécution : venv isolé hors dépôt,
wheels uniquement (aucun `setup.py`), sans les extras `openai`/`anthropic`/`mcp` — donc
aucun appel LLM possible, zéro euro, aucune clé. Contrôle avant exécution : le paquet ne
lit que des variables `GEO_*` et `PERPLEXITY_API_KEY`, aucune définie ici. Venv supprimé
après coup, rien de persistant. Rapport : `reports/geo_audit/AURITI_PASSAGE_UNIQUE_2026-08-11.json`.
Son score (67/100) est ignoré par doctrine — 4 de ses 13 recommandations sont des
pseudo-standards de son invention (`/.well-known/ai.txt`, `/ai/summary.json`,
`/ai/faq.json`, `/ai/service.json`, plus WebMCP) que **rien ne lit** ; Google écrit
explicitement qu'aucune donnée structurée particulière n'est requise pour ses fonctions
génératives. Écartés aussi : en-têtes HSTS/CSP/X-Frame-Options (GitHub Pages ne pose pas
d'en-têtes de réponse), « image sans alt » (**faux positif vérifié** : figure dans un
conteneur `aria-hidden="true"`, l'`alt` vide est la bonne pratique), « keyword stuffing
amazon 9,1 % » (artefact des liens d'achat légitimes — noté comme observation
spéculative, non actionnable).

**La trouvaille, et le correctif — `fix(schema)` : l'accueil pointait vers un auteur
introuvable.** L'accueil émettait `author`/`publisher` → `{"@id": ".../a-propos/#person"}`
sans jamais définir ce nœud dans le document. Le lien existait **en intention** ; il
**pointait dans le vide**. Pour un moteur qui ne lit que la page la plus récupérée du
site, l'auteur était un identifiant opaque : ni nom, ni ORCID, ni Wikidata — alors que
`data/author.toml` porte 9 identifiants externes. Encore la règle de surface du 11/08 :
la donnée existe au dépôt, la surface ne la reçoit pas, **en silence**.

⚠ **Pourquoi `audit_geo_v2.py` ne pouvait pas le voir** : `scripts/audit_geo_v2.py:245`
—`if URL_ABOUT and URL_ABOUT in html_cache:`— il teste `Person`/`sameAs`/`jobTitle`,
les bons champs, mais **uniquement sur `/a-propos/`**. Il vérifie que l'ancre d'entité
existe *quelque part*, jamais qu'elle existe *là où les moteurs arrivent d'abord*.
**Classe de défaut, pas instance** : notre auditeur contrôle des propriétés sur des
surfaces présumées.

**Mesure préventive PRISE — `audit_geo_v2.py` § A.2 bis, « Références `@id` — aucun
identifiant opaque ».** Règle retenue après calibrage sur le site réel : *tout `@id` cité
sur une page doit y être accompagné d'au moins un `@type`*. La formulation naïve — « tout
`@id` doit résoudre dans le document » — a été **écartée** : elle aurait signalé en faux
positifs les arêtes inter-pages **délibérées** du site-graphe (nœud concept
`#concept`, série AWP). La bonne frontière n'est pas *où le nœud est hébergé*, c'est
*est-il typé là où il est cité* : une référence typée et nommée livre une entité à un
moteur qui ne lit que cette page ; un `@id` nu ne livre qu'un pointeur.

**Calibrage vérifié dans les deux sens, sur fixture qui échoue** (le site en ligne porte
encore le défaut, le correctif n'étant pas déployé) : ❌ sur **Accueil FR et Accueil EN**
(`author, publisher` → `/a-propos/#person`), ✅ sur les **8 autres pages** auditées —
à-propos, définition, série, AWP FR/EN, trois livres. Zéro faux positif.

✅ **Déployé et vérifié le 11/08 à 04h38** (push `a1cf42a..c2fec20`, Actions *Deploy Hugo*
et *IndexNow* verts). Contrôle de non-régression passé : les deux accueils en ligne portent
désormais `@graph` = `WebSite` + `Person` (nom, jobTitle par langue, **9 identifiants
externes**), et **A.2 bis sort 10/10 en vert** — les deux ❌ sont devenus ✅, les huit autres
n'ont pas bougé. Le garde-fou a donc été observé rouge puis vert sur le même contrôle : il
mesure bien ce qu'il prétend mesurer.

Correctif appliqué dans `layouts/partials/schema-website.html` : `@graph` portant le
`WebSite` **et** un nœud `Person` minimal de même `@id` (nom, url, jobTitle, 9 `sameAs`)
— la référence se résout dans le document, sans duplication : `description` et
`knowsAbout` restent sur `/a-propos/`, qui demeure le nœud canonique. Au passage,
`$personID` cessait d'être **recopié en dur** : il se dérive de `data/author.toml`, avec
deux `warnf` (registre sans `canonicalProfileUrl`, registre sans `sameAs`).
**Garde-fou testé par mutation réelle** — champ retiré → `WARN` observé au build →
`data/author.toml` restauré, SHA-256 identique. Vérifié sur les deux accueils (FR et EN).
Build 0 warning, `check-geo-coverage` et `check-fiches-registre` à 0.

⚠ **Piège d'outillage à connaître** : `scripts/check-corpus-counters.py` sort **1** dans
un terminal cp1252 — non pas sur une divergence, mais parce qu'il **plante en imprimant
son message de succès** (`✓` non encodable). Verdict réel : « Aucune divergence
détectée ». Le lancer avec `PYTHONIOENCODING=utf-8` → exit 0. Ne pas lire ce 1 comme un
échec de corpus.

### 2026-08-11 — Le mur « Auteur » de /a-propos/ itère enfin sur le dépôt

**Défaut trouvé par l'auteur** : *La Société du premier coup*, publiée la veille,
était **absente de `/a-propos/`** — sans erreur, sans warning, sans trace.

**Cause** : les deux murs de la page étaient construits **à l'envers l'un de
l'autre**. Le mur presse itère sur `content/publications/` et n'utilise
`presse_objets` que comme table d'étiquettes avec repli — une publication
nouvelle y entre seule. Le mur livres, lui, itérait sur une **liste écrite à la
main** (`wall_corpus` / `wall_autres`) : un livre hors liste était invisible.

**Règle posée, commune aux deux murs** : *la présence vient du dépôt, l'éditorial
du front matter.* `partials/auteur-wall.html` lit désormais `content/livres/`
(groupé par `serie`, trié par `weight`) ; `wall_lignes` est une table de
surcharges par slug. Conséquences :

- `meta` **se dérive de `pages`** quand il n'est pas écrit — la valeur EN
  d'ANTHROPY (632 p.) n'est plus recopiée à la main, elle vient de sa fiche ;
- une `line` manquante n'efface plus le livre : la tuile s'affiche et le build
  émet `WARN auteur-wall :`. **Testé pour de vrai**, par mutation puis
  restauration du fichier — et le premier test a été un faux négatif : `--quiet`
  étouffe le warning. La CI (`hugo --minify`, sans `--quiet`) le laisse passer.

Les deux checklists, qui ne mentionnaient **ni l'un ni l'autre mur**, portent
maintenant l'étape — c'était la racine documentaire du trou.

### 2026-08-10 — *La Société du premier coup* en vente : vague 2 exécutée, 3e livre du corpus

**Mise en vente KDP le 2026-08-10** — broché `2958634760` (= ISBN-10 de
978-2-9586347-6-6), Kindle `B0H1619K7W`, 138 p., 13,90 € / 5,99 €.

Bascule de la **vague 2** de `docs/ARCHITECTURE_GEO_PREMIER_COUP.md`, préparée en
local depuis le 29/07 et jamais commitée :

- **fiche `/livres/la-societe-du-premier-coup/`** — paratexte écrit (elle n'était
  qu'une coquille : `description`, corps et `faq` vides), liens canoniques `/dp/`
  sur 7 marchés × 2 formats, FAQ book-scoped à 4 questions, `related_awp: awp-08` ;
- **`/premier-coup/` sorti de `draft`** — la **vague 1 n'avait jamais été poussée**,
  alors que l'adresse est **imprimée page 105** d'un livre désormais en vente : le
  compagnon répondait 404 sur une promesse imprimée. C'est le vrai défaut trouvé au
  passage, pas la fiche ;
- **maillage** — `/reversibilite-sociale/` → fiche, AWP-08 (FR+EN) → fiche via
  `related_book`, fiche → compagnon + maille + `/quest-ce-que-lanthropie/`.

**Compteur de corpus 2 → 3 livres** (home FR/EN, `content/livres/_index*.md`,
`static/llms.txt`) : `scripts/check-corpus-counters.py`, étendu au corpus de livres
le 10/08, aurait fait échouer le commit sans ces gestes. Registres synchronisés :
`data/works.yaml` (v1.12, `book-premier-coup`, total_works 38), `data/intent_matrix.yaml`.

**Deux décisions du jour, notées pour ne pas les re-litiger :**

1. **Page ressource offerte : fermée puis ouverte le soir même.** À la publication de
   la fiche, l'entrée du guichet s'activait d'elle-même (mécanisme C8) alors que
   `/stock` ne connaissait pas `premier-coup` : carte « momentanément indisponibles »
   sans stock derrière. Slug retiré. **Le soir, les 10 liens prépayés fournis par
   l'auteur ont été importés** (`gift.py autopilot` : 10 importés, 0 doublon, fichier
   source purgé, 8 poussés sur l'étagère, 2 en réserve ; `premier-coup` ouvert dans
   `open_books`), et les deux surfaces ont été ouvertes : slug remis dans `$order` et
   page propre `/ressources-offertes/la-societe-du-premier-coup/` sortie de draft
   (noindex, hors sitemap et hors RSS, comme ses quatre sœurs).
2. **Arbitrage « ne jamais inscrire ce livre à Select » supprimé** (décision auteur) :
   tous les titres sont en Select, Amazon est la seule place de distribution. La
   consigne traînait dans un bloc déjà marqué `[HISTORIQUE]` de
   `ARBITRAGE_FINAL_RESSOURCES_2026-07-31.md`, dont le § 3 disait déjà l'inverse.

**Correctif de gabarit** : `price` est stocké au format schema.org (point décimal).
Les trois autres livres ayant des prix entiers, l'affichage n'avait jamais eu à
trancher — « 13.90 € » serait parti en production. `layouts/livres/single.html`
affiche désormais la virgule hors anglais, sans toucher au JSON-LD (`"price": "13.90"`).

**Ajout du même jour** : le **sous-titre s'affiche sous le H1** de la fiche livre
(`book-single__subtitle`, idiome des AWP). La carte `/livres/` l'affichait déjà, la
fiche non — pour un livre dont le sous-titre porte l'argument, la surface la plus lue
était celle qui le perdait. Profite aussi à *L'Odyssée des idées* et à *Livresque des
mots* ; ANTHROPIE et *Dette publique* n'ont pas ce champ.

**Restent dus** : item Wikidata + OpenLibrary du livre, stock du guichet (liste en
cours côté auteur), et le relevé `amazon_rating`/`amazon_reviews` quand des avis
existeront (les deux champs absents = pas d'étoiles, anti preuve sociale inversée).
**Dépôt légal BnF** : opération auteur, hors chaîne — bloquant de rien.

### 2026-08-09 — /a-propos/ refondue : Auteur → Presse → Chercheur, deux murs de vignettes (FR + EN)

**Ordre inversé.** La page déployait Chercheur avant Auteur. Nouvel ordre :
Auteur (les 4 livres) → Dans la presse et les revues (les 17 textes) →
Chercheur (AWP) → Contact. Gradient d'accessibilité et gradient de preuve.
**La ligne ORCID · Google Scholar · Zenodo est remontée sous le premier
paragraphe**, indépendamment de l'ordre des sections : ce sont les ancres
d'identité les plus fortes de la page, les enterrer à trois écrans les
affaiblit.

**Mur Auteur** (`partials/auteur-wall.html`) : vignette de couverture +
mention d'édition + une ligne montée en HOOK (loi contre-intuitive) puis
RAISON DE CLIQUER. Titre, URL et vignette viennent de `content/livres/<slug>.md`
via `livres-merged.html` — la fiche native de la langue l'emporte (ANTHROPY sur
le site EN), sinon repli FR avec marqueur « In French ».

**Mur presse** (`partials/presse-wall.html`) : une tuile par texte, l'**objet**
en grand. Constat qui a décidé la forme — en lisant les 17 chapôs, *le thème
est invariant* (le déplacement du coût) ; le réduire à un thème donnerait 17
étiquettes identiques. C'est l'objet qui varie, et il montre l'étendue du cadre
appliqué. Le survol ne porte qu'un **bonus** (le titre complet) : objet et revue
restent lisibles sans souris, donc le mur fonctionne au tactile. Gabarit de
tuile réemployé de `publication-card.html` (`.pub-thumb--logo`, alternance
navy/crème) ; couleur de survol `--color-pivot` (#4A6FA5), le second bleu de la
palette, contraste ≈ 4,9:1 (AA).

**Effet de bord utile** : chaque carte de `/publications/` porte désormais
`id="<slug>"` et un `scroll-margin-top` — **toute recension est adressable en
profondeur** (`/publications/#rfse-lemoine-chasseurs-detats`). Le mur pointe
vers ces ancres : 17 liens internes ajoutés, aucun lien sortant direct.

**Mécanisme d'injection** : le découpage de `.Content` sur `<!-- AWP_LIST -->`
est remplacé par trois shortcodes (`mur-livres`, `mur-presse`, `liste-awp`) —
le marqueur tenait pour une injection, pas pour trois. `layouts/a-propos/list.html`
se réduit à `.Content`.

**Corrigé au passage** : `_components.scss:466` utilisait `rgb(0 0 0 / 18%)`
(bloc `.companion-banner`, travail en cours non commité) — syntaxe refusée par
le compilateur SCSS de Hugo 0.147, **tout `main.scss` cessait de compiler** et
le build CI aurait échoué au push.

**Vérifications** : build FR+EN sans erreur ; jeu de pages généré identique à
`HEAD` (86 fichiers, aucun ajout ni perte, comparé par worktree) ;
`check-corpus-counters.py` = 0 divergence ; `check-geo-coverage.py` = exit 0,
seul signal préexistant `la-societe-du-premier-coup` (livre encore en draft) ;
17 liens du mur ↔ 17 ancres, correspondance exacte, en FR comme en EN.

**Correctif d'affichage (même jour, apres mise en ligne)** : les trois `---` du
markdown dessinaient un second filet horizontal par-dessus celui que
`.home-section h2` porte deja (`border-top`, `_page-common.scss:70`) — trait
double avant chaque section, dans les deux langues. Separateurs retires : le
titre porte seul sa separation, comme sur toutes les autres pages du site. Les
`---` des fiches livres sont conserves : ils y precedent un paragraphe, pas un
`h2`, donc aucun doublon. Second correctif : les `h3` issus du markdown se
rendaient a 18 px serif sans graisse, indiscernables du corps a 16 px ; regle
ajoutee dans `_page-common.scss` en miroir de celle des `h2`, portee a 21 px
(valeur deja en service dans `_ressources-offertes`). `:not([class])` limite la
regle aux titres du markdown — tous les `h3` de gabarit portent une classe.
Perimetre reel constate : `/a-propos/` FR et EN seulement.

**Decision auteur — plus d'annee dans le mur Auteur (2026-08-09)** : le
millesime de l'edition courante compressait une decennie de travail en deux ans
(Livresque 1re ed. 2021 non deposee, L'Odyssee ecrite en 2022, ANTHROPIE mure
sur des annees). J'avais recommande l'intervalle origine -> edition courante ;
l'auteur a propose la suppression pure et simple, qui est le meilleur choix :
elle supprime aussi le probleme de reconciliation. Les registres ne s'accordent
pas — `works.yaml` donne Livresque au 2022-12-20 (edition deposee, pas la 1re)
et commente L'Odyssee « premiere edition 2023 », la ou l'auteur retient 2022
(ecriture) et debut 2024 (mise en ligne). Afficher une de ces annees creait une
divergence visible avec Wikidata, la BnF et Amazon. Le rang d'edition
(« 3e edition », « Nouvelle edition ») porte la duree sans nommer d'annee, et
les dates exactes restent la ou elles font foi : `datePublished` schema.org de
chaque fiche livre (verifie : Livresque 2022-12-20), `works.yaml`, Wikidata.
Effet de bord favorable : la page ne vieillit plus toute seule.
**Reste a arbitrer un jour** : l'ecart entre les annees d'origine reelles et les
annees deposees n'est toujours pas documente dans `works.yaml`.

**Reste ouvert** : les 17 « objets » (FR et EN) sont des brouillons machine à
valider ; la phrase d'intro qui énumérait les médias a été supprimée au profit
du mur — arbitrage GEO non tranché (une énumération en prose s'extrait mieux
qu'une série de tuiles) ; `/en/independent-researcher/` n'existe pas, la
section Researcher EN n'y renvoie donc pas.

### 2026-08-05 — SocArXiv clos pour les conceptuels ; RFSE parue → « Académique » activée ; navette Laura groupée

**SocArXiv — AWP-01 EN refusé une 2e fois (digest OSF du 04/08)** : « does not
meet our criteria for scholarly social science research ». Rapproché du refus
en lot du 14/05 (« Arts & Humanities » + suspicion « reference spamming ») et
de l'acceptation d'AWP-06 (09/05). Décision : **canal clos pour les papiers
conceptuels** — pas de 3e tentative, pas de réponse au modérateur, dépôt
AWP-02 prévu le 06/08 **annulé** (il était conditionné à l'acceptation
d'AWP-01), file d'attente vidée dans `check_deposits_status.py`. AWP-06 reste
en ligne (licence CC-BY 4.0 toujours à poser). Conséquence GEO : la
découvrabilité d'AWP-01 ES repose sur site + Zenodo — le chantier `/es/`
(Pareto point 2 du 03/08) monte en valeur marginale ; aucun dépôt plateforme
à prévoir pour la version ES.

**RFSE 2026/1 (n° 36) en ligne sur Cairn (04/08)** : recension Lemoine,
*Chasseurs d'États*, dans le bloc « Comptes rendus d'ouvrages », pp. 247-265,
DOI commun 10.3917/rfse.036.0247 (7 recenseurs). Fiche
`content/publications/rfse-lemoine-chasseurs-detats.md` créée + `works.yaml`
v1.11. **Décision auteur : option (b)** — catégorie « Académique » activée
(première revue à comité de lecture), Lectures et Revue de la régulation
reclassées (fiches + miroirs works.yaml + table §2 de NOTES_PUBLICATIONS.md).
Le tiré à part Cairn (accès libre jusqu'au 03/09/2026) est réservé à la
diffusion directe — jamais sur le site (lien expirant). `llms.txt` : liste des
supports complétée (Revue Projet manquait — classe « péremption d'état » ; +
RFSE).

**Wikidata — navette Laura groupée** :
`Wikidata/Import_Wikidata_Laura_2026-08-05_ES_RFSE/` (README + deep-link +
bloc de repli). Bloc 1 = ES sur Q139771989, **P953 corrigé vers le concept
21766183** (le batch du 03/08 dans Downloads figeait la v1 21766184, périmée
depuis la v2 — il est remplacé par cette navette). Bloc 2 = création de
l'item « Comptes rendus d'ouvrages » (P1433 Q3428732, P50 Q138909233 rang 4,
P2093 pour les 6 co-recenseurs, DOI/pages/numéro). Pas de P921 (bloc
multi-ouvrages, l'ouvrage recensé n'a pas d'item) ; pas de P973 vers la fiche
site (noindex, corps quasi vide). **Transmission à Laura après push.**

**Exécutée le jour même** : push auteur (`09529b3..3d7241b`, carte RFSE servie
40 s après), navette exécutée par Laura, **item créé Q140892752**, readback
API **23/23 conforme** (P50 rang 4 sourcé, DOI, P1433 Q3428732, 6 P2093,
P953 Cairn). Q139771989 porte désormais label + description ES et le P953
espagnol sur le concept 21766183 — **AWP-01 est trilingue sur Wikidata**.
QID reporté dans `works.yaml` (art-rfse-lemoine-2026, champ `wikidata`).

### 2026-08-03 (fin) — AWP-01 ES **v2 publiée** ; pourquoi on ne supprime pas une v1

**v2 publiée** : `10.5281/zenodo.21775366`. Corrige deux appels de note orphelins
restés dans le corps après la fusion des blocs, dont **le second renvoyait à la
mauvaise note** (la renumérotation avait déplacé la réfutabilité de la position 2
à la 3). Diff : 2 lignes, **0 mot changé**. Trouvé par le manifeste de
conservation, construit le jour même — aucun contrôle antérieur ne pouvait le voir.

**Correction retenue : retirer les appels, pas les renuméroter.** Le PDF français
de référence n'a aucun appel dans le corps ; ses notes sont des notes de fin
flottantes. Fidèle au pivot, et la classe de défaut disparaît par construction.

**Question tranchée : supprimer la v1 et republier sous un autre DOI ?** Non — et
ce n'est pas un arbitrage de goût, c'est indisponible. Vérifié : (1) Zenodo
n'offre au propriétaire qu'un `request_deletion` vers les curateurs, réservé aux
motifs légaux/copyright/données personnelles, pas aux corrections éditoriales ;
(2) **les deux DOI étaient `findable` chez DataCite une seconde après
publication** — donc déjà exposés à OpenAIRE, BASE, CORE, OpenAlex. Le compteur
à 0 téléchargement mesure des clics humains, pas la moisson machine, qui a déjà
eu lieu ; (3) un DOI retiré ne disparaît jamais : il devient une pierre tombale,
et une pierre tombale **se lit comme une rétractation** — le signal le plus
lourd de l'édition académique, pour un renvoi de note. La chaîne v1→v2 est la
vie normale d'un working paper ; le DOI de concept `21766183` résout vers la v2,
donc quiconque cite le concept ne voit jamais la v1.

**Réciprocité recalée** : le record français pointait sur `21766184`, DOI de
**version**, qui fige la v1. Il pointe désormais sur le concept `21766183`.
Règle : **une relation entre œuvres se pose sur le concept, une relation entre
états sur la version.**

**Convention mixte assumée dans `AWPS`** : l'espagnol est suivi par son concept
(il a des versions), les autres par leur recid de version. Migration complète
tentée le même jour, vérifiée sur les 16 records, et **revertée** : le contrôle
de liaison de traduction compare les relations telles que les records les
*déclarent*, et elles pointent vers des DOI de version — le passage au concept
faisait passer 16 records sur 17 en bloquant sans qu'aucun dépôt n'ait changé.
Leçon : **un registre doit parler la même langue que les données qu'il contrôle.**

Audit : **0 bloquant sur 17 records**.

### 2026-08-03 (suite) — AWP-01 ES **PUBLIÉ**, et trois records qui se croyaient en communauté

**Publié sur décision auteur** : `10.5281/zenodo.21766184`, 9 pages, communauté
admise, réciprocité `isSourceOf` posée sur le record français 19266862.
Audit : **0 bloquant sur 17 records**. L'outillage n'a toujours pas de commande
`--publish` — la publication a été faite par appel ponctuel, la doctrine tient.

**Contre-expertise externe reçue avant publication : verdict PDF BLOCKING, et
elle avait raison.** Huit défauts corrigés, dont deux que j'avais manqués et un
que j'avais annoncé corrigé sans l'être :

- `<html lang>` : mon patch avait un `replace(…, 1)` qui a frappé **le
  commentaire explicatif que je venais d'insérer** — il contenait la chaîne en
  exemple — au lieu du code, plus bas. J'avais vérifié la présence du drapeau
  `--lang`, jamais le HTML émis. **Contrôler l'entrée ne vaut pas contrôler la
  sortie** ;
- **double frontmatter** sur trois pages : `extract_body` cherchait « Licence »
  quand l'espagnol écrit « Licencia », et **renvoyait alors la source entière**
  au lieu d'échouer. Un fail-open ; c'est lui qui fabriquait un document
  plausible et faux. Rendu fail-closed ;
- libellés JEL/citation/licence encore français en page 2 ; espace française
  avant les deux-points (`ORCID :`) ; deux appareils de notes concurrents avec
  la note de réfutabilité en double ; notice bibliographique auto-contradictoire ;
  citation hors format de série (d'où la perte de l'italique du titre).

**Trois arbitrages contre l'auditeur, sur preuve** : sa refonte de la page 2 est
**refusée** — la page 2 quasi vide est la maquette de série, vérifiée sur le PDF
français de référence ; son atténuation de « dicen los ingenieros » est
**refusée** — le pivot français porte la même attribution ; son grief « deux
sections Notas » était partiellement un artefact d'extraction, mais **le fond
était juste** et le défaut réel a été corrigé.

**Angle mort de l'auditeur Zenodo corrigé, et il cachait un vrai trou** : le
contrôle de communauté lisait `metadata.communities` du record — c'est-à-dire la
**demande** d'inclusion, pas l'admission. Publier avec ce champ ouvre une requête
que la communauté doit accepter ; tant qu'elle dort, le record n'est dans aucune
communauté mais déclare la sienne, et l'audit passait au vert. **AWP-08 FR et EN
étaient hors communauté depuis leur dépôt du 02/08** — donc invisibles dans la
collection — pendant que l'audit les donnait conformes. Trois demandes acceptées
(AWP-01 ES, AWP-08 FR, AWP-08 EN) ; le contrôle interroge désormais la liste des
membres, seule source qui distingue « a demandé » de « est dedans ». Éprouvé par
corruption : un record hors communauté est bien signalé.

### 2026-08-03 — Ouverture de l'espagnol : chaîne ES et générateur PDF durci

**Chaîne complète exécutée** sur AWP-01 (`0000-TRADUCTIONS ESPAGNOL/AWP-01/`,
hors dépôt) : P0 stabilisation de source → P1 traduction en trois lots →
P2 critique bilingue → P3 relecture native semi-aveugle → fabrication PDF →
brouillon Zenodo **21766184** (DOI préréservé `10.5281/zenodo.21766184`,
`language: spa`, communauté `anthropie-working-papers`, relation
`isDerivedFrom → 10.5281/zenodo.19266862`, PDF attaché, ORCID au record).
**Non publié — la publication reste un geste d'auteur, aucun script ne publie.**

**Après publication, deux actes restent** : ajouter `"es": "21766184"` à `AWPS`
dans `scripts/zenodo_audit_complet.py` (l'auditeur ne voit pas les brouillons —
il porte 0 bloquant sur 16 records publiés, l'espagnol lui est encore invisible),
et poser la réciprocité `isSourceOf` sur le record français 19266862.

**Deux incidents de fabrication à retenir, de même famille** — un dispositif ne
se tait pas parce que tout va bien, il se tait quand il n'a rien pour voir :

1. *Une perte de 290 mots (10,5 % de l'article) n'a violé aucune règle écrite* :
   tous les contrôles du moteur de traduction sont des **détecteurs de présence**,
   aucun ne voit une absence. Cause immédiate : une extraction de source passée
   par `head`. Rattrapée par les deux passes P2, indépendamment. Règle consignée
   dans `stylecards/es_native.md`.
2. *Le générateur PDF était monolingue sans le dire* : sur une source espagnole
   il ne tombait pas en erreur, il sortait dix pages propres à l'œil et fausses
   sur cinq points (césure sous dictionnaire français, étiquettes de front matter,
   affiliation reconnue au mot « Économiste » — d'où **la ligne d'affiliation
   rendue à la place de la date**, police substituée en silence par Times+Cambria,
   flèche `↩` de note web embarquant une quatrième police). Corrigé, éprouvé,
   documenté : `PROCEDURE DE FABRICATION AWP/ARCHIVES/PATCH_2026-08-03_MULTILINGUE_ES.md`.

**Garde-fou ajouté au générateur** (extension de l'étape 8 existante, pas une
couche neuve) : contrôle des polices réellement embarquées dans le PDF **fini**.
Éprouvé par corruption sur les 14 PDF du corpus — 8 conformes, 6 alertes réelles.

**Ce que ce contrôle a révélé, hors mission et non traité** : toute la série
**anglaise publiée** (AWP-01, 02, 03, 04, 07) est composée en Times/Helvetica et
non en EB Garamond, avec des polices **non embarquées** pour quatre records sur
cinq (rendu variable selon le lecteur, hors profils d'archivage PDF/A) ; ces
fichiers ne viennent pas de ce générateur. **AWP-02 FR** embarque DejaVu-Serif à
côté d'EB Garamond (substitution partielle : un glyphe manquant). Records déjà
publiés → reprise = arbitrage d'auteur, consigné ici pour ne pas être
re-découvert dans six mois.

### 2026-08-01/02 — Contrôle visibilité EN, sync registres, arbitrages GEO-01/02/03

**Contrôle GEO EN (01/08, mode IA Google + WebSearch neutre)** : le concept
est VISIBLE en anglais — « The Socioeconomic Hypothesis » (Lalut) en section 2
du mode IA EN sur « anthropy » ; requête conceptuelle sans le mot entièrement
construite sur l'hypothèse ; **SSRN 6543618 n°1 hors personnalisation** (le
dépôt SSRN est devenu le premier actif EN). Nuance auteur : « Anthropy » nue
en navigation privée FR = entités commerciales seules (bataille de fréquence
de corpus — ne se corrige pas on-site). **Verdict : plateau on-site, maillage
auto-génératif par inférence de requêtes REJETÉ** (anti-doorway, moratoire,
non-cannibalisation). Topo : `Downloads/TOPO_GEO_EN_2026-08-01.md`.

**Sync registres avec l'édition anglaise du 21/07 (3 commits)** :
**9d106f2** `works.yaml` v1.10 (bloc `english_edition`, `site_pages.en`,
`abstract_short.en`) + `intent_matrix.yaml` (condition doctrine remplie) ;
**10cb115** `llms.txt` (AWP-08 manquant, « eight », édition EN) ;
**912bf1d** `check-geo-coverage.py` section [5] miroir EN (12/12 ok).
Hors dépôt : `08_ENGLISH_STRATEGY.md` interdit n°1 annoté caduc (ANTHROPIE
seul) ; `12_IMPLEMENTATION_BACKLOG.md` statuts rafraîchis et sourcés (B8/C1/
C2/C4/C6/D1/D4 = faits ; C5 seul incertain ; C7 échéance 24/08) ;
fiche T1 `reports/geo_audit/T1_SONDES_EN_2026-09-15.md` (5 sondes, double
lecture connecté/privé + instrumentation).

**Arbitrage GEO-03 (02/08, investigation externe)** : déploiement France
effectif le **22/07** (AI Mode généralisé, AIO sélectif) — le re-test
« ~23/09 » est fusionné dans T1 15/09. Guide Google màj 10/07 : RAG sur
ranking classique + query fan-out (pas de canal IA séparé) ; « no special
schema.org markup needed » → **gel de tout schema motivé par l'IA** ;
éligibilité snippets = condition d'inclusion (vérifié : 0 nosnippet sur le
site). Search Console : rapports « Search generative AI » + toggle (défaut =
inclus) à surveiller. Attente clics : **−30/−50 % de CTR** sur requêtes
couvertes — piloter aux impressions/absorption, pas aux clics. Recherche
2026 : réécritures « citables » agressives peuvent dégrader le retrieval
(anti-surcouche corroboré) ; viser l'absorption (densité de preuves
extractibles). GEO-01/02/03 : arbitrages rendus, notes closes.

**Rattrapage log — vague « nasse » de juillet (post-09/07, cf. git log)** :
mailles P0/P1 (fd041d7, 1692057), `/communs-negatifs/` (8d9492c),
`/chercheur-independant/` (d5b0e4e), `/livresque/methode-et-corpus/`
(affbc96), **linter `scripts/check-geo-coverage.py`** (318f703), **AWP-08**
FR+EN (04456c9, 23/07), **édition anglaise ANTHROPY** sur le site
(c67176e, 21/07), mailles EN (c2b1623, 1b6ba69), og:image par entité
(f6fb13a, cc43dbe). Wikidata : import fait, état vérifié par API le 01/08
(af4ba03). Obsolètes dans l'entrée du 09/07 : « baseline avant le 23/09 »
(lancement advenu le 22/07) ; T0 requêtes = fait le 09/07.

### 2026-08-02 (suite) — Multilingue : sondes ES/DE, dossier Wikidata, checklist langue

Sondes mode IA : ES = « antropía » occupé par le sens anthropisation, concept
absent ; DE = requête conceptuelle résolue vers **Lessenich /
Externalisierungsgesellschaft** (mêmes trois axes) — gate antériorité OK
(AWP-07 le démarque déjà). Verdict : aucune page ES/DE/JA sans produit ;
levier = entité Wikidata. Dossier de contre-expertise
`Downloads/WIKIDATA_LANGUES_Q138827949_2026-08-02.md` (corrections ES/DE/IT
dont dérive « mécanisme »→« hypothèse », ajouts it/pt/ja/zh/ru + ar/ko
recommandés ; import via Laura après arbitrage auteur). **Édition ES
d'ANTHROPIE annoncée par l'auteur (semaines à venir)** →
`docs/CHECKLIST_AJOUT_LANGUE.md` créée (séquence entité → produit → dépôt
tiers → surfaces → mesure, codifie le playbook EN ; contre-analyse GEO-04).

**Contre-expertise externe (ChatGPT) intégrée le 02/08** — verdicts amendés
et actés : moratoire on-site devient CONDITIONNEL (pages dérivées de
requêtes interdites ; nouvelle page = objet autonome + besoin observé +
lacune réelle) ; déclencheur langue assoupli (« actif public vérifiable »,
3 états privé/pré-ancrage/déploiement — checklist amendée) ; sur-affirmation
« SSRN n°1 mondial » corrigée (résultat daté/localisé, réplication sous
contrôle) ; « chaque langue a son Kapp » → chaque COMMUNAUTÉ intellectuelle
(ES : entrer par externalización de costes puis economía ecológica, CEPAL en
voisin, jamais en filiation) ; Wikidata GO RESTREINT (corrections ES/DE/IT,
labels latins par défaut ja/zh/ru/pt, AR/KO suspendus — addendum du dossier
Downloads) ; règle complétée « l'état interne suit l'acte, l'état externe
expire » (CLAUDE.md). **DÉCOUVERTE VÉRIFIÉE : collision de concept avec
anthropie.org** (« L'Anthropie », édifice 12 couches, anonyme, CC0, GitHub
créé 29/04/2026, 0 star, empreinte recherche quasi nulle au 02/08) →
`reports/geo_audit/REGISTRE_COLLISIONS.md` créé (9 entrées), sonde S6 de
veille ajoutée au T1, signature composée adoptée (« Anthropie — l'hypothèse
du déplacement du désordre, formulée par Stéphane Lalut »). Grille de
reprise en 4 niveaux (hébergement/mention/citation/application) intégrée
au T1 — les mesures d'août prouvent la récupération machine, pas encore
l'usage autonome par des tiers : c'est l'objectif des échéances 24/08+.

### 2026-07-09 — Rounds GEO-03/GEO-04 : indexation réparée, site-graphe ancré, lot 1 exécuté

Missions `_Consignes_GEO-03/04/05.txt` (audits + GO auteur item par item).

**GEO-03 (commis le 09/07, poussé sur GO)** : `fix(indexnow)` **2f3dae2** — le
workflow soumettait les **2 sitemaps XML** au lieu des pages depuis le passage
multilingue (la racine est un sitemapindex, IndexNow n'expanse pas) ; récursion
+ garde-fou <10 URLs = échec explicite. `docs(geo)` **d1785c6** checklists
ajout livre/publication. `fix(seo)` **b250cdf** aliases
`/en/what-is-anthropy/` (+ racine) — répare le **backlink Wikidata Q138827949
P973** qui pointait un 404 depuis mai. ⚠ push bloqué : les jetons git/gh
n'ont pas le scope `workflow` — `gh auth refresh -s workflow` requis.

**GEO-04 (doctrine)** : `data/intent_matrix.yaml` (matrice d'intentions 5
cercles, statuts, en-tête anti-doorway dur — AUCUNE page ne se crée depuis ce
fichier), `docs/CHECKLIST_AJOUT_CONCEPT.md`, hooks checklists (**1098329**).
Décision d'architecture : works.yaml reste le registre canonique unique —
aucun des 10 fichiers YAML parallèles suggérés n'est créé. Rapport complet :
`reports/geo_audit/GEO04_KNOWLEDGE_GRAPH_PROPAGATION.md` (local, gitignoré).

**Lot 1 site-graphe (GO _Consignes_GEO-05, 6 commits atomiques)** :
① **1b73852** nœud `DefinedTerm #concept` émis sur la page concept FR+EN —
le sommet était référencé par AWP/livres/série mais défini nulle part ;
② **6cc3beb** FAQ rendues sur les 4 fiches livres (book-scoped strict : la
question « qui paie la dette publique ? » reste la propriété exclusive de la
page pont) + `schema-faqpage` résout les placeholders `{citations}` via
desc-figures ; ③ **4aeb00c** chiffres canoniques page offrir via source
unique (shortcode stat : fallback `stats_isbn` + séparateur nommé `nbsp`) ;
④ **750c7d3** bloc « Du même auteur » (BEM `.book-others`) ; ⑤ **5f76680**
EN : « Order here. Debt elsewhere. » + « a quotation anthology in the
lineage of the commonplace book » sur /en/books/ ; ⑥ **a387298** fraîcheur
légère : `lastmod` manuel aux dates git réelles (concept, AWP-01/02/05/06,
fiches livres) + `dateModified` JSON-LD conditionnel (`ne .Lastmod .Date`).
**Jamais `enableGitInfo`** (checkout CI shallow = fake-freshness globale).
⑦ BreadcrumbList **différé** (bénéfice quasi nul à 2 niveaux, décision auteur).

Restent (hors dépôt ou à la demande) : run manuel IndexNow post-push (lire le
nombre d'URLs au log), baseline GoatCounter clics amazon-outbound avant le
23/09 (lancement AI Overviews France), T0 requêtes Google FR distinct des 18
prompts assistants, item Wikidata Livresque à créer, lecture intent_matrix
par la routine GEO trimestrielle (arbitrage auteur).

### 2026-07-04 — MODIFICATION DURABLE DE LA RÈGLE : levée anticipée du gel structurel

Décision explicite de l'auteur (session GEO du 04/07) : le gel structurel 90 j
(échéance initiale ~2026-08-12) est **levé de manière anticipée et la règle est
modifiée durablement**. Nouveau régime :

- les interventions sur le site se font **à la demande de l'auteur**, validées
  par diff avant commit (méthodologie inchangée) — plus de fenêtre calendaire ;
- la doctrine de fond demeure : **diffusion > optimisation**, conversion par
  autorité, pas de contenu creux, quota de pages maîtrisé, protocole de mesure
  (`reports/geo_audit/GEO_PROTOCOLE_MESURE.md`) inchangé ;
- conséquence immédiate : la « rafale » planifiée pour le 12-26 août est
  **publiée ce jour** (2 pages-ponts + 2 pages offrir + GoatCounter events).

Contexte : audit GEO complet + méta-analyse croisée du 04/07 (13 + 8 livrables,
`reports/geo_audit/` et `reports/geo_authority_conversion_audit/`), 16 commits
de phase 1/1-bis/GEO-01/QEA déployés le même jour, passe Zenodo (verbatim +
dates) exécutée, dossier Wikidata prêt pour import.

### 2026-06-15 — Clôture du journal post-90j de l'audit GEO (harmonisation définition + DOI AWP-05)

Round demandé par l'auteur : « faire toutes les améliorations nécessaires pour
améliorer la visibilité GEO », sur la base de `audits/diagnostic-2026-05-23.md`.
Gel 90 j **explicitement levé** pour ces items (la worklist GEO différée du
journal post-90j *est* l'objet de la demande). Périmètre **non structurel** :
routing, hreflang, sitemap, canonical, JSON-LD machine = intacts ; seuls du
contenu/wording et un DOI de citation sont touchés.

**Re-audit read-only préalable (clé) :** l'audit du 23/05 (`c8a44a3`) était
largement périmé. **5 des 7 items du journal avaient déjà été traités** entre
`c8a44a3` et `fd9c353` : distinction Anthropocène (page concept), 9ᵉ `sameAs`
SocArXiv (`data/author.toml`), sous-titre AWP-06 propagé en `citation_title`/
`headline`, `about=Anthropie` conditionné à `serie != autres-ouvrages`
(`livres/single.html:77`), `ItemList` sur `/livres/` (`livres/list.html`).
Seuls 2 chantiers restaient réellement ouverts.

**Correctifs appliqués (2 commits atomiques) :**

- **`feat(geo)` `e6c6b8a`** — single-source du **verbatim** de la définition
  canonique (`canonicalDefinition` de `params.toml`/`hugo.toml`) sur les
  surfaces à plus forte autorité : accueil FR (`layouts/index.html:19`, 1ʳᵉ
  phrase du lede alignée sur le verbatim, nuance spatial/temporel/social
  conservée, symétrie avec le lede EN déjà canonique) ; AWP-01 FR+EN et AWP-06
  FR via `{{< canonical-definition >}}` en ouverture (paraphrase rétrogradée
  en « Plus précisément / More precisely »). AWP-06 EN inchangé (verbatim déjà
  en incise). Drafts `audits/phase2-drafts/` marqués appliqués. Closes l'item
  n°1 (priorité GEO du journal). Build OK, verbatim rendu vérifié sur 4 surfaces.

- **`content(awp)` `53c1c65`** — uniformisation du DOI exposé d'**AWP-05**
  (seul des 6 à exposer son **concept** DOI `…19269486` au lieu du **version**
  DOI `…19269487` de son `pdf_url` et des 5 autres). Aligné sur la convention
  « version DOI » du 29/05 — sens qui *rentre* dans la convention, jamais
  l'inverse (bascule version→concept toujours interdite). `awp-05.md`
  (doi_zenodo + url_zenodo) et `awp-05.en.md` (translation.doi cross-link).
  Version DOI vérifiée via `api.zenodo.org`. Closes l'item n°3.

**Journal post-90j de `audits/diagnostic-2026-05-23.md` : intégralement clos**
(5 items déjà faits + 2 ce jour). Reprise du gel jusqu'à l'échéance
~2026-08-12. Les indicateurs externes du § 6 de l'audit restent à surveiller
sans intervention (OpenAlex, téléchargements Zenodo, AI Performance).

### 2026-06-04/05 — Liens Amazon canoniques + purge anthropie.fr (correctif bloquant hors-gel)

Round `_Commandes-158` (audit READ_ONLY puis patch sur GO explicite). Deux défauts
bloquants avérés corrigés, gel 90 j respecté (même classe que l'intervention du 29/05).

- **`fix(livres)` `4341fd7`** : les 21 liens Amazon des 3 fiches livres étaient des
  **shorteners** (`amzn.eu/d/…`, `a.co/…`) avec **collisions avérées** (Dette DE/IT
  pointaient le shortener d'un autre livre ; Livresque CA = lien FR). Remplacés par
  les **URL canoniques `/dp/<ASIN>`** + **boutons séparés Broché / Kindle par marché**
  (`url_amazon_<mkt>` / `url_amazon_<mkt>_kindle`, partial `amazon-button.html`).
  L'`Offer.url` du JSON-LD devient canonique. ASIN vérifiés contre les données de
  compte KDP ; **vérifié en production** : 0 shortener, 5/5 liens échantillonnés
  résolvent vers le bon livre (dont les ex-collisions .it/.ca et les Kindle .es).
  Prérequis posé pour les tags **Amazon Attribution** (câblage prévu septembre 2026).
- **`docs` `c2a77a2`** : purge des mentions « site pour anthropie.fr »
  (CLAUDE.md/AGENTS.md/README → stephane-lalut.com). **Dossier domaine CLOS** :
  anthropie.fr n'a jamais été détenu (aftermarket Premium GoDaddy) — aucun rachat,
  aucune redirection. La production n'émettait aucune référence (vérifié :
  sitemap/canonical/llms.txt = 0 hit). Les mentions historiques exactes
  (§ correctif `/presse/` ci-dessous, docs/memo) sont conservées.

### 2026-05-29 — Audit GEO/SEO/sécurité + 4 correctifs ciblés (intervention hors-gel, non structurelle)

Audit read-only en 5 lots (GEO/IA, maillage, SEO, performance, sécurité) demandé par l'auteur. Verdict : **0 défaut bloquant** ; le gel 90 jours n'est donc pas rompu sur le fond. 4 commits atomiques appliqués sur des défauts *utiles* (non structurels) — routing, JSON-LD, `citation_*`, hreflang, canonical : **intacts**.

**Correctifs (commits `0e4d026`, `60b1db8`, `75920d9`, `44fb770`) :**

- **`/presse/`** (`fix(seo)`) : page orpheline (0 lien entrant), indexable et au sitemap, au contenu vacant et à l'e-mail `contact@anthropie.fr` **non délivrable** (domaine `anthropie.fr` sans enregistrement MX, vérifié par DNS ; le domaine vivant est `stephane-lalut.com`/OVH). Passée en `noindex` + sortie du sitemap (`_build.list: never`, `render: always`). **Mécanisme `noindex` créé** dans `head.html` (flag front matter `noindex: true` → `<meta name="robots" content="noindex, follow">`) — n'existait nulle part auparavant. E-mail mort remplacé par un lien vers `/contact/` (formulaire Formspree). *Étape B à la main de l'auteur : remplir le kit presse, retirer les 2 blocs front matter, ajouter le lien colonne « Ressources » du footer.*

- **`scripts/audit_works.py`** (`fix(audit)`) : faux positifs `citation_*`. `hugo --minify` retire les guillemets d'attribut (`name=citation_title`) que la regex exigeait → 12 pages AWP conformes signalées à tort. Les 11 balises `citation_*` + le JSON-LD ScholarlyArticle sont bien présents (vérifié sur le live). Warnings : **18 → 6** (reste = DOI SSRN externes, attendus).

- **CI** (`fix(ci)` + `chore(ci)`) : actions GitHub épinglées au **SHA** (étaient en tag mutable `@v4/@v3/@v7`) sur les 6 workflows, SHA résolus via l'API GitHub — durcissement supply-chain (reco OpenSSF, post-incident *tj-actions* 2025) sur des workflows à droits `pages:write`/`id-token:write`/`contents:write`. À rafraîchir au J+90 (rappel déjà outillé). Healthcheck mensuel : 403 anti-bot Academia rendu non bloquant (évite un faux positif/issue chaque mois) + casse URL alignée sur `author.toml`.

**Laissés volontairement (test de suppression) :** subsetting polices, image LCP home en CDN Amazon, CSP `<meta>`, bascule DOI version→concept. Sur ce dernier point : les DOIs Zenodo exposés sont les **DOI de version** (ex. AWP-01 …862) ; le DOI concept (…861) existe à −1 et résout aussi — **ne pas « corriger » version→concept** sans décision éditoriale (casserait l'historique Scholar). Vérifié via `api.zenodo.org`.

**Modifications structurelles : aucune.** Seul le sitemap perd `/presse/` (page non stratégique). Reprise du gel après ces commits.

### 2026-05-12 — Chaîne de boucles sur la home (4e patch, conclusion alignement AWP-06)

Quatrième et dernier commit de la fenêtre éditoriale d'alignement avec AWP-06 et la campagne de diffusion S9-S10 2026. Ajout d'une animation SVG cyclique (24 s desktop / 30 s mobile) qui suit littéralement le contour des cercles externes Spatial et Social sur la home, avec croisement en X au centre du cercle Temporel — overlay décoratif en background derrière les cercles HTML existants.

**Justification doctrinale :** cohérence de grammaire visuelle (boucle anthropique) avec la page théorique, différenciation par le rythme (24 s desktop / 30 s mobile vs 16 s page théorique) et par la composition (4 lignes droites tangentes + 2 grands arcs contournant les sphères externes, croisement Temporel en X — vs lemniscate asymétrique simple en page théorique). Chaque page doit signifier seule pour des publics multiples (chercheurs, journalistes, éditeurs) qui ne suivent pas un parcours linéaire.

**Périmètre :**

- Assets : `static/img/figures/chaine-boucles-desktop.svg` (viewBox 1000×543, path `M…L…A…L…L…A…L…Z`, N=2295, K=1148) et `chaine-boucles-mobile.svg` (viewBox 360×900, path L+A équivalent vertical, N=2172, K=1086). Animation SMIL `stroke-dashoffset` + comet `animateMotion` synchronisés (K = N/2 exact). `prefers-reduced-motion` respecté sur les 2 SVG. Pas de texte dans les SVG (les textes des trois axes restent en HTML pour SEO et accessibilité).
- Partial nouveau : `layouts/partials/figures/chaine-boucles.html`, bascule responsive via `<picture><source media="(max-width:768px)">`, `aria-hidden="true"` (overlay décoratif).
- SCSS composant nouveau : `assets/scss/_figure-chaine-boucles.scss`. Desktop : `position:absolute; top:-135px; height:540px` (débord vertical pour arcs dépassant la rangée des sphères, total 540px = 270 sphères + 135 haut + 135 bas). Mobile (`@media max-width:768px`) : `height:auto; bottom:0` (overlay couvrant l'ensemble du triad-wrapper). Importé après `figure-boucle-anthropique` dans `main.scss`.
- Intégration home (`layouts/index.html`) : ajout d'un wrapper `.axes-overlay-wrapper` autour de la grille `.axis-grid` existante. `.axis-grid` reçoit `position:relative; z-index:1` (additif, les cercles HTML passent devant l'overlay z-index:0). Aucune modification du markup ni des textes des trois cercles.

**Modifications structurelles : aucune.** Routing, JSON-LD, `citation_*`, schema.org, hreflang, sitemap, canonical : intacts. Cercles HTML et leurs textes (Spatial / Temporel / Social, directions, body) : intacts.

**Reprise du gel :** dernière intervention de la fenêtre d'alignement AWP-06. Le gel 90 jours reprend strictement après ce commit. Échéance approximative : 2026-08-12. Aucune intervention non bloquante prévue d'ici là.

### 2026-05-12 — Boucle anthropique : home + page théorique (alignement AWP-06)

Le gel 90 jours initié au commit 3975b24 (mai 2026) est interrompu pour une intervention éditoriale ciblée, explicitement validée par l'auteur, dont l'objectif est l'alignement du site avec AWP-06 avant la campagne de diffusion académique septembre-octobre 2026.

**Périmètre exact :**

- Home (`layouts/index.html`) : ajout d'un bloc texte « Une frontière contemporaine — L'attention comme réceptacle » sous la section des trois axes, avec lien sortant vers AWP-06 (`{{ "/awp/awp-06/" | relLangURL }}`). Bilingue FR + EN inline. Aucune illustration ajoutée sur la home.
- Page « Qu'est-ce que l'anthropie ? » (FR `content/quest-ce-que-lanthropie/_index.md` + EN `_index.en.md`) : ajout d'un paragraphe théorique (extériorisation cognitive + retour anthropique) inséré entre la section des trois axes et la section « Anthropie et entropie », suivi de la figure « La boucle anthropique » via shortcode.
- Assets SVG nouveaux (4) dans `static/img/figures/` : variantes FR par défaut + variantes `-en`, `boucle-anthropique-desktop[-en].svg` (lemniscate horizontale animée SMIL, viewBox 900×440) et `boucle-anthropique-mobile[-en].svg` (lemniscate verticale animée SMIL, viewBox 360×720). Comète + queue à 7 niveaux d'opacité sur les 4. `prefers-reduced-motion` respecté sur les 4.
- Partial nouveau bilingue : `layouts/partials/figures/boucle-anthropique.html`, double bascule langue (`.Lang`) + viewport (`<picture><source media="(max-width:768px)">`).
- Shortcode markdown nouveau : `layouts/shortcodes/boucle-anthropique.html` wrappant le partial avec contexte `.Page`.
- Composant SCSS nouveau : `assets/scss/_figure-boucle-anthropique.scss`, figure alignée sur la largeur du gabarit texte en desktop, full-bleed en mobile (`@media (max-width: 768px)`), caption serif italique plafonnée à 720 px. Importé après `page-common` dans `main.scss`.
- Bloc home « frontière contemporaine » : règles SCSS ajoutées dans `_home.scss` section 2 bis (tokens existants `--font-sans/serif`, `--fs-micro/h2/body/small`, `--color-text-*`, `--color-accent[-hover]` ; pas de nouveaux tokens introduits).

**Modifications structurelles : aucune.** Routing, JSON-LD, métadonnées `citation_*`, schema.org, hreflang, sitemap, balises canonical : intacts. Aucune classe BEM existante modifiée hors `_home.scss`.

**AWP : aucun modifié.** Le concept de boucle techno-cognitive introduit ici est inscrit dans le livre ANTHROPIE (622 p., ISBN 978-2-9586347-2-8) et préparé dans AWP-02 (migration des modalités vers le temporel et le cognitif) et AWP-06 (quatre registres couplés énergie/matière/territoire/attention). Un AWP-07 dédié pourra formaliser le concept lors d'une campagne de diffusion ultérieure distincte.

**Reprise du gel :** la phase GEO/diffusion reprend après ce commit. Aucune autre intervention non bloquante prévue avant la fin de la fenêtre 90 jours (échéance approximative ~2026-08-12).

## 1. État de phase

**Depuis le 2026-07-04** : le gel calendaire est levé (voir log § 0) — le site
est en régime « interventions à la demande, validées par diff », avec pour
priorité d'énergie la **diffusion** (campagne académique, AWP-07, nœuds
externes), pas l'optimisation on-site.

*(Historique : phase active GEO/diffusion 90 jours de mai à juillet 2026 ;
la phase de construction infrastructurelle initiale est close.)*

L'audit de bascule a livré le verdict OUI sans correction obligatoire.
Les 3 recommandations triviales (R1+R2+R3) ont été appliquées dans 
un mini-commit polish.

## 2. Architecture finale (état au commit polish)

### Source unique de vérité
- `data/author.toml` : 8 identifiants sameAs (ORCID, Zenodo community, 
  OpenAlex, Google Scholar, Academia, Wikidata, SSRN, IdRef)
- Consommé par 9 surfaces (5 JSON-LD machine + 4 visibles humain)
- 0 ORCID hardcodé dans `layouts/` ni `config/`

### Identité auteur
- Statut unifié : "Économiste — Chercheur indépendant et essayiste"
- Bilinguisme JSON-LD Person + eyebrow accueil (FR/EN selon `.Lang`)
- Cohérence sur 16 positions du site

### Vignettes /publications/
- Tout le corpus (10 fiches) en bloc typographique
- Alternance navy/crème stricte par compteur logoIndex
- Champ `source_type` : 5 catégories (Revue, Magazine, Quotidien, 
  Journal, Portail) + Académique réservée

### Pattern technique critique
- Schema.org : toujours `dict→jsonify→safeJS`, jamais de concaténation
- BEM SCSS : sélecteurs descendants explicites depuis modifier 
  (jamais `&__xxx` qui produit `.parent--mod__xxx`)

## 3. Wikidata Q138909233

7 P-propriétés renseignées par Laura :
- P269 IdRef ID : 283054085
- P1960 Google Scholar : J4NqzwSfrHAC
- P10283 OpenAlex ID : A5130851063
- P496 ORCID iD : 0009-0002-1794-4895
- P3781 SSRN author ID : 11065608
- P5023 Academia.edu profile URL
- P9934 Zenodo communities ID : anthropie-working-papers

Note : la communauté Zenodo `anthropie-working-papers` est 
**rattachée au Concept Q138827949** (anthropy), pas au Person. 
Sémantiquement plus juste : c'est une communauté de concept, 
pas d'auteur.

## 4. Doctrine éditoriale

### Identifiants visibles humains
- Surfaces sobres (footer, credibility-strip) : labels courts 
  (ORCID, Google Scholar, Zenodo)
- Surfaces académiques (badge AWP, meta-strip série) : labelLong 
  ("ORCID 0009-0002-1794-4895") ou logo image SVG
- Pages individuelles AWP : badge image SVG (convention preprints)

### Statut auteur dans le contenu
- Énumérations narratives : "économiste, chercheur indépendant 
  et essayiste"
- AWP-05 : 2 occurrences génériques de "chercheur indépendant" 
  préservées (emploi catégoriel, non auto-référentiel)

## 5. Chantiers en cours (90 jours)

### Phase 1 — Diffusion académique ciblée
- Plan de citations internes pour AWP-06 + template mail chercheurs
- 15-20 cibles francophones/anglophones identifiées
- Vagues 3-5 mails/semaine maximum
- Suivi signaux externes : citations Scholar, backlinks .edu, 
  reprises, mentions

### Phase 2 — Pages-ponts (limitées)
- 2-3 pages-ponts maximum sur 90 jours
- Créées en réaction aux signaux externes (ex. si chercheur 
  demande positionnement vs Polanyi → page Polanyi)
- Format : nœuds de graphe 900-1500 mots, pas articles longs

### Phase 3 — Chantier édition (post-90j)
- Ouvrira après premiers retours diffusion
- Préparation troisième livre lié au cadre anthropique
- Site déjà testé comme tremplin éditorial réplicable

## 6. Chantiers reportés / à activer si signal

- **Catégorie "Académique"** dans NOTES_PUBLICATIONS.md : à activer 
  quand une vraie revue peer-reviewed publie une fiche 
  (ex. Droit et Société). Décision : reclasser ou non Lectures 
  et Revue de la régulation rétroactivement.
- **isIdenticalTo SSRN** sur AWP-02/03/04/05 EN : action externe 
  en attente d'APPROVED SSRN. Script `scripts/zenodo_add_ssrn_links.py` 
  prêt à relancer.
- **Densification Wikidata** des 4 items existants (claims < 8) : 
  impact GEO fort mais hors site lui-même. Via Laura.
- **knowsAbout EN** dans data/author.toml : actuellement français 
  unique. Néologisme "anthropie" volontaire en français. Marginal.
- **Refactor description/canonicalDefinition** doublons entre 
  params.toml et hugo.toml [params] : nettoyage cosmétique, 
  hors enjeu.

## 7. Méta-règles d'engagement

### Discipline pendant les 90 jours
- Pas de retour structurel sur le site sauf défaut bloquant
- Énergie transférée vers diffusion, pas captée par optimisation
- Pages-ponts en réaction à signaux externes, pas en anticipation
- Si tentation de revenir au code : relire la phrase de pilotage

### Phrase de pilotage
> "Le site est suffisamment robuste ; la prochaine preuve ne 
> viendra plus du code, mais des tiers."

### Anti-pattern à éviter
- Multiplier les sessions techniques pendant les 90 jours
- Créer 10+ pages-ponts d'un coup (dilution conceptuelle)
- Confondre GEO architecture avec diffusion réelle
- Chercher une nouvelle validation infrastructurelle après chaque 
  arbitrage

## 8. Référence aux fichiers de doctrine spécialisés

- `NOTES_PUBLICATIONS.md` : règles publications (front matter, 
  taxonomie source_type, règle d'or SCSS BEM)
- `data/author.toml` : source unique identité auteur

---

*Ce fichier est versionné dans le repo. Toute évolution majeure 
(fin des 90 jours, ouverture chantier édition, refactor structurel)
doit faire l'objet d'une mise à jour explicite avec préfixe 
`docs:` dans le message de commit.*
