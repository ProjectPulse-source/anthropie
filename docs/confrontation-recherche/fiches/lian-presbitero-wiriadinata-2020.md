# Weicheng Lian, Andrea F. Presbitero et Ursula Wiriadinata — Public Debt and r − g at Risk

- **Référence publiée** : Lian, W., Presbitero, A. F. et Wiriadinata, U., « Public Debt and r - g at Risk », *IMF Working Paper* WP/20/137, Fonds monétaire international, département de la recherche, juillet 2020, https://www.imf.org/en/publications/wp/issues/2020/07/24/public-debt-and-r-g-at-risk-49586. Auteurs, numéro et date vérifiés p. PDF 1 et 2 (« Prepared by Weicheng Lian, Andrea F. Presbitero, and Ursula Wiriadinata », « July 2020 »).
- **Version lue** : la version publiée (PDF du FMI, lien « Download PDF » de la page du document) — fichier `imf_wp20137.txt` (texte extrait du PDF `imf_wp20137.pdf`, PyMuPDF), SHA-256 du PDF `b38ff0cf6994e57ebc92190499d1b64999e371b84c499031d55e30313869dfa0`, 997 959 octets, 42 pages PDF. Le PDF refuse les scripts (« Access Denied ») ; il a été téléchargé le 16/10/2026 par le navigateur, depuis la page du document, sur mandat de l'auteur. Les figures sont des graphiques : seuls leurs titres, axes et notes ont été lus.
- **Lecture intégrale** : 16/10/2026, pages PDF 1 à 42 (page de titre, résumé, sections 1 à 5, références, figures 1 à 9, annexe en ligne : figures A1 à A6, tableaux A1 à A5) ; dernière ligne lue : tableau A5, colonne « No EMs ».
- **Lecture antérieure** : la chronique des auteurs sur *VoxEU* (fiche `wiriadinata-presbitero-2020-voxeu.md`), lue la veille de la disponibilité du document ; elle est remplacée dans la page par le document lui-même, qui la nuance sur un chiffre (E4 et E5).
- **Qui parle, et d'où** : trois économistes du département de la recherche du FMI (adresses `@imf.org`, p. PDF 2). Document de travail, « research in progress », non évalué par des pairs ; avertissement d'usage : les vues sont celles des auteurs (E12). **Ce que cette position peut incliner** : l'institution conseille aux pays endettés la prudence budgétaire ; le document s'ouvre contre la lecture « marges de manœuvre » d'un écart négatif (Blanchard 2019) et choisit des mesures qui éclairent le risque (queues de distribution, retournements). À l'inverse, il ne conteste pas l'efficacité d'une politique contracyclique à taux plancher (p. PDF 18), il exempte les pays « valeurs refuges », et ses propres résultats bornent sa thèse pour une dette en monnaie nationale (E8, E9) ; il signale lui-même qu'il ne tient pas compte de la baisse séculaire des taux (E13).

## Population, période, variables, méthode

- **Population et période** : (a) 17 économies avancées, dont la France (E2), 1950-2019, 72 épisodes d'écart négatif ; (b) 31 économies avancées et 25 émergentes, dont la France, 2000-2019 (E7 ; tableau A1, p. PDF 38), sans les pays à compte de capital fermé ; (c) 29 avancées et 21 émergentes pour les chocs de croissance (note de la figure 7) ; (d) 50 pays, données quotidiennes 2000-2018, pour les chocs de volatilité.
- **Variables** : **r = taux marginal** (rendement des obligations publiques à 10 ans en monnaie nationale, à défaut une autre maturité longue), **non le taux effectif** (intérêts rapportés à la dette) (E1) ; g = croissance nominale ; r − g nominal. Dette en devises : part de la dette publique libellée en monnaie étrangère (Fiscal Space Dataset et sources nationales).
- **Méthode** : durée des épisodes régressée sur la dette initiale (effets fixes pays) ; logit du retournement par quartiles de dette ; régressions de quantiles de l'écart moyen futur (deux et cinq ans) sur la dette, avec taux, croissance, inflation et indicatrice de récession ; réponse des taux aux erreurs de prévision de croissance et au VIX (projections locales). Associations estimées, sans stratégie d'identification causale.

## Résultat

