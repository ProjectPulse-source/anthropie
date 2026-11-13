# Fiche de conception — Déchets radioactifs : le volume dit-il le problème ?

<!-- Page de données née de l'arbitrage PRO-20261026-033434 (graphe G3 reconçu : volume, activité et gestion, articulés,
sans indice composite ; scénario S2 : page de faits distincte de la notion de communs négatifs). Fiche écrite AVANT le
texte, après la lecture des fichiers de l'Andra et le témoin des Essentiels 2026. -->

Page : `/dechets-radioactifs-volume-ou-radioactivite/` (FR) · `/en/radioactive-waste-volume-or-radioactivity/` (EN) ·
ouverte le 2026-10-26

## Forme

`quantitatif` : données ouvertes de l'Andra (Inventaire national, fichiers « déchets déclarés à fin AAAA »), lues par
`scripts/update_dechets_radioactifs.py` ; modèle complet des pages de données. Critères : définitions (volume en
équivalent conditionné ; activité déclarée, en becquerels ; catégories de l'Andra), millésimes distincts pour le volume
(dernier fichier) et l'activité (dernière édition qui la déclare), changement de périmètre (catégorie hors bilan
apparue dans le fichier de fin 2021), valeurs transcrites déclarées (état des filières), aucune lecture anthropique dans
les constats.

## Fiche de conception

### Question centrale

Le volume des déchets radioactifs, qui domine le débat, dit-il où est la radioactivité — et où sont les obligations qui
restent sans solution ?

### Enjeu

Le débat public sur les déchets nucléaires se joue souvent en mètres cubes. Si la radioactivité et l'absence de filière se
concentrent dans une part infime du volume, le chiffre qui circule le plus dit peu de ce qui reste à résoudre.

### Croyance initiale

Le problème des déchets nucléaires se mesure à leur volume ; plus il y en a, plus le problème est grand.

### Découverte principale

À fin 2021, les déchets de haute activité font quelques millièmes du volume et plus de 95 % de la radioactivité
déclarée ; avec la moyenne activité à vie longue, plus de 99 % (périmètre : les cinq catégories des bilans de l'inventaire ; résidus miniers, déchets à radioactivité naturelle élevée et résidus historiques de conversion de Malvési en sont hors (une partie des volumes récents de Malvési est, elle, classée TFA et FA-VL : second contrôle de la figure, 12/11/2026) : R1-2, R1-6, R1-7 ; l'activité déclarée de la haute activité est un majorant : R1). Elles font partie des trois catégories à vie longue qui
n'ont pas encore de stockage définitif (avec FA-VL). Le volume, lui, est porté à plus de neuf dixièmes par des
catégories qui ont un stockage en service.

### Mécanisme explicatif

