# Wiji Arulampalam, Michael P. Devereux et Giorgia Maffini — The Direct Incidence of Corporate Income Tax on Wages

- **Référence publiée** : Arulampalam, W., Devereux, M. P. et Maffini, G., « The Direct Incidence of Corporate Income Tax on Wages », *European Economic Review*, 56(6), 2012, p. 1038-1054, DOI 10.1016/j.euroecorev.2012.03.003.
- **Version lue** : manuscrit déposé sur le site de l'auteure (université de Warwick), page de titre « This version: March 2011 / Revised February 2012 » (fichier nommé « march2012 » ; la version publiée n'a pas été lue et peut différer) — fichier `adm2012_warwick.txt` (texte extrait du PDF), SHA-256 du PDF `9e3074f658b3f4071d8ba3e1fbfbcf8a492a58f9b3fbc323923520001ce3f466`, 36 pages PDF, https://warwick.ac.uk/fac/soc/economics/staff/swarulampalam/publications/adm_march2012.pdf
- **Lecture intégrale** : 30/09/2026, pages PDF 1 à 36 (texte, références, tableaux I à VIII, annexes 1 et 2) ; dernière page lue : « Time dummies are included in all of the above. »
- **Qui parle, et d'où** : économètres du travail et fiscalistes rattachés à l'Oxford University Centre for Business Taxation (Saïd Business School) ; W. Arulampalam aussi à Warwick et à l'IZA, M. P. Devereux aussi à l'IFS, CESifo et au CEPR. Manuscrit révisé après évaluation (un rapporteur anonyme est remercié), publié dans une revue à comité de lecture. Préparé pour une conférence de l'European Tax Policy Forum ; financements déclarés : Hundred Group, ETPF, ESRC (E11). Le texte ne décrit pas ces financeurs ; que le Hundred Group réunisse des directeurs financiers de grandes entreprises britanniques relève d'une connaissance extérieure, **non vérifiée ici**. Un résultat « les salariés supportent une part de l'impôt sur les sociétés » sert un plaidoyer pour l'alléger ; cela ne dit rien de sa validité, qui se juge sur la méthode, mais invite à lire exactement ce qui est mesuré — un effet direct, partiel, conditionnel.

## Population, période, variables, méthode

- **Population** : 55 082 entreprises non « micro », comptes sociaux non consolidés (base ORBIS), dans neuf pays européens — Belgique, Finlande, **France**, Allemagne, Italie, Pays-Bas, Espagne, Suède, Royaume-Uni ; données 1996-2003, observations d'estimation 1999-2003 ; 166 749 observations (E1). La France fournit 17 505 entreprises et 54 511 observations, environ un tiers de l'échantillon (tableau I, p. PDF 28).
- **Variable expliquée** : salaire moyen de l'entreprise (charges de personnel / effectif), seule mesure disponible.
- **Variable d'intérêt** : impôt comptabilisé par salarié, **à valeur ajoutée par salarié donnée**. Instruments : taux légal, taux effectifs marginal et moyen, et variables propres à l'entreprise retardées (structure des actifs, endettement, pertes antérieures).
- **Cadre théorique** : négociation salariale efficace (McDonald-Solow) ; l'impôt réduit la quasi-rente partagée entre l'entreprise et ses salariés. L'**incidence directe** est l'effet par ce seul canal, à activité donnée ; l'**incidence indirecte** (par l'investissement, le stock de capital, les prix — celle du modèle classique où le capital mobile fuit et le travail immobile paie) **n'est pas estimée** (E3, E5, E9).
- **Méthode** : panel dynamique, GMM en différences premières avec instruments restreints (colonne 8 du tableau V, puis colonne 3 du tableau VI avec densité syndicale et salaire extérieur).

## Résultat

- **Effet direct** : élasticité de long terme du salaire à l'impôt de -0,093 ; évalué à la moyenne, 1 dollar d'impôt supplémentaire réduit la masse salariale de 64 cents à court terme et de 49 cents à long terme ; environ 50 % de l'impôt passe dans les salaires par ce canal (E1, E4).
- Sensibilité déclarée par les auteurs : calculé sur les seules observations à impôt positif, l'effet de long terme tombe à -0,39 ; calculé observation par observation, la médiane est d'environ -1, soit un report intégral (E12). Le chiffre central dépend donc de la manière d'évaluer.
- Incohérence interne de la version lue : la note 6 annonce que le chiffre de 49 cents repose sur une élasticité de -0,076, alors que le tableau VII l'associe à -0,093 (-0,076 y est l'élasticité des entreprises indépendantes) (E13).
- **Multinationales contre entreprises indépendantes** : report un peu plus élevé pour les multinationales (54 cents contre 43), mais **aucune différence statistiquement significative** ; aucun effet des profits ou de l'impôt du reste du groupe (E6, E7, E8).
- Les estimations pays par pays ne passent pas toutes les tests de spécification : pas de résultat propre à la France (E10).

