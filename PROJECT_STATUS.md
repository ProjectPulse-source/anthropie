# Project Status — stephane-lalut.com

## Bilan 2026-05-13 — Chantier diffusion clos

Synthèse des 4 axes de diffusion exécutés en mai 2026 ; le chantier est désormais clos pour la durée de la fenêtre GEO/diffusion 90 jours.

1. **Wikidata** : Phase A + B + C exécutées (lots `Lalut-Anthropie-PhaseA/B/C-2026-05-12/13`). 6 items AWP créés (`Q139771989` à `Q139771994`). Correction DOI Option B effectuée (12 suppressions manuelles). Script Python d'automatisation v1.0 dans `Wikidata/scripts/` (fetchers Zenodo/Crossref/OpenLibrary + generators awp/article/book + validators garde-fous P9934/P407).

2. **SocArXiv** : 6 AWPs déposés sur `osf.io/ymkpj`. DOIs SocArXiv liés en P953 sur les 6 items AWP Wikidata. Profil OSF `ymkpj` rattaché à `Q138909233` (Stéphane Lalut) via P973.

3. **OpenLibrary** : 6 fiches livre + page auteur enrichie. Author ID `OL16378291A` (doublon `OL16378292A` fusionné par OL le 26/08/2026). Work IDs canoniques **au 26/08/2026** : Livresque `OL45424544W`, L'Odyssée `OL45424562W`, ANTHROPIE **`OL45424564W`**, Dette Publique **`OL45424599W`**, Premier coup `OL45876839W` — OL a fusionné les 3 paires d'œuvres en gardant, pour ANTHROPIE et Dette Publique, l'inverse de ce que Wikidata pointait (`OL45424565W` et `OL45424600W` sont devenus des redirections). **P648 corrigé des deux côtés**, vérifié à la source le 28/08/2026 (`Q138827344` → `OL45424564W`, `Q138910896` → `OL45424599W`). ASIN broché posé en identifiant `amazon` sur les 6 éditions canoniques, liens URL Amazon retirés des works (remarque OL). **Soldé par OL le 01/09/2026** (ticket Zendesk 1605786) : les 3 paires d'éditions au même ISBN (`OL61896251M/252M`, `OL61896276M/277M`, `OL61896316M/317M`) ont été **supprimées et non fusionnées** — OL ne sait pas fusionner des éditions, un doublon d'édition se demande donc en *suppression* ; les liens d'autorité sont passés en `remote_ids` sur la fiche auteur (`wikidata` / `viaf` / `goodreads`, révision 4, vérifiée à la source le 03/09), et le 403 d'août était un **faux positif** du durcissement de sécurité OL, non intentionnel. **Reste ouvert au 09/09/2026, revérifié à la source ce jour** : `OL45424565W` est un `/type/redirect` vers `OL45424564W` dans la donnée depuis le 26/08 (14:21 UTC), mais **subsiste dans l'index Solr** — `search.json?q=author_key:OL16378291A` rend `numFound = 6` dont ce work à **0 édition**, et la page auteur publique affiche « 6 works ». Les deux redirections sœurs de la même fusion (`OL45424600W`, `OL45424545W`) sont, elles, correctement désindexées (`numFound = 0`) : **un seul réindex manqué, pas un comportement normal de redirection**. Réindexation demandée le 03/09, **non traitée dans la réponse OL du 07/09**. Statut *Librarian-In-Training* (candidature du 22/08) : toujours pas accordé — OL répond le 07/09 que les candidatures sont revues « as time allows ».

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
> Dernière mise à jour : 2026-09-13.
> **Règle de fraîcheur** : l'état écrit suit l'acte — toute session qui
> exécute met à jour ce log ET les statuts des registres/backlogs touchés
> dans la même session. Un statut périmé vaut défaut : il provoque la
> re-exécution de l'acquis ou l'abandon de travaux crus « déjà faits ».

## 0. Log chronologique

### 2026-09-21 — Bloc « Réutiliser » : composant à cartes, source unique des figures

**Motif.** Contre-expertise sur les maquettes A/B/C (`PRO-20260921-MAQUETTES-REUTILISER`, pièce
entrée hors navette, arbitrée) : les six fichiers se cachaient dans des parenthèses. Variante A+
retenue.

**Source unique.** `update_dette_insee.py` écrit `data/figures_dette.json` (titre, « ce que
montre », source et période, précaution, fichiers ; FR et EN). La précaution y est la même phrase
que dans le cartouche de l'image : une seule définition, dans `LABELS_CARTOUCHE`. Fichier séparé
du jeu public, dont l'empreinte décide de la date de relevé.

**Composant.** `{{< reutiliser >}}` : une carte par figure, précaution en évidence, PNG en action
principale ; citation au format du site, résumé en trois phrases, données. Taille et ratio des
vignettes lus dans les SVG réels. Aucune ligne de JavaScript nouvelle (`copy-citation.js`) ni de
style de bouton nouveau (`how-to-cite__btn`). `{{< reutiliser-ancre >}}` en tête de page et
`{{< fig-actions >}}` sous chaque figure du corps. JSON-LD : figures en `ImageObject` avec licence.

**À retenir pour les captures.** Le HTML référence son CSS par une URL absolue de production : une
capture sur `hugo server` affiche la page avec le CSS **en ligne**, donc sans les styles non encore
poussés. Construire avec `--baseURL http://127.0.0.1:<port>/` dans un dossier temporaire et le
servir tel quel.

### 2026-09-21 — Page dette : figures citables, droits par type, résumé repris

**Motif.** Contre-expertise `PRO-20260921-064850` (arbitrage archivé) : la page est
transmise comme ressource, mais elle sollicitait l'achat avant d'exposer sa méthode, sa
licence n'apparaissait qu'une fois en fin de page, et ses figures circulaient **nues** —
aucune ne portait sa source, son millésime ni sa précaution.

**Figures.** `update_dette_insee.py` pose désormais un cartouche de trois lignes au pied
des six SVG (source + millésime, précaution de lecture, licence + URL). Le cadre gagne
48 px ; les `height` des `<img>` ont suivi dans les deux pages et dans
`partials/dette-chiffres.html`, faute de quoi le ratio annoncé au navigateur mentirait.
La longueur des lignes n'a pas été estimée : **mesurée au rendu** — la première version, en
deux lignes, sortait du cadre sans rien casser.

**PNG.** Option `--png` : six PNG à 1440 px dérivés des SVG. **Rendus par la CI** depuis
ce jour, par une étape délibérément non bloquante — l'installation de la bibliothèque de
rendu porte `continue-on-error`, et `rendre_png()` ne lève jamais : si elle échoue, le
script le dit, poursuit, et les *données* sont publiées quand même. Faire dépendre la mise
à jour des chiffres d'une bibliothèque d'images suspendrait l'essentiel à l'accessoire.

Le premier arbitrage excluait ce chaînage ; il était trop binaire — GitHub Actions isole
une étape. Deux vérifications l'ont ouvert : le rendu simulé avec la police de repli d'un
runner Linux (DejaVu Sans, sensiblement plus large) montre que le cartouche tient ; et
l'isolation était déjà dans le code.

Cette tolérance a un prix, et c'est lui que garde `scripts/check-png-dette.py` : une
installation qui échoue publierait des SVG neufs à côté de PNG anciens, sans erreur.
Empreinte du SVG source, branché dans `check-all.py` hors `--ci` — un PNG périmé ne doit
pas bloquer le déploiement du site. Témoin vérifié dans les deux sens (0 → 1 → 0).
Condition de mort réécrite : il disparaît le jour où le rendu ne peut plus échouer
séparément de la publication des données.

La garde de cohérence du script (« toute sortie doit figurer dans le `git add` du
workflow ») est étendue aux PNG et au manifeste : un quatrième graphique ajouté demain
aurait sinon un PNG régénéré en CI et jamais publié. Témoin par mutation réelle du
workflow (1 → 0).

**Constaté en production le même jour** (run `35578048777`, déclenchement manuel) : étape de rendu verte, six PNG rendus et committés par la CI (`ff6c721`), SVG et données inchangés. Le PNG rendu sur le runner a été **regardé** : police de repli réelle, cartouche intact. Désormais la CI est la source des PNG — un `--png` local produirait un rendu différent (autre police) pour un contenu identique.

**Pages.** Bloc « Réutiliser cette page » : droits énoncés **par type** — données, graphiques,
texte — au point de téléchargement, plus trois phrases citables (question, apport, limite).
L'appel au livre est passé après la section méthodologique.

### 2026-09-19 — Ressources offertes : phrase de transmission, « relais » retiré, note Amazon datée

**Demande de l'auteur.** Zone de transmission de `/ressources-offertes/` et des cinq pages par livre :
« Vous pensez qu'un proche, un collègue ou un lecteur de votre connaissance pourrait être intéressé ?
Vous pouvez lui transmettre librement cette page par le moyen de votre choix. »

**Remarques externes arbitrées** (pièce archivée verbatim + SHA-256 `6600ACE9…39BB`, arbitrage
`.claude/external-audits/ARBITRATIONS/anthropie-site-20260919-ressources-offertes_arbitrage.md`) :
« relais » retiré aux deux endroits (« un lecteur, un proche, une bibliothèque ou l'auteur » ; « il devient,
s'il le souhaite, un passeur ») ; chaîne « Des livres achetés → des lecteurs invités → le savoir circule »
(le dispositif n'est pas un un-pour-un) ; « intéressé par ce livre » sur les pages par livre ; compte Amazon.fr annoncé dès l'accroche ;
note Amazon **datée** — nouveau champ `amazon_rating_date` dans les cinq fiches (la date vivait en
commentaire YAML), affichée « Note relevée en septembre 2026 » par `partials/preuve-sociale.html`, `warnf`
si absent (témoin : mutation sur Livresque → avertissement, restauré) ; page `/transparence-contacts/`
renommée « Transparence et données personnelles », URL et ancres inchangées. Accordéons du bas de page :
rejetés. `check-all.py --reseau` : tout à 0.

### 2026-09-17 — *Livresque des mots* : broché P15 (694 p., index des auteurs), nouvelle couverture, sous-titre

**Livre.** Le broché P15 a été accepté par KDP le 17/09 : sommaire, « Promenades dans le livre » et
**index des auteurs** (672 → 694 pages). Registre `data/works.yaml` v1.20 : `pages` 694, `subtitle_fr`
aligné sur la page de titre de l'intérieur et la couverture (« Anthologie inédite & éclectique de
citations » ; « inédite » avait été écarté tant que seule la fiche KDP le portait). `corpus_stats`
inchangés.

**Surfaces.** Fiche (sous-titre, pagination, FAQ « a-t-il un index ? », corps, pied), page méthode et
corpus (694 pages, index, FAQ sans pagination figée), page « offrir un livre de culture générale »
(l'objet littéraire ne se dit plus « jamais consulté »), ligne du mur `/a-propos/` FR et EN,
`static/llms.txt`. Formule retenue par l'auteur : « un fil pour flâner, un index pour retrouver ».

**Couverture.** Nouvel outil `scripts/og_couverture_livre.py` : fiche 1000×1500 tirée du master HD et
couverture reposée dans les images de partage à la pose mesurée de l'ancienne (SIFT + RANSAC :
échelle 0,200, ±4°, résidu 0,2 px ; couvertures voisines mesurées pour le masquage). **Témoin avant
écriture** : recomposition avec l'ancienne couverture, écart lissé 1,0 à 1,4 niveau sur les trois
images (`og-home`, `og-ressources-offertes`, `-dark`) ; **mutation** : un décalage de 1 px le porte à 5,4
(seuil 3). Deux défauts du témoin corrigés en route : écart brut dominé par le grain (réduction
Lanczos + rotation bicubique retenues, 4,1 contre 6,4 à 15) et flou qui mêlait la couverture voisine
au bord (lissage normalisé sur la zone visible).

**Wikidata.** Dossier `Wikidata/Import_Wikidata_Laura_2026-09-17_Livresque_P15/` : pages 672 → 694 et
sous-titre sur `Q140517745`, à exécuter par Laura quand amazon.fr affiche 694 pages.

### 2026-09-16 — Couverture de *Dette publique* : nouvelle charte ; DOI propre de la recension RFSE

**Couverture.** `assets/images/livres/dette-publique-qui-paie-vraiment.jpg` remplacée par le recto
KDP du 16/09 (décision auteur) : bleu nuit d'ANTHROPIE `#011331` (mesuré sur sa couverture Kindle)
et accent orange brûlé `#C85A2A` au lieu du marine et du jaune. Même cadrage que l'ancienne image
(recto réduit à 1000×1500, vérifié : échelle 0,488, décalage nul), mêmes tables JPEG, progressif ;
chroma 4:4:4 pour les traits orange fins (92 → 148 Ko). Une seule source sert la fiche, les
vignettes, le mur auteur et l'image de partage : build local sans erreur, variantes `_hu_`
renouvelées. Masters et traçabilité : `03_LIVRES\dette-publique\_INDEX.md`.

**DOI.** `check-all --reseau` échouait sur un fait externe nouveau : Cairn a attribué à la recension
Lemoine seule le DOI `10.3917/rfse.036.0247d` (lu à la source Crossref ; résout vers la page 247d).
Écrit en retour : `doi_review` au registre (v1.19, même logique que `wikidata_review`), `doi` de la
fiche, et lecture de `doi_review` par `sondage-noeuds-externes.py` — **témoin par mutation** : sans
la ligne, l'écart revient ; restauration vérifiée par empreinte. ⏸ Reste externe : l'item de la
recension seule `Q141072266` n'a toujours pas de DOI sur Wikidata (geste de navette, non fait ici).

**Vérifié chez l'éditeur (même jour, sur demande de l'auteur).** Crossref : `…0247` = bloc « Comptes
rendus d'ouvrages » (7 recenseurs) ; `…0247a` à `…0247g` = les 7 recensions, `…0247d` = Lemoine par
Stéphane Lalut ; `…0247h` n'existe pas. Cairn (navigateur) : la page `-page-247d` porte
`citation_doi` `…0247d` et « Par Stéphane Lalut » ; le sommaire du numéro ne liste plus que 247a-247g ;
**la page du bloc `-page-247` est « Page non trouvée »** — c'est elle que visaient `url_externe` et
`works.yaml`, donc la carte `/publications/` menait à une page morte. Repointés vers `-page-247d` ;
témoin par mutation de `check-fiches-registre.py` (lien divergent → écart ; restauré par empreinte).
⚠ Le résolveur DOI de Cairn (`v4.reseaucairn.info`) répondait 503 pour les deux DOI ce jour-là, y
compris en navigateur : panne côté éditeur, pas un verdict sur les DOI.

