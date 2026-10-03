# Direction générale du Trésor — Finances publiques : une situation dégradée, un redressement nécessaire

- **Référence publiée** : Direction générale du Trésor (sous-direction des finances publiques), « Finances publiques : une situation dégradée, un redressement nécessaire », *Trésor-Éco*, n° 403, septembre 2026 (en ligne le 21/09/2026), ISSN 1777-8050, https://www.tresor.economie.gouv.fr/Articles/2026/09/21/finances-publiques-une-situation-degradee-un-redressement-necessaire
- **Version lue** : la version publiée (PDF « 2026-26-403.pdf » diffusé par la DG Trésor) — fichier `tresoreco403.txt` (texte extrait du PDF `tresoreco403.pdf`), SHA-256 du PDF `1f0cf7df4417dfcfbe684f0504f09ed0fd52d40a430dcc239117e601a0e90134`, 12 pages PDF, https://www.tresor.economie.gouv.fr/Articles/f43a5119-ed52-4b0c-9acb-24ca166d47ed/files/b228845d-3226-4438-b19f-c64ed0cb0f9e. Auteur collectif : aucun nom d'auteur, signature « Sous-direction des finances publiques » (p. PDF 1). Les graphiques 1 à 5 sont lus par leurs titres, sources et notes de lecture.
- **Lecture intégrale** : 03/10/2026, pages PDF 1 à 12 (synthèse, parties 1 à 4, encadré 1, notes 1 à 36, colophon) ; dernière phrase lue : « Pour toute demande presse, merci de vous adresser à presse@dgtresor.gouv.fr (01 44 87 73 24) ».
- **Qui parle, et d'où** : l'administration du ministère des Finances qui prépare la politique budgétaire, le programme de stabilité et le rapport d'avancement européen, au moment de l'examen du projet de loi de finances pour 2027 ; publication de la série « Les Clefs de l'économie », présentée en webinaire par la cheffe économiste le 06/10/2026. Avertissement d'usage : n'engage pas le ministère (E17). Non signé, non évalué par des pairs. **Ce que la position peut incliner** : le texte plaide la consolidation et, pour sa composition, « en priorité » la réduction de la dépense (E14) ; il présente les recettes surtout par leurs fonctions et leur « retour » (infrastructures, attractivité, p. PDF 4). Il reconnaît pourtant que des réformes de la dernière décennie ont « réduit durablement » les recettes (E6), et chiffre la part des recettes dans le redressement de 2011-2019 à 60 % (E2), ce qui n'est pas le plus commode pour sa thèse.

## Population, période, variables, méthode

- **Population** : la France ; comparaisons avec l'Allemagne (graphique de couverture, 2001-2025), l'UE (graphique 1, 2025) et la zone euro (structure des prélèvements 2024, dépense par fonction 2024).
- **Période** : 2001-2025 pour le récit ; décompositions chiffrées sur 2011-2019 (amélioration du solde) et 2019-2025 (dégradation) ; effort structurel 2011-2025.
- **Sources** : Insee (comptes de la nation), Eurostat, calculs DG Trésor ; dette 2025 à 115,7 % (Insee), quand la page retient 115,6 % (Eurostat, notification).
- **Variables** : solde public total ; solde primaire ; « solde stabilisant la dette » défini comme **solde public total** (E4), approché par le produit de la croissance nominale et de la dette de l'année précédente ; effort structurel, indicateur conventionnel corrigé de la conjoncture.
- **Méthode** : récit comptable et décompositions du solde par poste ; aucune estimation économétrique.

## Résultat

