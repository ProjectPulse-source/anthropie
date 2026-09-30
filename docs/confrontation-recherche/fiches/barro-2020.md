# Robert J. Barro — r Minus g

- **Référence publiée** : aucune publication ultérieure n'est indiquée dans le texte lu. À citer comme document de travail : Barro, Robert J. (2020, révisé en juin 2021), « r Minus g », NBER Working Paper n° 28002. (Une éventuelle publication en revue n'a pas été recherchée ici : **non vérifié**.)
- **Version lue** : NBER Working Paper 28002, « October 2020, Revised June 2021 » (p. 1) ; fichier `barro2020_nber.pdf` (texte extrait `barro2020_nber.txt`), SHA-256 `e7483005b18f33778ab9b9919e563a4de2bdfdf9cb66a14071e46bec3dda3d1c`, 30 pages PDF (p. 24 et p. 30 vides) ; https://www.nber.org/system/files/working_papers/w28002/w28002.pdf . La numérotation des sections saute de III à V (pas de section IV dans la version lue).
- **Lecture intégrale** : 30/09/2026, pages PDF 1 à 30 ; dernière page de texte courant (p. 23) : « provide a baseline setting for models with heterogeneity » ; dernière page non vide (p. 29, références) : « Nonexpected Utility in Macroeconomics ».
- **Qui parle, et d'où** : Robert J. Barro, département d'économie de Harvard et NBER (p. 2). Document de travail **non évalué par les pairs** (E1). Aucun financement déclaré ; remerciements à Angeletos, Campbell, Gabaix, Steinsson et Reis. Le texte répond explicitement au débat ouvert par Blanchard (2019), qu'il cite (p. 3). Hors texte, et donc non établi par cette lecture : Barro est l'auteur de référence de l'équivalence ricardienne. Ce que cette position peut faire au propos : la conclusion ricardienne découle ici d'hypothèses posées d'entrée (agent représentatif relié à ses descendants, E17 ; Ponzi exclu, E6) ; elle vaut **dans** ce cadre et ne constitue pas une mesure.

## Population, période, variables, méthode

- **Partie empirique** (tableau 1, p. 25-26) : 14 pays de l'OCDE, dont la **France**, 1870-2019 pour les rendements (1870-2017 pour la croissance par tête, 1880-2019 pour la population), sauf dates de départ indiquées. Variables : rendements réels **réalisés** (moyenne arithmétique) des actions, des bons à court terme (type bons du Trésor à 3 mois) et des obligations d'État (environ 10 ans), déflatés par les prix à la consommation (E9) ; croissance du PIB et de la consommation par tête, croissance de la population. Données surtout de Global Financial Data.
- **Robustesse** : résultats semblables si l'échantillon commence en 1960 (E11).
- **Partie théorique** : modèle à agent représentatif de type « AK » (arbre fruitier de Lucas) avec dépréciation stochastique et risque de désastres rares, préférences Epstein-Zin-Weil. Calibrage (tableau 2) : probabilité de désastre de 4 % par an, taille moyenne 0,21, estimées sur 185 contractions d'au moins 10 % du PIB par tête dans 40 pays (1870-2012). Le modèle donne un taux sans risque d'environ 0,1 % et un rendement espéré des actions de 6,2 %, pour une croissance de 3,2 % (moyenne américaine de long terme).
- **Obligations d'État** (section III) : bons publics assimilés aux titres privés sûrs à court terme (E13) ; contrainte budgétaire intertemporelle, jeu de Ponzi de l'État exclu par l'hypothèse que les agents privés refusent de détenir des titres de valeur actuelle asymptotiquement positive.

## Résultat

1. **Empirique** : sur la moyenne des 14 pays, rendements réels de 7,0 % (actions), 1,1 % (bons à court terme) et 2,6 % (obligations) ; croissance des niveaux : 2,8 % (PIB) et 2,6 % (consommation). La condition r > g tient avec le rendement des actions, pas avec celui des bons (E3) ; le rendement réel des obligations est **proche** de la croissance (E4). Tout dépend donc de la définition de r (E2).
2. **Ligne France du tableau 1 (p. 25)**, 1870-2019 : actions 0,065 ; bons −0,008 ; obligations d'État 0,008 ; PIB par tête 0,018 ; population 0,004. En additionnant les deux derniers, comme le texte l'indique pour les niveaux, la croissance du PIB serait d'environ 2,2 % l'an, au-dessus du rendement réel réalisé des obligations (0,8 %) et des bons (−0,8 %). Ce calcul est du lecteur ; Barro ne commente pas la France.
3. **Théorique** : dans le modèle, r > g tient pour le rendement espéré du capital. Avec le taux sans risque, r ≤ g reste possible **sans** signaler d'inefficacité dynamique, pourvu que le financement de Ponzi soit exclu pour les agents privés et pour l'État (E5, E6, E8).
4. **Dette publique** : le Ponzi public étant exclu, la valeur actuelle des impôts nets, actualisée au taux sûr, égale le stock de dette ; l'État ne choisit que le **calendrier** des impôts (E7). Le modèle vérifie l'équivalence ricardienne : la dette ne change ni la richesse nette de l'agent représentatif, ni les taux, l'investissement ou la croissance (E10). L'auteur note aussi qu'un titre public ne peut pas être entièrement sûr : le gage de l'État se limite à sa capacité fiscale (E12).
5. L'auteur présente son cadre comme une base pour des modèles hétérogènes, non comme un aboutissement (E14).

## Ce que le texte ne dit pas