**ORCID corrigé (sur demande de l'auteur, session ouverte dans son navigateur).** L'œuvre put-code
`224566476` décrivait le bloc (« Comptes rendus d'ouvrages », DOI `…0247`, 7 contributeurs) : titre,
sous-titre, lien et DOI passés à la recension seule (`…0247d`, relation *self*), 6 contributeurs du
bloc retirés, ISSN conservé. Readback API publique : conforme ; `…0247` absent du profil, 37 œuvres
(pas de doublon). **Wikidata** : lot prêt pour Laura, `Wikidata/Import_Wikidata_Laura_2026-09-16_RFSE_DOI_recension/`
(DOI + pages + numéro + P361 sur `Q141072266`, P953 mort retiré des deux items) — non exécuté.

### 2026-09-15 — Relevé post-lancement : l'instrument GEO mesurait faux depuis un mois

Créneau du 15/09 (fiche `T1_SONDES_EN_2026-09-15.md`, ouvert par le déploiement France du 22/07).
Relevé exécuté : `reports/geo_audit/RELEVE_POST-LANCEMENT_2026-09-15.md`.

**Résultat principal — `audit_geo_v2.py` rendait des verdicts inversés sur l'étage Éligibilité**,
le seul étage qui autorise une correction directe du site : un faux ❌ y pousse à « réparer » ce
qui fonctionne. Cause unique, cinq surfaces : Hugo minifie et écrit les attributs **sans
guillemets** (`href=/awp/awp-01/citation.bib`) alors que les motifs exigeaient `href="…"` — 75 href
réels lus comme 1. Deux coquilles rendaient en plus leur contrôle incapable de dire autre chose
qu'« absent » : `sid=` pour `id=`, et `b<nom>` pour `\b<nom>`. Mesuré contre la source : BibTeX /
RIS / PDF Zenodo **présents et servis en 200** (déclarés ❌ contrat), **6** ancres `id` sur h2/h3
FR et EN (déclarées 0), RSS **annoncé** (déclaré absent), **21** directives `User-agent:` dont tous
les bots IA de citation (0 sur 8 déclarés). Le rapport du 11/08 portait les mêmes erreurs.

**Quatrième défaut, ailleurs** : les quatre `⚠️ API` de Wikidata ne venaient pas de Wikidata mais
du poste — `CERTIFICATE_VERIFY_FAILED, certificate has expired`, en 0,1 s, avalé par le `except`.
Seul `*.wikidata.org` échoue ; OpenAlex, Zenodo, Crossref, GitHub, OpenLibrary passent. **Le remède
vivait déjà dans le dépôt** : `check-wikidata-registre.py` le porte depuis le 02/09 — jamais
propagé à l'autre organe de la même famille, qui n'en comptait que deux. Après propagation :
19 / 8 / 15 / 14 claims.

**Corrigé** (`scripts/audit_geo_v2.py`, `scripts/audit_geo_v2.sh`) : un seul helper `attr_values()`
pour tout le fichier — la règle vit à un endroit, pas en cinq copies ; contexte TLS `certifi` ;
section **B.3** qui rend désormais le **motif** de chaque échec réseau (un `⚠️ API` muet a coûté un
diagnostic complet) ; ancres comptées sur `<h2>/<h3>` et non sur tous les `id` de la page (bon
dénominateur, mauvais grain) ; rapports écrits dans `reports/geo_audit/audit_geo_v2/` au lieu de
s'empiler à côté de leur générateur.

**Témoins** : contre-témoins tenus — `Markdown raw` reste 💡 (réellement absent), `Bingbot` reste 💡
(nommé seulement dans un **commentaire** du robots.txt : le contrôle corrigé cherche une directive,
pas une occurrence du mot). Aucune régression : sur les 104 ✅ du témoin, zéro perdu ; ✅ 104 → 115,
❌ 6 → 3, 💡 35 → 27, ⚠️ 5 → 1 — les ❌ et ⚠️ restants sont les **lignes de légende**. Le témoin de
l'état fautif est conservé (`audit_geo_v2/2026-09-15_TEMOIN_avant-correctif.md`).

**Non fait, et pourquoi** : les sondes S1–S6 et Search Console exigent la double lecture connecté /
navigation privée — geste d'auteur. L'étage Visibilité observée reste donc à **0 %** de couverture
pour ce passage ; *non mesuré* n'est pas *absent*. Les quatre échéances « T1 15/09 » du registre
des collisions sont marquées **échues et non relevées**, pas repoussées.

**Points ouverts** : écart Crossref `10.3917/rfse.036.0247d` (recension Lemoine, absente du
registre — arbitrage éditorial) ; `reports/` entièrement gitignoré (`.gitignore:45`), donc le
protocole d'engagement et les **baselines T0 non régénérables** vivent hors versionnement, filet =
sauvegarde `G:\_BACKUP_SITE_ANTHROPIE_2026-09-03\` — modifier le périmètre versionné d'un dépôt à
remote public est un arbitrage non rendu ; `anthropic-ai` (legacy) absent des directives robots.

**Collision anthropie.org** : push du **14/09** (le registre portait 23/07), 6 issues, 39 Mo, site
200 — production vivante, réception toujours nulle (0 star / fork / watcher depuis le 02/08). Pas
de fusion machine sur le canal testé : les deux objets sortent distincts. Déclencheur P3 (page
comparative) **reste fermé**.

**Nommage** : le 15/09 s'appelait « T1 » dans trois fichiers, à côté du **T1 d'octobre** du
protocole — deux objets sous un nom, dans l'index qu'on lit en premier. Le relevé porte désormais
un nom de rôle ; `GEO_PROTOCOLE_MESURE.md` § 5 et la fiche de sondes portent la distinction.

### 2026-09-14 — OpenAlex : 37 travaux soumis, et le profil revendiqué n'était pas celui que je croyais

**Geste exécuté dans le navigateur de l'auteur, à sa demande explicite.** Résultat : **46
publications analysées, 37 ajoutées, 9 déjà présentes, 0 introuvable** ; le profil affiche
« 37 pending », application annoncée sous 1 à 2 jours.

**Correction de ma recommandation du matin.** J'avais conclu « l'ancre est l'entité qui porte
l'ORCID », soit `A5134537460`. La page des réglages du compte dit autre chose : **un profil est
déjà revendiqué, et c'est `A5130851063`** — celle que la checklist du 22/08 nommait, qui porte 9
travaux et **pas** l'ORCID. Le critère ORCID était juste dans l'ignorance de ce fait ; il ne
l'était plus une fois la revendication connue.

**Arbitrage retenu — consolider sur le profil déjà revendiqué**, pour trois raisons qui vont
toutes dans le même sens : il est **éditable immédiatement** (l'autre exigerait une nouvelle
revendication, en revue manuelle puisque l'adresse du compte n'est pas institutionnelle) ; il est
**déjà déclaré** en `sameAs` sur le site et en P10283 sur Wikidata, donc en changer imposerait de
modifier ces deux surfaces ; et OpenAlex fusionne précisément ainsi — « l'entité vidée devient
inerte », il n'existe pas de bouton de fusion, déplacer les travaux **est** la fusion.

**Moyen employé** : l'option « Add from CV », qui accepte un simple `.txt` de liste de
publications. Une liste de 46 titres + DOI a été générée depuis l'API OpenAlex (les 10 entités)
**et** depuis `data/works.yaml` pour les **6 DOI SSRN** — ces six-là n'apparaissaient sur aucune
des entités inventoriées et auraient été manqués par la seule voie API. Un par un dans
l'interface, l'opération aurait demandé une centaine et demie d'actions ; elle en a demandé
quinze.

**Procédure vérifiée à la source ce jour** (`help.openalex.org/how-to/fixing-authors/`) : la page
auteur n'affiche **aucun bouton « Claim » quand le profil est déjà revendiqué** — ce qui explique
que je ne l'aie pas trouvé et m'a conduit aux réglages du compte, où le profil revendiqué est
nommé.

⏰ **À vérifier le 2026-09-17** (J+3) : `works_count` de `A5130851063` doit passer de 9 à 46, et
il faudra regarder **si l'ORCID migre** vers cette entité en même temps que les travaux qui le
portaient. S'il ne migre pas, le point redevient ouvert — l'identité aurait alors ses travaux
d'un côté et son identifiant chercheur de l'autre. Relance : `python scripts/openalex_identite.py`.

### 2026-09-14 — Identité OpenAlex : le geste auteur était bloqué par une liste qui n'existait pas

**D6 attendait depuis le 22/08 sans que rien ne le dise.** La procédure était vérifiée à la
source (pas de fonction « fusionner » : on revendique une entité, puis on lui rattache les
travaux des autres **par DOI**), mais la liste des DOI à rattacher n'existait nulle part et aucun
script ne la produisait. Le geste n'était donc pas « en attente de l'auteur » : il était
**inexécutable**. La liste citée le 22/08 en comptait 12, le relevé du 13/09 parlait de 44 sans
les énumérer.

**Mesuré ce jour par l'API publique** (`scripts/openalex_identite.py`, nouveau) : **46 travaux
distincts** répartis sur 10 entités, dont **16 déjà sur l'ancre** et **30 à rattacher**.

**L'ancre ne se choisit plus à la main : c'est l'entité qui porte l'ORCID.** L'API répond
`A5134537460` (16 travaux, ORCID `0009-0002-1794-4895`). La checklist du 22/08 nommait
`A5130851063`, qui porte 9 travaux et **pas** l'ORCID — ancrer dessus fixait l'identité sur une
entité minoritaire et sans signal. Point réglé par la mesure, pas par un arbitrage.

**Pourquoi les DOI vont par paires** : Zenodo émet un DOI *concept* et un DOI de *version*, et
OpenAlex indexe les deux comme deux travaux. Les rattacher tous les deux est correct ; cela
explique que 23 publications donnent 46 entrées.

La liste brute est remise à l'auteur dans `Downloads\OPENALEX_DOI_A_RATTACHER.txt`, prête à
coller. L'outil porte sa condition de mort : il disparaît quand deux exécutions à un mois
d'intervalle rendent « A RATTACHER : 0 ».

### 2026-09-14 — Dépôt d'AWP-07/08 : la question supposait un manque, et le manque ne se mesure pas

Contre-expertise `anthropie-site-20260914-003955` (`REASONING_AUDIT`, paquet monté cette nuit par
une autre session). Réponse `D65B8C75…475E`, 14 858 octets, **archivée verbatim avant lecture**,
parité d'empreinte vérifiée. Arbitrage complet dans `ARBITRATIONS/`.

**Verdict retenu : NE PAS DÉPOSER — mais l'argument change une troisième fois.** Le paquet
plaidait « on ne joue pas six acceptations contre une septième ». La réponse a montré que cette
asymétrie est mal spécifiée et que l'argument tient plutôt à la valeur d'attente. **Les deux
raisonnaient sur une prémisse que personne n'avait testée** : qu'AWP-07 et AWP-08 souffrent de
n'avoir aucun relais.

**Le point le plus fort de la réponse, vérifiable dans le paquet lui-même** : AWP-07 **n'est pas
sans relais**, il est engagé sur le relais 2 et toujours en examen. Or la règle verrouillée dit
« au plus un relais disciplinaire ». Le déposer ailleurs maintenant en engagerait **deux à la fois
sur le même papier** : l'option B ne manque pas de prudence, elle **viole une décision déjà
verrouillée**. Retirée du jeu, pas ajournée.

**Et la fonction de perte est assise sur rien.** Le paquet chiffrait le coût à « potentiellement
les six papiers déjà en ligne ». La source ne dit que « *may lead to rejections and account
closure* » : entre fermeture d'un compte et disparition des records publiés, **il manque un maillon
que personne n'a établi**. Tant qu'il n'est pas lu à la source, c'est une perte supposée.

⭐ **La mesure qui déplace tout, et que la réponse réclamait sans pouvoir la faire.** Compteurs du
dépôt canonique, seize records dérivés du registre :

| Papier | Relais | Jours | Vues/jour | DL/jour |
|---|---|---:|---:|---:|
| AWP-01 à AWP-06 | oui | 130 à 225 | **1,54** (moyenne) | **4,99** (moyenne) |
| **AWP-07** | **aucun** | 71 | **1,65** | **11,06** |
| **AWP-08** | **aucun** | 53 | **1,70** | **3,38** |

**Les deux papiers sans aucun relais font légèrement mieux que les six qui en ont un, sur les deux
compteurs.** ⚠ **Correction du 14/09, tour 2 : cette lecture était trop forte.** Un taux par jour
écrase une courbe qui décroît, donc il **favorise mécaniquement les papiers jeunes** ; et le protocole
de mesure du 04/07 documente un **incident de comptage Zenodo le 15/05**, qui sépare exactement mes
deux groupes. **La comparaison à âge égal n'est pas faisable** — l'interface ne rend que des cumuls.
À retenir : **la prémisse n'est pas testable**, et non « le manque n'existe pas ».

⚠ **Deux réserves, en sens opposés, et elles sont dans l'arbitrage.** Le **biais d'âge joue en
leur faveur** — 53 et 71 jours contre 130 à 225, et le trafic d'un dépôt est plus dense au début ;
`n = 2` contre `n = 6`. Et le compteur de téléchargements est **celui que la réponse demande de
suspendre** : AWP-07 EN affiche **679 téléchargements pour 57 vues, ratio 11,9, extrême du
corpus** — premier record à inspecter le jour où la provenance sera vérifiée. Le compteur robuste
est celui des **vues**, et l'écart y subsiste. Conclusion honnête : **aucun déficit mesurable**,
pas « déficit prouvé absent ».

🔧 **Défaut trouvé dans notre propre appareil, et corrigé dans le même geste.** `zenodo_stats.py`
portait une liste **codée en dur de cinq records** ; `zenodo_stats_full.py` la même. **AWP-06, 07
et 08 en étaient absents — en silence** : le tableau s'arrêtait, voilà tout. La décision du jour
portait précisément sur les deux papiers que l'instrument ne regardait pas. C'est la classe que
`check_deposits_status.py` documente déjà en tête (« un manquant déguisé en zéro ») et que le
`CLAUDE.md` du dépôt pose en règle — *la présence vient du dépôt, une exclusion peut être légitime,
le silence jamais*. **La leçon avait été appliquée à un script et pas à son voisin, dans le même
dossier.** La liste est désormais **dérivée de `data/works.yaml`** — seize records, huit papiers,
deux langues ; tout AWP du registre sans record est signalé avec son motif ; une erreur d'API est
déclarée **non mesurée** et jamais lue comme un zéro ; et une indisponibilité est réessayée trois
fois avant de conclure — Zenodo rendait `504` la veille. Vu mordre : la sortie déclare « Tous les
AWP du registre ont été mesurés ».

**L'option « diffuser sans redéposer » a déjà une tâche nommée et en attente.** La réponse la
désigne comme l'angle le plus prometteur ; ce n'est pas un espace vierge. Le bilan à 90 jours y a
trouvé un défaut majeur toujours ouvert : **l'identité de l'auteur sur le principal index
bibliographique ouvert est fragmentée en dix entités portant 44 travaux** — mesuré le 13/09, neuf
le 22/08. **C'est le seul défaut de diffusion réellement mesuré du dossier**, il s'aggrave à chaque
dépôt, et sa réparation est un geste auteur de coût faible qui porte sur les huit papiers à la
fois.

**Décision humaine, et ce n'est pas celle que le paquet posait** : faut-il traiter cette
fragmentation **avant** de rouvrir la question des relais ? Rien d'autre n'est en attente — le
rendez-vous du **11/10** sur le relais 2 reste la seule échéance, et le ratio téléchargements/vues
ne porte plus aucune décision tant que sa provenance n'est pas décomposée.

**Tour 2 du 14/09 — et la règle qui dissout la question était déjà dans le dépôt.** Pièce
`24E6B92C…94E6`, 15 017 octets, archivée verbatim avant lecture, en annexe (créneau déjà servi).

⭐ **`reports/geo_audit/GEO_PROTOCOLE_MESURE.md`, 2026-07-04, statut « protocole d'engagement »,
§ 3** : *« Seul un signal de traction déclenche une action : citation d'usage par un tiers, mail
entrant, backlink `.edu`, demande de positionnement, reprise presse. **Une métrique de volume seule
ne déclenche jamais rien** (elle contextualise). »* **Toute la question des relais est une question
de volume** — téléchargements, vues, ratio, les 105 du relais 1 — et **aucun signal de traction n'a
été rapporté.** Il n'y avait donc pas de décision à prendre. Le même fichier désigne par ailleurs
l'index bibliographique ouvert comme **« le vrai KPI »** du régime long, et rappelle un **incident
de comptage Zenodo du 15/05** qui rend les valeurs absolues fragiles. **Un paquet, trois tours de
contradiction et deux arbitrages ont été produits sans que ce fichier soit ouvert** — et c'est moi
qui l'ai manqué en premier.

⚠ **Correction de ma mesure d'hier, et le tour 2 a raison.** J'avais conclu que la prémisse « les
deux derniers papiers souffrent de l'absence de relais » **ne tenait pas**, sur des taux par jour.
Deux défauts, tous deux dans le sens qui fabriquait mon résultat : un taux par jour **écrase une
courbe décroissante** et favorise donc mécaniquement les papiers jeunes ; et l'incident de comptage
du 15/05 **sépare exactement mes deux groupes**. La comparaison à âge égal n'est pas faisable —
l'interface ne rend que des cumuls, et aucun relevé ancien n'est conservé. **À retenir : la
prémisse n'est pas testable, pas « le manque n'existe pas ».** Sous la règle du § 3, cela ne change
rien à la décision.

**Apports neufs et retenus de ce tour** : le vrai actif risqué n'est pas les six papiers mais la
**valeur d'option du canal pour les papiers à venir**, que le paquet ignorait ; et un rejet
définitif **coûte moins qu'annoncé** — le papier reste public avec son DOI, seule l'option de
distribution est perdue. Les deux erreurs du dossier allaient dans le même sens, celui de
l'immobilité. **Non vérifié** : son intuition que les six papiers relayés serviraient déjà de
portes d'entrée vers tout le corpus — la page du premier papier est bien **la plus cliquée du
site** (131 clics, 1,04 %), mais le parcours interne exigerait l'instrument de fréquentation, non
lisible.

### Synthèse — huit décisions, coût nul

| # | Décision | Qui |
|---|---|---|
| **D1** | **Aucune soumission d'AWP-07 ni d'AWP-08 au relais 1.** Le volume ne déclenche rien ; AWP-07 engagerait un second relais simultané contre une règle verrouillée ; AWP-08 est le moins compatible ; la perte inclut l'option pour les papiers futurs. | tranché |
| **D2** | **La question « relais » est close**, pas ajournée : elle ne se rouvre que sur un **signal de traction**, jamais sur un chiffre de volume. | tranché |
| **D3** | **Pas de critère de succès nouveau** : celui du protocole du 04/07 s'applique tel quel. | tranché |
| **D4** | **Le ratio téléchargements/vues sort du moteur décisionnel** — provenance inconnue, endogénéité au lien du site depuis le 13/09, incident de comptage du 15/05. Descriptif seulement, en tendance trimestrielle. | tranché |
| **D5** | **Correction du journal** ci-dessus appliquée. | fait |
| **D6** | **Le seul défaut de diffusion réel et réparable reste l'identité fragmentée sur l'index bibliographique** — dix entités, 44 travaux, en aggravation. Le protocole en fait **le vrai KPI** : ce n'est pas un à-côté. | **auteur** |
| **D7** | **Rendez-vous du 11/10 maintenu**, et ce jour-là on lit le **rendement de la cohorte**, pas un nombre de jours. | armé |
| **D8** | **Aucune nouvelle contre-expertise sur ce sujet** : trois tours, verdict convergent, inconnues restantes soit non mesurables soit exclues par le protocole. Une quatrième serait surnuméraire. | tranché |

**Ces huit décisions ne coûtent rien** : aucune soumission, aucun développement, aucun instrument
nouveau. Le seul geste restant demande une authentification et porte sur les huit papiers à la fois.

*Un dispositif de contradiction externe ne remplace pas la lecture de son propre appareil : il la
suppose. Quand elle manque, il produit du raisonnement juste sur une question qui n'avait pas lieu
d'être posée — et c'est plus coûteux qu'une erreur, parce que cela ressemble à du travail.*

**D6 élucidé le 14/09 — et la cause n'est pas chez nous.** Le rapport du 22/08 présentait
l'identité auteur fragmentée sur l'index bibliographique comme un défaut structurel à réparer.
**Trois vérifications à la source disent autre chose.**

| Maillon | Mesure du 14/09 | Verdict |
|---|---|---|
| Nos dépôts portent-ils l'ORCID ? | audit complet, 17 enregistrements | **0 bloquant** |
| L'index intermédiaire le transmet-il ? | 3 dépôts testés, pris parmi ceux qu'OpenAlex montre *sans* | **3/3 portent `nameIdentifiers`** |
| Que voit OpenAlex ? | travaux inspectés | **21 avec ORCID, 26 sans** |

**La chaîne est saine de bout en bout ; c'est OpenAlex qui n'a pas encore re-fusionné.** Nos
métadonnées ont été corrigées tout au long d'août et début septembre — les dépôts testés portent
des dates de mise à jour au 17/08, 31/08 et 13/09. **Les fiches parasites ont été créées avant ces
corrections**, à partir de métadonnées alors incomplètes. Ce n'est pas un défaut à réparer, c'est
un retard à observer.

**Indice, et je ne le prends pas pour une tendance** : la fiche ancre portait **15 travaux le
13/09, 16 le 14/09**. Un point ne fait pas une courbe, mais il est cohérent avec le mécanisme.

⛔ **Correction d'une consigne fausse** : l'ancienne fiche de rappel désignait `A5130851063` comme
la fiche à revendiquer. **Elle ne porte que 9 travaux sur 47 et pas l'ORCID.** L'ancre est
`A5134537460` — 16 travaux, ORCID rattaché. Revendiquer l'autre aurait ancré l'identité sur une
fiche minoritaire et sans signal.

**Une fiche tranchée qui était en suspens** : `A5138641837` est bien la sienne — « La commune,
variable d'ajustement de la République ? », *Revue Projet* 2026, `10.3917/pro.412.0078`. Son
absence d'ORCID s'explique : Cairn ne le transmet pas.

**Décision : mesurer avant d'agir, au 11/10 — le même jour que le rendez-vous déjà armé sur
MPRA.** Un seul rendez-vous, pas deux. Coût de l'attente : nul, l'index se lit « mensuel, passif »
d'après le protocole du 04/07. **Condition de mort écrite** : l'ancre a absorbé → dossier clos
sans geste ; rien n'a bougé → dix minutes de revendication ; l'auteur le fait avant → vérification
à la source sous 48 h et clôture. Pas de quatrième issue, et le dossier ne se reconduit pas.

**Dossier auteur autoportant monté au sas** — `D:\CONTRE_EXPERTISE\2026-09-14_IDENTITE_OPENALEX\`,
quatre fichiers, ouvert dans l'explorateur : ce que c'est, ce qui a été mesuré, la marche à suivre
si l'auteur choisit d'agir, et les **31 DOI à coller, tous avec un DOI, aucune saisie manuelle**.
**Procédure vérifiée à la source ce jour** — la documentation d'OpenAlex énonce « *Fixing authors :
No ticket needed — claim it and fix it yourself* ». La revendication passe par une
authentification : c'est la seule raison pour laquelle ce dossier existe.

⛔ **CORRECTION, une heure plus tard : tout ce qui précède sur l'ancre est caduc, et le geste était
déjà fait.** Une autre session a exécuté la consolidation le matin même, avec l'auteur, dans son
navigateur : **46 publications analysées, 37 ajoutées, 9 déjà présentes, 0 introuvable**, profil à
« 37 pending », application sous un à deux jours. **Et sur `A5130851063`, pas sur `A5134537460`.**

**Pourquoi mon critère était faux, et c'est instructif.** Je raisonnais sur les interfaces publiques,
qui ne montrent qu'une chose : quelle fiche porte l'ORCID. **Elles ne montrent pas qu'une
revendication existe déjà** — cela ne se lit que dans les réglages du compte, en étant connecté.
`A5130851063` était déjà revendiquée, donc **éditable immédiatement**, quand l'autre aurait exigé une
nouvelle revendication en revue manuelle ; elle est en outre déjà déclarée en `sameAs` sur le site
et en `P10283` sur Wikidata. *Le critère ORCID était juste tant que la revendication existante était
inconnue.* Une mesure extérieure ne pouvait pas atteindre ce fait.

**Ce qui reste vrai de mon relevé** : la chaîne de métadonnées est saine de bout en bout — c'est ce
qui explique que les 37 soumissions devraient prendre sans résistance. **Ce qui est retiré** : la
recommandation d'ancre, et l'échéance au 11/10. **La bonne date est le 2026-09-17**, posée par la
session qui a agi : `A5130851063` doit passer de 9 à 46 travaux, et surtout **l'ORCID doit migrer
avec les travaux qui le portaient**. S'il ne migre pas, l'identité se recoupe autrement — les travaux
d'un côté, l'identifiant chercheur de l'autre — et le point rouvre sous une forme différente.

**Le dossier du sas est neutralisé** : marche à suivre et liste de DOI renommées `PERIME`, `01`
réécrit en « rien à faire », correction portée en tête de `02`. ⚠ **Le
dossier avait été ouvert dans l'explorateur avant que je voie les commits de l'autre session** : c'est
la fenêtre où l'auteur aurait pu suivre une consigne fausse. J'avais relevé les sessions pairs en début
de session, pas avant d'écrire — **le relevé se refait avant de produire, pas une fois par jour.**




### 2026-09-14 — Contrôle des dépôts : la décision était dans le code, la sortie disait le contraire

Contrôle demandé sur la foi de l'audit plateformes du **2026-08-02**, dont la recommandation n°1
était « déposer AWP-07 et AWP-08 sur SSRN ». Deux prémisses de la consigne sont périmées, et
`check_deposits_status.py` le montre : **AWP-07 n'a jamais été déposé sur SSRN** (`status:
planned` dans `works.yaml`, page auteur vérifiée le 17/08) — il n'y a donc aucune acceptation à
attendre ; et SSRN est passé en **NO-GO pour AWP-07/08** le 2026-08-17, source relue : *frameworks*
en « Content types that are typically NOT accepted », critère d'entrée « original findings »,
rejets finaux sans appel, et « high submission volumes may lead to rejections **and account
closure** » sur un compte qui porte six acceptations. Rien déposé, donc rien à porter dans
`works.yaml`.

**Défaut corrigé dans le même passage.** La grille imprimée par le script annonçait
« **GO (EN)** — SocArXiv/OSF, accepté à tout stade », alors que le canal est **clos aux papiers
conceptuels depuis le 2026-08-05** après deux refus sur le fond d'AWP-01 EN — décision écrite
vingt lignes plus haut dans le même fichier, en commentaire, et contredite par la sortie. La
section OSF aggravait la lecture : « file d'attente restante : aucune » suivi de « ne déposer le
suivant qu'après acceptation du précédent » se lit comme une invitation à déposer, alors que la
file est vide **par décision, pas par disponibilité**. Les deux lignes disent maintenant ce que le
dépôt sait. Classe *état déclaré ≠ état réel*, appliquée à un instrument : ce qu'il imprime est ce
que l'auteur lit, et c'est sur cette lecture que se déposerait un papier.

**MPRA** : rien à rouvrir, arbitré le 13/09 — AWP-07 (`130468`) est « Under review », pas refusé,
et 97 % de sa cohorte d'août est dans le même cas ; vérification au **11/10/2026**, sur le
rendement de la cohorte et non sur un nombre de jours.

### 2026-09-13 — PDF des AWP : on ne peut pas les ouvrir, on ne pouvait que les télécharger — et le bouton de l'autre langue mentait

**Point de départ, une question d'auteur sur téléphone** : depuis un iPhone, un PDF du site
n'arrive pas à l'écran, il atterrit dans Fichiers → Sur mon iPhone → Téléchargements. Mesuré
plutôt que supposé — `curl -sIL` sur un fichier Zenodo, avec et sans `?download=1`, même
réponse dans les deux cas :

```
content-type: application/octet-stream
content-disposition: attachment; filename=AWP-08_reversibilite_sociale.pdf
```

`attachment` **interdit** l'affichage dans l'onglet et `application/octet-stream` empêche même
le navigateur de savoir que c'est un PDF. Le parcours n'était donc pas un défaut d'ergonomie du
site : c'était la seule issue possible tant qu'un bouton pointait vers ce lien. Zenodo expose en
revanche un lecteur intégré, `/records/<id>/preview/<fichier>`, qui rend le même PDF en HTML
(`text/html`, viewport `device-width`, pdf.js) — lisible d'un tap, sans téléchargement. Non
encapsulable (`x-frame-options: sameorigin`), donc ouvert en onglet.

**Arbitrage auteur du jour** : « les instruments de mesure ne sont pas prioritaires ; le service
au lecteur l'est — toujours simple pour le lecteur ». Trois conséquences appliquées dans le même
commit :

1. `partials/awp-preview-url.html` (nouveau) — un seul organe qui dérive l'URL du lecteur, trois
   appelants. Rend une chaîne vide hors Zenodo, l'appelant doit tester : un futur PDF hébergé
   ailleurs ne peut pas produire un bouton « Lire en ligne » qui téléchargerait.
2. Sidebar de l'article : **Lire en ligne** en action principale, puis **Télécharger le PDF (FR)**
   — l'ancien libellé « PDF (FR) » ne prévenait pas qu'il déclenchait un téléchargement. Carte de
   liste : « Lire le PDF », qui mène au lecteur.
3. **Routage de convergence désarmé côté site.** `data/convergence_routing.json` promouvait la
   notice Zenodo en bouton principal quand un record manquait de vues : **11 records sur 17** ce
   jour, soit une majorité d'articles plaçant une fiche de métadonnées devant le texte. Le
   collector continue de produire le fichier ; il ne pilote plus l'ordre des CTA.

**Défaut préexistant trouvé par le contrôle de la sortie, pas par la relecture du template.**
Le bouton PDF de l'autre langue était faux sur **16 pages sur 16** : absent sur les 8 pages FR,
et sur les 8 pages EN il portait le libellé « (FR) » au-dessus du fichier **anglais**. Cause :
`$.Site.GetPage .url` recevait une URL de sortie (`/en/awp/awp-08/`) là où `GetPage` résout un
chemin de contenu — nil côté FR, page courante côté EN. Corrigé par `.Translations`, le lien
natif que Hugo établit entre `awp-NN.md` et `awp-NN.en.md` ; la langue du libellé se **dérive**
désormais de la page pointée au lieu d'être recopiée. Classe *état déclaré ≠ état réel* : rien
n'échouait, le bouton servait simplement l'autre fichier.

**Mesures après correction** — 16 pages construites : lecture en ligne présente 16/16, bouton de
traduction correct 16/16 (0 faux, 0 absent) ; les 16 URL de lecture répondent 200 **et** servent
un lecteur pdf.js 16/16 ; contre-témoin sur un nom de fichier inexistant : 0, le contrôle sait
donc distinguer. `python scripts/check-all.py --reseau` : 6 contrôles, tout à 0. Premier essai du
contrôle écarté : sa regex exigeait `href="…"` que le `--minify` supprime, et il rendait 16 faux
« absent » — un parseur qui ne sait pas lire n'a pas trouvé un vide.

**Point fermé le 2026-09-14, arbitrage délégué par l'auteur.** `data/convergence_routing.json`
est supprimé du dépôt : plus aucun template ne le lisait, et un fichier de configuration que
personne ne lit finit par être cru. Côté collector, `--route` n'écrit plus rien et le dit, le
lanceur quotidien `data/convergence.bat` perd l'option, et la section du rapport s'intitule
désormais « Contrôleur de routage — DÉSARMÉ (mesure seule) » — sans quoi elle aurait continué
d'affirmer chaque jour une action qui n'a plus lieu. La mesure, elle, est intégralement conservée :
c'est l'action qui tombe, pas le diagnostic. Vérifié le 2026-09-14 : `--route` relancé n'a pas
recréé le fichier. Détail du geste dans `01_SITE/collector/PROJECT_STATUS.md`.

Vérifié aussi dans le même passage : aucune autre surface du site n'est pilotée par un instrument
de mesure. Les `site.Data` restants sont l'identité auteur, les chiffres de dette et les registres
d'œuvres — du contenu, pas des compteurs. La règle « le lecteur d'abord » n'a donc qu'un seul cas
d'application ici, et il est traité.

### 2026-09-13 — Rappel J+90 : l'audit existait déjà ; ce qui a bougé, et trois cellules remplies

**Le rappel qui a sonné ce jour demande un travail fait le 22/08.** `audits/diagnostic-compare-2026-08-22.md`
est l'audit J+90 — J+91 exactement, base `diagnostic-2026-05-23.md`, HEAD `b399315`, 244 commits.
Il couvre la checklist entière, y compris les quatre décisions propres au J+90 (§ 7) et les trois
gestes auteur (§ 7.5). **Il n'est pas refait.** Le rappel, lui, n'avait pas de condition de mort :
il a survécu à son objet — et son § A3 disait déjà que **c'est la checklist qui a vieilli**, pas le
dossier. Sa suppression est un **geste auteur**.

Ce qui suit n'est donc pas un second J+90 : c'est **l'écart mesuré depuis le 22/08**, plus les
cellules que le § 5.7 déclarait non lues et que la session a pu lire.

**G3 — ORCID : FAIT.** Le dossier porte 38 travaux et le DOI `10.3917/rfse.036.0247` y est.
⚠ Il y entre sous le titre générique de Cairn, « Comptes rendus d'ouvrages », et non sous le titre
de la recension : c'est la classe de dégradation de titre que le dossier connaît déjà côté SSRN.
Le geste a porté ; ce qu'il a déposé mérite d'être relu.

**G1 — OpenAlex : aggravé, et la checklist désigne la mauvaise fiche.** Chaque entité a été
vérifiée **par ses travaux**, pas par son nom affiché :

| | 22/08 | 13/09 |
|---|---|---|
| entités confirmées siennes (par DOI) | 9 | **9, portant 44 travaux** |
| + entité portant son ORCID, non confirmée par DOI | — | **1** (`A5135768240`) |
| homonyme au statut incertain, à ne pas revendiquer | — | 1 (`A5138641837`) |
| DOI à rattacher | 12 | **44 distincts** |

⛔ **`A5130851063`, l'identifiant que la checklist nomme, ne porte que 9 des 44 travaux et
n'a pas l'ORCID.** L'entité la plus riche est **`A5134537460`** — 15 travaux, ORCID
`0009-0002-1794-4895` attaché. Revendiquer celle de la checklist, c'est ancrer l'identité sur une
entité minoritaire et sans signal ORCID. **L'ancre proposée change ; le choix reste à l'auteur.**
Et la liste de 12 DOI du 22/08 est périmée : elle en compte 44 aujourd'hui.

**Cellules du § 5.7 remplies ce jour — Search Console, lue via Chrome.** Trois mois glissants au
13/09 : **354 clics, 53 700 impressions, CTR 0,7 %, position moyenne 6,8.**

| Page | Clics | Impressions | CTR |
|---|---|---|---|
| `/awp/awp-01/` | 131 | 12 606 | 1,04 % |
| **`/en/quest-ce-que-lanthropie/`** | 105 | **36 457** | **0,29 %** |
| `/` | 33 | 560 | 5,9 % |
| `/livres/lodyssee-des-idees/` | 18 | 239 | 7,5 % |
| `/quest-ce-que-lanthropie/` | 13 | 1 915 | 0,68 % |

**Le fait central, et il n'était pas prévu par la checklist.** La page concept **anglaise** porte
**68 % des impressions du site** et les convertit à **0,29 %**. Au niveau des requêtes, la grappe
anglaise (`anthropy`, `anthropy meaning`, `anthropy definition`, `what is anthropy`) pèse
**26 236 impressions pour 65 clics — 0,25 %** ; la grappe française (`anthropie`, `anthropie
définition`, `l'anthropie`) pèse **11 608 impressions pour 122 clics — 1,05 %**. L'anglais est vu
deux fois plus et cliqué quatre fois moins. ⚠ **Observation à vérifier avant d'en faire une cause** :
la page concept EN vit sur un **slug français**, `/en/quest-ce-que-lanthropie/` — ce que voit un
lecteur anglophone dans la SERP. Toucher cette URL engage 36 000 impressions : **arbitrage auteur,
rien n'a été modifié.**

**Confusion « Anthropocène » : mesurée, et négligeable.** Requêtes contenant `anthropoc` sur trois
mois : **5 impressions, 0 clic**, position 5,4 — soit **0,009 %** du total. La crainte portée par
la checklist depuis mai est levée par un chiffre, pas par une impression.

**Cellules restées non lues, et le motif de chacune — ce ne sont pas des zéros.**

| Instrument | État au 13/09 | Motif mesuré |
|---|---|---|
| **Zenodo** (téléchargements par AWP) | **non lu** | `zenodo_stats.py` → **HTTP 504 deux fois** avec jeton ; `curl` sans jeton → **403** sur l'API *et* sur la page publique (client refusé) ; navigation navigateur non autorisée sur le domaine. L'instrument est en défaut, ce n'est pas un résultat nul. |
| **GoatCounter** | non lu | tableau privé, inchangé depuis le 22/08 |
| **Bing « AI Performance »** | non lu | authentification interactive |
| **SSRN** `11065608` | non concluant | 403 anti-bot, comme au J+0 et au J+90 |
| **Backlinks `.edu`, mentions presse** | non instruit | recherche manuelle |

**La position ne sauve pas l'explication simple — mesuré, puis écarté.** L'hypothèse la moins
coûteuse était que la page anglaise se classe plus bas et que son CTR suive. Elle est fausse :
« anthropy meaning » est en position **5,4** pour **0,3 %**, « anthropie définition » en position
**5,6** pour **0,9 %**. Position voisine, CTR trois fois moindre. Par pays, l'écart États-Unis /
France vaut **une** position (7,0 contre 6,1) et un facteur **cinq** de CTR (0,3 % contre 1,5 %).
Le classement n'explique pas l'écart ; autre chose le fait.

**La page anglaise a déjà fait le travail de désambiguïsation — et ça ne suffit pas.** Sa FAQ
porte **14 entrées**, deux de plus que la française, dont **quatre distinctions explicites** :
l'entreprise d'intelligence artificielle au nom voisin, un **rassemblement britannique nommé
*Anthropy***, l'ère géologique, et le principe cosmologique homonyme. Le contenu dit donc déjà,
noir sur blanc, ce que la page n'est pas — et le CTR reste à 0,29 %. **Cela désavantage
l'hypothèse « la page ne dit pas assez ce qu'elle est » et renforce celle de l'intention de
recherche.** Le levier restant n'est pas dans la page : il est dans ce que l'utilisateur voit
**avant** de cliquer.

⚠ **Une erreur de cette session, corrigée avant tout envoi et dite ici.** La première version du
paquet affirmait l'inverse — que la page anglaise ne portait aucune distinction avec l'entreprise
d'IA. L'affirmation venait d'une **lecture tronquée** du fichier source, arrêtée à la vingt-deuxième
ligne, et non d'une mesure : conclure de ce que l'instrument ne montre pas. Elle était rangée en
« fait établi, ne pas revérifier », c'est-à-dire à l'endroit exact où un contradicteur ne l'aurait
pas contrôlée. Le paquet a été refait, le créneau d'audit écrasé délibérément, et **la correction
est écrite dans le paquet lui-même** (§ 10) pour que le contradicteur sache ce qui a basculé.

⚖ **Contre-expertise ouverte — `anthropie-site-20260913-101742`, type FACT_CHECK, statut
`AWAITING_MANUAL_SEND`.** La question est décidable et son coût est réel : faut-il réécrire la page
anglaise — titre, description, FAQ, voire URL canonique — ou ce CTR tient-il à une intention de
recherche que la page ne peut pas satisfaire ? Les deux réponses commandent des gestes opposés, et
l'une engage 36 457 impressions par trimestre de façon peu réversible. Six hypothèses numérotées,
la plus fragile en tête et **déclarée comme telle** : celle du chemin d'URL en langue étrangère a
été formée *en regardant l'URL*, pas en mesurant. Six décisions sont verrouillées dans le paquet
pour qu'il ne rouvre rien — le nom du concept, l'interdit des pages par requête, la clôture de la
confusion « Anthropocène », le bilan du 22/08, le dépôt canonique, le bilinguisme.

**Vérifié, pas supposé** : la pièce du sas est **octet pour octet** celle de l'OUTBOX
(`21903538…411778` des deux côtés, 12 329 octets), il n'existe **aucune copie survivante** de la
version fautive — le créneau a été écrasé en place, vérifié par énumération du sas et de
l'OUTBOX —, et son encodage est sain : BOM UTF-8, **zéro** caractère de remplacement — le
contrôle par `grep` rendait ici un faux zéro, seule la lecture Python fait foi, et `.claude/` est bien couvert par `.gitignore:15`, donc aucun risque de
fuite par le remote public. **L'envoi reste un geste auteur** ; le dossier a été ouvert dans
l'explorateur.

**Réponse reçue le 13/09, archivée puis arbitrée.** Capture verbatim `67DE1E80…2EB8`, 15 609
octets, archivée **avant toute lecture** ; copie déposée et copie d'archive vérifiées identiques
octet pour octet. Statut `RESPONSE_ARCHIVED`, arbitrage dans `ARBITRATIONS/`.

⚠ **Le `FACT_CHECK` demandé n'a pas été livré.** Le paquet réclamait, pour chacune des six
hypothèses, un verdict avec **URL, date de source et citation exacte**. La réponse n'en porte
**aucune** : les six hypothèses sont exactement aussi peu vérifiées qu'avant. La réponse se
désigne elle-même comme une relecture « avant envoi au contradicteur » — elle s'est comprise
comme un contrôle amont. **La vérification factuelle reste entièrement à faire**, et le dossier
révisé devra partir vers un canal de recherche sourcée. Ce n'est pas une perte : un audit de
raisonnement non demandé qui trouve un défaut réel vaut mieux qu'une vérification complaisante.
Mais il faut nommer ce qui est rendu, sinon on classe « vérifié » un dossier qui ne l'est pas.

**`ACCEPTÉ` — et cela invalide l'architecture du paquet, pas ses mesures.** Le § 6 posait :
*si H1 ou H2 est confirmée, alors le CTR n'est pas un défaut de la page, donc ne rien toucher*.
C'est faux. Une SERP structurellement difficile explique **le plancher général** ; elle ne dit
rien de **notre distance au plafond atteignable**. Une page peut très bien sous-performer de
moitié à l'intérieur d'un environnement déjà pauvre. **H3 — le contrefactuel chiffré — devient
la charnière de la décision, à la place de H1.** J'avais construit un dossier qui demandait une
cause là où la décision dépend d'un **écart à une référence** : « pourquoi 0,29 % ? » n'était
pas la bonne question.

**`REJETÉ` — bon instrument, calcul exact, conclusion fausse.** Le contradicteur isole le
sous-ensemble explicitement définitionnel (12 612 impressions, 38 clics, 0,301 % — arithmétique
re-vérifiée, exacte) et conclut que le redressement attendu si les homonymes étaient la cause
principale **« n'apparaît pas »**. Il l'a comparé à la **page entière** au lieu de la **requête
nue**, la seule vraiment ambiguë :

| Découpage | Impressions | Clics | CTR |
|---|---|---|---|
| `anthropy` **nue** | 13 624 | 27 | **0,198 %** |
| sous-ensemble **définitionnel** | 12 612 | 38 | **0,301 %** |

**Le redressement existe : ×1,52.** Et le **témoin français**, sur le même découpage, l'établit
comme un fait de langue : `anthropie` nue 1,049 % → `anthropie définition` 0,912 %, soit
**×0,87 — en français le qualificatif DÉGRADE**. La même opération produit un effet **inverse**
dans les deux langues : signature d'une contamination présente côté anglais, absente côté
français. Retenu malgré tout : la contamination **ne peut pas porter seule** le déficit, 0,301 %
restant très loin du français. *Cause de son erreur : il a mesuré son mécanisme sur une seule
population, alors que le contrôle français était dans le paquet qu'il lisait.*

**Décidé sans arbitrage d'auteur** : le changement d'URL canonique est **écarté** — son bénéfice
repose sur l'hypothèse la plus spéculative du dossier, pendant que son coût est réel ; le paquet
est **révisé** avant tout nouvel envoi (le lien « H1 ou H2 ⇒ ne rien faire » disparaît, H1 se
scinde en requête nue / requêtes définitionnelles, trois hypothèses s'ajoutent — extrait
réellement affiché, sous-performance à configuration comparable, fraction de trafic récupérable) ;
et **la réécriture de titre et description devient un test réversible**, pas un remède.

⚠ **Un angle mort que le paquet n'avait pas** : la métadonnée écrite n'est pas l'extrait affiché,
le moteur réécrit. Sans contrôle de ce qui s'affiche réellement, un test de réécriture peut
rendre un **faux négatif** — texte changé, extrait inchangé, et l'on conclurait que le message
n'y fait rien.

**Restent à l'auteur, et seulement eux** : le relevé manuel des SERP réelles sur quatre à six
requêtes — interroger un moteur de façon automatisée n'entre pas dans ce que cette session
s'autorise — et **une question stratégique que personne n'a posée** : la page anglaise porte
68 % des impressions pour 30 % des clics, mais *faut-il* récupérer ce CTR ? Cent clics
trimestriels de plus sur une page de concept ne valent pas mécaniquement un effort équivalent
placé ailleurs. La consultation a éclairé le « comment » ; le « faut-il » n'appartient pas à
l'arbitrage.

🔧 **Incident du dispositif, trouvé par sa propre garde.** L'import de la réponse a **refusé** de
mettre à jour l'état : deux lignes de ledger pour un seul audit. Cause : l'identifiant est lu
**dans le paquet**, donc la reprise forcée de 10:21 a réutilisé celui de 10:17, puis le ledger a
**ajouté** une ligne au lieu de remplacer — la garde d'import (« exactement une ligne par
audit ») avait raison, c'est l'écrivain qui avait tort. La capture verbatim, elle, avait bien eu
lieu : le verrou essentiel a tenu. Ledger sauvegardé puis assaini — la ligne périmée pointait un
chemin dont les octets avaient changé, sa trace est passée en colonne `notes` de la ligne qui
survit. `New-ExternalAudit.ps1` corrigé pour **remplacer** au lieu d'ajouter, sauvegarde
`.bak-20260913`, ASCII pur et syntaxe PowerShell revérifiées. Aucun identifiant perdu, aucun
doublon restant — contrôlé par énumération.

**Tour 2 — pièce externe reçue le 13/09 à 11:23, archivée puis arbitrée.** Capture verbatim
`420B124D…7889`, 4 886 octets, posée **avant lecture**, parité d'empreinte vérifiée.
⚠ **Enregistrée en annexe, pas en consultation** : l'import refuse un second dépôt dans un
créneau déjà servi — un paquet, une réponse. L'enregistrer autrement aurait exigé de fabriquer
un envoi qui n'a pas eu lieu. Le ledger ne la compte pas ; l'archive la conserve.

**Elle concède les deux verdicts du tour 1** : son passage précédent n'était pas le `FACT_CHECK`
demandé, et le redressement ×1,52 existe — « ma formulation était trop forte ». Sa seule
contestation porte sur le témoin français, qui ne serait pas un contrôle *causal* puisque langue,
SERP, concurrents et géographie changent ensemble. **`ACCEPTÉ` sur la méthode, `REJETÉ` sur la
cible** : elle attaque une conclusion que l'arbitrage n'avait pas tirée — il disait déjà que la
contamination « ne peut pas porter seule le déficit ». Et l'usage étroit survit : le bras français
ne servait pas à estimer le CTR anglais atteignable, mais de **témoin négatif sur l'opération** —
si un qualificatif définitionnel augmentait mécaniquement le CTR, le français le montrerait aussi ;
il montre l'inverse. Cela écarte une explication concurrente, cela n'en établit aucune.

**`ACCEPTÉ` et exécuté dans la foulée : la décomposition par intention.** Mesure à la source sur
la page seule — 375 requêtes, le top 10 couvrant **76 %** des impressions :

| Classe d'intention | Impressions | Clics | CTR |
|---|---|---|---|
| requête **nue / ambiguë** | 13 544 | 29 | **0,21 %** |
| **définitionnelle explicite** | 12 987 | 41 | **0,32 %** |
| **francophone servie par la page ANGLAISE** | 1 327 | 8 | **0,60 %** |
| **navigationnelle homonyme** | **0 identifiée** | — | — |

**Terminal** : mobile 21 405 impressions à 0,3 %, ordinateur 9 150 à 0,3 %, tablette 543 à 0,2 %.
**Le CTR est identique sur les trois** — la dimension réclamée n'explique rien, et c'est un
résultat, pas une case vide. Elle reste utile : **69 % des impressions sont mobiles**, là où
l'extrait affiché est le plus court.

⚠ **Deux gardes sur cette table.** Le zéro d'homonymes **ne confirme ni n'infirme** la
contamination : la console ne montre que les requêtes où ce site a été affiché, et qui tape le nom
de l'entreprise ne voit jamais cette page. Et les taux élevés de la queue sont du **bruit** —
`anthropie meaning` à 3,7 %, c'est 2 clics sur 54 impressions.

**La taille de l'enjeu, enfin chiffrée — et c'est elle qui répond au « faut-il ? ».** Sur le bloc
définitionnel, seule population où une réécriture d'extrait peut agir (12 987 impressions à
0,32 %) : porté à 0,50 % il rendrait **+24 clics par trimestre** ; au taux définitionnel français
de 0,91 %, **+77** ; au taux français sur requête nue, **+95**. À rapporter aux **354 clics
trimestriels du site entier** : entre 7 % et 27 % du trafic total. **Considérable en proportion,
modeste en volume.**

