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
déclarée ; avec la moyenne activité à vie longue, plus de 99 %. Elles font partie des trois catégories à vie longue qui
n'ont pas encore de stockage définitif (avec FA-VL). Le volume, lui, est porté à plus de neuf dixièmes par des
catégories qui ont un stockage en service.

### Mécanisme explicatif

La classification de l'Andra croise niveau d'activité et durée de vie ; le volume se concentre dans les catégories
faiblement actives (démantèlement, exploitation courante), l'activité dans les résidus du retraitement des combustibles.
Les filières ont été créées d'abord pour les déchets les plus volumineux et les moins actifs (CSA en 1992, Cires en
2003) ; le stockage profond des plus actifs est en projet.

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