- Il ne mesure **pas le coût de la dette pour l'État** : ses r sont des rendements réalisés pour le détenteur (plus-values comprises), déflatés par les prix à la consommation (E9), et non le taux apparent de la charge d'intérêts. Assimiler « rendement réel des obligations » à « coût moyen du stock » serait un glissement de variable.
- Il ne dit **pas** que la France a connu r < g à cause de l'inflation : le texte ne commente aucun pays et ne décompose pas les rendements négatifs des bons français. Toute lecture en ce sens est une inférence, à ne pas lui attribuer.
- Il ne dit **pas** qu'un État peut s'endetter sans jamais relever l'impôt quand r < g : son modèle **exclut** ce cas par hypothèse (E6, E8). Le texte ne prouve pas l'impossibilité empirique d'un tel roulement ; il montre qu'un équilibre avec r ≤ g n'en a pas besoin.
- Rien sur la maturité, le refinancement ou la transmission des taux : la structure par terme est plate dans le modèle (E15) et les titres sûrs sont en offre nette nulle (E16).
- Rien sur l'inflation, les titres indexés ou 2022.
- L'équivalence ricardienne n'est pas testée empiriquement : c'est une propriété du modèle (E10), construite sur des liens d'altruisme entre générations (E17).

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| C1 | sans rapport | Modèle à taux sans risque constant et structure par terme plate (E15) ; aucune dynamique de refinancement. |
| C2 | sans rapport | Ni facture annuelle ni court terme ; le texte raisonne en valeur actuelle sur horizon infini (E7). |
| C3 | nuance (première phrase) / appuie (seconde) | **Première phrase** : Barro montre que le signe de r − g dépend entièrement de la définition de r (E2, E3). Le « r » qui gouverne la dynamique du ratio est le taux payé par l'État sur son stock ; les rendements du tableau 1 sont des rendements réalisés pour le détenteur (E9), variable différente. Dans son cadre, même avec r sûr < g, l'État doit couvrir sa dette par des excédents primaires futurs en valeur actuelle (E7). « Le ratio baisse sans le moindre effort budgétaire » n'y a donc pas de sens hors d'un solde primaire nul. Pour la France, 1870-2019, le rendement réel réalisé des obligations (0,8 %) est resté sous la croissance (environ 2,2 %) : c'est un témoin sur série longue, de même sens que la page, mais pour une autre variable. **Seconde phrase** (« ce chiffre seul ne tranche pas ») : appuyée, car un r sûr < g « does not signal dynamic inefficiency » dans son modèle (E5, E8). |
| Q3 | appuie (dans le modèle) | La page écrit : « dans la même succession passent la charge et la créance ». Chez Barro, la dette ne modifie pas la richesse nette parce que les agents actuels sont reliés à leurs descendants (E17, E10) et que la valeur actuelle des impôts égale la dette (E7). L'appui n'est que théorique, sous hypothèse d'altruisme intergénérationnel et d'agent représentatif (E14) ; Blanchard juge l'inverse, tout aussi hypothétique. Il ne dit rien de l'usage de la dette, qui est la condition de la page. |
| I2 | sans rapport (mécanisme voisin) | Le texte admet qu'une dette souveraine ne peut pas être entièrement sûre, faute d'un gage supérieur à la capacité fiscale (E12) ; il ne traite ni l'euro, ni la banque centrale, ni le risque de change. |

## Extraits exacts

E1. p. PDF 1 : « NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors »
E2. p. PDF 3 : « Whether r>g applies empirically depends mainly on how one defines r. »
E3. p. PDF 3 : « the condition holds if r is gauged by the average of the realized real rate of return on equity and does not hold if r equals the average of the realized real rate of return on short-term government bills. »
E4. p. PDF 5 : « In contrast, real rates of return on bonds were close to the growth rates of GDP and consumer expenditure. »
E5. p. PDF 15 : « In any event, the model does not require the r>g condition to hold when the r refers to the risk-free rate. »
E6. p. PDF 20 : « This result rules out Ponzi borrowing by the government, and equation (23) becomes, when expressed over an infinite horizon »
E7. p. PDF 20 : « Equation (24) says that the government can choose the timing of tax collections (and, therefore, budget deficits), but the present value of net taxes is pinned down to equal the starting amount of »
E8. p. PDF 23 : « As long as Ponzi-type finance for private agents and the government are precluded, the equilibrium can feature a risk-free rate, rf, below the expected growth rate, E(g), and possibly close to zero. »
E9. p. PDF 26 : « Rates of return are calculated arithmetically from nominal total returns divided by consumer price indexes. »
E10. p. PDF 21 : « It follows that the model satisfies Ricardian Equivalence—the equilibrium with respect to real rates of return, investment, and economic growth is invariant with choices related to public debt. »
E11. p. PDF 4 : « Results are similar if samples start in 1960, rather than 1870. »
E12. p. PDF 20 : « government bonds cannot be entirely safe because the government’s collateral is limited to the present value of its taxing capacity. »
E13. p. PDF 19 : « This assumption of equal interest rates is not far from reality for the United States if one identifies private bonds with prime corporate obligations. »
E14. p. PDF 23 : « The present results for a representative-agent economy provide a baseline setting for models with heterogeneity. »
E15. p. PDF 13 : « Since the model has i.i.d. shocks, the term structure of risk-free rates is flat »
E16. p. PDF 13 : « The aggregate of risk-free assets always equals zero; that is, these assets are in zero net supply. »
E17. p. PDF 4 : « This result emerges from a specification in which individuals currently alive are connected as parents to members of future generations; for example, through altruistic linkages. »