## Ce que le texte ne dit pas

- **Il ne dit rien de la dette publique, ni d'un ajustement budgétaire, ni de la « ligne de moindre résistance »** : il mesure l'incidence d'un impôt existant, pas le choix politique de l'instrument d'ajustement.
- **Il ne teste pas la mobilité des personnes.** Le salarié y est le facteur moins mobile par hypothèse du cadre classique (E2), mais le canal estimé est la négociation salariale, non la fuite du capital. La seule mesure qui approche une différence de mobilité — l'entreprise multinationale, dotée d'une option de sortie — ne produit **aucune différence significative** (E6, E8).
- **Il ne donne pas l'incidence totale** de l'impôt sur les sociétés (E9) ; les effets indirects « s'ajoutent » éventuellement à l'effet direct, sans être chiffrés (E5).
- Il ne porte ni sur l'impôt sur le revenu ni sur l'impôt sur le patrimoine, les deux prélèvements que répartit la page « Qui paie ».
- Période 1996-2003, avant la crise de 2008 et les consolidations de 2010-2019.

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| Q4 | nuance | Portée **indirecte**. L'article montre, sur des entreprises de neuf pays européens dont un tiers françaises, 1996-2003, qu'une part d'un impôt assis sur une base mobile (le bénéfice) retombe sur un groupe moins mobile, les salariés (E2, E4) : cela rend plausible la prémisse de la page selon laquelle les entreprises « échappent plus facilement à un prélèvement que les salariés ». Mais (a) le mécanisme mesuré est la négociation, non la mobilité ; (b) l'unique contraste de mobilité testé (multinationales / indépendantes) est non significatif (E6, E8) ; (c) aucun ajustement budgétaire n'est étudié. Il ne peut être cité ni comme preuve de Q4, ni comme réfutation. |
| Q1 | nuance | Rappelle que l'incidence légale d'un impôt n'est pas son incidence économique : environ la moitié de l'impôt sur les sociétés, par le seul canal direct, pèse sur les salaires (E4, E12). Le profil de la page attribue l'effort fiscal au prorata de ce que chaque dixième verse déjà — incidence légale, sans comportement, ce que la page dit. L'impôt réparti par la page (revenus et patrimoine) n'est pas celui de l'article : pas de transfert direct du chiffre, mais une raison de ne pas lire la courbe « impôt » comme une incidence finale. |

## Extraits exacts

E1. p. PDF 1 : « Using data on 55,082 companies located in nine European countries over the period 1996–2003, we estimate the long run elasticity of the wage bill with respect to taxation to be -0.093. »
E2. p. PDF 2 : « The standard model with mobile capital and immobile labour implies that, in a small open economy, a source-based tax on capital is wholly passed onto labour »
E3. p. PDF 2 : « We do not attempt to estimate the indirect effect. The key problem with attempting to do so is that any control variables that could be included in estimating a single wage equation »
E4. p. PDF 24 : « Our results suggest that approximately 50 per cent of an exogenous increase in tax is passed on in lower wages in the long run. »
E5. p. PDF 24 : « These estimates are for the direct effect of the tax only, conditional on value added (and hence indirectly conditional on investment); they are additional to possible indirect effects through value added. »
E6. p. PDF 25 : « do not find any significant difference between the two groups. Nor do we find any effect on the wage rate of the profit or tax liability elsewhere in the multinational group. »
E7. p. PDF 23 : « The long-run incidence of an exogenous $1 rise in tax is thus slightly higher for multi-national group of companies, with compensation falling by 54 cents for employees of multinational groups and by 43 cents for stand-alone companies. »
E8. p. PDF 23 : « However, none of these differences between the two groups of companies are statistically significant. »
E9. p. PDF 11 : « We do not derive nor estimate expressions for the total incidence in this paper. »
E10. p. PDF 19 : « Although there are some differences across countries, the specification in column (8) does not pass the specification tests in all cases. »
E11. p. PDF 1 : « Financial support from the Hundred Group, the ETPF and the Economic and Social Research Council (ESRC) »
E12. p. PDF 22 : « The median of the resulting distribution for the incidence of taxation is approximately -1, indicating that, at the median, the entire increase in tax would be passed on in lower wages. »
E13. p. PDF 7 : « Calculations are based on the estimated long run elasticity of -0.076 and are detailed in Section IV.C. »
