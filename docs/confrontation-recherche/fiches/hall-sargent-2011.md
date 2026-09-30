# George J. Hall et Thomas J. Sargent — Interest Rate Risk and Other Determinants of Post-WWII U.S. Government Debt/GDP Dynamics

- **Référence publiée** : Hall, George J. et Thomas J. Sargent (2011), « Interest Rate Risk and Other Determinants of Post-WWII U.S. Government Debt/GDP Dynamics », *American Economic Journal: Macroeconomics*, 3(3), p. 192-214, DOI 10.1257/mac.3.3.192. Version publiée **non lue** : les écarts avec le document de travail (chiffres, périmètre, annexes) ne sont pas connus.
- **Version lue** : NBER Working Paper 15702, janvier 2010 ; fichier `hallsargent_nber.pdf` (texte extrait `hallsargent_nber.txt`), SHA-256 `f1de43f97ae48569c29facff5794038a7d9bdd154e736642581bcbb4382233e7`, 31 pages PDF ; https://www.nber.org/system/files/working_papers/w15702/w15702.pdf
- **Lecture intégrale** : 30/09/2026, pages PDF 1 à 31 ; dernière page de texte courant (p. 15) : « whose intertemporal properties diﬀer from ours substantially » ; dernière page lue (p. 31, références) : « Spline Methods for Extracting Interest Rate Curves from Coupon Bond Prices ».
- **Qui parle, et d'où** : George J. Hall (Brandeis University, NBER) et Thomas J. Sargent (New York University, NBER) (p. 2). Document de travail **non évalué par les pairs** au moment de sa diffusion (E1) ; aucun financement déclaré ; remerciements à Henning Bohn et à des assistants de recherche. Le texte s'écrit contre la comptabilité officielle des intérêts (Trésor et comptabilité nationale américaine), qu'il appelle « Bad accounting » (annexe B). Il se situe dans le contexte de 2009 : prévision du CBO d'un retour de la dette au niveau de la Seconde Guerre mondiale, craintes d'inflation dans la presse, « unpleasant monetarist arithmetic » de Sargent et Wallace (1981), cosignée par l'un des auteurs (p. 15). Ce que cette position peut faire au propos : la thèse, qui veut que la mesure officielle ne soit pas le bon concept, est aussi l'objet du papier ; ce qu'ils mesurent (rendements de détention en valeur de marché) est solide, mais leur verdict sur l'« erreur » officielle dépend du concept de dette retenu (valeur de marché contre valeur nominale).

## Population, période, variables, méthode

- **Population** : dette fédérale des **États-Unis**, titres négociables porteurs d'intérêts détenus par les investisseurs privés, **en valeur de marché** (E12) ; hors titres non négociables, hors titres détenus par la Fed ou le fonds de la Sécurité sociale, hors dette d'agences.
- **Période** : 1941-2008 (rendements à partir de 1942) ; titres indexés (TIPS) de 1998 à 2008.
- **Méthode** : décomposition comptable de la contrainte budgétaire période par période. Chaque obligation est éclatée en zéros-coupons ; on calcule, par maturité, le **rendement de détention sur un an** (plus- et moins-values comprises), puis on attribue la variation du ratio dette/PIB à quatre composantes : rendements nominaux par maturité, inflation, croissance du PIB réel, déficit primaire. Données CRSP, Treasury Bulletin, courbes de Gurkaynak, Sack et Wright ; courbe ajustée par splines avant 1970. Les rendements réels indexés sont approchés en supposant une inflation en marche aléatoire.
- **Annexe B** : reconstitution de la série officielle d'intérêts (coupons plus rendement à un an sur le principal échu), corrélée à 0,97 avec la série publiée.
- **Annexe C** : contrefactuels de gestion de la dette (tout en bons à 1 an, tout à 10 ans, variance minimale, « clairvoyance »), à taux et inflation historiques inchangés.

## Résultat

