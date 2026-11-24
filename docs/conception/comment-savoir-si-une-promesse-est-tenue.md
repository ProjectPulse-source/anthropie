# Fiche de conception — Comment savoir si une promesse est tenue ?

Page : `/comment-savoir-si-une-promesse-est-tenue/` (FR) · `/en/how-can-we-tell-whether-a-promise-was-kept/` (EN) · ouverte le
2026-10-05 ; refondue le 2026-10-12 ; fiche écrite le 2026-11-17, à la reprise du lot « promesses-b »
(`D:\PRO\06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\promesses-b\`), après la relecture des sources.

## Forme

`juridique-institutionnel` et `quantitatif`. Critères : définitions et champs des deux mesures (âge, territoire, logement,
registre ou enquête), millésime et date de chaque relevé, ruptures de série datées et attribuées à leur source,
incertitude d'enquête dite ; aucune contribution comptable présentée comme un effet ; chaque nombre lu par le générateur
(`scripts/update_promesses_mesurer.py`, gardes M0 à M9, mutations vues mordre).

## Fiche de conception

### Question centrale

Quand un candidat promet de faire baisser le chômage, quel chiffre regarder, depuis quand, avec quelle règle de comptage,
et quelle part du résultat peut-on lui attribuer ?

### Enjeu

Deux chiffres exacts, publiés par des institutions différentes, peuvent dire deux histoires différentes du même mandat ; qui
juge une promesse sans choisir son indicateur ni vérifier sa règle peut conclure à volonté.

### Croyance initiale

« Le chiffre du chômage » serait un seul nombre ; ou bien, à l'inverse, les chiffres seraient « truqués » parce qu'ils
divergent.

### Découverte principale

En 2024, selon l'estimation de l'Insee, 49 % seulement des inscrits en catégorie A sont chômeurs au sens du BIT, et 62 %
des chômeurs au sens du BIT sont inscrits en catégorie A ; la plupart des autres inscrits sont eux aussi sans emploi ; et
la règle de comptage des inscrits a changé en 2022, à la fin de 2024 et en 2025, dans des sens opposés. — Lignes qui la
portent : relecture `SOURCES\comment-savoir-si-une-promesse-est-tenue_R1.md`, l. 25-36 (CONFORME À LA SOURCE : tableur et PDF
de l'Insee, figure 2, recalculés), § 5 (la phrase « 49 % » prise seule laisse croire que l'autre moitié travaille : 84 % des
inscrits non chômeurs sont sans emploi), l. 72-116 (ruptures, conformes aux métadonnées de la Dares et à la Dreets).

### Mécanisme explicatif

Une enquête mesure une situation (sans emploi, disponible, en recherche active), un registre enregistre une inscription
et une catégorie administrative, qui dépendent de règles que l'opérateur et le législateur changent : les deux populations
se recoupent partiellement, et le registre bouge quand ses règles bougent. Une contribution comptable dit où se trouve une
hausse, non ce qui l'a causée. — Lignes qui le portent : `_R1`, l. 15-19 et 160-171 (définitions, contributions et leurs
réserves, conformes) ; P1-2 (le chiffrage de l'Insee est passé de « près de la moitié » à « moins de la moitié » entre le
n° 192 et le n° 270 : une contribution varie avec le trimestre, ce qui confirme qu'elle n'est pas un effet mesuré).

### Preuve décisive

Le croisement de l'Insee, restitué depuis le tableur et vérifié par une extraction indépendante du PDF (35 valeurs, figure 8
en témoin de définition) ; les séries de la Dares avec et sans les publics inscrits d'office, qui montent toutes deux au
1er trimestre 2025 (garde M9).

### Pouvoir discriminant

Explications rivales soutenues : « les chiffres divergent parce qu'ils sont manipulés » ; « la loi pour le plein emploi
explique la hausse ». Le croisement départage la première (deux définitions, populations qui se recoupent, écart expliqué
par les catégories) ; la seconde ne se départage pas avec ces données (contributions comptables, aucun contrefactuel), et la
page le dit. Robustesse : la série hors RSA et hors jeunes en parcours porte elle aussi la rupture de 2025 (variante
calculée ; nom complet de la série, définition de la Dares, depuis le 24/11/2026).

### Limite

Le croisement décrit la moyenne de 2024 ; aucune donnée lue ne mesure l'effet de la loi ; les séries corrigées des
changements de procédure que publient la Dares et France Travail n'ont pas été lues (CAPTCHA, relecture § 3).

### Valeur finale

Quatre questions réutilisables pour juger toute promesse de résultat sur l'emploi ; le croisement et les séries en CSV.

### Singularité

Cette page existe parce qu'elle met côte à côte, avec leurs ruptures datées et la suspension du label, deux mesures que le
lecteur ne trouve que séparément dans les publications de l'Insee et de la Dares.

### Raccords

- Définition de l'anthropie : écartée (page de faits).
- Livre *Un président peut-il tenir ses promesses ?* : retenu (bloc d'appel « Juger une promesse jusqu'au bout »).
- Working paper : écarté.
- Pages voisines : retenue « Neuf promesses de campagne » (thème Emploi, qui renvoie ici) ; « Une loi votée
  s'applique-t-elle tout de suite ? » (même dossier, barre des onglets).

## Fiche D0

Résultat visé : qu'un lecteur qui reprend un chiffre de chômage dise lequel, sur quel champ, et ne lise pas une contribution
comme un effet. Diagnostics : Search Console (« chômage BIT catégorie A », « différence chômage France Travail Insee »),
citations par les moteurs génératifs ; envoi programmé du 07 au 09/12/2026 qui cite la page. État initial et relevés J+30,
J+60 : à inscrire dans `06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` à la mise en ligne.

## Étapes de la méthode

- Plan d'outils : non fait à la reprise (page existante).
- Protocole du type : fait (2026-11-17, relecture `_R1` ; sources relues dans leur publication la plus récente : Informations
  rapides n° 270 du 10/11/2026 intégrées au générateur, garde M7 et mutation vues mordre).
- Scénarios, panel avant, contre-expertise de phase A : faits à la refonte du 12/10/2026 (`REFONTE_PILOTE\MESURER\`).
- Gardes vues mordre : fait (autotest du générateur : 9 mutations, dont celle du n° 270).
- Figures téléphone : inchangées (parité contrôlée par le générateur).
- Recette, juge interne à l'aveugle, premier écran : voir `LOT.md` du lot.
- Relecture phrase à phrase, instantané, accord de l'auteur : à la publication (pas avant le 10/12/2026, envoi du 07 au 09/12).
