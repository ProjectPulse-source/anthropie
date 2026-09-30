# Luca Agnello et Ricardo M. Sousa — How Does Fiscal Consolidation Impact on Income Inequality?

- **Référence publiée** : Agnello, L. et Sousa, R. M., « How Does Fiscal Consolidation Impact on Income Inequality? », *Review of Income and Wealth*, 60(4), décembre 2014, p. 702-726 (en ligne le 17/12/2012), DOI 10.1111/roiw.12004.
- **Version lue** : Banque de France, Document de travail n° 382, mai 2012 (manuscrit antérieur à la publication ; la version publiée n'a pas été lue et peut différer) — fichier `agnellosousa_bdf.txt` (texte extrait du PDF), SHA-256 du PDF `0cc0884672c76bc1a3eb84ae649487aa7c677cd2096ff49be65ad41eba2bb898`, 32 pages PDF, https://publications.banque-france.fr/sites/default/files/medias/documents/working-paper_382_2012.pdf
- **Lecture intégrale** : 30/09/2026, pages PDF 1 à 32 (texte, références, tableaux 1 à 6, figures 1 à 3, liste de la collection) ; dernière page lue : « For a complete list of Working Papers published by the Banque de France, please visit the website »
- **Qui parle, et d'où** : Luca Agnello, économiste au service d'étude des politiques de finances publiques (FIPU) de la Banque de France et à l'université de Palerme ; Ricardo M. Sousa, LSE (Financial Markets Group) et université du Minho. Document de travail d'une banque centrale de l'Eurosystème, non évalué dans cette version, avec l'avertissement d'usage : les opinions n'engagent pas l'institution (E13). Aucun financement particulier n'est déclaré. La position institutionnelle aurait pu incliner vers la thèse, alors dominante et citée par les auteurs (Alesina et Ardagna), que la consolidation par la dépense est la plus efficace ; le résultat va dans l'autre sens pour la répartition, et les auteurs présentent explicitement l'arbitrage (efficacité contre inégalité, p. PDF 14). Leur ambition déclarée est descriptive, non normative (E11).

## Population, période, variables, méthode

- **Population** : panel de 18 pays industrialisés (Australie, Autriche, Belgique, Canada, Danemark, Finlande, **France**, Allemagne, Grèce, Irlande, Italie, Japon, Pays-Bas, Portugal, Espagne, Suède, Royaume-Uni, États-Unis), données annuelles, 1978-2009, 518 observations (E1).
- **Variable expliquée** : indice de Gini du revenu **net** (après impôts directs et cotisations sociales) et du revenu brut, base SWIID. Aucune mesure par décile ou par quintile.
- **Variable d'intérêt** : épisodes de consolidation identifiés par l'approche narrative de Devries et al. (FMI, 2011) — mesures discrétionnaires explicitement motivées par la réduction du déficit (E10) ; indicatrices « consolidation », « deux années suivantes », « menée par la dépense », « menée par les recettes » ; puis taille des mesures en % du PIB, seuils (1 % du PIB au total, 0,57 % pour l'impôt, 0,77 % pour la dépense), croisement avec inflation, croissance et crises bancaires.
- **Contrôles** : log du PIB par habitant et son carré (courbe de Kuznets), ouverture commerciale. Aucun autre déterminant politique ou institutionnel (note 2, E10).
- **Méthode** : système de régressions apparemment indépendantes (SUR) sur panel, effets individuels aléatoires supposés non corrélés aux régresseurs. **Par construction**, les indicatrices de consolidation n'entrent que dans l'équation du Gini net ; leurs coefficients sont contraints à zéro dans l'équation du Gini brut (E4, E5). Robustesse : restriction aux épisodes avec amélioration du solde primaire structurel d'au moins 1,5 % du PIB (tableau 5).

## Résultat

- Les périodes de consolidation vont avec une hausse significative du Gini net (coefficient 0,026, significatif à 1 %, tableau 1) (E1).
- **Composition** : consolidation menée par la dépense, coefficient positif et significatif (0,035) ; menée par l'impôt, coefficient négatif (-0,004) **mais non significatif** dans la spécification de base (E3). Le signe égalisateur de l'impôt devient significatif dans les spécifications en taille (-0,010, significatif à 10 %) et, nettement, sur le sous-échantillon des grandes consolidations (-0,0448, tableau 5) (E2, E8).
- **Canal avancé par les auteurs**, non testé : baisse des salaires publics et hausse du chômage, notamment de longue durée, par la baisse de la consommation et de l'investissement publics (E6).
- **Taille** : les plans inférieurs à 1 % du PIB ont un effet plus défavorable sur le Gini que les plus grands (0,034 contre 0,018 ; test d'égalité rejeté seulement à 10 %, p = 0,06) (E7). Dans le détail, seuls les relèvements d'impôt **supérieurs à 0,57 % du PIB** ont un effet égalisateur significatif (-0,012) ; en dessous, le coefficient est **positif et non significatif** (0,022, tableau 4, colonne 4, p. PDF 26). Symétriquement, seules les coupes supérieures à 0,77 % du PIB creusent significativement l'écart (0,029) ; en dessous, 0,008, non significatif (E8).
- L'effet disparaît deux ans après le programme (E12). L'inflation et une croissance inférieure à 2 % l'amplifient (E14) ; il est non significatif pendant une crise bancaire et amplifié après.
- Degré de certitude : les auteurs écrivent « seems », « suggests », « likely » pour les résultats de composition et de taille, et se présentent comme une description (E11).

## Ce que le texte ne dit pas

- **Il ne dit pas qui supporte l'effort par décile.** Une hausse du Gini est compatible avec plusieurs répartitions ; la phrase « the burden … affects disproportionately households at the bottom » est une inférence des auteurs à partir du Gini, pas une mesure par groupe de revenu.
- **Il ne mesure pas l'effet d'une coupe dans l'enseignement.** Le Gini du revenu disponible monétaire n'inclut pas la valeur des services publics en nature ; le canal que les auteurs invoquent passe par les salaires publics et le chômage (E6), pas par la perte d'un service. La page dit elle-même qu'« un service public valorisé n'est pas un revenu monétaire ». On ne peut donc pas écrire que l'article « confirme » la courbe « enseignement » de la page.
- **Il ne distingue pas les impôts** (directs, indirects, sur le patrimoine) à l'intérieur des consolidations « menées par les recettes » ; l'effet égalisateur est attribué à la progressivité par hypothèse. La page, elle, répartit une hausse des impôts sur les revenus et le patrimoine.
- **Il ne porte pas sur la France seule** : la France est l'un des 18 pays, sans estimation propre. Période 1978-2009, antérieure aux consolidations de 2010-2019.
- **Il n'établit pas un effet causal au sens strict** : l'identification narrative élimine la réponse endogène de la politique budgétaire au cycle (argument des auteurs, p. PDF 11), mais le modèle ne contient que trois contrôles et suppose les effets pays non corrélés aux régresseurs ; la contrainte « aucun effet sur le Gini brut » est imposée, non testée.
- **Il ne dit rien de la mobilité des contribuables** (Q4) ni des générations (Q3).
- Coquille dans la version lue : « Ball et al. (2001) » p. PDF 14 renvoie à Ball et al. (2011) de la bibliographie.

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| Q1 (sens de l'écart dépense/impôt) | appuie | Même contraste de signe que la page — coupe de dépense défavorable aux plus modestes, hausse d'impôt égalisatrice — mais sur des consolidations réelles de 18 pays, 1978-2009, mesurées par le Gini du revenu net, et non sur un profil comptable français 2023 par dixième. C'est un appui **indépendant** (effets observés, comportements inclus), pas une reproduction de la mesure (E1, E2, E6). |
| Q1 (portée : taille et instrument) | nuance | (a) Effort de la page : 10 Md€, soit de l'ordre de 0,35 % du PIB français (calcul du lecteur, PIB 2023 d'environ 2 800 Md€) — dans la classe des petits relèvements d'impôt, où l'article **ne trouve pas** d'effet égalisateur significatif (coefficient positif, non significatif) ; l'égalisation n'apparaît qu'au-dessus de 0,57 % du PIB (E8, E3). (b) La coupe « enseignement » de la page n'est pas captée par un Gini monétaire ; le canal de l'article est l'emploi et les salaires publics (E5, E6). (c) Effet transitoire, disparu à deux ans (E12). La lecture comptable de la page n'est pas contredite, mais l'article ne peut être cité comme confirmation que pour la direction de l'écart, pas pour son ampleur à cette taille ni pour l'instrument « enseignement ». |
| Q2 | sans rapport | L'article associe inflation et hausse du Gini net, sans distinguer inflation anticipée et non anticipée ni créanciers nominaux (E14). |

## Extraits exacts

E1. p. PDF 4 : « Using a panel of 18 industrialized countries from 1978 to 2009, we find that income inequality significantly rises during periods of fiscal consolidation. »
E2. p. PDF 4 : « while fiscal policy that is driven by spending cuts seems to be detrimental for income distribution, tax hikes seem to have an equalizing effect. »
E3. p. PDF 13 : « Moreover, the evidence suggests that fiscal adjustments that are driven by the revenue side help reducing the income gap, although the effect is not statistically significant. »
E4. p. PDF 13 : « We remark that all abovementioned dummy variables enter only the net income inequality equation. »
E5. p. PDF 13 : « one can only infer about the effects of fiscal consolidation on income inequality after deducting direct taxes and social security contributions from gross income »
E6. p. PDF 14 : « This can be explained by the fact that fiscal austerity plans typically call for a fall in public sector wages or lead to an increase in unemployment »
E7. p. PDF 17 : « consolidation plans that amount to less than 1% of GDP have a more detrimental impact on income inequality than austerity measures that are bigger in size »
E8. p. PDF 17 : « tax rises above 0.57% of GDP contribute to a large fall in inequality. From a policy perspective, the last result suggests that properly designed tax-based consolidation plans could be an effective tool »
E9. p. PDF 14 : « As a result, although spending cuts can be more effective (than tax increases) at promoting a stabilization of the debt and boosting economic growth in the medium-term »
E10. p. PDF 11 : « We remark that the current paper looks at consolidation measures that are explicitly motivated by the deficit reduction. »
E11. p. PDF 10 : « Rather than judging about the merits of such policies, our paper tries to provide a comprehensive description of the effects of fiscal consolidation on income inequality. »
E12. p. PDF 14 : « We also find that the effects of fiscal consolidation on income inequality tend to disappear two years after the implementation of the program. »
E13. p. PDF 2 : « Working Papers reflect the opinions of the authors and do not necessarily express the views of the Banque de France. »
E14. p. PDF 15 : « In line with Albanesi (2007), our results show that there is a strongly positive relationship between inflation and income inequality. »