1. **Réponses de l'introduction** : l'inflation n'a allégé la dette que « Sometimes, but not usually » (E2) ; la croissance a « beaucoup » contribué (E3) ; la variation des rendements selon la maturité a compté par moments, peu en moyenne après-guerre.
2. **1945-1974** : le ratio passe de 66,2 % à 11,3 % du PIB. Sur 54,9 points, 12,5 viennent des rendements réels négatifs dus à l'inflation, surtout supportés par les porteurs de long terme (10,3 sur 12,5), 21,6 de la croissance et 20,8 des excédents primaires (p. 10). En conclusion : environ 20 % par l'inflation, le reste réparti à peu près également entre croissance et excédents (E7).
3. **Années 1970** : la maturité raccourcie par une loi (abrogée en 1975) a empêché l'État de profiter pleinement des taux réels négatifs (E5).
4. **1981-1993** : le ratio passe de 16,6 % à 42,0 % du PIB ; près de la moitié vient des déficits primaires, mais les rendements réels élevés servis après la désinflation Volcker y ajoutent près de 10 points (E8). Sur l'ensemble de l'échantillon, la croissance a dépassé le rendement de la dette dans la première moitié, et l'inverse dans la seconde (E6).
5. **Moyennes 1942-2008** : rendement réel moyen de la dette nominale de 1,69 % (écart-type 4,87) ; croissance réelle de 3,28 %. La croissance réelle moyenne dépasse la somme du rendement réel moyen et du déficit moyen (E14).
6. **Mesure officielle et mesure économique** : la série officielle (5,79 % de la dette en moyenne) ne mesure pas le concept de la contrainte budgétaire (E4) ; elle pourrait même être ramenée à zéro par un simple roulement d'obligations zéro-coupon (E13). La série des auteurs est plus basse en moyenne et **bien plus volatile** (E9). Avant 1980, l'écart tient surtout à l'inflation (E10) ; après, au risque de taux (E11).
7. **Titres indexés, 1998-2008** : leur rendement réel (4,3 %) a dépassé celui de la dette nominale (3,3 %) (E15).
8. **Contrefactuels** : sur tout l'échantillon, une dette plus courte aurait coûté moins cher et laissé un ratio plus bas en 2008 (27,3 % contre 37,8 %) (E16) ; même avec une clairvoyance parfaite, on n'aurait pas pu reporter toute la charge sur les porteurs (E17).

## Ce que le texte ne dit pas

- Rien sur la **France** ni sur la zone euro : c'est la dette fédérale américaine, en valeur de marché, hors détentions publiques et hors Fed (E12). Le ratio n'est pas le ratio en valeur nominale (type Maastricht) qu'utilisent les pages.
- Il ne mesure **pas de retard de transmission** des taux à la charge comptable. Il montre autre chose : dans le concept de la contrainte budgétaire en valeur de marché, une hausse de taux se transmet **immédiatement** sous forme de moins-values pour les porteurs de titres longs (E9, E11). Le lissage de la série officielle est une propriété de la mesure (E4, E13), non une loi de la dette.
- Il ne distingue **pas** inflation anticipée et inflation non anticipée : il mesure des rendements réels **réalisés**. Le « perhaps unexpectedly » de la conclusion, au sujet de la désinflation Volcker (p. 14), est une réserve, non une estimation.
- Il ne dit pas que l'inflation est un bon moyen de réduire la dette : sa réponse est « not usually » (E2) et, après-guerre, 20 % seulement de la baisse (E7).
- Il ne recommande pas une maturité : les contrefactuels sont rétrospectifs, à taux historiques donnés. La note 17 rappelle qu'il n'est peut-être pas optimal de minimiser la volatilité, la dette nominale servant de couverture contre les chocs budgétaires.
- Rien après 2008, donc rien sur 2022.

## Effet sur nos hypothèses

