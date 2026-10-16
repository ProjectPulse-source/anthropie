# Philipp Heimberger — Public debt and r-g risks in advanced economies: Eurozone versus stand-alone

- **Référence publiée** : Heimberger, P., « Public debt and r-g risks in advanced economies: Eurozone versus stand-alone », *Journal of International Money and Finance*, vol. 136, article 102877, septembre 2023, https://doi.org/10.1016/j.jimonfin.2023.102877. Auteur unique (Crossref, page de l'éditeur), licence CC BY 4.0, accès libre. Évalué par les pairs (« two anonymous reviewers », remerciements).
- **Version lue** : texte de l'article publié rendu par le navigateur sur la page de l'éditeur (16/10/2026), fichier `heimberger2023_jimf_article.txt` : texte de l'élément `article`, copié depuis la page ; longueur (78 015 caractères) et empreinte polynomiale calculées dans la page et sur le fichier, identiques ; marqueur « page PDF 1 » ajouté en tête pour le contrôle des extraits (aucune pagination dans l'original). SHA-256 du fichier `922450449cdc33908244a8fd18b424e633d951ec3f4021510ff8f8f375d8c1ef`. Annexe en ligne (« Supplementary data 1 ») : `heimberger2023_annexe.pdf`, 19 p., SHA-256 `a630158aa062f7b453fa081275bb8e5b7c183b25dd86302c3545d77f33846b3d`, téléchargée par script sur le serveur de l'éditeur. Canaux : PDF de l'article refusé aux scripts (403), page de l'éditeur derrière un défi anti-robot non contourné, puis ouverte dans le navigateur de l'auteur ; le PDF s'ouvre dans la visionneuse sans pouvoir être enregistré par l'outil, d'où le texte HTML. Les figures sont des images : seuls leurs titres et notes ont été lus.
- **Lecture intégrale** : 16/10/2026, faits saillants, résumé, sections 1 à 7, déclarations, remerciements, notes 1 à 15 ; annexe : tableaux A1 à A10 et titres des figures A1 à A7. Dernière ligne lue : « © 2023 The Author(s). Published by Elsevier Ltd. »
- **Qui parle, et d'où** : un économiste de l'Institut viennois d'études économiques internationales (wiiw ; affiliation de notoriété, page de l'institut, absente du texte rendu), financé par la Banque nationale d'Autriche (subvention 18699, E10). Son hypothèse vient de la théorie de la fragilité de la zone euro de De Grauwe (E3), qu'il remercie avec Yuemei Ji ; ses travaux antérieurs attribuent la rechute de 2012 à la consolidation budgétaire (Heimberger 2017, cité). **Ce que cette position peut incliner** : vers l'idée que l'architecture de l'euro, non le niveau de dette, porte le risque, et vers le filet de sécurité de la BCE et l'intégration budgétaire qu'il recommande (E9). À l'inverse, il écrit que la mécanique de la dette amplifie le risque quand elle est élevée (E8) et recommande de réduire la dette de la périphérie (E9) ; il dit sa propre limite : aucune analyse des mécanismes (E11).

## Population, période, variables, méthode

