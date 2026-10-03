# Éric Heyer, Mathieu Plane, Xavier Ragot, Raul Sampognaro et Xavier Timbeau — Quelles trajectoires pour les finances publiques de la France ? (document de travail)

- **Référence publiée** : Heyer, É., Plane, M., Ragot, X., Sampognaro, R. et Timbeau, X., « Quelles trajectoires pour les finances publiques de la France ? », document de travail de l'OFCE (Working Paper) n° 13, publié le 11/07/2025, https://ofce.github.io/psmt/PB.pdf. Le texte se désigne lui-même aussi comme « Policy Brief » (p. PDF 19 et 25). C'est le document que résume le billet du blog de l'OFCE (fiche `ofce-2025-trajectoires.md`), dont il établit la date : « Publié le : 2025-07-11 » (E15).
- **Version lue** : PDF en ligne — fichier `ofce_psmt_pb.txt` (texte extrait du PDF `ofce_psmt_pb.pdf`), SHA-256 du PDF `9cb4bdbb720dd7916b22ff3beffe135f6d213bda056ddbeb297dc660b6a7c8b9`, 27 pages PDF, généré le 17/07/2025 (métadonnées). Figures 1.1 à 2.1 lues par leurs titres ; tableaux 1.1 à 2.2 lus dans le texte extrait.
- **Lecture intégrale** : 03/10/2026, pages PDF 1 à 27 (principaux points, sections 1 à 3, encadrés 1 à 3, tableaux, références) ; dernière ligne lue : « Timbeau, X., Aurissergues, E. & Heyer, E. (2021), « La dette publique au XXI siècle. Une analyse de la dynamique de la dette publique avec Debtwatch », Policy brief de l'OFCE. »
- **Qui parle, et d'où** : cinq économistes de l'OFCE (Sciences Po), dont son président, X. Ragot, également coauteur de la Note du CAE n° 82 et du Focus n° 124. Document de travail, non évalué par des pairs. **Position** : le texte défend un ajustement « plus progressif » que celui du gouvernement, pour limiter la hausse du chômage (p. PDF 25), et lit la dégradation depuis 2017 comme le produit de la politique fiscale de l'offre (E4) ; il se présente comme un diagnostic, non comme le choix des bonnes politiques (note 2, p. PDF 6). Il juge la remontée de la charge d'intérêts moins certaine que les projections officielles (E12), lecture qui sert sa thèse d'un ajustement étalé. À rapprocher de la DG Trésor (fiche `tresor-eco-403-2026.md`), qui plaide une consolidation « en priorité » par la dépense : deux institutions situées, aux conclusions opposées sur la composition.

## Population, période, variables, méthode

