# Laubach — New Evidence on the Interest Rate Effects of Budget Deficits and Debt

- **Référence publiée** : Thomas Laubach, « New Evidence on the Interest Rate Effects of Budget Deficits and Debt », *Journal of the European Economic Association*, 7(4), 2009, p. 858-885, DOI 10.1162/JEEA.2009.7.4.858 (version publiée **non lue**). Indice d'écart entre les versions : Gruber et Kamin (2010) attribuent à « Laubach (2009) » un effet de 3 à 4 pb par point de dette, quand la version lue annonce 4 à 5 pb ; les chiffres publiés sont à relire avant toute citation.
- **Version lue** : Finance and Economics Discussion Series 2003-12, Federal Reserve Board, mai 2003 ; fichier `laubach_feds.txt` (extrait de `200312pap.pdf`), SHA-256 69d07187752827b7d098c8dcbb41be49b06b0f16ec7ead32da93728ab547bff6, 21 pages PDF, https://www.federalreserve.gov/pubs/feds/2003/200312/200312pap.pdf
- **Lecture intégrale** : 30/09/2026, pages PDF 1 à 21 ; dernière page lue : « Figure 4: Projected GDP Growth and Equity Premium ». **Complétude** : le document de 2003 paraît complet — pagination continue de 1 à 20 après la page de titre, sections 1 à 5, références [1] à [18], annexe A, tableaux 1 à 5 et figures 1 à 4, tous appelés dans le texte et présents. Il est court parce que c'est la version de travail de 2003, non la version publiée de 2009, plus longue (28 pages de revue).
- **Qui parle, et d'où** : économiste du Conseil des gouverneurs de la Réserve fédérale, remerciant des collègues de la Fed ; opinions données pour les siennes, non celles de la Fed. Document de travail, non évalué à cette date ; publié six ans plus tard. Aucun financement extérieur mentionné. Ce que la position peut faire au propos : écrit en 2003, pendant le retour des déficits fédéraux américains, par un économiste de la banque centrale dont la politique monétaire est justement ce qu'il faut séparer de l'effet budgétaire ; le texte cite lui-même le rapport du Council of Economic Advisers de 2003, qui défendait un argument voisin. Cela oriente la question (quel effet des déficits sur les taux américains ?) sans être un argument contre la méthode.

## Population, période, variables, méthode