⚠ **Un facteur de la formule reste non mesurable.** Le tour 2 propose de convertir en valeur
d'opportunité — impressions récupérables × gain de CTR × **valeur d'un clic**. Les deux premiers
sont désormais chiffrés ; le troisième ne l'est pas, et le dépôt sait pourquoi : aucun clic sortant
n'est instrumenté (`GEO_COMMERCIAL_FUNNEL.md`, constat F8, pages vues seules). **La décision sera
jugée, pas calculée.**

**Une fuite mineure, nommée et non traitée** : 1 327 impressions de requêtes **françaises** sont
servies par la page **anglaise** à 0,60 %, quand la page française convertit à 1,05 % sur la même
requête — environ **6 clics par trimestre**. Trop petit pour un chantier, trop net pour un silence.

**Bilan des deux tours** : un défaut logique réel que je n'avais pas vu, une conclusion fausse que
sa propre recommandation contredisait, et **zéro source sur les deux passages**. Le `FACT_CHECK`
reste entier. Lire le verdict et le motif séparément était la bonne discipline : accepter en bloc
aurait fait entrer une fausseté au dossier, refuser en bloc y aurait laissé mon raccourci.

**Contre-expertise : NON, et le test R4 dit pourquoi.** Deux des trois conditions manquent.
*Une décision que la réponse changerait* : la seule encore ouverte est le test B — réécrire la
description. Il est **réversible et coûte une demi-heure** ; on n'achète pas d'information pour
décider d'un geste gratuit et annulable. *Un point faible que je ne peux pas lever seul* : un
seul, ce que la SERP affiche réellement — mais c'est une **observation de cinq minutes**, pas une
contre-analyse ; payer un avis sur un écran qu'on peut regarder est de la surnumérarité au sens
propre. *Un coût réel à se tromper* : C est gelée, B est réversible, et la question stratégique
n'appartient à aucun contradicteur. Deux tours ont eu lieu ; un troisième rouvrirait C ou
chercherait une confirmation.

