# William D. Nordhaus — Baumol's Diseases: A Macroeconomic Perspective

- **Référence publiée** : Nordhaus, W. D. (2008), « Baumol's Diseases: A Macroeconomic Perspective », *The B.E. Journal of Macroeconomics*, 8(1) (référence de la commande). **Ce que dit le texte lu** : c'est le document de travail NBER n° 12218, daté de mai 2006 ; il ne mentionne **aucune** publication en revue. La publication de 2008 et l'identité de son contenu avec cette version ne sont donc **pas vérifiées** par le document lu. Seul indice : l'auteur remercie des « anonymous referees » (p. 1), ce qui situe la version après au moins un tour d'évaluation.
- **Version lue** : `nordhaus_nber.pdf` (texte extrait `nordhaus_nber.txt`), SHA-256 du PDF 14a635e280eb12940c72d99c6652d39706a6439c2522801793a5087f7fe659bc (recalculé, conforme), 58 pages PDF, https://www.nber.org/system/files/working_papers/w12218/w12218.pdf . Les « Accompanying Notes » (dérivations, erreurs, sources), annoncées « at the end of this paper » et sur le site de Yale, **ne figurent pas** dans ce PDF et n'ont pas été lues.
- **Lecture intégrale** : 30/09/2026, pages PDF 1 à 58 (tableaux, figures, annexes A et B compris) ; dernière page lue : « The unweighted statistics weight each equation equally. »
- **Qui parle, et d'où** : William D. Nordhaus, département d'économie de l'université Yale et NBER ; document de travail (non évalué comme tel), avec l'avertissement d'usage que les vues ne sont pas celles du NBER ; aucun financement déclaré. Il teste les hypothèses de William Baumol, qu'il remercie pour ses commentaires et dont il rapporte deux « personal communications » : Baumol y corrige lui-même deux lectures de ses travaux (salaires bas des secteurs stagnants ; « maladie de croissance »). Le texte est donc à la fois un test et un dialogue avec l'auteur testé ; cela invite à distinguer ce que Nordhaus mesure de ce qu'il attribue à Baumol.

## Population, période, variables, méthode

- **Population** : économie des **États-Unis**, comptes par branche du Bureau of Economic Analysis (BEA), 67 branches détaillées (SIC 1987), 14 grandes branches, et un sous-ensemble de **28 branches « bien mesurées »** — agriculture, mines, industrie manufacturière, transports, télécommunications, énergie, commerce. **Aucune branche de santé, d'enseignement ni d'administration** n'est dans les 28 ; les administrations fédérales et locales n'ont pas d'estimation de productivité globale des facteurs (PGF), faute de données de capital.
- **Période** : 1948-2001 ; quatre sous-périodes (1948-59, 1959-73, 1973-89, 1989-2001) ; coupe 1977-2000 jugée de meilleure qualité.
- **Variables** : productivité (PGF en valeur ajoutée, et productivité du travail) ; prix relatifs, production réelle, production nominale, heures et emploi, salaires, profits par branche.
- **Méthode** : régressions en forme réduite de chaque variable sur la croissance de la productivité, 24 spécifications (deux mesures de productivité × trois ensembles de branches × quatre périodes ; panels à effets fixes et coupes longues) ; pour la « maladie de croissance », taux de croissance à parts fixes (FSGR) selon l'année de pondération.

## Résultat

1. **Maladie des coûts et des prix** : « definitely confirmed ». Les branches à productivité plus lente ont des prix relatifs qui montent presque point pour point (coefficient −0,965 pour les branches bien mesurées, non différent de −1) ; la productivité explique environ 85 % de la variance des prix relatifs sur un demi-siècle dans ces branches. Au moins 95 % des gains de productivité passent aux consommateurs par les prix.
2. **Production réelle stagnante** : « strongly confirmed » ; un point de productivité en moins, environ trois quarts de point de production réelle en moins.
3. **Part nominale** : association négative entre productivité et croissance nominale (les branches stagnantes prennent une part croissante), mais **seulement marginalement significative** (coefficients −0,21 à −0,28, t de −1,2 à −1,4).
4. **Emploi et heures** : les branches plus productives perdent des heures (−0,26 point par point), relation inversée dans l'industrie manufacturière ouverte.
5. **Rémunérations** : effet de la productivité propre de la branche sur ses salaires et profits « extremely small » ; salaires et profits suivent l'économie d'ensemble. C'est le ressort de la maladie des coûts : le salaire d'une branche stagnante suit le salaire général.
6. **Maladie de croissance** : le déplacement de la dépense vers les branches stagnantes (« government, education, and construction ») a abaissé la croissance annuelle de la productivité agrégée d'un peu plus d'un demi-point sur 1948-2001 (1,49 % par an aux parts de 1948 contre 0,85 % aux parts de 2001).