- **Estimé (a)** : épisodes d'écart négatif plus courts quand la dette initiale est plus élevée, de près de 5 mois par 10 points de dette (E3) ; probabilité de retournement d'environ 25 % sous la médiane à « almost 75 % » dans le quartile supérieur dans la section des résultats (E4), « more than 75 % » dans l'introduction (E5) — le document se contredit sur ce chiffre ; la page retient « près de 75 % ».
- **Estimé (b)** : de 40 à 120 % du PIB, neuvième décile de l'écart moyen des cinq années suivantes d'environ 0 à 2 points ; médiane +0,8 point, premier décile +1,2 point (E6) : le risque d'un écart élevé croît plus que l'écart typique, et la chance d'un écart très bas diminue. Les deux composantes, taux et croissance, y contribuent (E11).
- **Estimé (c), dette en devises** : à l'intérieur de chaque pays, l'écart suit la dette libellée en devises (E9) ; tableau A4 (p. PDF 41), effets fixes pays : coefficient de la dette en devises 15,55 (e.-t. 3,41) et 13,18 (3,50), significatifs ; dette en monnaie nationale 2,26 (1,99) et 1,48 (2,43), non significatifs. Les pays très endettés dont la dette est peu libellée en devises gardent un écart faible et négatif (E8).
- **Estimé (d), chocs** : une croissance inférieure d'au moins 1 point aux prévisions va avec +75 points de base en moyenne, +72 pour une dette élevée peu libellée en devises, +155 pour une dette élevée et largement en devises (p. PDF 15) ; aucune relation entre dette et sensibilité au VIX pour les valeurs refuges (États-Unis, Royaume-Uni, Japon, Suisse, Allemagne).
- **Interprétation des auteurs** : l'écart est « endogène » à la taille et à la dynamique de la dette (E10) ; la balance des risques penche du mauvais côté pour les pays à dette élevée et largement en devises (E14).

## Ce que le texte ne dit pas

- **Rien sur la France en particulier**, ni sur la zone euro : la France est dans les échantillons sans être isolée ; l'euro y compte comme monnaie nationale, et le document ne traite pas le cas d'une monnaie nationale émise sans banque centrale nationale.
- **Rien sur le taux implicite** : r est un taux de marché (E1) ; la transmission au taux implicite de la page (refinancement du stock) n'est pas étudiée.
- **Aucun seuil de dette** : quartiles d'échantillon ; 40 et 120 % sont deux points d'une courbe estimée.
- **Pas de causalité établie** : des associations, et un biais que les auteurs disent jouer contre eux (E13).

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| B2 | nuance | Le solde stabilisant de la page est calculé à écart donné ; le document trouve l'écart plus élevé, et sa queue haute nettement plus élevée, quand la dette l'est (E6, E10). Appui à « il n'est pas une constante ». Mais l'écart y est mesuré au taux à 10 ans (E1), non au taux implicite, et l'association passe surtout par la dette en devises (E8, E9) : pour une dette en euros, la portée est bornée. |
| B4 | appuie | La durée d'un écart négatif et la probabilité de son retournement dépendent du niveau de dette (E3, E4), et la réaction des taux aux chocs aussi : la soutenabilité ne se lit pas dans le seul écart observé. Même sens que Clavères (taux à 10 ans, 18 pays avancés) ; prudence sur la position de l'institution (E12). |

## Extraits exacts

E1. p. PDF 7 : « Throughout the analysis, we measure r using the marginal rate on government debt (the interest rate on new government borrowing or on the secondary market) rather than the effective interest rate (the ratio of the interest expenses to government debt), as the former responds faster to changes in global and domestic conditions (Mauro and Zhou, 2020). »
E2. p. PDF 7 : « The 17 AEs are Australia, Belgium, Canada, Denmark, Finland, France, Germany, Greece, Italy, Japan, Norway, Portugal, Spain, Sweden, Switzerland, the UK, and the U.S. »
E3. p. PDF 9 : « the duration of negative r-g episodes is, on average, almost 5 months shorter. »
E4. p. PDF 10 : « from about 25% for countries with debt-to-GDP ratios below the sample median to almost 75% for countries in the top quartile of the public debt-to-GDP distribution »
E5. p. PDF 4 : « the likelihood of a reversal increases from about 25% for debt to-GDP ratios below the median to more than 75% for countries in the top quartile of the debt-to-GDP distribution. »
E6. p. PDF 12 : « as the current debt-to-GDP ratio increases from 40% to 120%, the 90th percentile of average r-g over the next five years increases from around zero to 2 percent. Meanwhile, the median and 10th percentile also increase, by around 0.8 and 1.2 percentage points, respectively. »
E7. p. PDF 8 : « To avoid having our results driven by changes in the sample composition, we restrict the sample period to the last 20 years (2000-2019). »
E8. p. PDF 13 : « While high-debt countries with a low share of foreign currency denominated debt still have low and negative interest rate-growth differentials, it is when countries combine a high debt with a high share of foreign currency denomination that r-g becomes positive and significantly larger than in the rest of the sample. »
E9. p. PDF 13 : « shows that the dynamics of the interest rate-growth differential is driven by foreign currency denominated debt, especially in the within-country dimension »
E10. p. PDF 10 : « especially because the interest rate-growth differential is endogenous to the size and dynamics of public debt (Wyplosz, 2019). »
E11. p. PDF 5 : « These patterns hold for interest rates and growth separately, suggesting that both components contribute to the positive association between public debt and r-g at risk. »
E12. p. PDF 2 : « The views expressed herein are those of the authors and should not be attributed to the International Monetary Fund, its Executive Boards, or its management. »
E13. p. PDF 14 : « in the data, rising public debt went together with a secular decline in interest rate, and our analysis does not consider that it becomes easier to finance public debt when interest rates are lower. »
E14. p. PDF 18 : « the balance of risks is tilted to the downside for countries with high public debts and a high share of foreign currency denominated public debt. »