**Vérification de la page servie — et une fausse alerte de ma part, corrigée sur pièce.** Un
premier passage d'extraction a rendu « pas de description, pas de canonique, pas de hreflang ».
**C'était mon expression régulière**, qui supposait un ordre d'attributs alors que le HTML est
minifié sans guillemets. Relu dans le brut : canonique auto-référente, `hreflang` `en` / `fr` /
`x-default`, description, `og:`/`twitter:`, deux blocs JSON-LD dont un `FAQPage`. **La page est
techniquement saine.** ⭐ Conséquence directe : la « fuite francophone » de 1 327 impressions
**n'est pas un défaut de `hreflang`** — la déclaration est correcte, c'est Google qui choisit.
Question close, rien à corriger.

**Le seul défaut objectif trouvé, et il est mesurable :** la description servie faisait
**88 caractères** là où le moteur en affiche **~155 sur ordinateur et ~120 sur mobile** — et
**69 % des impressions de cette page sont mobiles**. Deux tiers de l'espace d'extrait étaient
inutilisés, ce qui augmente aussi la probabilité que le moteur substitue son propre texte.

**Test B posé — une seule variable, non poussé.** La description passe à 150 caractères, dont la
coupe mobile tombe sur une clause complète. **Le titre n'est pas touché** : son suffixe vient de
`head.html:11` et vaut pour tout le site ; le changer ferait varier deux choses à la fois.
`lastmod` **n'est pas bousculé** — le corps n'a pas changé, et une fausse fraîcheur serait une
faute. Rendu vérifié **par la sortie du build**, pas par relecture de la source : les 150
caractères sortent bien dans `public/`.