| Id | Effet | Motif précis (population/période/variable comparées à celles de la page) |
|---|---|---|
| C1 | nuance — met en danger une lecture économique | La page décrit la **charge comptable** (« la charge d'une année rémunère un stock émis à des dates différentes »). Hall et Sargent n'en contestent pas le retard, mais montrent, pour les États-Unis de 1942 à 2008, que la mesure officielle des intérêts n'est pas le coût qui gouverne la dette en valeur de marché (E4, E13). Dans ce concept, le choc de taux passe tout de suite, par les plus- et moins-values des titres longs (E9, E11). Le retard est donc un fait de la **mesure** et de la maturité, pas un délai du **coût économique**. La page ne doit pas présenter la charge retardée comme le coût réel instantané de la dette. La maturité règle bien la vitesse de transmission (E5, E16), ce qui appuie le mécanisme invoqué. |
| C2 | nuance | Les auteurs montrent que la série officielle des intérêts et la dynamique du ratio (en valeur de marché) divergent fortement : la première est lisse, la seconde volatile (E9). Cela va dans le sens de « stabiliser le ratio ne stabilise pas la facture » ; le ratio est toutefois en valeur de marché et la population américaine. Le texte ne teste pas la phrase de la page. |
| C3 | appuie (mécanisme) / nuance (« sans effort ») | L'écart entre croissance et rendement de la dette gouverne bien le sens de la dynamique : la croissance l'emporte dans la première moitié de l'échantillon, puis c'est l'inverse (E6, E14). Mais la grande baisse de 1945-1974 ne s'est **pas** faite sans effort budgétaire : les excédents primaires en expliquent à peu près autant que la croissance (E7). Le cas historique le plus favorable ne réalise donc pas « sans le moindre effort budgétaire ». Autre variable : le rendement de détention en valeur de marché, et non le coût moyen du stock. |
| C6 | sans rapport | Période close en 2008. Seul point voisin : de 1998 à 2008, les titres indexés américains ont rapporté davantage que la dette nominale, sans poussée d'inflation (E15) ; cela ne dit rien de 2022. |
| Q2 | appuie (mécanisme), sans tester la distinction | Des rendements réels négatifs dus à l'inflation ont réduit la dette après-guerre, aux dépens surtout des porteurs de titres longs (E8) ; l'effet dépend de la maturité (E5). La désinflation inverse le transfert au profit des porteurs (E8). Le texte mesure des rendements **réalisés** : il ne sépare pas l'inflation anticipée de l'inflation non anticipée, que la page tient pour seule opérante. États-Unis 1942-2008. |

## Extraits exacts

E1. p. PDF 1 : « NBER working papers are circulated for discussion and comment purposes. They have not been »
E2. p. PDF 3 : « Did the U.S. inﬂate away much of the debt by using inﬂation to pay negative real rates of return? Sometimes, but not usually. »
E3. p. PDF 3 : « How much did growth in GDP help contribute to holding down the debt GDP ratio? A lot. »
E4. p. PDF 3 : « Unfortunately, the government’s interest payments series fails to measure the concept that appears in the government budget constraint »
E5. p. PDF 5 : « by causing the Treasury to shorten the average maturity of its debt during the high inﬂation years of the 1970s, this law prevented the government from fully beneﬁting from the negative implicit real interest it managed to pay through inﬂation. »
E6. p. PDF 10 : « For the ﬁrst half of the sample, the growth rate of GDP exceeded the return on the debt, while in the second half of the sample, the return on the government debt exceeded the growth rate. »
E7. p. PDF 14 : « Only about 20 percent of the decline in the debt-GDP came from using inﬂation to deliver negative returns to bond-holders. The remaining 80 percent was split about equally between growth in GDP and running net-of-interest surpluses. »
E8. p. PDF 10 : « Thus, while long-term bondholders were heavily taxed by inﬂation after WWII, they did very well when Volcker brought inﬂation down during the early 1980s. »
E9. p. PDF 21 : « As can be seen in this ﬁgure, our series is lower on average and considerably more volatile than the government’s. »
E10. p. PDF 21 : « Up until the 1980s it appears that much of the diﬀerence between the reported series and our series is due to inﬂation. »
E11. p. PDF 21 : « Post-1980 something else is going on, namely, nominal interest rate risk that, in a lower and less volatile inﬂation environment, translated into real interest rate risk. »
E12. p. PDF 5 : « Further each security is valued at market prices rather than par values. »
E13. p. PDF 3 : « The government could drive that measure of interest payments to zero every period by perpetually rolling over, let us say, zero-coupon 10 year bonds. »
E14. p. PDF 14 : « We see in table 2 that the average growth rate of the real GDP exceeds the sum the average real return paid to the government’s creditors and the average deﬁcit-to-GDP ratio. »
E15. p. PDF 14 : « Finally it is interesting to note that since the introduction of TIPS, their returns have on average exceeded those of the nominal debt. »
E16. p. PDF 25 : « Over the entire sample, a portfolio of shorter maturity debt would have generated lower borrowing costs, a reduction in the variance of the returns, and a lower 2008 debt-to-GDP ratio than a portfolio of longer maturity debt. »
E17. p. PDF 26 : « Even with the 20/20 hindsight, it would not have been possible to shift all the burden of deﬁcit spending onto bondholders. »
