# Fiche de conception — Neuf promesses de campagne : que peut vraiment faire un président ?

Page : `/que-peut-faire-un-president-promesse-par-promesse/` (FR) · `/en/what-can-a-president-do-promise-by-promise/` (EN) ·
ouverte le 2026-11-01

## Forme

`juridique-institutionnel` (protocole : distinguer pouvoir formel, initiative, décision, contreseing, mise en œuvre et
effet réel ; références juridiques datées ; conditions, exceptions et séquences de décision contrôlées séparément ;
aucun jeu de données artificiel). Page **sans données** : elle ne publie aucune série, elle applique une grille à neuf
thèmes de promesses. Elle ne déclare donc pas `donnees:` et ne fabrique pas de jeu pour satisfaire le modèle
quantitatif. Les chiffres éventuels sont ceux du livre, sourcés en clair et datés (catégorie « écrit en clair, étude
citée » de l'audit des affirmations de méthode).

Origine : arbitrage PRO-20261101-060949, point 1 (« compléter les cinq promesses » ; tableau transversal des neuf).
**Écart déclaré à l'arbitrage** : celui-ci prévoyait d'enrichir une page mère existante ; aucune page du dossier
« promesses » ne traite les promesses par thème (chacune traite un mécanisme : décider seul, faire voter, appliquer,
mesurer, délais, référendum, Europe). Ajouter cinq sections thématiques à l'une d'elles l'écarterait de sa question.
D'où une page mère nouvelle, dans le dossier, qui regroupe les neuf thèmes en sections ancrées (règle « une question,
une section d'une page mère »).

## Fiche de conception

### Question centrale

Sur chacune des grandes promesses d'une campagne présidentielle — santé, salaires, prix, école, emploi, sécurité, dette,
immigration, climat —, que peut décider un président dans sa propre chaîne de pouvoir, que doit-il faire voter, que
doit-il négocier, et qu'est-ce qui ne dépend pas de lui ?

### Enjeu

Avant l'élection d'avril-mai 2027, distinguer ce qu'un candidat contrôle de ce qu'il espère ; après, distinguer celui qui
n'a pas pu, celui qui n'a pas essayé, et celui qui revendique un résultat qu'il n'a pas causé.

### Croyance initiale

« Élu, le président peut appliquer son programme » — ou, en miroir, « un président ne peut rien ».

### Découverte principale

Le pouvoir se répartit différemment selon le thème : sur les salaires, la décision directe porte sur le SMIC et les
traitements publics, pas sur les salaires du privé ; sur les prix, sur quelques tarifs réglementés et taxes, pas sur
les prix de marché ; sur l'emploi, sur des dispositifs, pas sur les embauches ; sur la sécurité, sur les moyens et
l'organisation, avec une chaîne d'exécution longue ; sur l'immigration, une partie des règles relève du droit européen
et des conventions internationales. Aucune promesse n'est « tenable » ou « intenable » en bloc : chacune se découpe en
zones.

### Mécanisme explicatif

La grille en quatre zones du livre *Un président peut-il tenir ses promesses ?* : ce que le président décide dans sa
chaîne de pouvoir (décrets, nominations, consignes, sous contreseing) ; ce qu'il doit faire voter (loi, budget) ; ce
qu'il doit négocier (partenaires sociaux, collectivités, Union européenne, autres États) ; ce qui ne dépend pas de lui
(conjoncture, comportements, délais incompressibles).

### Preuve décisive

Pour chaque thème, l'instrument juridique qui porte la décision, cité dans le texte en vigueur (Constitution, codes,
règlements européens), tel que le livre l'établit et le source (appareil de sources du livre, ≈ 300 entrées), relu à la
source pour chaque référence reprise sur la page.

### Pouvoir discriminant

Sans objet au sens d'une page de données (aucun graphe). Le pouvoir discriminant de la page est la grille elle-même :
elle départage, pour une même promesse, la part qui relève d'une décision, d'un vote, d'une négociation ou d'un résultat
extérieur — là où le débat public oppose seulement « tenable » et « intenable ».

### Limite

La page résume chaque chapitre du livre ; elle ne refait pas la démonstration complète ni l'examen des promesses déjà
formulées. Elle n'évalue aucun candidat, ne donne aucun conseil de vote, ne déclare aucune promesse bonne ou mauvaise.
Le droit cité est celui en vigueur au jour de la rédaction (date de lecture indiquée).

### Valeur finale

Une grille réutilisable : le lecteur peut prendre n'importe quelle promesse de 2027 et la découper lui-même en quatre
zones, thème par thème, avec le tableau transversal des neuf promesses.

### Singularité

Cette page existe parce qu'elle applique, thème par thème, une même grille de pouvoir aux promesses de campagne, ce que
le lecteur ne trouve pas dans les fiches institutionnelles générales (vie-publique.fr, « le rôle du président ») ni dans
les pages du dossier, qui traitent chacune un mécanisme et non un thème (lues le 01/11/2026).

### Raccords

- Livre *Un président peut-il tenir ses promesses ?* : **retenu** — chaque section se clôt sur ce que le chapitre
  correspondant ajoute ; appel au livre en fin de page.