- **Population et période** : 22 pays de l'OCDE, 11 de la zone euro (cœur : Autriche, Belgique, Finlande, **France**, Allemagne, Pays-Bas ; périphérie : Grèce, Italie, Irlande, Portugal, Espagne) et 11 « autonomes » qui émettent dans leur propre monnaie ; 1970-2018 (E4).
- **Variables** : r = rendement moyen des obligations publiques à 10 ans (OCDE), **non le taux implicite** (E5) ; g = taux de croissance annuel du PIB « at current Dollars » (annexe, tableau A1, p. PDF 11). **Contrôlé sur les données de réplication de l'auteur** (`rg-dynamics-JIMF-final.csv`, dépôt GitHub cité dans l'article, lu le 16/10/2026) : pour la France, 5,22 % en 2016 et 4,07 % en 2017, contre 1,38 % et 2,68 % en euros courants (Eurostat, `nama_10_gdp`, CP_MEUR) ; le niveau 2016 (2 864 106) vaut 1,28 fois le PIB en millions d'euros, ce qui correspond à des dollars à parité de pouvoir d'achat (déduction, non écrite par l'auteur). L'écart r − g de l'article mêle donc un taux en euros et une croissance en dollars. Dette brute en % du PIB (base mondiale de la dette du FMI) ; contrôles : taux réel de long terme retardé, inflation, croissance démographique, solde primaire, ouverture financière (Chinn-Ito), « sûreté » des titres (corrélation passée avec le rendement allemand), indicatrices d'appartenance à l'euro avant 2007, de crise de l'euro 2008-2012.
- **Méthode** : régressions à effets fixes pays de r − g sur la dette de l'année précédente (E6) ; régressions de quantiles de l'écart moyen des trois années suivantes (cinq en robustesse) ; probit de la probabilité d'un écart positif à trois ans. Robustesse : sans l'Allemagne et les États-Unis, moyennes de trois ans, autre référence de sûreté, variable instrumentale (dette moyenne des autres pays), GMM système (note 13).

## Résultat

- **Estimé (a), panel** : coefficient de la dette retardée de signe « faux » et non significatif dans l'ensemble (−0,004, e.-t. 0,014) ; négatif dans tous les sous-échantillons, significatif chez les pays autonomes (−0,016) (E6, tableau 2) ; même conclusion avec instrument et GMM (E7). Le solde primaire prédit l'écart (−0,35 point par point de PIB).
- **Estimé (b), quantiles** : courbes des 10e, 50e et 90e centiles de l'écart futur « essentiellement plates » en fonction de la dette, contrairement à Lian et al. (E2).
- **Estimé (c), durée** : la durée des épisodes d'écart négatif ne dépend pas de la dette initiale (annexe, tableau A3 : −0,00593, e.-t. 0,00746 ; effets fixes pays et années).
- **Estimé (d), zone euro** : la crise de l'euro va avec un écart plus élevé dans la seule périphérie, d'autant moins que les titres passaient auparavant pour sûrs (interaction sûreté × crise : −15,38 sur l'ensemble, négative et significative dans la périphérie seulement) (E1).
- **Estimé (e), probit** : aux valeurs moyennes de 2009-2018, probabilité d'un écart positif à trois ans proche de 85 % pour la Grèce, au-dessus de 40 % pour le Portugal ; de 9,2 % (Finlande) à 15,9 % (Belgique) pour le cœur de la zone euro hors Allemagne (8,3 %) — la valeur française n'est pas donnée dans le texte.
- **Interprétation de l'auteur** : la dette « n'est pas un bon prédicteur » de l'écart ; l'architecture institutionnelle de la zone euro compte (E1, E9).

## Ce que le texte ne dit pas

- **Rien sur la France isolée** : elle est dans le cœur de la zone euro, sans résultat propre hormis la figure 4 (image).
- **Rien sur le taux implicite** : r est un taux de marché à 10 ans (E5), et g n'est pas exprimé en euros (tableau A1).
- **Pas d'effet de la dette « à taux donné » seulement** : le coefficient est estimé à taux réel retardé et inflation donnés ; une hausse de l'écart qui passerait par les taux est en partie absorbée par ces contrôles (déduction de la spécification, non discutée par l'auteur).
- **Pas de causalité** : l'auteur ne propose aucun mécanisme testé (E11).

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| B2 | nuance | Le solde stabilisant de la page est calculé à écart donné ; ici, l'écart futur ne dépend pas du niveau de dette, ce qui contredit Lian et al. et la BCE sur cette relation, non sur l'identité comptable, que l'article rappelle (E8). Taux à 10 ans, croissance en dollars, 22 pays 1970-2018. |
| B4 | nuance | La durée d'un écart négatif ne dépend pas ici de la dette initiale (tableau A3), contre Lian et al. ; le risque d'écart positif se concentre dans la périphérie de l'euro et tient à la sûreté perçue des titres (E1). |

## Extraits exacts

E1. p. PDF 1 : « Applying regression methods to data on 22 OECD countries over 1970–2018 shows that higher public debt levels are not predictive of more unfavourable r-g in both Eurozone and stand-alone countries, where the latter issue debt in their own currency. »
E2. p. PDF 1 : « The lines for the three quantiles are all essentially flat, implying no relation between contemporaneous public debt levels and predicted future r-g. »
E3. p. PDF 1 : « The motivation for this distinction is rooted in the Eurozone fragility theory put forward by De Grauwe (2012) »
E4. p. PDF 1 : « We construct a panel data set for 22 OECD countries – 11 Eurozone, 11 stand-alone – over the time period 1970–2018 »
E5. p. PDF 1 : « We use data on average market interest rates for government bonds maturing in 10 years »
E6. p. PDF 1 : « We can see that the coefficient for the lagged public-debt-to-GDP ratio has the “wrong” sign (although it is very small and statistically insignificant); this rejects the hypothesis that higher public debt levels predict more unfavourable r-g differentials. »
E7. p. PDF 1 : « importantly, higher public debt levels are still not a good predictor of more unfavourable r-g differentials when we use our instrumental variable approach. »
E8. p. PDF 1 : « the mechanics of public debt accumulation make it unavoidable that risks for fiscal policy-makers related to a deterioration of r-g are magnified at higher debt levels. »
E9. p. PDF 1 : « It might be possible to reduce the r-g risks by ensuring that the ECB is always in a position to credibly backstop government bond markets »
E10. p. PDF 1 : « Supported by funds from the Austrian central bank (OeNB) under grant number 18699. »
E11. p. PDF 1 : « A major limitation of this paper is that it lacks an in-depth analysis of the mechanisms through which certain economic, fiscal and institutional factors do or do not affect r-g. »

Annexe (`heimberger2023_annexe.txt`, contrôlé par recherche dans le texte, hors du vérificateur, qui ne lit qu'une source par fiche) :

- A1. p. PDF 11, tableau A1, ligne g : « Annual growth rate of GDP at current Dollars in % »
- A2. p. PDF 11, tableau A3 : « Initial public debt » « -0.00593 » « 0.00746 »