- **Causes nommées de la dégradation** (lecture de l'institution, non une décomposition causale identifiée) : crises et mesures de soutien (E1) ; sur 2019-2025, dégradation de 2,7 points du solde (E7), dont l'ordre de 0,7 point par la charge d'intérêts (E8) et +1,0 point de dépenses de sécurité sociale hors charge de la dette (E9) ; réformes (taxe d'habitation, taux normal de l'impôt sur les sociétés) qui ont « réduit durablement » les recettes (E6).
- **Redressement 2011-2019** : +2,9 points de solde, à 60 % par les recettes, 24 % par la dépense hors charge de la dette, 14 % par l'environnement (E2).
- **Dette** : « relative stabilité » de 2001 à 2007, forte hausse à partir de 2008 (E3) ; hausse de 3 points par an en moyenne depuis 2023, les déficits primaires restant supérieurs au solde stabilisant (E5).
- **Solde stabilisant 2025** : −2,1 % du PIB **en solde total** (E4), pour un déficit de 5,1 % : 3 points d'écart.
- **Taux et croissance** : la remontée des taux inverse la période de r − g négatif et exige un léger excédent primaire à moyen terme (E12) ; la hausse des taux se répercute progressivement sur le stock à mesure du refinancement (E8) ; la charge d'intérêts n'est « pas à la main des pouvoirs publics » (E11).
- **Soutenabilité** : la stabilisation du ratio est une condition **nécessaire** (E10) ; « ce qui importe in fine » est la capacité à financer durablement la dette sans compromettre la croissance (E13).
- **Coquille relevée** : le rapport des quatre économistes est dit « publié en juin 2026 » (E15) puis « publié en juillet 2026 » (E16).

## Témoin (calcul du lecteur, séries publiées par Eurostat, `gov_10a_main`, % du PIB, relevé du 03/10/2026)

L'OFCE (fiche `ofce-2025-trajectoires.md`, E5, E6) attribue le creusement du déficit depuis 2017 à la baisse des
prélèvements, dépenses stables ; le Trésor attribue celui de 2019-2025 surtout à la dépense. Sur les séries publiées :
de 2017 à 2024, solde −2,4 points, recettes −3,1, dépenses hors intérêts −0,9 ; de 2019 à 2025, solde −2,8 points,
dépenses hors intérêts +1,2, recettes −0,9 ; de 2017 à 2019, dépenses −2,4. **Chacune des deux lectures se retrouve sur
sa fenêtre ; c'est l'année de départ qui fait la conclusion.** Ce calcul est porté par `update_dette_dynamique.py`
(jetons `ofce_*`, `tresor_*`, `entre_dep`, gardés), non par le texte.

Dette 2001-2007 sur la série de la page (Eurostat, PIB de la notification) : 59,3 % → 65,5 %, +6,2 points : la
« relative stabilité » du Trésor est une appréciation que la série ne soutient qu'en comparaison de la hausse d'après 2008.

## Ce que le texte ne dit pas

- **Il ne décompose pas la variation du ratio** en effet taux-croissance, solde primaire et flux-stock sur 1995-2025 ;
  il ne chiffre ni l'effet de l'inflation de 2021-2023 sur le ratio, ni le taux implicite par année.
- **Ses décompositions ne sont pas causales** : ce sont des imputations par poste sur des fenêtres choisies (2011-2019,
  2019-2025) ; le témoin ci-dessus montre que la fenêtre détermine le poste mis en avant.
- **Il ne mesure ni l'accès au marché ni la confiance des investisseurs** : il les invoque (crédibilité, p. PDF 8).
- **Il ne fixe aucun seuil de dette.**
- **Le « solde stabilisant » n'est pas celui de la page** : solde total contre solde primaire ; et l'approximation
  g × d(t−1) omet le facteur 1/(1 + g).

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| D1 | appuie | Même diagnostic sur 2001-2025 : la dette monte parce que les déficits restent supérieurs au solde stabilisant, y compris en période favorable (E5, p. PDF 2 note 3) ; aucune décomposition chiffrée de l'effet taux-croissance. |
| D2 | appuie (et éprouvé par le témoin) | Le texte décompose le solde par poste, sans causalité identifiée ; le témoin montre que le poste mis en avant dépend de l'année de départ : raison de plus de s'en tenir, sur la page, à « par quel terme ». |
| D3 | nuance | « Relative stabilité » de 2001 à 2007 (E3) contre +6,2 points sur la série de la page ; même profil ensuite (forte hausse à partir de 2008, recul 2021-2022, hausse depuis 2023). |
| D4 | appuie | La remontée des taux inverse la période de r − g négatif (E12) ; répercussion progressive par le refinancement (E8). Projection qualitative, non chiffrée. |
| B1 | sans rapport | Aucune comparaison de pays qui ont réduit leur dette. |
| B2 | appuie | Solde stabilisant dépendant de la croissance et de la dette de l'année précédente (E4), donné pour une année. |
| B3 | appuie | La stabilisation est une étape (« condition nécessaire », E10) ; le texte distingue stabiliser et dégager un excédent (E12). |
| B4 | appuie | Soutenabilité = capacité à financer durablement la dette (E13), stabilisation nécessaire mais non suffisante (E10), crédibilité invoquée, non mesurée. |
| T1 | **met en danger, puis nuance** | La DG Trésor nomme des causes à la dégradation de 2019-2025 (E6 à E9), comme la Note du CAE : la page le dit déjà depuis la contre-expertise. Mais ses chiffres sont des imputations par poste sur une fenêtre ; le témoin montre qu'une autre fenêtre (OFCE, 2017) en met en avant un autre. La phrase « aucun texte ne fournit une décomposition causale des déficits primaires 1995-2025 » tient. |
| T2 | appuie | E8 (répercussion progressive à mesure du refinancement), E12 (inversion de r − g), E11 (charge « pas à la main des pouvoirs publics ») ; observation 2025 : charge 65,7 Md€, +10 Md€ par an (p. PDF 3). |
| T3 | appuie | Aucun seuil ; stabilisation « condition nécessaire » ; solde stabilisant total −2,1 % pour un déficit de 5,1 % : 3 points d'écart, comme les 2,9 points mesurés par la page en solde primaire — deux conventions, un même écart. |

## Extraits exacts

E1. p. PDF 1 : « Après une amélioration continue entre 2011 et 2019, le solde public s'est détérioré sous l'effet des crises successives et des mesures de soutien mises en œuvre pour en atténuer les conséquences économiques et sociales. »
E2. p. PDF 2 : « l'amélioration du solde nominal entre 2011 et 2019 (+2,9 pt de PIB) s'explique à 60 % par l'effort en recettes, à 24 % par la maîtrise de la dépense hors charge de la dette, et à 14 % par l'environnement favorable »
E3. p. PDF 2 : « Après une relative stabilité entre 2001 et 2007, favorisée par une croissance soutenue, le ratio de dette s'est fortement accru à partir de 2008 »
E4. p. PDF 2 : « Il se calcule comme le produit entre le taux de croissance nominale du PIB et la dette en points de PIB de l'année N-1(voir partie 3). En 2025, le solde stabilisant la dette était de –2,1 % du PIB. »
E5. p. PDF 3 : « Il repart toutefois à la hausse depuis 2023, de 3 points de PIB par an en moyenne, les déficits primaires demeurant supérieurs au solde stabilisant la dette »
E6. p. PDF 5 : « notamment la suppression progressive de la taxe d'habitation sur les résidences principales et la baisse du taux normal de l'impôt sur les sociétés, ont contribué à réduire durablement le niveau des recettes publiques »
E7. p. PDF 7 : « certaines dépenses publiques ont connu un fort dynamisme sur la période 2019-2025, participant à la dégradation de 2,7 points du solde public. »
E8. p. PDF 7 : « Ce poste de dépense explique de l'ordre de 0,7 point de PIB de la hausse du déficit public, évolution appelée à se poursuivre car l'augmentation des taux est répercutée progressivement sur le stock de dette à mesure qu'elle est refinancée. »
E9. p. PDF 7 : « les dépenses des administrations de sécurité sociale ont connu un fort dynamisme entre 2019 et 2025 (+1,0 point de PIB) »
E10. p. PDF 8 : « La stabilisation du ratio de dette constitue une condition nécessaire à la soutenabilité des finances publiques. »
E11. p. PDF 8 : « Cette dernière n'étant pas à la main des pouvoirs publics, stabiliser la dette implique d'améliorer le solde primaire au-delà d'un niveau appelé le »
E12. p. PDF 8 : « la remontée des taux vient inverser ce phénomène et nécessite désormais d'atteindre un léger excédent primaire à moyen terme pour stabiliser le ratio de dette. »
E13. p. PDF 3 : « Ce qui importe in fine est la capacité de l'État à financer durablement sa dette sans compromettre sa croissance. »
E14. p. PDF 9 : « la consolidation budgétaire pourrait passer en priorité par une réduction de la dépense publique »
E15. p. PDF 1 : « Un rapport de quatre économistes publié en juin 2026 »
E16. p. PDF 8 : « Dans un rapport publié en juillet 2026 »
E18. p. PDF 4 : « sur 2019-2024, la dépense française a progressé de +1,6 point de PIB contre +2,4 points en zone euro »
E17. p. PDF 12 : « Ce document a été élaboré sous la responsabilité de la direction générale du Trésor et ne reflète pas nécessairement la position du ministère »