- Pages du dossier : **retenues** — `/pouvoirs-du-president-de-la-republique/` (zone « décider »),
  `/qui-peut-faire-adopter-une-loi/` (zone « faire voter »), `/ce-que-la-france-peut-decider-dans-l-union-europeenne/`
  (zone « négocier », immigration), `/une-loi-votee-s-applique-t-elle-tout-de-suite/` (exécution),
  `/comment-savoir-si-une-promesse-est-tenue/` (emploi : mesurer), `/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/`
  (santé). Pages hors dossier pour dette, école, climat (sections courtes de renvoi).
- Définition de l'anthropie, working paper : **écartés** — page de faits institutionnels ; le livre lui-même ne teste
  pas l'anthropie (« Note de l'auteur »).

## Fiche D0

Résultat visé : que les lecteurs qui cherchent « que peut faire un président sur les salaires / les prix / l'emploi /
la sécurité / l'immigration » trouvent une réponse fiable et le livre qui la prolonge. Diagnostics : indexation de la
page, liens entrants depuis le dossier. Pas de campagne de mesure des réponses d'IA (décision de l'auteur du
01/11/2026). État initial : page inexistante (01/11/2026).

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : fait (01/11/2026) — retenus : vérificateur de références (articles
  de code et textes de l'Union cités), relecture de langue (`check_langue.py`), recette 320-1280 ; panel : non (page non
  pilote).
- Protocole du type juridique-institutionnel : appliqué dans cette fiche (forme, preuve décisive).
- Scénarios d'architecture : fait (01/11/2026) — trois envisagés : sections ajoutées à une page existante (écarté :
  déplace la question des pages) ; une page par promesse (écarté : règle « une question, une section ») ; page mère à
  neuf sections ancrées (retenu).
- Panel avant : non fait (page nouvelle, non pilote).
- Contre-expertise de phase A : faite au niveau du programme (PRO-20261101-060949) ; pas de contre-expertise propre à
  cette architecture.
- Rédaction des sections depuis les chapitres du livre : fait (01/11/2026) — six rédacteurs, chacun sur un chapitre et
  `SOURCES.md` ; brouillons dans `D:\PRO\06_PROMOTION\PLAN_SUJETS_LIVRES_2026-11\BROUILLONS\` ; relus contre les
  chapitres (chiffres et articles des sections salaires et prix contrôlés dans le chapitre ou `SOURCES.md`) ; retouches :
  une phrase obscure retirée (sécurité), un « y » ambigu levé (immigration).
- Vérification des références : fait (01/11/2026) — `python -m sources verifier` : 17 références CONFORMES (5 textes,
  10 articles, 2 actes de l'Union), 0 écart, rapport `PLAN_SUJETS_LIVRES_2026-11\VERIF_SOURCES_2026-11-01.md` ; 12 articles
  non rattachés par l'outil relus un à un sur Légifrance (MCP `legifrance_article_code`) : L. 122-1 et L. 411-1 CSI,
  L. 1434-4 CSP, L. 611-1 Ceseda, L. 6121-1, L. 2261-17 et L. 2261-25 du code du travail TROUVÉS en vigueur et
  conformes à ce que la page en dit ; non relus par l'outil : L. 222-1 A C. env. (format refusé), L. 2261-24, L. 2261-32
  à 34, L. 3231-12 (repris de l'appareil du livre).
- Gardes vues mordre : sans objet (aucun jeton de données).
- Figures téléphone : sans objet (aucune figure). Tableau des neuf promesses en HTML (`div.table-scroll` +
  `table.pouvoirs-table`, `data-label` par case) : la règle globale `main table` écrasait les colonnes 4 et 5 à partir
  de 1024 px (recette du 01/11, premier passage en ÉCART), et le mode cartes perdait ses libellés au téléphone.
- Version anglaise : fait (01/11/2026), `/en/what-can-a-president-do-promise-by-promise/`, traduite sur le modèle de
  `/en/what-can-the-french-president-decide-alone/` (gloses des institutions, « our translation » pour les citations).
- Relecture de langue : fait (01/11/2026), `check_langue.py` sur le texte FR servi : 6 signalements, tous écartés à la
  lecture (« victimation » est le terme de l'enquête ; accords corrects).
- Recette 320-1600 : fait (01/11/2026), FR et EN `RECETTE OK` après correction du tableau ; barre du dossier à huit
  onglets contrôlée sur `/qui-peut-faire-adopter-une-loi/` et son pendant anglais : `RECETTE OK`.
- Relecture phrase à phrase : fait (01/11/2026) — FR sur les brouillons assemblés, EN sur le texte servi ; deux
  reprises imposées par `check-rendu-ressources.py` (« ont monté » → « ont augmenté » ; « its 2021 point » → « its 2021
  level »).
- Instantanés de relecture : fait (01/11/2026), FR et EN, `docs/relectures/`.
- Contrôles : `check-all --ci` 0 ; build `--minify` 0 ; `audit-liens-build` 0 critique ; `check-dates-build` 73/73 ;
  `check-rendu-ressources` sans écart sur la page.
- Panel après, gate éditorial : non faits (page non pilote ; la contre-expertise de la page en tient lieu).
- Contre-expertise de la page : faite (01/11/2026), PRO-20261101-063929, option B acceptée ; arbitrage écrit ; corrections appliquées FR et EN ; recomptage des chiffres emploi, sécurité, immigration dans le livre ; contrôles et recette relancés : 0 écart. Accord de l'auteur : à recueillir.