La classification de l'Andra croise niveau d'activité et durée de vie ; le volume se concentre dans les catégories
faiblement actives (démantèlement, exploitation courante), l'activité dans les résidus du retraitement des combustibles.
Les filières ont été créées d'abord pour les déchets les plus volumineux et les moins actifs (CSA en 1992, Cires en
2003) ; le stockage profond des plus actifs est en projet : ils sont entreposés, non stockés (C. env., art. L. 542-1-1 : R2-2). Relecture des sources du 12/11/2026 : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\SOURCES\dechets-radioactifs-volume-ou-radioactivite_SYNTHESE.md`.

### Preuve décisive

Le fichier de fin 2024 (volumes, localisation) et l'édition de fin 2021 (activité), lus par script ; le témoin des
Essentiels 2026 de l'Andra (volumes par catégorie et volumes stockés, retrouvés à l'arrondi près) ; la variante qui
crédite les volumes non déclarés de l'activité moyenne de leur catégorie (HA : 96,7 % au lieu de 97,1 %) ; cinq
éditions qui déclarent l'activité (2013 à 2016, 2021).

### Pouvoir discriminant

- **Lectures rivales réellement soutenues.** (a) Le volume mesure le problème (lecture implicite des comparaisons en
  piscines olympiques et des chiffres de « tonnes de déchets ») ; (b) la radioactivité et l'absence de filière mesurent
  mieux ce qui reste à résoudre (lecture de l'Andra elle-même, qui publie la mise en regard volume / radioactivité).
- **Ce que le graphe tranche.** Il montre que les deux *hiérarchies* diffèrent fortement (HA, dernière en volume, est
  première en radioactivité ; FMA-VC, première en volume, n'est que troisième : aucune inversion stricte ; corrigé après
  PRO-20261026-045248) ; et ce qui sépare les catégories avec et sans stockage n'est ni le volume ni la radioactivité, mais la
  durée de vie (les trois catégories à vie longue n'en ont pas, FA-VL comprise, très peu radioactive). Correction du
  26/10/2026, trouvée en écrivant le paquet de contre-expertise : la page disait « l'absence de stockage suit la
  radioactivité », que FA-VL dément. Il ne départage pas des
  *explications* causales : c'est une page de description qui le dit (« ce graphe décrit, il ne tranche pas la question
  du risque »).
- **Ce que la série isolée ne montre pas.** La mise en regard volume / activité est publiée par l'Andra ; l'apport de la
  page est la troisième dimension, l'état de la filière, croisée avec les deux autres, et la localisation lue par script.
- **Niveau atteint** (seconde réponse de PRO-20261026-045248) : figure descriptive à trois dimensions ; elle n'évalue pas
  les décisions de gestion. Piste ouverte, non publiée : le fichier ouvert suit les volumes de Malvési de l'Andra jusqu'à
  fin 2022 (RTCU 0,67 puis 0,65 Mm³) et s'en écarte depuis le fichier de fin 2023 (0,90, puis 0,89) ; l'Andra a révisé à
  fin 2024 d'un facteur 1,65 le volume estimé des bassins de décantation (bathymétrie, tassement), ce qui ne l'explique
  pas à lui seul. À rapprocher famille par famille avant toute phrase.
- **Robustesse, montrée par une variante calculée.** Activité créditée pour les volumes non déclarés ; cinq éditions
  (de 84,7 % en 2014 à 97,1 % en 2021 pour la part HA : la page donne la plage, pas le seul maximum).
- **Levier ou risque éclairé.** La question publique n'est pas « combien de mètres cubes » mais « quelles catégories
  attendent une solution, chez qui, et depuis quand » : le stockage des plus actifs est en projet, ils sont entreposés
  sur les sites de production.

### Limite

La radioactivité (Bq) ne mesure ni le risque sanitaire ni le coût de gestion : elle décroît, elle dépend des
radionucléides, et le risque dépend de l'exposition. L'activité déclarée date de la dernière édition (fin 2021) ; une
partie des volumes n'a pas d'activité déclarée (corrigée par la variante). Les déchets hors bilans (résidus de
conversion de l'uranium à Malvési, stockages historiques) ne sont pas dans les parts ; leur total est donné à part ; le
volume « RTCU » du fichier ouvert (0,89 million de m³) ne recoupe pas les volumes de Malvési des Essentiels
(0,69 million de m³) : la page ne publie que le total hors bilan lu dans le fichier. Les matières radioactives (uranium
appauvri, combustibles usés en attente de retraitement), qui ne sont pas des déchets au sens de la loi, sont hors champ.

### Valeur finale

Un tableau à trois colonnes que le lecteur peut reprendre : volume, radioactivité, filière ; et la question qui reste
ouverte (le stockage des déchets les plus actifs).

### Singularité

Cette page existe parce qu'elle croise volume, radioactivité et état de la filière, calculés sur les fichiers ouverts
et contrôlés contre la publication de l'Andra, ce que le lecteur ne trouve pas réunis dans les Essentiels (lus : volume
et filière d'un côté, radioactivité ailleurs) ni dans la presse (lue partiellement : la paire « 0,2 % du volume, 95 % de
la radioactivité », sans la filière).

### Raccords

- Définition de l'anthropie — écartée du corps (page de faits) ; un encadré séparé renvoie à la notion de communs
  négatifs, présentée comme lecture de l'auteur.
- Livre — retenu : *ANTHROPIE — Ordre ici. Dette ailleurs* (appel en fin de page, `ressource.livres`).
- Working paper — AWP-06 (communs négatifs candidats) cité dans l'encadré séparé ; non retenu dans le corps.
- Pages voisines — `/communs-negatifs/` (phrase de renvoi ajoutée dans la notion).

## Fiche D0

Résultat visé : la page citée pour la mise en regard des trois dimensions (presse, enseignants, débat public sur Cigéo).
Diagnostics : vues, citations. État initial : page nouvelle ; relevé au J+60.

## Étapes de la méthode

- Plan d'outils : fait le 26/10/2026.
- Protocole du type `quantitatif` : fait (fichiers lus, millésimes séparés, changement de périmètre, valeurs transcrites
  déclarées, témoin des Essentiels).
- Scénarios d'architecture : tranché par l'arbitrage (S2).
- Panel avant : remplacé par le test de compréhension simulé, demandé par l'auteur le 26/10/2026 (à consigner ci-dessous).
- Contre-expertise de phase A : faite (PRO-20261026-033434) ; contre-expertise de la page : demandée par l'auteur après
  le test simulé.
- Gardes vues mordre : faites — 10 gardes, chacune mutée ; la garde des éditions a mordu sur la donnée réelle (2014 :
  84,7 %), la phrase est passée de « neuf dixièmes » à « quatre cinquièmes ».
- Figures téléphone : faites (versions `-m`, parité contrôlée ; « 0,00 % » remplacé par « < 0,01 % », qui ne se lit pas
  comme une radioactivité nulle).
- Relecture de langue : faite (LanguageTool FR et EN sur le texte servi ; signalements tranchés : extraction, titre
  français cité, orthographe britannique, « la première compte » correct).
- Relecture phrase à phrase FR et EN : faite le 26/10/2026 ; corrections : résumé « Réutiliser » (HA et MA-VL présentés à
  tort comme seules catégories sans stockage ; « catégories déjà stockées » → « qui ont un stockage en service »),
  encadré (lecture attribuée à AWP-06 retirée), étiquette de la carte de partage (FMA-VC n'est pas « faible activité »).
- Composant `appel-livre` corrigé pour un livre qui a une édition anglaise (devise de la fiche, Amazon.com, sans
  « French edition ») : premier appel d'ANTHROPY depuis une page anglaise.
- Générateur : PNG rendus en mémoire avant toute écriture (un rendu échoué avait laissé un JSON neuf, 26/10/2026) ;
  même correction dans `update_menages_imprevu.py`. Les autres générateurs du site écrivent encore les données avant
  les figures : point ouvert, à adopter à la refonte de chaque page.
- Recette 320-1600 : faite (`recette.py`, 12/12).
- Instantané de relecture : fait (FR, EN).
- Gate éditorial — auto-évaluation, non indépendante : exactitude *tenu* (11 gardes, témoin des Essentiels, variante,
  plage des éditions) ; clarté *tenu* ; accroche *tenu* ; progression *tenu* (volume → radioactivité → robustesse →
  stockage → hors bilans → limites) ; originalité *partiel* (la paire volume / radioactivité est publiée par l'Andra ;
  l'apport est la filière et la localisation calculées, et la plage des éditions) ; valeur finale *tenu*.
- Test de compréhension simulé (six lecteurs, deux pages) : fait, consigné ci-dessous ; test réel : décision de l'auteur.
- Seconde réponse (26/10/2026) : arbitrée ; préfecture de la Haute-Marne ajoutée en source de Cigéo ; phrase du hors bilan
  précisée (1,33 Mm³ à fin 2024, catégorie présente depuis 2021) ; piste Malvési dans « pouvoir discriminant ».
- Contre-expertise de la page : faite (PRO-20261026-045248, arbitrée le 26/10/2026). Erreur factuelle corrigée : Cigéo
  (enquête publique close le 16/07/2026, avis favorable en août, autorisation non délivrée à la mi-septembre ; dépêche AFP
  du 14/09/2026). Comparaison volume / activité au même millésime (fin 2021) ; « hiérarchies très différentes » au lieu de
  « classement inverse » ; durée de vie présentée comme une contrainte parmi d'autres ; centre de la Manche « fermé aux
  nouvelles réceptions » ; Malvési d'après l'Andra, écart du fichier ouvert non interprété. 12 gardes ; recette 12/12 FR
  et EN ; LanguageTool refait ; instantanés refaits.

## Test de compréhension simulé (26/10/2026)

Même protocole que la page « dépense imprévue » (trois lecteurs simulés isolés, texte servi seul, questions de D2).

| Lecteur | Contresens relevés (citations) |
|---|---|
| Professeure de physique-chimie, lecture attentive | aucun ; signale deux incohérences de forme : le résumé « En trois phrases » disait « plus de 95 % » quand la page dit 97,1 % (corrigé : jetons) ; une description de figure tronquée (artefact de l'extraction du test, le HTML servi est complet) |
| Lectrice rapide, sans formation scientifique | « les déchets **les plus dangereux**, ceux de haute activité » (la page dit que radioactivité n'est pas danger, mais seulement en deuxième section) ; « on ne sait **toujours pas où** les mettre définitivement » (la page disait « en projet », sans lieu ni étape) |
| Journaliste énergie | aucun ; phrase publiable exacte, avec source |

Corrections : mise en garde « Radioactivité ne veut pas dire danger » placée au contact des premiers chiffres ; état de
Cigéo sourcé (lettre de l'ASNR du 30/03/2026 : Bure, Meuse ; demande de janvier 2023 ; enquête publique pouvant être
engagée) ; chapô et résultat : « prévu à Bure (Cigéo), mais pas encore autorisé ». Contre-épreuve sur le texte corrigé,
même lectrice : « j'ai compris que "radioactif" et "dangereux", ce n'est pas tout à fait pareil » ; « en attendant
Cigéo, à Bure, qui n'est pas encore autorisé » ; persiste dans sa phrase à une amie : « on ne sait toujours pas où les
mettre » et « les plus dangereux, enfin les plus radioactifs » (auto-corrigé). Le chapô et le résultat ont été réécrits
après la contre-épreuve ; non retestés.

### Reprise du lot « guides » (12/11/2026)

Méthode `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\METHODE_REPRISE_RESSOURCE.md` ; dossier `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\` (rapport
`RAPPORTS\dechets-radioactifs-volume-ou-radioactivite.md`, état `LOT.md`).

- Relecture des sources : faite le 12/11/2026, deux relecteurs indépendants et les sondes de la session
  (`SOURCES\dechets-radioactifs-volume-ou-radioactivite_R1.md`, `_R2.md`, `_SYNTHESE.md`, `SONDES_SESSION.md`) ; écarts de
  la version en ligne corrigés : 97,2 % présentés sans dire que la radioactivité déclarée est, pour l'essentiel, un
  maximum ; centre de la Manche dit « en surveillance » alors qu'il est en phase de fermeture ; localisation des déchets
  de haute activité et de moyenne activité à vie longue généralisée aux sites de production ; résidus de conversion
  rapprochés de Malvési ; éditions lues comme une série ; entreposage et stockage ; requalification des matières.
- Interventions : `specs\dechets-radioactifs-volume-ou-radioactivite.py`, 117 remplacements (FR et EN), dont une
  explication (DR-9, Malvési) tranchée en faveur de la version proposée par le contradicteur externe ; témoin : la
  spécification appliquée à la page d'origine redonne cette page, en-tête de publication et organe de forme
  (`figure-lecture`) à part. Reste en ligne, à arbitrer, « Ce constat reflète des contraintes de gestion… » (le retirer
  retirerait une explication).
- Juge interne à l'aveugle : deux tours sur le lot ; contradicteur externe `PRO-20261112-140721` (réponse archivée avant
  lecture, SHA-256 `A71FAC4D…`) : version proposée retenue sur 16 passages sur 17, le passage 5 réécrit sur sa proposition
  (deux classements, aucun ne mesure à lui seul doses, durée de danger ou coût) ; décisions 10 à 13 appliquées : note de
  la figure (année et part majorante lues dans le jeu), « pour l'essentiel un maximum » documenté (fichier, méthode,
  garde), Cigéo vérifié sur Légifrance et sur la page de la préfecture, tonnes et mètres cubes non additionnés ; carte de partage et son texte
  alternatif portent la réserve (décision 26) ; arbitrage `ARBITRATIONS\PRO-20261112-140721_arbitrage.md`.
- Générateur (`scripts/update_dechets_radioactifs.py`) : lit la colonne MAJORATION (signe « < » : activité majorante) ;
  part majorante de l'activité déclarée fin 2021, 89,7 % pour la haute activité et 88,4 % pour les cinq catégories,
  égale à la mesure indépendante de la relecture R1 ; deux gardes nouvelles, vues mordre (`--mutation=majorant` :
  « pour l'essentiel un maximum » ; `--mutation=hors_edition` : hors des éditions, moins d'un millième du volume avec
  activité déclarée, mesuré à 0,006-0,013 %) ; JSON (`meta.activite_majorante`, `parts.activite_majorante`) et CSV (colonne
  `activite_declaree_majorante_bq`, anciennes colonnes inchangées) ; fichiers sources de l'Andra inchangés (empreintes),
  relevé porté au 12/11/2026. Mesure de la session : « n'est déclarée qu'aux éditions » était inexact à la lettre (120 à
  241 m³ déclarés certaines années hors édition) : la page dit « pour l'essentiel du volume ».
- Cigéo : au 12/11/2026, Légifrance (Journal officiel, « Cigéo », trié par date) ne montre aucun décret d'autorisation de
  création, et la préfecture de la Meuse aucune étape après le 14 septembre (`SONDES_SESSION.md`).
- Figure régénérée par le générateur : note (année, périmètre et ce qu'il laisse de côté, résidus miniers et résidus historiques de conversion de Malvési ; part majorante ; « non comme une mesure exacte » ; « ne mesure pas le risque sanitaire et ne classe ni les risques ni les coûts »), en-têtes « radioactivité déclarée » et « Filière de stockage », sous-titre téléphone, description pour lecteur d'écran ; plancher de tracé de 1,5 px commenté (chaque barre porte sa valeur). Protocole des figures : `check-figures` 0 défaut ; contrôleur de géométrie et de données (chaque nombre recalculé dans le fichier de l'Andra, témoin positif vu) et contrôleur de lecture, puis deux passages sur l'état corrigé, le premier trouvant un défaut nouveau (Malvési : une partie récente de ses volumes est classée TFA et FA-VL), le second un seul défaut cosmétique, corrigé ; carte de partage régénérée avec la réserve (`scripts/og_dechets_radioactifs.py`, décision 26).
- Relecture de langue phrase à phrase du texte servi, FR (138 phrases : 4 fautes, 13 maladresses) et EN (134 : 7 erreurs, 22 maladresses) : corrigées, sauf la ponctuation de la citation et deux libellés du gabarit commun (commit séparé) ; préférences retenues quand elles éclairent ; le titre anglais (« does volume tell the problem? », calque) est laissé à l'auteur, la méthode gardant les titres. Points de fond tranchés au passage : la FAQ date Cigéo du 12 novembre 2026, comme le corps ; « se vérifie à chaque étape », qui ne décrivait aucun contrôle (relecture R2), dit ce qui a été lu et vérifié ; les centres de l'Aube et de la Manche, non les départements. Relecture de contrôle des phrases changées (`JUGE\RELECTURE_LANGUE_DECHETS_CONTROLE.md`) : aucune faute ; une inexactitude introduite en anglais (« the latest year for which the inventory declares radioactivity » : fin 2022 en déclare pour 241 m³), corrigée ; reports de parité entre les deux langues.
- Contrôles : `check-all --ci` 0 ; build et `typo_build` 0 défaut ; rendu 0 ; liens 0 critique ; dates 83/83, 0 bloc sans
  période ; couverture : 15 signaux, aucun nouveau ; lettre : chaque écart rattaché à son intervention, sauf la date de mise
  à jour (en-tête).
- Envois : la page est citée par un courriel de la campagne ANTHROPY-EN (LOT3, parti le 12/11), qui reste exact face à
  la page corrigée ; publication décidée par l'auteur le 12/11/2026.
- Instantané de relecture : fait le 12/11/2026 (139 phrases FR, 134 EN) ; `refonte` porté au 12/11/2026 ; journal créé, entrée du 12/11/2026 ; relevé du jeu porté au 12/11/2026, fichiers sources de l'Andra inchangés.
- Mise en ligne : poussée sur décision de l'auteur, le 12/11/2026 (commit 1e4c0ac) ; déploiement `hugo.yml`
  n° 43256651052 réussi (build, relecture, deploy, contrôle de fumée de la production).
- Attestation de la version servie : faite le 12/11/2026 vers 17 h 17 (heure de Paris). HTML servi identique au build
  contrôlé, aux empreintes de cache des scripts près (neuf en FR, huit en EN : fins de ligne du poste) ; les quatre SVG
  de la figure et les deux cartes de partage servis identiques, octet pour octet, au commit ; CSV servi avec la colonne
  `activite_declaree_majorante_bq` ; « Page mise à jour le 12 novembre 2026 ».
- Laissés à l'auteur : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\A_ARBITRER.md`.

