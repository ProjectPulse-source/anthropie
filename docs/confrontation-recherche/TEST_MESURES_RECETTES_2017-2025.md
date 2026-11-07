# Test : le recul des recettes depuis 2017 tient-il aux baisses d'impôts ? (06/11/2026)

**Origine.** Le chantier vient de la session RADAR EMAIL DETTE (`06_PROMOTION\CAMPAGNES\2026-10-16_RADAR_DETTE_ONGLETS\TRANSMISSION_SITE_DECOMPOSITION_2017.md`).
Deux engagements ont été pris le 20/10 :
- **Michaël Zemmour** : rapporter le recul des recettes corrigées du cycle au coût chiffré des mesures et à la normalisation après 2023 ;
- **Emmanuel Jessua** (Cour des comptes) : relire le chapitre III du rapport de juin 2025 et confronter nos séries à son analyse de la soutenabilité.

**Statut.** Résultat de recherche contrôlé. La section `#mesures` de `/pourquoi-la-dette-publique-augmente/` (FR et EN) en tire ses chiffres par `scripts/update_dette_dynamique.py` (fonction `prelevements`, gardes de prose) ; contre-expertise faite et arbitrée le 07/11/2026 (PRO-20261107-011012, close) ; **publiée le 07/11/2026** (commit `9a6d0d5`, accords de « point » corrigés au commit suivant). Le script de recherche est `test_mesures_po_2017_2025.py`, dans ce dossier.

**Mise à jour du 07/11/2026, après la contre-expertise (PRO-20261107-011012, verdict O2 ; arbitrage `D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261107-011012_arbitrage.md`). Elle prime sur tout ce qui suit :**
- **Raccordement des crédits d'impôt, mesuré.** La série PTC d'Eurostat suit à 0,12 Md€ près, de 2015 à 2020, la chronique des **recettes** de crédits d'impôt de l'INSEE (« L'enregistrement des crédits d'impôt en base 2020 », mars 2024, tableau 4-1 ; pièce `scripts/sources_dette/insee_credits_impot_base2020_2024-03.pdf`, SHA-256 `0c0ae45c…4d39`, transcrite dans `insee_credits_impot_base2020.csv`), et s'écarte de 17,9 Md€ des **dépenses** en 2019 (18,3 contre 36,2). TR − PTC est donc l'impôt après imputation des crédits, ce que déduisent les PO nets. « PTC compté en dépense par Eurostat » était inexact : la dépense de crédit d'impôt, en base 2020, est enregistrée l'année du fait générateur, et diffère de PTC une année donnée. Sur des moyennes de période, le décalage dépenses − recettes vaut 0,085 point de PIB en 2015-2019 ; il n'est pas publié pour 2021-2025. La hausse nette des dépenses (+0,91) devient « environ 0,9 » sur la page. Témoin 5 du générateur, vu mordre.
- **Témoin de la Cour remplacé.** Celui de juillet 2023 (base 2014 : mesures −2,0, élasticité +2,3) est retiré ; celui de juillet 2024 (base 2020, graphique n° 5, p. 36 : mesures −1,9, spontané +1,6) le remplace. La Cour rapporte le cumul des mesures en euros au PIB de l'année finale (p. 35 : 62 Md€ = 2,2 points de PIB 2023) et son « spontané » est le résidu de la variation observée. À cette convention, le calcul donne −1,97 et +1,72 (témoin 1, seuil 0,15, vu mordre). Rapportées chacune au PIB de leur année (identité exacte, tableau de la page), les mesures font −2,13.
- **Formulations corrigées** (FR et EN) : recettes « observées », crédits d'impôt « restituables », « écart de rapprochement » au lieu d'« autres recettes », « l'effet des baisses devient visible » au lieu de « le coût apparaît », citation de la Cour (juillet 2024, p. 35) sur le masquage, fonds de résolution unique (−3,9 Md€, neutre sur le solde ; 7,1 Md€ de mesures 2024 hors prélèvements européens), « décomposition comptable, non une attribution causale », écart de bouclage maximal au centième (0,21).