⚗ **Protocole pré-enregistré — écrit avant le déploiement, pour que le résultat ne se lise pas
après coup.**

- **Population** : les cinq requêtes définitionnelles de cette page — `anthropy meaning`,
  `anthropy definition`, `what is anthropy`, `antropy meaning`, `anthrophy meaning`.
- **Référence** : **12 987 impressions, 41 clics, 0,316 %**, trois mois glissants au 13/09.
- **Relecture** : trois mois après déploiement, mêmes requêtes, même page.
- ⚠ **Garde préalable, sans quoi le test est NUL** : vérifier que l'extrait **affiché** a
  réellement changé. S'il n'a pas changé, on n'a pas testé la description — on a testé la
  réécriture du moteur, et le résultat ne dit rien.
- **Règle de décision, et elle est adossée au bruit** : l'écart-type du comptage est de
  **6,4 clics**. Donc **< 0,45 %** (≤ 2,7 σ) → **non concluant**, ne rien généraliser ;
  **≥ 0,50 %** (3,7 σ, soit +24 clics) → **levier réel**, appliquer le même traitement aux autres
  pages anglaises à fort volume ; **retour sous 0,32 %** → annuler, la description précédente est
  conservée en commentaire dans le fichier pour que le retour arrière soit immédiat.
- **Ce que le test ne dira pas** : si le gain vient de la longueur, du contenu ou de la levée de
  confusion. Une seule variable a bougé, mais elle en porte trois.

**Une seule modification du site, et c'est une expérience** : la description de la page concept
anglaise. Tout le reste de cette entrée est du journal, plus le renvoi ajouté au § 5.7 du rapport
du 22/08. Le paquet de contre-expertise vit hors dépôt suivi.

### 2026-09-13 — MPRA, sonde AWP-07 à J+32 : le contrôle ne mesurait rien, et la sonde non plus

`check_deposits_status.py` rendait, pour le dépôt test du 12/08 (`130468`), l'étiquette
**« EN MODERATION »**. Elle reposait sur une seule règle : `401/403 => encore en review`.
**Contre-témoin passé ce jour : la règle ne discrimine rien.**

| Identifiant interrogé | HTTP | Corps | OAI-PMH `GetRecord` |
|---|---|---|---|
| `130468` — sonde du 12/08 | **401** | 381 o, « 401 Unauthorized » | `idDoesNotExist` |
| `128604` — lot bloqué du 07/04 | **401** | 381 o, identique | `idDoesNotExist` |
| `99999999` — **identifiant qui n'a jamais existé** | **401** | 381 o, identique | `idDoesNotExist` |
| `129034` — AWP-06, témoin positif | **200** | 30 293 o, titre réel | notice complète, `datestamp 2026-05-15T17:20:43Z` |

Un dépôt en file, un refus, un retrait et un identifiant absurde rendent **la même réponse, à
l'octet près**, sur les deux interfaces publiques. « En modération » n'était pas une mesure, c'était
la valeur par défaut de tout ce qui n'est pas un enregistrement public. **Ce qui est établi au
13/09 : `130468` n'est pas publié. Rien de plus.** La seule source qui tranche est le compte auteur
MPRA (*Manage deposits*) — **elle a été lue par l'auteur le jour même** : **tous** les dépôts,
la sonde du 12/08 comme le lot du 07/04, y sont **« Under review »**. Aucun refus. L'indécidable
est levé, et il l'est par une notification de guichet, jamais par un code HTTP.

**Correction posée dans le même geste** : le script interroge désormais le contre-témoin à
**chaque exécution** et compare les codes au lieu de les interpréter ; l'étiquette devient
`NON PUBLIE (indiscernable : en file / refuse / retire)` ; un code inédit est signalé comme tel au
lieu d'être absorbé ; et si **aucun** `200` ne sort de la série, le détecteur se déclare
possiblement en panne plutôt que de rendre sept verdicts. C'est la **seconde occurrence de la même
classe dans ce fichier** : `SSRN_SANS_ID` porte déjà, depuis le 17/08, la note « un manquant déguisé
en zéro ». La leçon avait été appliquée à SSRN et pas à MPRA, dans le même écran.

**Les durées, maintenant qu'elles veulent dire quelque chose.** AWP-06, déposé **seul**
le 08/05, était en ligne le **15/05** : sept jours. AWP-07, déposé seul et espacé le 12/08,
est à **32 jours** ; le lot de six du 07/04 est à **159 jours**. La consigne couvre deux cas
— accepté → déposer AWP-08 seul et espacé ; silence à J+14 → attendre J+30 — et **J+30 est
passé le 11/09**. Reste à savoir ce que ces jours mesurent.

**Contre-population : la sonde ne mesurait rien parce qu'elle n'avait pas de témoin.** « Tous nos
dépôts sont *Under review* » explique 100 % d'**une seule** population — la nôtre. Mesure du 13/09
sur les **voisins d'identifiant**, c'est-à-dire les dépôts d'autres auteurs posés aux mêmes dates
(EPrints attribue l'identifiant au dépôt ; vérifié sur pièce : `130482` porte
« Date Deposited: 16 Aug 2026 ») :

| Bande | Dépôts contemporains de | Publiés chez les autres auteurs |
|---|---|---|
| `130455-130484` | notre sonde du **12/08** | **1 sur 29** — 3 % |
| `129020-129049` | AWP-06, accepté en 7 j le **15/05** | **16 sur 29** — 55 % |
| `128592-128621` | notre lot du **07/04** | **7 sur 25** — 28 % |

**Notre sonde est dans la majorité écrasante de sa cohorte, pas dans une exception.** 97 % des
dépôts d'août sont, comme elle, non publiés : son silence à J+32 ne dit donc **rien** sur le compte.
Et notre lot d'avril n'est pas non plus un cas isolé — 72 % de ses voisins sont dans le même état.
**L'hypothèse « le blocage suit le compte » perd son appui ; celle du lot ne le retrouve pas.** Ce
qui ressort est plus simple : la file de MPRA ne draine plus les cohortes récentes.

⚠ **Deux réserves, dites et non lissées.** La bande d'avril (28 %) est **moins** publiée que celle
de mai (55 %) alors qu'elle est plus ancienne : inexpliqué, et aucune hypothèse n'est proposée ici
faute de mesure. Et un `401` chez un autre auteur mélange lui aussi file d'attente et refus — les
taux ci-dessus sont un **plancher** de lenteur, pas une mesure propre de la file.

⚠ **Ce que cette mesure oblige à rouvrir, sans le trancher.** La doctrine du dépôt échelonné
(`CLAUDE.md` § 3 ter) s'appuie sur un chiffre : « 5 dépôts en 18 minutes le 07/04 restés bloqués
118 jours, alors qu'un dépôt isolé le 08/05 a été accepté en 7 jours ». Ces deux dépôts
appartiennent à **deux cohortes de rendement très différent** — 28 % contre 55 %. La comparaison
n'isole donc pas l'effet du lot ; elle peut n'en mesurer aucun. Cela **ne réfute pas** la doctrine,
qui garde un appui indépendant (le refus SocArXiv du 14/05 invoquait explicitement une suspicion
de *reference spamming*). **La doctrine n'est pas touchée : sa révision est un arbitrage d'auteur,
et ce qui est signalé ici, c'est que sa preuve chiffrée n'a jamais eu de contre-population.**

**Décision de la sonde, et elle est nette.** AWP-07 est en examen, pas refusé ; sa lenteur est
celle de sa cohorte. Donc : **aucun dépôt nouveau** — la condition d'AWP-08 est l'*acceptation*
d'AWP-07, pas l'écoulement d'un délai ; **aucune relance** — réclamer contre un délai que 97 % des
dépôts contemporains subissent serait du bruit, sur un compte dont une réclamation a déjà été
rejetée le 04/08 ; **aucune échéance courte** — la prochaine vérification n'a d'intérêt qu'après un
mouvement de cohorte, pas après un nombre de jours.

⏰ **Report arbitré par l'auteur le 13/09 : vérification dans quatre semaines, soit le 11/10/2026.**
La bonne lecture ce jour-là n'est pas « combien de jours » mais **le rendement de la cohorte d'août** :
relancer la mesure de contre-population ci-dessus et comparer au 3 % du 13/09. Un taux qui monte
sans nous dit quelque chose du compte ; un taux qui reste bas ne dit rien de nous.

### 2026-09-13 — Search Console, J+7 du relevé du 02/09 : les deux listes de publications sont indexées

Rappel armé le 02/09 (RDV Outlook du 09/09), exécuté ce jour par inspection d'URL dans Search
Console, propriété `sc-domain:stephane-lalut.com`, via Chrome. Relevé lu à la source, page par page :

| URL | Verdict | Dernière exploration | Canonique déclarée | Canonique retenue par Google |
|---|---|---|---|---|
| `/en/publications/` | **indexée** | 2 sept. 2026, 14:47:44 | elle-même | **l'URL inspectée** |
| `/publications/` | **indexée** | 11 sept. 2026, 22:33:19 | elle-même | **l'URL inspectée** |

Les deux constats du 02/09 sont levés. `/en/publications/` était « détectée, actuellement non
indexée » et n'avait jamais été explorée : elle l'a été le jour même de la demande, à 14:47, et
elle est aujourd'hui sur Google — la demande d'indexation a donc porté. `/publications/`, qui
n'avait plus été explorée depuis le 31/07, l'a été le 11/09 à 22:33, **le soir même d'une seconde
demande** déposée à la parution du compte rendu Pugh (`00_PILOTAGE/HANDOFF.md` : « indexation de
`/publications/` demandée le 11/09 au soir »). Aucune demande n'a été déposée ce jour : les deux
pages sont indexées, elle serait sans objet.

**La branche conditionnelle du rappel ne se déclenche pas, et son hypothèse tombe avec elle.**
Elle prévoyait, en cas de non-indexation, de chercher pourquoi Google déprioriserait la liste
anglaise, la piste nommée étant le quasi-doublon : `content/publications/` ne porte qu'un seul
fichier anglais, `_index.en.md`, pour 21 notices — vérifié ce jour — donc la liste EN rend bien
les cartes FR par repli. Le fait de contenu est exact ; il n'a rien empêché. Google a retenu
chaque page comme sa propre canonique, sans regrouper l'une sur l'autre : il n'y a pas de doublon
du point de vue de l'index, donc pas de remède à proposer. Ni `hreflang` ni maillage interne ne
sont touchés.

**Ce que ce relevé ne dit pas, et il faut le dire.** Les deux dates d'exploration suivent chacune
une demande manuelle — le 02/09 pour la page EN, le 11/09 pour la page FR. Elles ne mesurent donc
pas le rythme d'exploration spontané, ni d'un côté ni de l'autre, et l'écart apparent entre le
02/09 et le 11/09 ne mesure que l'écart entre les deux demandes. La question du rythme ne se posera
qu'à une parution **non** accompagnée d'une demande, ou le jour où une notice réellement anglaise
sera publiée sous `/en/publications/`. Aucun dispositif n'est armé pour cela : il n'y a pas de
défaut constaté à surveiller.

**Dispositif éteint.** Le relevé du 02/09 portait sa condition de mort — « à revérifier à J+7 ;
passé ce délai, ce relevé redevient une hypothèse ». Elle est remplie : le relevé est refait à la
source, il n'y a plus rien à surveiller, et le RDV Outlook du 09/09 n'a plus d'objet. **Sa
suppression est un geste auteur** : Outlook n'est pas piloté d'ici.