- **Population** : **un seul pays, les États-Unis** ; État fédéral (dette fédérale détenue par le public). Aucune comparaison entre pays.
- **Période** : projections du CBO de 1976 à janvier 2003 (annuelles jusqu'en 1984, semestrielles ensuite ; échantillon annuel de 28 observations), projections de l'OMB depuis 1983 (21 observations) (E10).
- **Variable expliquée** : **taux anticipé** — le rendement du Treasury à dix ans **attendu dans cinq ans**, tiré des taux à terme de la courbe zéro-coupon (moyenne des taux à terme à un an de 5 à 14 ans), réel ou nominal (E2, E9) ; en variantes, le taux à cinq ans dans cinq ans et le **taux à dix ans courant**. Ce n'est ni un taux implicite, ni un écart entre pays.
- **Variables budgétaires** : **projections à cinq ans** du CBO et de l'OMB du déficit/PIB, de la dette/PIB (détenue par le public), du déficit primaire, des dépenses totales (E3). Contrôles : croissance tendancielle projetée par le CBO, prime de risque sur actions, inflation anticipée (enquêtes).
- **Méthode** : régressions de série temporelle en forme réduite, écarts-types de Newey-West ; l'auteur signale que les tests de racine unitaire ne rejettent pas la non-stationnarité (E7) et que l'endogénéité n'est jamais complètement levée (E5, E8).

## Résultat

- **+1 point de déficit/PIB projeté → +20 à 40 pb sur le taux à dix ans anticipé dans cinq ans, estimation typique 25 pb ; +1 point de dette/PIB projetée → +4 à 5 pb**, statistiquement significatifs (E1, E6). Tableau 1 (réel) : 0,052-0,053 point par point de dette ; tableau 2 (nominal, inflation anticipée en contrôle) : 0,036 (CBO) et 0,046 (OMB). Illustration de l'auteur : la révision des projections du CBO entre janvier 2001 et janvier 2003 (dette projetée de 9,5 % à 28,5 % du PIB) aurait ajouté environ 99 pb au taux réel anticipé, 75 pb en nominal, toutes choses égales.
- **Sur le taux à dix ans courant, l'effet disparaît** : tableau 4, coefficient de la dette 0,007 (t = 0,45), du déficit 0,09 (t = 1,40), non significatifs ; l'auteur en conclut qu'il faut écarter la composante cyclique de la partie courte de la courbe pour identifier l'effet (E4).
- Le rapport d'environ 7 entre coefficient du déficit et coefficient de la dette est jugé cohérent avec des déficits persistants mais non permanents.
- Le modèle de croissance néoclassique, avec des hypothèses posées par l'auteur (part du capital 1/3, capital/production 2,5, éviction de 60 %), prédit environ 2,1 pb par point de dette, « half » de l'effet réel estimé, proche de l'effet nominal.
- Degrés de certitude posés par l'auteur : forme réduite, endogénéité « unlikely » à être entièrement levée (E5) ; t de Student à lire avec prudence (E7) ; lecture sceptique possible (E8).

## Ce que le texte ne dit pas

- Rien sur une **coupe entre pays**, ni sur l'Europe, ni sur la zone euro, ni sur un risque de défaut : c'est une série temporelle américaine, et l'effet passe par l'éviction du capital dans le cadre théorique proposé.
- Rien sur le **taux implicite** (coût moyen du stock) : l'effet est mesuré sur un taux **anticipé à horizon de cinq ans**, et il **n'est pas significatif sur le taux à dix ans courant** (E4). A fortiori, un coût moyen du stock, qui mêle des émissions anciennes, n'est pas l'objet du texte.
- Il ne dit pas que la dette **actuelle** fait monter les taux : ses variables sont des **projections** à cinq ans ; que les marchés aient ces projections pour anticipations est une hypothèse, non testable directement selon l'auteur.
- Il ne dit rien de l'**écart taux-croissance** comme moteur de la dynamique du ratio, ni d'un **seuil** : ses spécifications sont linéaires.
- Les chiffres publiés en 2009 peuvent différer (voir l'indice ci-dessus) ; la fiche ne vaut que pour la version de 2003.

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| I1 (« sur une année et entre pays, le niveau ne permet pas de prédire son prix ») | sans rapport | Aucune coupe entre pays : un seul pays (États-Unis), série 1976-2003. Le texte ne peut ni appuyer ni contredire une coupe UE 2025 sur le taux implicite. E3, E10 |
| I1 (« ce qui ne veut pas dire qu'il n'a jamais d'effet » ; « le prix ne découle pas de son niveau ») | nuance | Dans le temps, pour les États-Unis, la dette **projetée** élève le taux **anticipé** d'environ 4 pb par point (E1, E6) : la clause de la page est appuyée ; sa seconde phrase, lue sans borne, est nuancée. Mais le même texte ne trouve **aucun effet significatif sur le taux à dix ans courant** (E4) — variable plus proche du prix payé que le taux anticipé —, ce qui limite la portée du contre-exemple pour un taux implicite. E1, E4, E6 |
| C3 (« l'écart taux-croissance gouverne la dynamique du ratio ; aucun seuil ne tranche ») | nuance | Le texte ne traite pas de la dynamique du ratio. Il indique seulement que le taux lui-même dépend un peu de la dette projetée (≈ 4 pb par point, E6) et, dans le cadre théorique, de la croissance tendancielle (E11) : l'écart n'est donc pas entièrement indépendant de la dette, mais l'ordre de grandeur est faible, et aucun seuil n'est testé (spécifications linéaires). Sur « aucun seuil » : sans rapport. E6, E11 |

## Extraits exacts

E1. p. PDF 3 : « Similarly, a percentage point increase in the projected debt-to-GDP ratio raises future interest rates by about 4 to 5 basis points, and these estimates are statistically signiﬁcant, too. »
E2. p. PDF 3 : « the analysis focuses on expectations of future nominal interest rates derived from forward rates 5 to 14 years ahead embedded in the term structure of interest rates. »
E3. p. PDF 2 : « Expectations of future ﬁscal policy are proxied in this paper by projections published by the Congressional Budget Oﬃce (CBO) and the Oﬃce of Management and Budget (OMB) »
E4. p. PDF 10 : « The results using the conventional 10-year Treasury yield show clearly that controlling for the cyclical variation embedded in the short end of the yield curve is important for identifying the eﬀects of ﬁscal variables on interest rates »
E5. p. PDF 2 : « Of course, there are many conceivable factors that jointly determine ﬁscal variables and interest rates, and it is unlikely that a reduced-form regression would ever completely overcome this endogeneity problem »
E6. p. PDF 14 : « All else equal, the results of this study suggest that interest rates rise by about 25 basis points in response to a percentage point increase in the projected deﬁcit-to-GDP ratio, and by about 4 basis points in response to a percentage point increase in the projected debt-to-GDP ratio. »
E7. p. PDF 8 : « caveat in interpreting the t statistics is that augmented Dickey-Fuller tests do not reject the hypothesis of a unit root at the 5 percent level for either the dependent variable or for the regressors. »
E8. p. PDF 12 : « A skeptical view of the evidence presented in the previous section would hold that the identiﬁcation problems involved in these kinds of regressions are too severe to be ever completely overcome. »
E9. p. PDF 1 : « this paper studies the relationship between long-horizon expected government debt and deﬁcits, measured by CBO and OMB projections, and expected future long-term interest rates. »
E10. p. PDF 5 : « From the CBO, ﬁve-year-ahead projections for both the uniﬁed budget deﬁcit and GDP (GNP until 1991) are available at an annual frequency from 1976 to 1984, and at a semiannual frequency from 1985 until the most recent projection in January 2003. »
E11. p. PDF 5 : « an increase in trend growth should raise interest rates, whereas an increase in risk aversion should lower Treasury yields because it raises the demand for safe assets. »