### Reprise du style (13/11/2026)

- Consigne de l'auteur (13/11/2026) : une mise en page « ultra lisible », au niveau de la page Parcoursup (règle 17
  du `CLAUDE.md` du site), adaptée au sujet. Étude, choix et mesures :
  `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\ETUDE_STYLE.md`. Organes existants seulement
  (`_ressource-relief.scss`, `reperes-page.html`) ; les phrases ne changent pas, elles prennent une forme.
- Organes : trois repères (97,2 % de la radioactivité déclarée, pour l'essentiel un maximum, non une mesure exacte,
  dans 0,25 % du volume, fin 2021 ; plus de neuf dixièmes du volume pour 0,12 % ; Cigéo pas encore autorisé, repère à
  changer avec le résultat en une phrase à la publication d'un décret) ; la procédure de Cigéo en fiche d'étapes (trois
  étapes datées, puis la suite prévue ; la phrase vérifiée du 12/11/2026 reste sous la fiche ; « en août » devient
  « août 2026 ») ; deux paragraphes coupés. Jetons `{dr.*}` seulement.
- Inchangés : titre, adresse, ancres, chapô, figures, nombres, réserves, questions fréquentes, sources, « Réutiliser ».
  Aucune modification de fond : `lastmod`, journal et `data/dates_affichage.json` inchangés ; `refonte` reste au
  12/11/2026 (instantané du 13/11, postérieur).
- Contrôles : `check-all --ci` 19/19 à 0 ; build CI et `typo_build` 0 défaut ; liens 0 critique ; rendu 0 ; dates 83/83,
  0 bloc sans période ; 0 débordement sur onze largeurs de 320 à 1 440 px, avec et sans JavaScript ; aucun texte des
  blocs sous 12 px ; repères absents sous 600 px ; lecture à côté de la figure dans la limite. Lettre : texte servi avant
  et après, phrase à phrase ; seules changent les phrases mises en forme ; nombres inchangés. Langue et fidélité : la
  session, puis un relecteur indépendant (aucun P0 ; P1 traités). Premier écran : deux tours de lecteurs neufs (FR, EN) et un témoin trompeur vu mordre
  (`LOTS\guides\P\premier_ecran_style.md`) ; constats sur le chapô, inchangé : `LOTS\guides\A_ARBITRER.md`.
- Instantané de relecture refait le 13/11/2026.
- Mise en ligne : poussée sur demande de l'auteur le 13/11/2026 (commits `cf3ad02` à `17d3598`) ; déploiement `hugo.yml`
  n° 43351148379 réussi (build, mise en ligne, relecture). Attestation de la version servie : faite le 13/11/2026 vers 03 h 20 (heure de
  Paris) ; HTML servi identique au build contrôlé, aux empreintes de cache des feuilles et scripts près.

### Arbitrage externe et relectures (13/11/2026)

- Pièce remise par l'auteur, archivée avant lecture et arbitrée par écrit : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\ARBITRAGE_EXTERNE_2026-11-13.md`.
- Fond : l'explication de l'absence de filière par des contraintes de gestion, non établie pour ce constat, est retirée ;
  reste la réserve, « Ce constat ne permet pas d'attribuer cette absence de filière à la seule durée de vie ». Cigéo « n'a
  pas encore reçu son autorisation de création » (description, chapô, repère, résultat, « Réutiliser ») ; il a été déclaré
  d'utilité publique par le décret n° 2022-993 du 7 juillet 2022 (lu sur Légifrance), autre procédure. Titre anglais
  « Radioactive waste: what can volume really tell us? » (titre, partage, lien de la page « negative commons »,
  `llms.txt`), adresse inchangée. « En France » au chapô. `lastmod` au 13/11/2026, journal, historique des dates.
- Langue : relecteur indépendant, aucun P0 ni P1 ; la relative accrochée à « Bure (Cigéo) » est rattachée au centre (« à
  Bure, dans le centre Cigéo, qui … » ; « in the Cigéo facility at Bure, which … » : en anglais, la licence va à
  l'installation, non à « disposal »). Restent en P3, à changer partout ou nulle part : « Andra's balances », « creation
  licence ».
- Premier écran : le second repère met 0,12 % en gras et porte sa date ; troisième tour, aucune conclusion interdite (FR,
  EN).
- Reportés : concentration de l'activité déclarée (lot P3, calcul reproductible d'abord) ; à la publication d'un décret
  d'autorisation de Cigéo, changer ensemble repère, résultat, description, chapô et « Réutiliser » (`A_ARBITRER.md` du lot).
- Contrôles : `check-all --ci` à 0 ; build CI et typographie 0 défaut ; liens 0 critique ; rendu 0 ; dates 83/83 ;
  0 débordement sur onze largeurs de 320 à 1 440 px, avec et sans JavaScript (la mesure vérifie désormais le statut
  HTTP de chaque page) ; lettre : texte servi avant et après, phrase à phrase, seules changent les phrases décidées.
- Instantanés de relecture refaits le 13/11/2026.