## Ce que le texte ne dit pas

- Il ne porte que sur les **États-Unis**, et sur l'économie marchande ; il ne dit rien de la France ni d'aucun budget public.
- Il ne **démontre pas** la maladie des coûts dans la santé, l'enseignement ou l'administration : l'auteur écrit que la mesure y est particulièrement défaillante, la production y étant mesurée par les intrants ; ces branches sont absentes des 28 « bien mesurées » sur lesquelles reposent les conclusions les plus fermes, et les administrations n'ont pas de PGF. Leur forte croissance nominale (santé, services sociaux) est notée avec « serious questions about measurement ».
- Il ne dit pas que les secteurs stagnants absorbent une part croissante de la dépense de façon robuste : ce lien est seulement marginalement significatif.
- Il ne parle ni de dette, ni de charge d'intérêts, ni de tension ressentie par les agents des services publics.
- Baumol lui-même, selon Nordhaus, tient la maladie pour une maladie **des coûts** et non de la croissance, et ne soutient plus que les secteurs stagnants paient forcément des salaires bas : lui faire dire l'une ou l'autre chose serait une double erreur d'attribution.

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| C5 | appuie | Le mécanisme invoqué par la page (des coûts qui suivent les salaires et non les gains de productivité propres) est confirmé comme régularité de long terme : prix relatifs point pour point, salaires de branche fixés par l'économie d'ensemble. Mais population américaine, 1948-2001, branches marchandes. E1, E2, E6 |
| C5 | nuance | La preuve la plus ferme porte sur 28 branches bien mesurées qui ne comptent ni santé, ni enseignement, ni administration ; pour ces services, la production est mesurée par les intrants et la productivité n'est pas observée. La page a raison de dire « plausible, mais […] non démontrée » : ce texte ne la démontre pas non plus pour les services publics, a fortiori en France. E4, E5, E8 |
| C4 | nuance | Inférence de notre part, que le texte ne formule pas pour les budgets publics : si les coûts des services stagnants montent plus vite que les prix moyens, un budget de santé ou d'enseignement qui ne baisse pas en valeur (ou en part du PIB) peut couvrir un volume de service stable ou en recul ; « la dette n'a pas fait baisser ces budgets » ne vaut donc pas absence de contrainte en volume. Le lien entre stagnation et part nominale croissante n'est lui-même que marginalement significatif aux États-Unis. E3, E4 |

## Extraits exacts

E1. p. PDF 2 : « It finds that technologically stagnant sectors clearly have rising relative prices and declining relative real outputs. »
E2. p. PDF 19 : « They indicate that the major determinant of long-term relative price trends is relative productivity trends. »
E3. p. PDF 25 : « stagnant industries tend to take a rising share of nominal output; however, the relationship is only marginally statistically significant. »
E4. p. PDF 25 : « With the exception of air, these had low measured TFP growth, although there are serious questions about measurement in most cases. »
E5. p. PDF 37 : « This shortcoming is particularly serious in services such as health, education, and personal services, for which the output measures are in reality measures of inputs. »
E6. p. PDF 39 : « For the most part, industrial wage and profit trends are determined by the aggregate economy and not by the productivity experience of individual sectors. »
E7. p. PDF 39 : « The growth disease has lowered annual aggregate productivity growth by slightly more than one-half percentage point over the last half century. »
E8. p. PDF 53 : « (Asterisks denote industries that do not have total factor productivity estimates because BEA does not publish capital stock data.) »
E9. p. PDF 13 : « The data used here are a complete set of industry accounts for the period 1948-2001. »
E10. p. PDF 32 : « he views the disease as a cost disease, not a growth disease (personal communication, October 28, 2004). »