- **Population** : la France ; comparaisons avec la zone euro, l'Allemagne, l'Italie, l'Espagne, les États-Unis, le Royaume-Uni.
- **Période** : 2000-2024 ; découpage par cycles (datation de l'AFSE) : 2000-2007, 2007-2011, 2012-2019, 2019-2024 ; « période récente » 2017-2024, ouverte par l'élection présidentielle de 2017 (E1).
- **Variables** : solde public et solde **structurel** (FMI, Insee, calculs des auteurs) ; prélèvements obligatoires par agent payeur, sans incidence économique (note 8) ; dépenses en points de PIB **potentiel** pour 2017-2024 (tableau 1.4) ; solde primaire stabilisant.
- **Méthode** : décomposition comptable du solde (structurel, mesures exceptionnelles, intérêts, conjoncture) ; projections du modèle Debtwatch v2 (stochastique, 256 tirages), hypothèses r = g = 3 % à moyen terme, multiplicateurs 0,5 et 1.

## Résultat

- **2017-2024** : déficit de 3,4 % à 5,8 % du PIB ; 2,1 points sur 2,4 imputés au solde primaire structurel (E2), 0,6 aux mesures exceptionnelles, 0,3 aux intérêts (E3), compensés en partie (0,6) ; dégradation expliquée « essentiellement par la baisse non financée des PO » (E4), dépenses primaires en recul de 0,3 point de PIB potentiel (E5), dépense totale stable (E16) ; baisse des PO de 2,5 points (taxe d'habitation −1,0, cotisations patronales −1,1, CVAE −0,5, IR −0,3 ; CSG +0,9).
- **Depuis 2019, par rapport à la zone euro** : la dégradation française n'est pas imputée à une hausse plus marquée des dépenses (+1,8 point en France, +2,6 en zone euro) mais à la baisse des recettes françaises (−1,6) (E6, E7).
- **2000-2007** : près de la moitié de l'écart de déficit avec la zone euro date d'avant la crise de 2008 (E8) ; solde structurel français −2 points, dépenses +1 point quand elles baissent de 1,4 en zone euro (p. PDF 6).
- **Solde stabilisant** : en 2024, le solde primaire est inférieur de 2,1 points de PIB à celui qui stabiliserait la dette (E9).
- **Charge d'intérêts** : inférieure en 2024 à son niveau de 2000, de 0,9 point de PIB (E14) ; renouveler au taux à 10 ans (3,3 % au 4 juillet 2025) les 900 Md€ de titres arrivant à échéance d'ici 2029 coûterait 15 Md€, +0,5 point de PIB (E10), contre +1,2 point projeté par le FMI (E11) : « un peu plus rassurant que les publications officielles » (E12).
- **Projection** : dans le modèle, taux apparent inférieur à la croissance nominale à partir de 2026 (E13), r − g → 0 à long terme ; ajustement de long terme de 3,4 points pour stabiliser à 110 % ; 2,8 points d'ici 2029 en trajectoire progressive.

## Témoin (calcul du lecteur, séries de la page)

Eurostat `gov_10a_main`, % du PIB, 2019 → 2024 : dépenses +1,7, recettes −1,8 (OFCE : +1,8 et −1,6). Écart au solde
stabilisant en 2024 sur la série de la page (`dette_baisse.json`) : −2,0 points (OFCE : −2,1). **Les chiffres de l'OFCE
se retrouvent ; ce qui le distingue de la DG Trésor n'est pas la mesure mais la référence** : l'OFCE juge la
dégradation depuis 2019 **par rapport à la zone euro**, la DG Trésor la décompose **en niveau**.

## Ce que le texte ne dit pas

- Il ne décompose pas la variation du ratio de dette en effet taux-croissance et solde primaire sur 1995-2025.
- Ses décompositions sont comptables, sur des périodes choisies (cycles, élection) ; la causalité de la politique
  fiscale n'est pas identifiée, et l'incidence économique des PO est exclue de son propre aveu (note 8).
- Ses projections reposent sur des hypothèses (r = g, multiplicateurs, croissance potentielle 1,2 %) qu'il dit incertaines.
- Coquille : « L'effort à accomplir jusqu'en 2019, l'horizon du PSMT » (p. PDF 24), pour 2029.

## Effet sur nos hypothèses

| Id | Effet | Motif précis |
|---|---|---|
| O1 | **nuance** | Fidèle pour 2017-2024 (E1 à E5, E16) ; mais la page ne dit pas que l'OFCE voit aussi, depuis 2019, une hausse des dépenses (+1,8), qu'il compare à la zone euro (E6). Présenter l'OFCE comme lisant « les recettes » sans dire sa référence (la zone euro) appauvrit sa position. |
| O2 | **appuie, et précise** | La période (2017 ouverte par l'élection, E1) et la grandeur (PO par agent payeur, dépenses en PIB potentiel) diffèrent bien ; s'y ajoute la **référence** (zone euro contre niveau). Les chiffres des deux institutions se retrouvent sur les séries de la page (témoin). |
| O3 | appuie | Décomposition comptable du solde, non du ratio sur 1995-2025, sans causalité identifiée. |
| D3 | appuie | 2000-2007 : dégradation structurelle de 2 points, dépenses en hausse quand elles baissent en zone euro — contre la « relative stabilité » du Trésor. |
| B2 | appuie | Solde stabilisant 2024 : écart de 2,1 points (E9), comme les 2,0 de la page. |
| T2 | **nuance** | Le taux implicite remonte (accord), mais l'OFCE juge la hausse de la charge moins forte que les projections officielles (E10 à E12) et suppose un taux apparent sous la croissance nominale à partir de 2026 (E13) : projection, mais à dire face à « l'égalité de 2025 n'est pas un état acquis ». |

## Extraits exacts

E1. p. PDF 13 : « Sur la période récente, que l'on fait débuter à la première élection d'Emmanuel Macron en 2017, les comptes publics français ont connu une détérioration plus marquée que ceux de l'ensemble de la zone euro. »
E2. p. PDF 13 : « Selon nos calculs, 2,1 points seraient imputables à la dégradation du solde public structurel primaire, ce qui représente plus de 80 % de l'aggravation totale du déficit sur la période. »
E3. p. PDF 13 : « la charge d'intérêts a contribué pour 0,3 point de PIB à l'augmentation du déficit au cours de cette période. »
E4. p. PDF 16 : « La dégradation du solde structurel observé entre 2017 et 2024 s'explique essentiellement par la baisse non financée des PO, et non par une dérive des dépenses publiques primaires. »
E5. p. PDF 16 : « celles-ci ont reculé de 0,3 point de PIB potentiel sur la période. »
E6. p. PDF 7 : « Il convient de noter que cette dégradation n'est pas attribuable à une augmentation plus marquée des dépenses publiques en France par rapport à la zone euro (respectivement 1,8 et 2,6 points de PIB), mais plutôt à une diminution significative des recettes publiques françaises (-1,6 point de PIB) »
E7. p. PDF 6 : « Depuis 2019, la situation budgétaire en France se dégrade de nouveau par rapport au reste de la zone euro. »
E8. p. PDF 6 : « Il apparaît que près de la moitié de l'écart entre le déficit public français et la moyenne de la zone euro a eu lieu avant la crise financière globale de 2007-2008 »
E9. p. PDF 9 : « En France, la persistance de ce déséquilibre entre dépenses et recettes publiques se traduit en 2024 par un solde public primaire significativement inférieur (un écart de -2,1 points de PIB) au niveau requis pour stabiliser la dette »
E10. p. PDF 12 : « implique un surcoût pour les finances publiques de 15 milliards d'euros (+0,5 point de PIB). »
E11. p. PDF 11 : « Selon les projections de l'organisme publiées en avril 2025, la charge d'intérêts française devrait alors augmenter de 1,2 point de PIB par rapport au niveau de 2024. »
E12. p. PDF 12 : « Ce calcul est donc un peu plus rassurant que les publications officielles. »
E13. p. PDF 23 : « Cela s'explique principalement par la prise en compte, à partir de 2026, d'un taux d'intérêt apparent (ou moyen pondéré) inférieur à la croissance nominale. »
E14. p. PDF 10 : « Ainsi, en 2024, la charge d'intérêts supportée par les administrations publiques françaises reste inférieure à son niveau de 2000 (de -0,9 point de PIB) »
E15. p. PDF 1 : « Publié le : 2025-07-11 »
E16. p. PDF 4 : « Au cours de cette période, les dépenses publiques sont restées stables. »