**Mise à jour du 06/11/2026, après le premier état de cette note. Les § 4 à 7 gardent ce premier état (mesures 2024 à 6,5, reste −0,85) ; là où ils divergent, cette mise à jour prime :**
- **Écart de bouclage levé.** Rejoué sur une série unique, le taux de PO de l'INSEE en base 2020 (`scripts/sources_dette/insee_taux_po_2014-2025.csv`, extrait de `econ-fin-pub-prelev-oblig.xlsx`, SHA-256 `1934fdb2…7020`), l'écart tombe à −0,08 sur 2017-2022 et −0,09 sur 2022-2025, au plus 0,21 une année. Deux causes : le changement de base (2014 → 2020) entre les taux publiés, et une erreur de concept en 2024 : la valeur « solde public » (6,5 Md€) avait été prise au lieu de la valeur en PO (3,2 Md€, juin 2026, p. 27, dont fonds de résolution unique −3,9 et CICE +1,0), et la croissance spontanée de 2024 est révisée (2,3 % pour 3,6 % de PIB).
- **Le reste de −0,85 point expliqué, et il est comptable.** Eurostat (et AMECO) comptent les recettes AVANT crédits d'impôt et rangent les crédits payables (PTC) en dépense ; l'INSEE et la Cour comptent des PO NETS. Entre les fenêtres : TR −1,60 = PO nets −1,00 + PTC −0,61 + recettes hors PO +0,02. La fin du CICE, remplacé par des baisses de cotisations, abaisse la recette brute et la dépense de crédit d'impôt d'autant. Nets des crédits, les dépenses hors intérêts observées augmentent de +0,91 au lieu de +0,30.
- **La convention de cumul est tranchée** : la somme des MN rapportées au PIB de leur année est la somme exacte des contributions annuelles de l'identité ; le bouclage sur l'INSEE le confirme. La variante « convention Cour » (−1,54) n'est plus retenue.
- **Incohérence de la Cour, juin 2026, p. 46** : relue au PDF, le texte écrit « un différentiel de 2,8 points » juste avant le tableau n° 8 (écart 3,0) et « Cet écart de 3,0 points » juste après. Non publiée (une convention de signe sur le déficit stabilisant de −0,1 pourrait l'expliquer : 2,9 − 0,1) ; question à poser à E. Jessua.

## 1. Les deux chiffres « non vérifiés » de la transmission, lus à la source

| Chiffre cité | Ce que dit la source | Verdict |
|---|---|---|
| « plus de 60 Md€ » de baisses depuis 2018 | « Au cours de la période 2018-2023, elles ont atteint **près de** 60 Md€ » (juin 2025, p. 33). L'édition de juillet 2024 écrit « 62 Md€ en 2023, soit 2,2 pts de PIB » (p. 35). | Exact à l'arrondi, mais « plus de » ne se reprend pas tel quel : la Cour dit « près de 60 » en 2025, « 62 » en 2024. |
| mesures nouvelles −6,1 Md€ en 2023 et +3,6 Md€ en 2024 | Juin 2025, p. 29, tableau n° 8. | Exact, avec deux réserves. Le chiffre de 2024 est révisé à 3,2 en juin 2026 (p. 27, tableau n° 1). Les mesures qui touchent le solde public font 6,5 Md€ en 2024 (juin 2025, p. 31), parce que la contribution au fonds de résolution unique (−3,9) est neutre sur le déficit. |

## 2. Données

- **Mesures nouvelles hors effet temporaire de la transformation du CICE**, chaque année au dernier millésime de la Cour, avec la page de chaque valeur dans le script. La somme 2018-2023 fait **−63,1 Md€**, contre « 62 » pour la Cour (2024) : la transcription est validée.
- **Croissance spontanée et croissance du PIB en valeur** : rapports 2022 à 2026.
- **PIB** : Eurostat, notification d'octobre 2026.
- Toutes les valeurs ont été relues à la source, y compris celles qu'avait relevées l'agent de collecte. Le tableau n° 7 de 2022 a été relu en mode brut, sa mise en page se décalant à l'extraction.
- **Pièces** : `06_PROMOTION\RECHERCHE_SOLUTIONS_DETTE_2026-10-02\pieces_lues\cc_rspfp2016.pdf` à `cc_rspfp2026.pdf`, téléchargées depuis ccomptes.fr et vie-publique.fr (HTTP 200). Les SHA-256 sont ci-dessous ; le relevé de collecte est `RAPPORT_SERIE_PO_2026-11-06.md`.

## 3. Méthode

On part de l'identité de la Cour : PO(t) = PO(t−1) + évolution spontanée + mesures nouvelles. En taux de prélèvements obligatoires (τ = PO/PIB), elle s'écrit :

Δτ = τ(t−1)·(s − g)/(1 + g) + MN/PIB.

Elle sépare chaque année deux effets :
- l'**effet des mesures**, MN/PIB, dont le cumul mesure le coût persistant en part de PIB ;
- l'**effet d'élasticité**, qui joue quand la croissance spontanée s s'écarte de la croissance du PIB g.

Les deux cumuls sont ensuite moyennés sur les fenêtres de la page, 2015-2019 et 2022-2025, pour les rapporter au recul des recettes corrigées du cycle selon la Commission européenne (AMECO, printemps 2026).

## 4. Résultats

| | 2015-2019 → 2022-2025 (points de PIB) |
|---|---|
| Recettes corrigées du cycle (Commission), à expliquer | **−1,62** |
| Mesures nouvelles hors CICE, cumulées | **−1,84** |
| Transformation du CICE (année double de 2019 et contrecoups) | +0,18 |
| Effet d'élasticité, cumulé | **+0,89** |
| Total de l'identité des prélèvements obligatoires | −0,77 |
| Reste : recettes hors prélèvements obligatoires, changement de base, écart de bouclage | −0,85 |

**Le masquage, année par année.** De 2018 à 2022, les mesures cumulées retirent 2,1 points de PIB et l'élasticité en rend 2,1. Le taux de prélèvements obligatoires de 2022 reste donc proche de celui de 2017. Puis l'élasticité retire 1,6 point en 2023 et 0,5 en 2024. En 2024-2025, les mesures nouvelles rendent 1,0 point. Le cumul des mesures passe ainsi de −2,5 points en 2023 à −1,5 en 2025, sous deux réserves :
- une partie des hausses de 2025 est annoncée comme temporaire, soit 8,5 Md€ (surtaxe sur les grandes entreprises, CDHR, taxe sur le fret maritime ; juin 2026, p. 30) ;
- une partie relève de la sortie du bouclier énergétique, par la fraction d'accise sur l'électricité (ex-TICFE).

**Témoins.**
1. **Indépendant.** La Cour décompose elle-même 2017-2022 (juillet 2023, p. 31) : −2,0 points pour les mesures, +2,3 pour l'élasticité. Le calcul donne −2,13 et +2,09 : même conclusion, à 0,2 point près.
2. **Bouclage sur les taux publiés.** De 2017 à 2022 (base 2014), le calcul donne −0,2, CICE compris, contre +0,3 observé (45,1 puis 45,4, édition 2023). De 2022 à 2025 (base 2020), il donne −1,1, contre −1,4 observé (45,0 puis 43,6). Les écarts sont de 0,5 et de 0,3 point.
   - **Origine identifiée en partie.** Chaque mesure est rapportée au PIB de son année, ce qui revient à un coût qui croît comme le PIB. La Cour rapporte le cumul au PIB de la dernière année : 53,9 Md€, soit 2,0 points de 2022. Son élasticité vaut 2,3 points, contre 2,1 ici.
   - **Effet sur le résultat.** Avec la convention de la Cour (cumul en euros rapporté au PIB de chaque année), l'effet des mesures entre les fenêtres vaut −1,54 au lieu de −1,84. Il reste de l'ordre du recul de −1,6 : **la conclusion « même ordre de grandeur » tient sous les deux conventions, mais pas la phrase « les mesures dépassent le recul »**, qui dépend de la convention.
   - **Autres explications, non démontrées** : millésimes de la croissance, changement de base, taux de PO approché.
   - **Limite déclarée.**
3. **Total des recettes observé** (Eurostat) : −1,6 point entre les mêmes fenêtres, comme la série corrigée. La correction du cycle pèse donc peu entre ces deux moyennes.

## 5. Lecture : accord et écart avec l'objection

- **Accord, sur le mécanisme.** Des baisses de prélèvements décidées, pérennes pour l'essentiel (taxe d'habitation −15,7, IS −11,1, impôts de production −11,3, barème de l'IR −5,4 Md€ de 2017 à 2022 ; Cour, juillet 2023, tableau n° 2), ont été compensées jusqu'en 2022 par une élasticité supérieure à 1. Leur effet est apparu en 2023-2024. C'est aussi la lecture de la Cour, et elle se retrouve dans le calcul.
- **Accord, sur l'ordre de grandeur.** Entre les deux fenêtres, les mesures cumulées (−1,5 à −1,8 point selon la convention) sont du même ordre que le recul des recettes corrigées (−1,6). Les dépenses corrigées, elles, varient de +0,1 (page, `#conjoncture`).
- **Écart, ou plus exactement ce que l'objection ne dit pas.** Le recul observé n'est pas le seul effet des mesures. L'élasticité reste, en 2022-2025, au-dessus de son cumul de 2015-2019 (+0,9 point) : elle compense encore une partie des baisses. Et un reste de −0,85 point n'est pas expliqué par les prélèvements obligatoires dans ces données ; il mêle recettes hors prélèvements, changement de base et écart de bouclage, sans que ces données le départagent. Ensuite, la « normalisation après 2023 » est double : un retournement de l'élasticité (2023-2024), puis des hausses de mesures (2024-2025), dont une partie est temporaire.
- **Non établi ici.** Ce que les recettes auraient été sans ces mesures, comportements compris (contrefactuel). Les chiffrages de mesures sont ceux de l'administration, faits à comportement constant pour l'essentiel ; ils ne mesurent ni l'effet retour sur l'activité ni l'effet sur les assiettes. La question « pourquoi le déficit est élevé » relève d'une autre décomposition, en niveau, que ce test ne fait pas.
- **Piège État ≠ administrations publiques, traité.** Les mesures nouvelles de la Cour portent sur les prélèvements obligatoires de l'ensemble des administrations. La suppression de la taxe d'habitation y compte une fois ; la fraction de TVA versée en compensation est un transfert interne, neutre.

## 6. Engagement envers Jessua : le chapitre III relu (juin 2025, p. 79-126)

- **Même identité que la page**, avec le terme de l'effet boule de neige (p. 89).
- **Concordance chiffrée** avec le tableau n° 8 de juin 2026 (p. 46). En 2025, la Cour trouve un solde primaire stabilisant de +0,1, un déficit primaire effectif de 2,9, un écart de 3,0, des flux de créances de 0,1 et une variation de 3,1. La page, sur Eurostat, trouve 0,10, 2,87, 2,97, 0,08 et 3,05. Sur 2020-2024, les déficits primaires font +22,9 points dans nos séries, « +23 » pour la Cour (p. 94).
- **Incohérence interne de la source, à signaler sans en tirer plus.** Le texte de juin 2026 (p. 46) écrit « un différentiel de 2,8 points » entre déficit primaire effectif et stabilisant ; son tableau n° 8 donne 3,0 sur la même ligne.
- **Longue période.** De 1978 à 2024, la Cour attribue 57,4 points aux déficits primaires et 8,8 à l'effet boule de neige (p. 93-94). Cela concorde avec le constat de la page sur 1995-2025 : la hausse tient aux déficits primaires, intérêts et croissance se compensent presque.
- **Lecture normative de la Cour** : un retour à des excédents primaires durables, de l'ordre de 1,1 point de PIB, pour un écart taux-croissance de 1,1 (p. 123) ; l'accent mis sur un écart durablement négatif est jugé « rétrospectivement peu prudent » (p. 91). C'est la thèse d'une institution dont le mandat est le contrôle des finances publiques. La page `#soutenable` (dette-publique-peut-elle-baisser) l'éprouve déjà par la littérature : Lian et al., Checherita-Westphal et Semeano, Heimberger. **Proposition** : ajouter à sa confrontation la concordance du tableau n° 8 et le chapitre III aux références lues (p. 79-126).

## 7. Suite proposée (état au premier jet ; voir la mise à jour en tête : points 1 et 3 faits, 2 en cours)

1. **Section « Baisses d'impôts ou recettes spontanées ? »** sur `/pourquoi-la-dette-publique-augmente/`, après `#conjoncture`, FR et EN. Les valeurs de la Cour y entrent comme pièce transcrite dans `scripts/sources_dette/` (catégorie « transcrite et vérifiée contre la source archivée »). Les calculs passent dans `update_dette_dynamique.py`, avec des gardes : mesures ≥ recul, élasticité positive, témoin Cour 2017-2022 à 0,3 près, qui s'arrête au-delà.
2. **Contre-expertise avant publication** : les deux réponses partent vers un économiste et vers la Cour.
3. **Avant de rédiger, lever l'écart de bouclage (0,3 à 0,5 point)**, en rejouant le calcul sur la série de taux de PO de l'Insee en base 2020.

## SHA-256 des pièces

```
c4a3bc34a9960bd5541eea37aa3510ec874d4ad234ae130f5e325708d618a12b  cc_rspfp2016.pdf
c9bb850e3caec9e3e6fe7ffa9ceceace894b610296952b31486e97093ba0d545  cc_rspfp2017.pdf
afe58d4dc907b0a20a776a3a7d9a0f803e2ec30854efb2e4f98dad73b2c381fe  cc_rspfp2018.pdf
9441662afd3a494649ca7c192618ad4bebe500668ed50e3fb4a4aaed21a640c9  cc_rspfp2019.pdf
229ed6d3ebf0a4d8e978fed3ec392948583ab4b966829905db6ca78b7d9d19eb  cc_rspfp2020.pdf
480150112cdc7e743cfcc49ba92052471e69c35f21398e4e6407ba266dbb34aa  cc_rspfp2021.pdf
f9cfc356e7ece96fc1dbb9e63cf65aa941b9a551e20c1b39c4fa100a2f7b2341  cc_rspfp2022.pdf
8a73674a3f703bd172fba03932bd5267f5098affcea4f9676b0df4670e70c3c8  cc_rspfp2023.pdf
8ab1f575646c26a00b60d1fa42add4a7ca79fd23837aa0b6a32666e7081cc56a  cc_rspfp2024.pdf
94da8b0477bbf00d0dbd89006327c4290e78c42bb64ebe37c7e6dcbe294d303e  cc_rspfp2025.pdf
11942092110b9b6626ec77d6fffc4b31fa20c604044fca260857cb76fbf7cc61  cc_rspfp2026.pdf
0c0ae45c5c37ac088ec3319b358d94fa55e3f75eb9aadf1d4835011545674d39  insee_credits_impot_base2020_2024-03.pdf
```