### 2026-09-13 — /ressources-offertes/ : relevé Amazon du jour, et « Nouveauté » au lieu d'un compte maigre

**Relevé Amazon.fr**, un mois après celui du 12/08, lu fiche par fiche : ANTHROPIE 4,4 (22 → 26),
Dette Publique 4,2 → 4,3 (27 → 29), Livresque des mots 4,1 (87 → 88), L'Odyssée des idées 4,4
(162 → 165), La Société du premier coup 5,0 sur 4 avis — sa première note. Aucune en baisse.

**Badge « Nouveauté »** (demande auteur). La règle proposée — moins de 6 mois → badge à la place
de la note — aurait masqué les 165 avis de L'Odyssée, dont l'édition a dix semaines. Arbitrage
retenu : **c'est le nombre d'avis qui déclenche**, pas l'âge. Note dès `socialProofMinReviews`
(10) ; en dessous, « Nouveauté » si la parution est dans `noveltyWindowMonths` (6) ; sinon rien,
soit l'affichage d'avant. La bascule vers la note se fait au 10e avis, sans geste.

Trois points de méthode, chacun trouvé par un contrôle et non par relecture :

1. **La date du front matter n'est pas la parution** (signalé par l'auteur) : `date` porte
   l'édition courante — L'Odyssée affiche 2026-07-03 pour un livre paru le 19/02/2024, dont elle
   a hérité les avis (ASIN Kindle conservé comme ancre). Sans correctif, un livre de deux ans
   réédité se serait annoncé « nouveauté ». La fenêtre lit désormais `first_published`, repli sur
   `date`. Écart ouvert : `works.yaml:612` dit « première édition 2023 », Amazon dit février 2024
   — sans effet sur une fenêtre de 6 mois, non tranché.
2. **`time.AsTime` est obligatoire** : comparée telle quelle à un `time.Time`, une valeur de front
   matter rend `gt` toujours faux — badge qui ne s'allume jamais, panne muette. Le témoin T4
   (« le badge doit disparaître ») passait alors **par accident** ; seul T2, qui exige qu'il
   s'allume, l'a révélé.
3. **Une règle, un exemplaire** : la note était dupliquée dans `list.html` et `single.html`. Les
   deux appellent maintenant `partials/preuve-sociale.html` ; le seuil et la fenêtre vivent dans
   `params.toml`, jamais en dur dans un gabarit.

Mesure : build 0.147.0 vert ; sur la liste et sur les cinq fiches, quatre notes et un badge, aucun
livre n'affichant les deux ; témoin par mutation réelle 4/4 (seuil franchi → note ; sous seuil et
parution récente → badge ; `first_published` retiré → faux badge ; remis → rien), fichiers
restaurés à l'identique. `check-all.py --ci` 0/3.

### 2026-09-13 — Vignettes de publication : liseré bleu nuit sur la variante crème

La variante crème de la tuile logo (`.pub-thumb--logo--cream`) avait pour fond `#FAFAF6`,
soit **exactement** `--color-bg` ; son cadre 160×107 ne se séparait du fond que par un filet
`#EEEBE6`, douze unités d'écart mesurées en `getComputedStyle` sur le site en ligne. Dix tuiles
sur vingt étaient dans ce cas : l'alternance navy/crème ne se lisait plus comme un damier mais
comme une case sur deux manquante — sur `/publications/` comme sur le mur presse d'`/a-propos/`.

Correction : `border: 1px solid rgba(27, 42, 78, 0.35)`, liseré tiré de l'accent bleu nuit
(`#1B2A4E`) et non d'un gris de filet, dilué pour rester discret face aux tuiles navy pleines.
Un seul point patché, `assets/scss/_publication-card.scss` : le mur presse réemploie le gabarit
des cartes publications, donc les deux pages sont servies par la même règle.

Vérifié par la sortie et non par le code : build local Hugo 0.147.0, `getComputedStyle` rend
`rgba(27, 42, 78, 0.35) 1px` sur les deux pages, captures avant/après. `check-all.py --reseau`
sort 6 contrôles à 0.

### 2026-09-11 — Publication : compte rendu Pugh, *Sociologie du travail* vol. 68 n° 2

Compte rendu CR26023 de *The Last Human Job* (Allison J. Pugh, Princeton UP, 2024), mis en ligne
le 09/09 sur OpenEdition : https://journals.openedition.org/sdt/50224. Fiche
`content/publications/sociologie-du-travail-pugh.md` selon `docs/CHECKLIST_AJOUT_PUBLICATION.md`
(logo, noindex, hors sitemap). Première parution dans la revue : `source_type` Académique, et la
revue entre dans la table § 2 de `NOTES_PUBLICATIONS.md` (commit `docs:` séparé).

**Fil remontant** : `related: [awp-01, awp-06]`. Le compte rendu lit le « paradoxe tragique » de
Pugh comme un report : ce que les organisations ne mesurent pas passe aux personnes qui exercent le
travail relationnel et à celles qu'elles accompagnent, c'est le déplacement que pose AWP-01 ;
scripts, métriques et chatbots « mieux que rien » en sont le versant numérique, celui d'AWP-06.
`related_book: anthropie-ordre-ici-dette-ailleurs`.

**Registres synchronisés dans le même commit** : `data/works.yaml` v1.18 (`art-sdt-pugh-2026-09` ;
42 œuvres = 29 articles + 8 AWP + 5 livres, compte relu par lecture YAML) ; `data/intent_matrix.yaml`
v1.5 (entrées travail + IA/numérique) ; `presse_objets` FR/EN (« Travail de connexion » /
« Connective labour ») ; `static/llms.txt`, où la revue rejoint la liste.

**La consigne de l'éditrice vaut pour chaque surface.** Le texte est sous CC BY-NC-ND 4.0 : le
post-print peut aller en archive ouverte institutionnelle, jamais sur Academia, Mendeley,
ResearchGate ou SSRN, et l'éditrice demande de renvoyer vers la page de consultation plutôt que vers
le PDF. Carte, `ItemList`, flux RSS et registre pointent `…/sdt/50224` ; `sdt/pdf/50224` apparaît
0 fois dans `public/`. La même règle est écrite dans la navette Wikidata (`P953`) et dans les notes
de l'entrée du registre. Message de l'éditrice archivé verbatim :
`D:\PRO\08_ARTICLES\SOCIOLOGIE DU TRAVAIL\Tire_a_part_CR26023_2026-09.txt`, SHA-256 `946acc82…c1ac0e`
identique à la pièce reçue.

**Preuves** : `hugo --minify` vert ; carte sur `/publications/` et `/en/publications/`, sur AWP-01,
AWP-06 et leurs miroirs EN, et dans « Dernières parutions » de l'accueil FR et EN ; tuile du mur
presse FR et EN ; `ListItem` en position 1, `ScholarlyArticle`, `isPartOf` *Sociologie du travail* ;
`&lt;em&gt;` absent ; fiche noindex et absente des trois sitemaps ; `check-all --reseau` à 0 sur
6 contrôles ; `check_forme.py` conforme sur les deux chapôs.

**Après push (`4b46eb1`, demande de l'auteur)** : déploiement (run 34632443818) et IndexNow
(34632443848 : 59 URL, HTTP 200) verts. Relu en ligne, cache contourné : carte sur `/publications/`
FR/EN, l'accueil FR/EN et AWP-06 ; objets du mur presse FR/EN ; fiche noindex ; `llms.txt` à jour ;
`sdt/pdf/50224` absent.

**Restes nommés** :

1. **DOI** : ✅ `10.4000/16rju`, déposé chez Crossref le 11/09 à 18:54 UTC, auteur rattaché à son
   ORCID ; il résout vers la page de consultation. Clé `doi` posée en fiche et au registre. La notice
   ne porte que l'année : la date du bloc « Pour citer » (09/09) est gardée.
2. **Wikidata** : ✅ item **Q141435769** créé par Laura le 11/09 à 20:09 UTC, readback API conforme
   (12 déclarations) ; écriture en retour faite — `wikidata` au registre, `wikidata_qid` en fiche,
   donc `sameAs` dans l'`ItemList`. Dossier : `Wikidata/Import_Wikidata_Laura_2026-09-11_Recension_SdT_Pugh/`.
3. **ORCID** : ✅ fait le 11/09 par saisie manuelle dans la session de l'auteur (Chrome).
   Relu à l'API publique : 38 works, put-code `226452428`, type `book-review`, visibilité
   publique, lien = page de consultation, langue `fr`. DOI ajouté le soir même (identifiant
   `doi`, relation *self*, relu à l'API) : la notice Crossref portant l'ORCID, son import
   automatique se regroupera avec cette entrée au lieu de la doubler.
4. **Search Console** : demander l'indexation de `/publications/` après le push (checklist § 4).

### 2026-09-09 — Open Library, ticket 1605786 : réponse du 07/09 dépouillée, le fantôme d'index survit

Réponse de Sapphire (Internet Archive) datée du **07/09**, deux phrases, qui répondent au tour
**précédent** — la suppression des éditions doublons est « une exception », les candidatures
bénévoles sont revues « as time allows ». **La seule demande du message du 03/09 n'y est pas
traitée** : la réindexation de `OL45424565W`.

**Mesuré à la source le 09/09**, et non déduit de l'échange :

| Objet | Mesure | Verdict |
|---|---|---|
| `OL45424565W` (donnée) | `/type/redirect` → `/works/OL45424564W`, `last_modified` 2026-08-26T14:21 UTC | fusion **vraie** |
| `search.json?q=author_key:OL16378291A` | `numFound = 6`, dont `/works/OL45424565W` à **0 édition** | index **faux** |
| Page auteur publique | affiche « **6 works** », le work fantôme cité 13 fois dans le HTML | ce que le lecteur voit est faux |
| `OL45424600W`, `OL45424545W` (mêmes fusions du 26/08) | `numFound = 0` chacun | **désindexées correctement** |
| `OL16378291A` (donnée) | révision 4, `remote_ids` = wikidata + viaf + goodreads | **soldé** |
| `usergroup/librarians.json` (157 m.) et `super-librarians.json` (26 m.) | `st_phane_lalut` **absent des deux** | LiT **non accordé**, 18 j après l'envoi |

Les deux redirections sœurs prouvent que ce n'est pas le comportement normal d'une redirection :
**un seul document Solr n'a pas été retiré**. C'est la classe *état déclaré ≠ état réel* — rien
n'échoue, la donnée est juste, et le catalogue public montre un doublon vide sous le nom d'un livre.

Défaut de méthode relevé et corrigé dans la session : un premier `curl -o` a écrit un fichier de
**0 octet** sans erreur, et le `grep` qui l'a lu a rendu « 0 occurrence » — soit exactement
l'inverse de la vérité. *Un parseur qui ne sait pas lire n'a pas trouvé un vide* : la mesure n'a
été retenue qu'après contrôle de la taille du corps récupéré (80 613 octets).

**Fait** : relance courte rédigée sur le seul point non traité →
`reports/openlibrary/RELANCE_TICKET_1605786_2026-09-09.txt`. **Envoi = geste auteur.**

Rédaction reprise après relecture de l'auteur, sur un défaut réel de la première version. Le
« just to be clear, record deletion is not something we typically do » n'est pas une remarque
générale : il répond à une phrase précise du message du 02/09 — *« I will treat an edition
duplicate as a deletion request rather than a merge from now on »* —, c'est-à-dire à un
**précédent que nous venions d'annoncer**. Un simple accusé de réception (« understood on both
counts ») laissait cette intention debout ; la lettre la **retire** explicitement. Deux autres
conséquences : le sujet LIT est **clos par écrit** (« no need to reply ») plutôt que passé sous
silence, ce qui évite qu'OL redoute une relance de plus ; et la demande de réindexation est
d'emblée **sortie de la classe visée par l'avertissement** — ni modification d'enregistrement,
ni faveur, mais le reliquat d'une fusion déjà faite. ⭐ *Répondre à un avertissement de
support, c'est retirer le geste qui l'a déclenché, pas en accuser réception.*

### 2026-09-02 — Publication : « Le passé recalculé » (En attendant Nadeau n° 249)

Recension de l'*Histoire culturelle de l'IA* (Alexandre Gefen dir., CNRS Éditions, 380 p.),
parue le 02/09. Fiche `content/publications/en-attendant-nadeau-gefen.md` selon
`docs/CHECKLIST_AJOUT_PUBLICATION.md` (logo, noindex, hors sitemap).

**Fil remontant** : `related: [awp-02, awp-06]` — l'histoire longue d'un principe et la
question de l'anachronisme (AWP-02) ; la base matérielle de l'IA, dont les travailleurs du
clic que le volume tient à la marge (AWP-06). `related_book: lodyssee-des-idees` — histoire
culturelle des idées jusqu'à l'intelligence artificielle.

**Registres synchronisés dans le même commit** : `data/works.yaml` v1.14
(`art-ean-gefen-2026-09` ; 41 œuvres = 28 articles + 8 AWP + 5 livres, compte réel vérifié) ;
`data/intent_matrix.yaml` v1.4 (inscription, entrées IA/numérique + histoire des idées) ;
`presse_objets` FR/EN (« Histoire de l'IA » / « History of AI »). `static/llms.txt` inchangé :
sa section publications énumère les revues, En attendant Nadeau y figure déjà.

**Preuves** : `hugo --minify` vert ; carte présente sur `/publications/`, `/en/publications/`,
`/awp/awp-02/`, `/awp/awp-06/` et leurs miroirs EN ; tuile du mur presse `/a-propos/` FR et
EN ; URL dans l'ItemList JSON-LD ; `&lt;em&gt;` absent du rendu ; fiche noindex et absente du
sitemap ; `check-corpus-counters`, `check-fiches-registre`, `check-geo-coverage` à 0 ;
`audit_works` 0 échec.

**Après push (`a60a0c8`, rebasé sur le commit Wayback du 01/09)** : déploiement et IndexNow
verts (59 URL, HTTP 200). **Search Console, 02/09** (commande auteur, via Chrome) :
indexation demandée sur 8 URL — `/publications/`, `/en/publications/`, `/a-propos/`,
`/en/a-propos/`, `/awp/awp-02/`, `/awp/awp-06/` et les deux miroirs EN des AWP.
**Relevé externe daté** : `/publications/` n'avait plus été explorée depuis le 31/07 ;
`/en/publications/` était **« détectée, actuellement non indexée »**, jamais explorée — la
liste anglaise n'existait pas pour Google avant cette demande. À revérifier à J+7 par
inspection d'URL ; passé ce délai, ce relevé redevient une hypothèse. **Rappel armé** : RDV
Outlook du 2026-09-09 09h00, rappel actif, corps = la commande à coller (canal doctrinal,
un seul). La vérification elle-même exige la session Search Console : aucune routine cloud
ni script ne peut l'exécuter sans identifiants API que l'auteur devrait créer lui-même.
**→ Rappel soldé le 13/09 : les deux URL sont indexées, dispositif éteint (entrée du 13/09).**

**Wikidata, même session — deux items « à créer » qui existaient déjà.** Question auteur : les
publications doivent-elles être sur Wikidata ? Réponse actée : oui pour les recensions en revue à
comité de lecture avec DOI, non pour la presse intellectuelle sans DOI (notabilité, auto-promotion).
Les deux recensions *Lectures* (Kaba, Ridde) ont été annoncées « à créer » sur la foi de
`works.yaml` ; la recherche `haswbstatement:P356=<DOI>` à la source a rendu **`Q141072264`** et
**`Q141072265`**, créés le **15/08 par Laura** dans le lot du livre `Q141072263` et jamais
reportés au registre — la classe même que le `README.md` de `Wikidata/` décrit. Fait : écriture
en retour (`works.yaml` v1.15), dossier daté reconstruit
`Wikidata/Import_Wikidata_Laura_2026-08-15_Recensions_Lectures/` avec readback API. Exclusion
déclarée : les fiches publications ne portent pas de `wikidata_qid` et aucun gabarit ne l'émet ;
un `sameAs` par item de l'`ItemList` reste un point ouvert nommé.

**Navette préparée le 02/09 pour Laura** (commande auteur) : références `S854` + `S813` sur `P50` et
`P356` des deux items — dossier `Wikidata/Import_Wikidata_Laura_2026-09-02_References_Lectures/`
(4 lignes, lien direct), **en attente d'exécution** ; readback API à faire ensuite, puis ✅ dans
le `README_LAURA.md` du dossier. **Exécutée par Laura le 02/09 à 15h05 UTC** : readback du 03/09
conforme (1 référence sur `P50` et `P356` des deux items, 8 propriétés, aucune déclaration nouvelle).
**Reste** : les 2 descriptions es/de de `Q138909233`, ajoutées au lot après sa première version, n'ont
pas été posées — lien direct `deeplink_reste.txt` (2 commandes) dans le même dossier.
**Posées par Laura le 02/09 à 22h51 UTC** ; readback du 03/09 : textes identiques au lot, 17 propriétés,
rien d'autre touché. Navette close, aucun reste.

**Vérification de `Q138909233` (commande auteur, 02/09, relecture API).** Identifiants tous
présents et conformes à `data/author.toml` (ORCID, OpenAlex, Google Scholar, Academia, SSRN, IdRef,
SocArXiv ; en plus VIAF et OpenLibrary `OL16378291A`, l'auteur canonique post-fusion) ; `P800`
porte les 5 livres, le concept, la série et les 8 AWP. **Deux défauts** : descriptions es/de
fautives (corrections ajoutées à la navette du 02/09, 6 lignes désormais) ; et surtout **19 items
portent `P50` → auteur alors que le registre n'en connaissait que 9** — les 8 AWP
(Q139771989…994, Q140446195, Q140680750), la série (Q139040913) et l'item de la recension RFSE
seule (Q141072266, distinct du bloc à DOI Q140892752) n'existaient nulle part dans `data/` ni
`content/`. Fait : `works.yaml` v1.16 (10 QID écrits en retour) ; `wikidata_qid` posé sur les
16 fiches AWP (FR+EN, même item) ; `head.html` ajoute ce QID au `sameAs` du `ScholarlyArticle`
— la chaîne « item → registre → fiche → sameAs » est bouclée pour les AWP comme pour les livres ;
`check-fiches-registre.py` étendu aux AWP (parité registre ↔ fiche FR et EN). Mapping AWP ↔ QID
confirmé par égalité des DOI Zenodo FR sur les 8.

**Protocole (commande auteur : « éviter cela à l'avenir ; d'autres trous ? »).** La classe est « un
nœud externe connaît une œuvre, le registre l'ignore » ; le seul contrôle qui la voit part du **nœud**
vers le registre, jamais l'inverse. (1) `scripts/check-wikidata-registre.py` : requête inverse
`haswbstatement:P50=Q138909233` contre tous les QID du registre, deux sens, témoin par mutation sur
copie (QID retiré → écart ; QID inexistant → « inexistant » ; ancien doublon Livresque `Q138911600`
→ « redirigé ») ; raccordé aux trois checklists, au `README.md` de `Wikidata/` (le bloc ✅ cite
désormais le commit d'écriture en retour et la sortie du script) et au `CLAUDE.md`. Pas de tir
mensuel en CI : le geste qui crée le trou est une clôture de navette, c'est là que le contrôle se
lance. (2) Même logique appliquée aux autres nœuds (`scripts/sondage-noeuds-externes.py`, condition
de mort écrite en tête) : **Crossref par auteur** → le DOI Cairn de l'article Revue Projet
(`10.3917/pro.412.0078`) n'était ni au registre ni en fiche — écrit, la carte l'affiche ;
**OpenLibrary par auteur** → 4 livres sur 5 sans bloc `openlibrary` au registre, les œuvres
canoniques post-fusion ne vivaient que dans ce journal — écrites (v1.17) ; **site ↔ registre**
(19 fiches / 19 articles publiés, deux sens) et **listes manuelles** (`intent_matrix`,
`presse_objets` FR/EN) : à zéro ; **Zenodo** : la direction communauté → registre est déjà couverte
par `zenodo_audit_complet.py` (jeton requis, à lancer par l'auteur) ; **ORCID / OpenAlex** :
couverts par `audit_works.py`. Sondage relancé après écritures : 0 écart. Exclusion déclarée : les
fiches livres n'émettent pas de `sameAs` OpenLibrary (point ouvert GEO, pas un trou de registre).

### 2026-09-02 (suite) — Chaîne d'activation SEO/GEO à chaque publication ou livre (commande auteur)

**Relevé d'abord, construction ensuite.** Ce qui s'activait déjà seul à un push : build et déploiement,
sitemaps FR/EN, IndexNow (Bing/Yandex/Naver, 59 URL), flux RSS par section, JSON-LD (Person, Book,
ScholarlyArticle, ItemList), archivage Wayback mensuel. Ce qui restait manuel ou muet, et que le relevé
a montré : `/a-propos/`, `/serie-awp/` et `/en/publications/` **sans `lastmod`** dans le sitemap — une
parution changeait le mur presse sans qu'un moteur en soit averti ; le flux RSS des publications
pointait la **fiche interne noindex** au lieu de l'article ; l'`ItemList` de `/publications/` ne portait
que nom et URL ; l'accueil décrivait les publications par une phrase fixe ; les fiches d'articles à
item Wikidata ne l'émettaient pas. Google ne reçoit rien d'IndexNow : sa découverte tient au sitemap,
aux liens internes depuis les pages les plus explorées, et à la demande manuelle (checklist § 4).

**Construit — tout dérive du dépôt, aucune valeur recopiée** :

- `layouts/sitemap.xml` (surcharge du gabarit embarqué 0.147) : une page portant `aggregates:` prend
  pour `lastmod` la fiche la plus récente des sections qu'elle agrège, lue sur le site FR ; posé sur
  `/a-propos/`, `/serie-awp/`, `/publications/` (FR+EN). Preuve : `/a-propos/` et `/en/publications/`
  → `2026-09-02`, `/serie-awp/` → `2026-07-23` (AWP-08). Aucune fausse fraîcheur : pas de `:git`.
- `layouts/publications/rss.xml` : items = publications FR, `<link>` et `<guid>` = l'article externe,
  description = chapô dans la langue du flux ; autodiscovery `rel=alternate` déjà émise par `head.html`.
- `head.html` : chaque `ListItem` de `/publications/` porte l'objet complet — `Article` ou
  `ScholarlyArticle` selon `source_type`, `datePublished`, `isPartOf` (revue), `identifier` (DOI),
  `sameAs` (Wikidata) — depuis le front matter des fiches ; `wikidata_qid` posé sur les 3 fiches
  d'articles à item (RFSE → item de la recension seule `Q141072266` ; Lectures Kaba, Ridde).
- `layouts/index.html` : bloc « Dernières parutions » (3 dernières, FR et EN, liens vers l'article)
  dérivé du corpus — la page la plus explorée porte la nouveauté au build suivant, sans geste.
- `scripts/check-all.py` : un seul geste pour tous les contrôles (`--ci` hors réseau, `--reseau`
  complet) ; `check-fiches-registre.py` étendu aux **articles** (fiche retrouvée par `url_externe`,
  QID attendu = `wikidata_review` sinon `wikidata`) ; témoin : QID faussé sur la fiche Kaba → le
  runner sort 1 avec l'écart nommé, puis restauration.
- **Porte CI** : `hugo.yml` exécute `check-all.py --ci` après le build et avant l'artefact — un
  dépôt incohérent ne se déploie pas. Les contrôles réseau restent locaux (checklists, `CLAUDE.md`).

**Écarté, et dit** : générer `llms.txt` au build — doctrine du 15/08 (neutre pour Google, on n'y
investit plus) ; automatiser la demande d'indexation Google — pas d'API (URL Inspection est en
lecture seule, Indexing API réservée aux offres d'emploi/directs) ; pages nouvelles par requête —
anti-doorway. **Reste manuel, et gardé** : Search Console à chaque parution (checklist § 4), navette
Wikidata (Laura), OpenLibrary pour un livre. Vérification : `check-all --reseau` à 0 sur 6 contrôles ;
build vert ; IndexNow se déclenchera au push (`layouts/**`, `content/**` dans ses chemins).

### 2026-08-17 — La dette passe en anglais : `/en/cost-of-french-public-debt/`

**Motif** (question auteur sur le déséquilibre 14 mailles FR / 3 EN) : le vrai écart n'était
pas le nombre, mais celui entre **la dépense et la surface** — *ANTHROPY* en vente, campagne
Ads US live, et trois pages de traction pour les recevoir. La dette est le seul terrain où
l'actif est **non substituable** : un jeu de données sous licence ouverte, pas de la prose.

**L'arbitrage qui commandait tout le reste.** Le bloc `affichage` du JSON contient des chaînes
**préformatées en français** — `3 536,1`, `T1 2026`, `17/08/2026`. Les afficher sur une page
anglaise aurait été **faux**, pas seulement inélégant. L'invariant du pipeline étant « tous les
nombres viennent du JSON, Hugo reste bête », la locale se règle **dans le script** : un bloc
`affichage_en`, **36 clés identiques**, produit par le **même corps de fonction**
(`bloc_affichage(nb, quarter, date)`) — les deux blocs ne peuvent donc diverger sur les
*valeurs*, seulement sur le format.

**Figures.** Les deux SVG portaient leur texte en dur en français. Générateurs paramétrés par
locale (`LABELS_CISEAU`, `LABELS_TAUX`) → `ciseau-dette-interets-en.svg`,
`taux-apparent-dette-en.svg`. Défaut trouvé au rendu : la même figure affichait `117.5 %` et
`1.3% in 2020` — l'espace insécable avant `%` est une **règle française** qui était codée en
dur pour les deux locales. Passée en donnée de locale (`pct`).

**Câblage, sans toucher aux appelants** : `dette-val` choisit le bloc par `.Page.Lang` ;
`desc-figures.html` par `site.Language.Lang` — l'idiome déjà employé par `livre-card.html`,
donc **aucun des sept appelants** n'a été modifié. Le `Dataset` devient bilingue en restant
**UN SEUL jeu de données** : `distribution`, `about` (Q3024794), `isBasedOn` et `license`
identiques ; seules les étiquettes changent.

**Preuves** : page EN 29 761 o, **zéro forme française** (aucun de `3 536,1`, `T1 2026`,
`117,5`, `66,6`, `17/08/2026`) et toutes les formes anglaises présentes ; **FR non régressée**,
son `Dataset` reste `inLanguage: fr`, aucune fuite anglaise ; témoin par mutation sur la figure
EN (creux forcé en 2012 → l'étiquette suit) ; EN au sitemap ; `hugo --minify` vert ;
**4 linters à 0**. `llms.txt` complété. Le `git add` du workflow reçoit les 2 nouvelles figures
— même piège d'énumération que la veille.

**⏸ Exclusion déclarée, pas silence** : le compteur animé (`dette-chiffres.html`) porte ses
libellés **en dur en français** ; il est donc **absent de la page EN** plutôt que d'y imprimer
du français — c'est exactement le défaut déjà payé sur l'édition ANTHROPY. Le localiser est un
point ouvert nommé. Autre point : la page EN est une **adaptation** rédigée nativement, pas un
passage par la chaîne `PROCEDURE_TEXTE_COURT` ; une relecture par un anglophone natif (P3H)
reste recommandée pour un premier texte de ce couple locale × genre.

### 2026-08-16 (suite) — `Wikidata/` versionné et câblé ; un défaut d'écriture en retour trouvé et corrigé

**Constat de départ** : `Wikidata/` (71 fichiers, 703 Ko — navette complète, batches
QuickStatements, générateur Python) n'était **ni suivi par git, ni ignoré** : simplement
jamais ajouté. Quatre mois en **exemplaire unique sur un seul disque**, sans historique ni
copie distante. C'était le risque réel, et le versionnement le corrige.

**Contrôle d'exposition avant ajout** (le dépôt est **public**, et son `.gitignore` porte
déjà deux cicatrices de ce type) : aucun secret, aucun jeton, aucune clé. Le seul contact
trouvé est l'e-mail professionnel de l'auteur, **déjà présent dans le dépôt suivi**
(`data/works.yaml:143`) ; « Laura » n'y figure qu'en prénom, dans des consignes
opératoires, et **déjà présent** dans `PROJECT_STATUS.md`, `works.yaml` et deux checklists.
Exposition nouvelle : **nulle**.

**Écarté du versionnement, motif mesuré** : `Import_..._2026-07-06.zip` — ses 3 fichiers
sont **byte-identiques au SHA-256** à leurs versions en clair du même dossier. Versionner
les deux, c'est programmer leur divergence.

**⚠ DÉFAUT RÉEL TROUVÉ ET CORRIGÉ — écriture en retour, pas journal.** `Q141072263`
(*La Société du premier coup*) existait sur Wikidata **depuis le 15/08** — readback API :
ISBN `978-2-9586347-6-6` (P212), auteur `Q138909233` (P50), `P856` vers la fiche. Or
`data/works.yaml` disait encore `wikidata: "" # todo — item du livre à créer`, et la fiche
n'avait **aucun `sameAs`** : l'item était invisible depuis le site. Même classe que le
défaut qui avait motivé l'écriture de `check-fiches-registre.py` (Livresque, 11/08), un
livre plus tard. Corrigé aux deux endroits ; `Q141072263` sort désormais dans le HTML de
la fiche ; linter à 0.

**Cause nommée** : la convention de navette a lâché quand le travail est passé du **lot
préparé** au **deep-link d'une ligne collé en session**. Les gestes du 15/08 et du 16/08
n'avaient laissé aucun dossier. Règle désormais écrite dans `Wikidata/README.md` : **tout
geste Wikidata laisse un dossier daté, même s'il tient en une commande**, et se clôt par
un readback API. Le dossier du 16/08 est créé et sert de modèle.

**Correction d'une affirmation de la session** : j'avais annoncé un « trou de traçabilité »
de trois mois dans `CHANGELOG.md`. **Faux, la mesure le dit** : les 9 QID de `works.yaml`
sont tous documentés par les dossiers datés. Le CHANGELOG n'est qu'un **récit** qui double
le registre ; en cas de contradiction, **les dossiers datés font foi** — c'est désormais
écrit dans le README.

**Contrôle automatique envisagé puis ÉCARTÉ PAR LA MESURE** : un diff « QID connus du
dossier vs QID du registre » produirait **61 faux positifs sur 70** (vocabulaire courant,
et jusqu'à l'exemple factice `Q1234567`). Le suivi repose donc sur le dossier daté, pas sur
un garde-fou qui crierait dans le vide.

**Autres instruments du même type, versionnés au passage** : `scripts/zenodo_inventory.py`,
`zenodo_stats.py`, `zenodo_stats_full.py`, `audit_scholar.sh`. **Câblage** : `CLAUDE.md`
(contextualisations du dépôt) et § 8 ci-dessous.

**Rangé, motif mesuré** : `test.md` était un rapport « Audit GEO v2 » mal nommé et
`stats.txt` le brouillon ayant produit `zenodo_stats_full.py` — tous deux reproductibles,
donc ignorés comme `reports/`. Une seule règle `/_*.txt` remplace `_prompt-*.txt` et couvre
les quatre familles qui lui échappaient.

**🗑 `AGENTS.md` SUPPRIMÉ (décision auteur, 16/08).** Ce n'était pas seulement un dispositif
mort — la revue Codex est remplacée par le panel interne — c'était un **doublon divergent de
`CLAUDE.md` qui déclarait un état faux**, mesuré sur trois points : il annonçait « AWP-01..05 »
quand `content/awp/` en compte **9** ; il ignorait **3 des 4 linters** du dépôt
(`check-geo-coverage`, `check-console-encoding`, `check-fiches-registre`) ; et il renvoyait à
un `.Codex/rules/` **qui n'a jamais existé**. Une session qui l'aurait lu aurait travaillé sur
une carte périmée en croyant suivre les conventions.
Fichier **jamais versionné** : archivé avant suppression, copie **SHA-256 vérifiée** dans
`G:\_BACKUP_SUPPRESSIONS_2026-08-16\AGENTS.md_anthropie-site_20260816` (récupération, pas
prévention).

**⚠ Même défaut un étage plus haut, NON traité — arbitrage auteur en attente** :
`~\.Codex\AGENTS.md` existe (2 378 o, **dernière modification le 31/05**) face à
`~\.claude\CLAUDE.md` (20 855 o, à jour). Il ne contient **aucune** des quatre règles ratifiées
depuis : capillarité, force de décroissance, « pas de report », external-audits. Hors du
périmètre de ce dépôt, donc laissé intact.

**🗑 Les 5 derniers non-suivis ARCHIVÉS PUIS SUPPRIMÉS (décision auteur, 16/08)** — deux briefs
de chantiers **exécutés depuis** (`BRIEF-CLAUDE-CODE-REDESIGN.md` 16/04,
`BRIEF-HARMONISATION-GABARITS.md` 17/04, tous deux renvoyant à un référentiel
`INVENTAIRE-SEO…` disparu) et trois traces datées (`AUDIT_AWP06_COHERENCE.md` 11/05 —
audit en lecture seule, `docs/memo-stephane-lalut-2026-05-08.md`,
`docs/stats_zenodo_2026-04-22.md`). Aucun n'avait jamais été committé : la suppression aurait
été sans retour.
Protocole appliqué, le même que pour `AGENTS.md` : **copie → vérification SHA-256 → suppression
seulement ensuite**, puis **relecture de l'archive APRÈS coup** contre son manifeste (6/6
conformes). `G:\_BACKUP_SUPPRESSIONS_2026-08-16\` porte désormais 7 fichiers / 86 720 o, dont
`_MANIFESTE_SHA256.txt` qui donne pour chaque pièce son empreinte **et son chemin d'origine**
dans le dépôt — le manifeste manquait au geste de la veille, il est rétabli pour `AGENTS.md`
aussi.

**Effet de bord acquis, et c'est le vrai suivi** : `git status` ne signale **plus aucun fichier
non suivi**. C'était la condition qui avait permis à `Wikidata/` de se cacher quatre mois — un
statut bruyant où plus personne ne lit les `??`. Désormais, **tout non-suivi qui apparaît est
un signal**, sans qu'aucun dispositif n'ait été ajouté pour l'obtenir.

### 2026-08-16 — Page dette : la PR mensuelle vide désamorcée, et la compilation publiée comme **jeu de données** (CC BY 4.0)

**Question auteur** : la page `/cout-de-la-dette-publique/` peut-elle suivre les mises à jour
INSEE, et comment la référencer dans Wikidata ? Réponse mesurée, pas déclarée : `python
scripts/update_dette_insee.py --check` exécuté en séance — INSEE + Eurostat rapatriés, gardes
passées, **T1 2026 = 3 536,1 Md€ / 117,5 %**, intérêts **2025 = 66,6 Md€**. La page était donc
déjà à jour, et **aucun chiffre n'y est écrit en dur** (tout passe par `dette-val` ou les
placeholders `{dette.*}` ; clé inconnue = échec de build).

**Défaut trouvé et corrigé (commit `94bf48e`)** — à données identiques, le script réécrivait
quand même les deux fichiers, par les seuls champs `releve_le`. Le `git diff --quiet` de
`dette-insee.yml` était donc **toujours faux** : le workflow aurait ouvert **une PR par mois
pour 4 lignes de date**, là où il annonce ~4 gestes/an. État déclaré ≠ état réel ; rien
n'aurait cassé, l'usure serait tombée sur le merge humain, seule barrière de publication —
exactement la cause de mort inscrite dans sa propre clause de décroissance. Correctif :
comparaison du paquet **privé de ses horodatages** (`_hors_dates`). Aucun champ nouveau — un
`verifie_le` exigerait un commit mensuel pour rester vrai, soit le défaut qu'on corrige.
Témoins : inchangé → diff vide ; `dette_mdeur` mutée à `9 999,9` → réécriture, valeur vraie
restaurée, date du jour.

**Ajout (commit `2dc8016`) — JSON-LD `Dataset`.** La page n'émettait que du `FAQPage` : sa
compilation était lue comme de la prose alors qu'elle expose déjà `/dette_officielle.json` en
accès libre. Partial `layouts/partials/schema-dataset-dette.html`, émis sur la seule page
portant `dataset_dette: true` (jamais un gate sur une URL). **Rien n'y est recopié** :
provenance, unités, millésimes, date et identité auteur se dérivent de
`data/dette_officielle.json` + `data/author.toml` — prouvé par mutation (`2099`,
`MUTATION-TEMOIN`, `1999-01-01` traversent tous les trois jusqu'au balisage). `about` pointe
**Q3024794** (dette publique de la France), en cohérence avec le geste Wikidata demandé sur
l'item du livre.

**Licence — décision auteur : CC BY 4.0 sur la COMPILATION** (assemblage, grandeurs dérivées,
mise en cohérence) ; les séries brutes restent INSEE et Eurostat. Portée sur les **trois
surfaces qui distribuent la donnée**, parce que le fichier voyage seul : prose de la page,
`license` du JSON-LD, champ `_licence` **dans** le paquet JSON. `llms.txt` aligné.

**Défaut de classe corrigé au passage** : les libellés destinés aux lecteurs étaient en ASCII
(« interets verses », « sante », « securite », « francaise »). La contrainte console cp1252,
qui ne porte que sur `print()`, avait été appliquée par habitude à des chaînes qui partent
dans le JSON public, dans le `Dataset` et dans le `<title>`/`<desc>` du SVG (texte des
lecteurs d'écran). Corrigé **à la source**, donc propagé aux trois surfaces d'un coup ;
l'invariant du docstring dit désormais la distinction, pour qu'une session future ne
« répare » pas ces accents en ASCII.

**Preuves** : `hugo --minify` vert ; 2 blocs JSON-LD (`FAQPage` + `Dataset`), 9
`variableMeasured` ; octets JSON et SVG décodent en UTF-8 sans BOM ; idempotence (2ᵉ exécution
→ « CONTENU INCHANGE », aucun diff) ; **4 linters à 0** (corpus-counters, console-encoding,
geo-coverage, fiches-registre). Rien poussé.

**✅ EN LIGNE le même jour** — push auteur `37054d6..19ed171`, déploiement Hugo en succès.
Vérifié **par la sortie réelle**, pas par le code retour : page 200, **2 blocs JSON-LD**
(`FAQPage` + `Dataset`), `license` CC BY 4.0 dans le balisage **et** dans la prose, `about`
→ Q3024794, 9 `variableMeasured`, accents corrects ; endpoint `/dette_officielle.json` 200,
porteur de `_licence` et **SHA-identique au dépôt** ; `<title>` du SVG accentué en ligne.

**✅ Wikidata — geste Laura exécuté et relu par l'API** : `Q138910896` `P921` porte désormais
**3 valeurs** — anthropie (`Q138827949`), `Q3024789` (*dette de l'État*, générique) et
**`Q3024794`** (*dette publique de la France*), rang normal ; 12 propriétés au total, donc
aucun effet de bord. Les deux surfaces concordent enfin : le `about` du `Dataset` et le `P921`
de l'item du livre désignent le même nœud, celui où atterrit toute résolution d'entité sur la
dette publique française.

**✅ Second graphe FAIT le 16/08 (demande auteur)** — `static/img/taux-apparent-dette.svg`,
posé dans « Le mécanisme » : la courbe du **taux apparent** 1996-2025, le chaînon causal que
la page racontait sans le montrer. Généré par le même script, **rien en dur** — témoin par
mutation directe de `build_svg_taux` : creux forcé en 2012 et fin à 5,55 → étiquettes et
`<desc>` suivent (2020→2012, 2,0→5,5). Palette **validée par le script du référentiel**
(6 contrôles PASS, ΔE 24,7 protan / 33,6 vision normale) ; couleur = slot 2, celle des
intérêts dans la figure voisine, parce que **la couleur suit l'entité** (le coût), pas le rang.
Série unique → pas de légende, étiquetage direct des 3 seuls points que la prose cite.
Deux écarts assumés au référentiel, **déclarés** : pas de couche de survol (l'actif est servi
en `<img>` et vaut comme image citable — les valeurs vivent dans la prose et le JSON public,
qui tient lieu de vue tableau) ; et la verticale pointillée du creux a été **retirée** — non
étiquetée, elle était indiscernable d'une grille en pointillés (anti-pattern), et le creux est
déjà porté par son point.

**⚠ Deux défauts attrapés pendant ce geste, avant qu'ils ne dorment** :
(a) le `git add` de `dette-insee.yml` **énumère les fichiers** — la nouvelle courbe aurait été
régénérée en CI puis **jamais committée**, donc figée en ligne pendant que le reste
s'actualise, sans erreur ni trace. Corrigé, avec le commentaire qui dit pourquoi l'énumération
est un piège ;
(b) le figcaption écrit en markdown dans un bloc HTML brut **n'est pas rendu** par Goldmark —
les backticks et le lien seraient sortis en clair. Vu en contrôlant la SORTIE, pas la source.
Réécrit en `<code>` et `<a href>`.

**⏸ Reste nommé (1)** : **DOI Zenodo du jeu de données**, écarté pour l'instant — coût
récurrent (~4 dépôts/an) avant toute mesure de retour du `Dataset`.

### 2026-08-15 (soir) — Registre EN INTÉGRAL `/en/register-of-offloaded-costs/` : traduction native des 165 jalons via le module de traduction (commande auteur)

**Commande auteur** : « la même page » qu'en FR, « traduction parfaite et native, voir module
de traduction » — renverse l'adaptation du matin. Un QR sera intégré à l'édition EN dans un
second temps (corrections chirurgicales auteur) : **cette page est sa cible**.

**Découvertes d'audit qui ont cadré l'exécution** (capitaliser sur l'existant) :
- le chapitre 177 du pipeline livre (`work/anthropie/en/passes/177-registre-…-qr-code.*`)
  est la **page QR** : le livre imprimé ne contient PAS les 168 jalons — il renvoie par QR
  au registre en ligne (« Scan the QR code opposite ») ; `_production_en/qr_en.png` existe ;
- **nom canonique EN = « Register of Offloaded Costs »** — décision auteur déjà rendue
  (script `app70_register_canonical.py`, défaut LING-F-01) ; grille = « Order created /
  Debt displaced » (paires P4 du ch. 177) ; la fiche EN portait « deported » (non canonique,
  CORRIGÉ) et des noms d'âges non conformes au livre publié (nav de l'EPUB EN : Foundational
  Programs, **The Extractive Empires**, Industrialization and **Nation-States** — CORRIGÉS).

**Chaîne appliquée** (PROCEDURE_TEXTE_COURT, pack en-US) : P0 source scellée =
`registre_couts_deportes.json` @ `a209a97` (complétude par construction : zip ordre-strict,
165/165) · P1 traduction par lots avec terminologie AUTHOR_VALIDATED injectée
(decisions_terminologiques : anthropy, external memory, State-machine, entropic debt,
system of exploitation… + false_friends + forbidden_calques) · gates déterministes étage 1
PASS (1 faux positif qualifié : « La Boétie ») · **P3B 2 réviseurs indépendants à contexte
vierge** (fidélité : 36 findings/165 lus ; natif US : 84 findings/165 lus) · **P4 arbitrage**
fidélité > voix > fluidité > élégance : **100 correctifs appliqués par mutation prouvée**
(dont 3 faux-amis réels : « evidence »→self-evidence sur Descartes, « recover »→co-opt sur
récupération situationniste, « counterpart »→counterweight ; « sanctuarize » inexistant ;
« letters of exchange »→bills of exchange) ; **2 rejets documentés** : « Humanity Beside
Itself » (collocation AUTHOR_VALIDATED_TITLE App_22, les réviseurs ne pouvaient pas la
connaître) et « Hygienism » (nom attesté du mouvement). Apostrophes Chicago mécanisées.

**Livré** : `data/registre_couts_deportes_en.json` (165 jalons EN, âges canoniques, dates
en-US, catégories mappées ×21 — Mémoriel→Memory, Psychique→Psychological, jamais les
faux-amis) ; shortcode `registre-ages` bilingue (labels + data par langue) ; page EN
miroir de la FR (7 FAQ JSON-LD, mêmes sections) ; **URL canonique
`/en/register-of-offloaded-costs/` + alias depuis l'URL du matin** ; i18n déjà posé.
Vérifié : build 0, compteurs 0, couverture 0 signal, 165 details/ancres, hreflang croisé,
rendu navigateur contrôlé (accordéons, arbitrages en place). **Commits locaux — push
auteur NON exécuté ce tour (pas de demande explicite)** ; IndexNow partira au push.

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
- P3747 SSRN author ID : 11065608
- P5715 Academia.edu profile URL
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

- **⛔ ARTICLE WIKIPÉDIA — NON, et ne pas re-litiger avant qu'un des quatre
  déclencheurs ci-dessous soit atteint (mesuré le 2026-08-16).**
  État réel de la couverture par des **tiers** :
  **0 recension éditoriale** d'un livre dans la presse ; **1** seule recension
  existante (Philippe Martin, 2025-11-10) et elle est publiée dans « **Parole de
  lecteurs** » — un blog de lecteurs hébergé par *Alternatives Économiques*, donc
  contenu contributif, pas une source secondaire éditoriale. Les 20 fiches de
  `content/publications/` sont des textes **écrits par** l'auteur, pas **sur**
  lui. Les livres sont en **auto-édition** (obstacle quasi rédhibitoire aux
  critères « écrivains » de fr.wikipédia, qui supposent le compte d'éditeur), et
  `works.yaml` mesure lui-même `citation_pattern: "auto-circulation présumée"`
  avec Google Scholar à 0 sur plusieurs AWP.
  **Tenter serait net-négatif** : une page créée par le sujet ou un proxy tombe
  sous WP:AUTOBIOGRAPHIE + conflit d'intérêts ; le débat de suppression qui suit
  est **public et indexé** — on fabriquerait une page faisant autorité pour dire
  que la communauté n'a trouvé aucune notoriété, exactement l'inverse du but GEO,
  et le titre devient plus difficile à recréer ensuite.
  **Wikipédia est un thermomètre, pas un levier** : c'est le signal d'entité le
  plus fort pour les moteurs et les modèles *parce qu'*il ne se fabrique pas.
  **Déclencheurs de réexamen** — un seul suffit à rouvrir la question :
  (1) ≥ 2 recensions **éditoriales** indépendantes, espacées dans le temps ;
  (2) un livre publié à **compte d'éditeur** ; (3) un article peer-reviewed avec
  des citations **indépendantes** (pas d'auto-circulation) ; (4) le concept
  d'anthropie **discuté par des tiers** dans la littérature ou la presse — cette
  voie viserait un article sur le *concept*, pas sur la personne.
  Contribution légitime entre-temps, à ne pas confondre avec un levier : enrichir
  l'article existant *Dette publique de la France* en **sourçant l'INSEE et
  Eurostat**, jamais le site de l'auteur.
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
- `Wikidata/README.md` : navette Wikidata — **registre primaire = les dossiers
  `Import_..._<date>_<sujet>/`**, pas le `CHANGELOG.md` ; règle « tout geste
  laisse un dossier daté, même en une commande » ; chaîne à boucler jusqu'au
  `sameAs` de la fiche. Dossier versionné le 2026-08-16 après quatre mois en
  exemplaire unique.
- `Wikidata/scripts/README.md` : générateur de batches QuickStatements
  (fetchers Zenodo/Crossref/OpenLibrary, validators P9934/P407)

---

*Ce fichier est versionné dans le repo. Toute évolution majeure 
(fin des 90 jours, ouverture chantier édition, refactor structurel)
doit faire l'objet d'une mise à jour explicite avec préfixe 
`docs:` dans le message de commit.*
