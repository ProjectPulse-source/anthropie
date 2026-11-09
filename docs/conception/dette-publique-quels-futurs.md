# Fiche de conception — Peut-on changer les règles du jeu de la dette publique ?

Page : `/dette-publique-quels-futurs/` (FR, slug à confirmer à l'arbitrage de phase A) · `/en/public-debt-what-futures/`
(EN, idem) · ouverte le 2026-11-09

Origine : pièce « Dette-02 » du 09/11/2026 (SHA-256 `314b569f…e7a1`) et son arbitrage
`D:\PRO\.claude\external-audits\ARBITRATIONS\ENTRANTE_2026-11-09_Dette-02_arbitrage.md` ; commande `/dette-quels-futurs`.
Matière de la session : `D:\PRO\06_PROMOTION\RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\` (sources archivées, test décisif).

**Décisions déjà prises, non rouvertes ici** : onglet du dossier dette (sixième volet), FR et EN, pas une rubrique du
menu ; volet prospectif, « Peut-elle baisser ? » reste rétrospectif ; une matrice commune et des hypothèses communes,
chiffres par générateur ; la technologie aussi en variable transversale ; ni vitrine du livre ni recommandation d'un
scénario ; l'hypothèse « transformer sans transférer ailleurs les contraintes » dans un bloc séparé, présentée comme
celle de l'auteur.

## Forme

`quantitatif` et `juridique-institutionnel` (`ressource.type: ["quantitatif", "juridique-institutionnel"]`), avec les
exigences d'`explicatif-causal` qui s'imposent à une page prospective (contrefactuels, hypothèses concurrentes, ce qui
ferait varier la conclusion) : la contre-expertise de phase A dira si la page doit déclarer ce troisième type à la place
du second.
- Quantitatif : la page déclare `donnees: [dette_futurs]` et prend tout le modèle vérifié par machine (carte de partage
  et vignette, résultat en une phrase, figure signature SVG et PNG avec version téléphone, Réutiliser, Dataset, JSON et
  CSV, jetons, gardes vues mordre). Périmètre : dette de Maastricht des administrations publiques, % du PIB ; millésime
  des projections (DSM 2025, publié le 12/02/2026) dit partout ; une projection n'est jamais une mesure ; un écart en
  points de PIB n'est pas un montant.
- Juridique-institutionnel : pour chaque levier, distinguer le droit applicable (règlement (UE) 2024/1263, articles 123
  et 125 TFUE, traités), ce qu'il faudrait changer (règlement à la majorité qualifiée, traité à l'unanimité et
  ratification, Constitution allemande), et qui décide (État, Parlement, Conseil, BCE, partenaires) ; textes datés,
  lus au texte.
- Explicatif-causal : séparer l'arithmétique (ce que le levier fait au ratio si tout le reste est égal) de la causalité
  économique (ce qu'il ferait aux taux, à la croissance, aux détenteurs) ; dire, levier par levier, ce qui ferait varier
  la conclusion.

## Fiche de conception

### Question centrale

Changer les règles du jeu (règles budgétaires européennes, financement commun, statut de la dette détenue par la banque
centrale, restructuration, monnaie, fiscalité des patrimoines, croissance de la productivité) modifierait-il la
trajectoire de la dette publique française d'ici 2035, de combien, à quelles conditions juridiques, et en faisant porter
quoi à qui ?

### Enjeu

La campagne de 2027 fera s'affronter des propositions qui promettent d'alléger la contrainte de la dette autrement que
par l'ajustement budgétaire : annuler la dette détenue par la banque centrale, mutualiser les emprunts européens,
exclure l'investissement des règles, restructurer, sortir de l'euro, taxer les grands patrimoines, compter sur la
productivité. Leurs ordres de grandeur ne sont jamais posés côte à côte, sur les mêmes hypothèses, ni rapportés à ce
qu'ils changent (stock, flux, taux, capacité productive), à qui en supporte le coût et à qui peut les décider. Le lecteur
ne peut donc pas distinguer une proposition qui déplace la contrainte d'une proposition qui la réduit ou qui l'aggrave.

### Croyance initiale

Deux croyances opposées et symétriques : « il suffirait de changer les règles » ; « il n'y a pas d'autre voie que
l'ajustement ». Toutes deux tiennent la question pour tranchée d'avance, sans mesurer ce que chaque levier change ni qui
le porte.

### Découverte principale

Rien n'est établi à ce stade : la découverte se constate après la phase B, levier par levier. Ce qui est posé
(arbitrages `PRO-20261109-063209` et `ENTRANTE_2026-11-09_Dette-04`) :
- **Clé de lecture comptable**, non une découverte : à solde primaire, taux implicite, croissance et ajustements
  inchangés, une réforme institutionnelle ne change pas à elle seule la trajectoire calculée du ratio. Elle n'agit que
  par ces variables, ou par une opération sur le stock.
- **Hypothèse économique à éprouver** : certaines réformes peuvent améliorer ces variables, donc réduire la contrainte
  au-delà d'une redistribution ; d'autres la déplacent (vers d'autres détenteurs, d'autres années, d'autres risques) ;
  d'autres l'aggravent. Pour chaque levier, la page conclut à l'une de quatre issues (déplacée, réduite, aggravée,
  dépendante de conditions nommées) ; aucune n'est fixée d'avance.
- **Sensibilités exploratoires** du test du 09/11 (à refaire avec le moteur de l'annexe A2.2 avant toute publication) :
  un point de solde primaire ≈ −9 points en 2035 ; ±0,5 point de croissance nominale ≈ ∓6 ; −10 à −20 pb de taux de
  marché ≈ −0,7 à −1,5 ; un à deux points de PIB d'investissement emprunté sans effet productif ≈ +9 à +18 ; décote de
  30 à 40 % en 2028, effet mécanique seul ≈ −38 à −50. Ce sont des expériences calibrées sur une même référence, non des
  efforts équivalents ni des politiques également réalisables.

### Mécanisme explicatif

L'identité `Δd = (i − g)/(1 + g) · d₋₁ − sp + ajustements` fixe les canaux : un levier agit sur le solde primaire (effet
cumulé, un pour un), sur le taux implicite (effet lent : la dette à court terme suit le taux de marché dans l'année, la
dette à long terme seulement à mesure qu'elle est renouvelée), sur la croissance nominale (effet sur tout le stock ;
croissance réelle et inflation séparées, leurs effets distributifs diffèrent), ou sur le stock (une fois). Ce qui
détermine si une réforme réduit la contrainte, et non seulement la déplace, est hors de l'identité : son effet causal sur
ces variables (multiplicateurs, durée des effets, recettes induites, primes de risque), à sourcer levier par levier.

### Preuve décisive

À ce jour, une preuve de faisabilité, non une validation : le moteur reproduit approximativement une sensibilité
publiée de la Commission (« lower SPB » : +5,0 contre +4,9 en 2036) et encadre une seconde sous plusieurs répartitions
possibles du choc (« adverse r-g » : +10,1 à +12,6 contre +11,6) ; une mutation sur le passage des taux fait échouer le
second test, une erreur de calendrier passe le premier. Cela justifie de poursuivre, non de publier. Protocole de phase B
(arbitrages du 09/11) : passage des taux selon l'annexe A2.2 ; chocs appliqués au solde primaire **structurel**, la
composante conjoncturelle recalculée par l'écart de production et la semi-élasticité de la France, le coût du
vieillissement repris tel quel ; tests de reproduction supplémentaires dans le même cadre (« historical SPB » +2,1,
« financial stress » +2,7), écarts contrôlés en 2028, 2030, 2032 et 2035, tolérances écrites avant le calcul par type
d'erreur. Aucune validation indépendante n'est disponible : la page présente des sensibilités conditionnelles et le dit.
Pour chaque levier publié, l'effet mécanique s'accompagne de ses contreparties, chiffrées ou dites inconnues.

### Pouvoir discriminant

Les rivales ne sont pas des camps mais trois mécanismes, ni exclusifs ni homogènes : **modifier les règles de
financement** (taux, maturités, détenteurs, statut des titres), **modifier les flux budgétaires** (dépenses, recettes),
**modifier les capacités productives** (investissement, productivité, technologie). Une position n'est attribuée qu'à
qui l'a écrite, citation lue au texte ; la Commission ne prescrit rien dans le DSM (« descriptive, not prescriptive »),
elle fournit la référence.
Témoin : la même trajectoire de référence, un levier modifié à la fois, l'écart en 2028, 2030 et 2035.
- Ce que la mise en regard révèle qu'une série isolée ne montre pas : par quel canal chaque proposition agit, avec quel
  délai, et sur qui retombe son coût ; la même grille appliquée à toutes.
- Ce qu'elle départage : une proposition qui ne passe par aucun canal de l'identité ne change pas la trajectoire ; pour
  les autres, la page dit si l'effet est une redistribution, une réduction ou une aggravation, et sous quelles
  hypothèses causales le verdict change.
- Robustesse : chaque sensibilité refaite sous le choc « adverse r-g » ; si l'issue d'un levier change, la page le dit.
- Si un levier ne se laisse pas trancher, la page l'écrit (« dépend de… »), sans rivale inventée.

### Limite

- Une projection à politique inchangée n'est ni une prévision ni le scénario le plus probable (la Commission l'écrit,
  DSM 2025, chapitre 1). Trois objets distincts dans la page : la référence sans nouvelles mesures, une trajectoire
  conditionnelle d'engagements (plan budgétaire et structurel à moyen terme de la France, à lire), les sensibilités
  construites pour la page.
- Leviers pris un à un : sensibilités de premier ordre, non conséquences nettes d'une politique complète ; dit au contact
  de chaque chiffre.
- Investissement modélisé en trajectoire de niveau du PIB, jamais en points de croissance permanents ; paramètres
  sourcés avant le calcul.
- Ratio de dette ≠ bien-être : une dépense peut alourdir le ratio et améliorer le patrimoine public ou éviter un coût
  futur ; une cession peut l'alléger sans enrichir la collectivité.
- Les probabilités qualitatives du livre ne sont ni reprises ni remplacées ; les chiffres du livre retirés depuis ne sont
  pas repris.

### Valeur finale

Après lecture, le lecteur peut dire sans jargon ce qu'il croyait (changer les règles suffirait, ou rien ne peut
changer), ce qu'il sait (par quel canal chaque proposition agit, de combien sur une même référence, qui en porte le coût,
qui peut la décider), sur quelles preuves (projections de la Commission, moteur testé contre ses sensibilités, textes
juridiques lus), et quelle question s'ouvre (quelles conditions font qu'une transformation réduit la contrainte au lieu
de la déplacer). Outil réutilisable : la grille, applicable à toute proposition de la campagne.

### Singularité

Cette page existe parce qu'elle propose une **cartographie des transformations de la contrainte d'endettement** :
pour chaque proposition, ce qui change (stock, flux, taux, croissance), qui supporte (coûts, pertes, risques, délais) et
qui décide (pouvoir juridique, coordination). Une seule question par proposition : réduit-elle un stock, modifie-t-elle
un flux, améliore-t-elle une capacité productive, change-t-elle la répartition des risques, ou combine-t-elle plusieurs
de ces mécanismes ? Ni le DSM de la Commission (qui teste des chocs de solde, de taux et de croissance, jamais des
changements de règle), ni `/dette-publique-peut-elle-baisser/` (rétrospective), ni `/formules-du-debat-sur-la-dette/`
(qui recense les énoncés sans les chiffrer), ni le livre (récits, bornes 2035 non rapportées à une référence commune) ne
l'ont sous cette forme. Le résultat vaut même si aucune solution ne domine.

### Raccords

- **Définition de l'anthropie** : retenue, dans un bloc séparé et présenté comme l'hypothèse de l'auteur
  (`{{< canonical-definition >}}`) : « transformer un système d'endettement sans transférer ailleurs les contraintes ».
  Le bloc ne dit pas que la page démontre l'hypothèse : il la propose comme lecture des constats, qui restent valables
  sans elle. Pas de phrase depuis « Quelques domaines d'application » de `/quest-ce-que-lanthropie/` (aucune
  démonstration ici).
- **Livre *Dette publique : qui paie vraiment ?*** : retenu, en prolongement (`appel-livre` en fin de page, `avis="non"`,
  surtitre vrai : « Les quatre scénarios, racontés sur dix ans ») ; `ressource.livres`. Écart dit, non caché : la
  continuité du livre (≈ 130 % en 2035) est moins sombre que la référence de la Commission (140,8 %), sur des hypothèses
  différentes ; les points du livre corrigés par le site vont au plan de révision d'avril 2027.
- **Working paper** : écarté (aucun AWP ne traite des règles budgétaires ; AWP-08 porte sur la réversibilité, à relire
  avant de confirmer l'écart si le bloc d'hypothèse invoque la réversibilité).
- **Pages voisines** :
  - `/dette-publique-peut-elle-baisser/` : retenue (« ce qui a fait baisser la dette ailleurs » → « ce qui la ferait
    baisser ici, sur dix ans ») ; réciproque : une phrase en fin de page renvoie au nouveau volet ;
  - `/dette-publique-generations-futures/` : relation tenue par la barre du dossier (prolongement « Plus ») ; pas de phrase
    ajoutée (09/11/2026) : la page ne mobilise pas l'indicateur S2, un renvoi n'apporterait pas de relation lisible ;
  - `/qui-paie-la-dette-publique/#annuler-banque-de-france` : retenue, le levier « annulation » y renvoie au lieu d'être
    recalculé ; aucune modification de la section sans le dire à l'auteur ;
  - `/qui-paie-la-dette-publique/` FAQ « engrenage » (commit `43ad0eb`) : retenue, elle renverra au volet ;
  - `/inflation-et-dette-publique/` : écarté à la phase B (09/11/2026) — la fiche 9 ne simule pas l'inflation d'une
    sortie de l'euro (« Non simulé ») ; un renvoi à l'épisode 2021-2023 laisserait croire à une transposition ;
  - `/formules-du-debat-sur-la-dette/` : retenue (les énoncés de campagne y renvoient à leur levier) ;
  - `/dette-publique-comparaison-internationale/` : écarté (09/11/2026) — la page ne traite pas des précédents
    étrangers ; un lien promettrait une comparaison qu'elle ne fait pas ; la page y renvoie déjà par ses pastilles (« Et ailleurs ? ») ;
  - `/registre-des-couts-deportes/` : écarté de l'exposé des constats ; candidat pour le seul bloc d'hypothèse.

## Fiche D0

- **Résultat visé** (au plus près des finalités) : que la page soit citée ou reprise comme la comparaison chiffrée des
  propositions de « changement de règles » pendant la campagne de 2027 (presse, enseignants, moteurs de réponse,
  contradicteurs des deux camps) ; finalités servies : crédibilité de l'auteur sur la dette publique (pièce la plus
  originale du dossier) ; diffusion du livre, dont la page est le prolongement chiffré des scénarios.
- **Diagnostics** : Search Console (impressions, clics ; requêtes « annuler la dette », « euro-obligations »,
  « règle d'or », « sortie de l'euro dette », « avenir de la dette », « dette 2035 ») ; Bing (requêtes et citations IA) ;
  navigation interne depuis les cinq volets ; demandes d'exemplaire ; reprises observées, jamais déclarées d'avance.
- **État initial (09/11/2026)** : page inexistante. Demande mesurée sur le site : **aucune** — sur 90 jours au 06/11/2026
  (`06_PROMOTION\BOUCLE_GEO_2026-11-06\brut\perf_page_requete_90j.json`, 1 120 couples page-requête), aucune requête ne
  porte sur l'avenir de la dette, une réforme des règles, une restructuration, des euro-obligations ou l'annulation ;
  Bing (`bing_ai_performance_2026-11-06.txt`) : aucune. Ce relevé mesure ce que le site attrape, pas l'intérêt public.
  L'intérêt public tient à la campagne de 2027 (énoncés recensés par `/formules-du-debat-sur-la-dette/`) ; il n'est pas
  mesuré. La recevabilité (règle 4) repose donc sur l'apport propre et la décision de l'auteur, et elle est dite comme telle.
- **Ce qui l'infirme** : au relevé J+60, page indexée, aucune impression sur ces requêtes et aucune reprise.
- **Relevés** : J+30 et J+60 après publication ; inscription dans `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`
  avant publication.

## Scénarios d'architecture

Trois scénarios, à soumettre à la contre-expertise de phase A ; aucun n'est retenu avant son arbitrage.

- **A — La matrice** (recommandé). Chapô qui donne la réponse ; figure signature : barres horizontales de l'écart en 2035
  par levier, sur la référence de la Commission, colorées par famille (flux, financement, stock) ; « le résultat en une
  phrase » ; puis trois sections par régime du livre (continuité, réforme négociée, ruptures), chacune avec le même
  tableau à six lignes (dette et intérêts, investissement, pouvoir de décision, répartition, droit applicable et
  changements requis, robustesse au choc « adverse r-g ») ; la technologie en variable transversale (une figure :
  trois régimes × croissance −0,5 / +0,5 point) ; « Ce que ces projections ne disent pas » ; bloc d'hypothèse de
  l'auteur ; livre ; sources ; Réutiliser. Force : la matrice décidée est le corps de la page. Risque : un tableau
  répété trois fois, lourd au téléphone.
- **B — L'enquête sur une promesse**. Part de la croyance « il suffirait de changer les règles » et éprouve les leviers du
  plus petit effet au plus grand (euro-obligations → règle d'or → croissance → solde → stock), chaque étape avec sa
  ligne de la matrice ; la matrice complète vient en fin, comme synthèse réutilisable. Force : progression et accroche.
  Risque : l'ordre « du petit au grand » peut se lire comme un plaidoyer pour l'ajustement ; il faut l'équilibrer par les
  porteurs de chaque levier.
- **C — Les trajectoires**. Figure de quatre trajectoires 2025-2035 (référence et trois régimes du livre traduits en
  combinaisons de leviers), puis la matrice. Force : visuel immédiat. Risque majeur : traduire un récit en paquet de
  paramètres fabrique des prévisions qui n'existent ni dans le livre ni chez la Commission ; contraire à
  « scénario ≠ prévision ». Proposé pour être écarté, sauf avis contraire motivé.

Barre du dossier : un sixième onglet change la largeur de la rangée (936 px pour cinq, bascule vers les libellés courts
sous 968 px de barre, mesure du 03/10/2026) ; à remesurer en phase B, avec `data/dossier_dette.yaml` (source unique des
libellés), la liste des volets de `layouts/shortcodes/dossier-dette.html` (volet inconnu = échec) et le sous-titre
« Le dossier, en N pages » ; libellé court envisagé « Futurs » / « Futures », rôle « scénarios » / « scenarios ».

Générateur envisagé : `scripts/update_dette_futurs.py`, jeu `dette_futurs` ; la pièce DSM est celle du générateur
« générations » (même fichier, même empreinte) : une seule pièce, un lecteur commun à factoriser plutôt qu'à copier.

## Étapes de la méthode

- Vérification qu'aucune autre session n'a ouvert le chantier : fait (09/11/2026 ; ni fiche dans `docs/conception/`, ni
  mention au `HANDOFF.md`).
- Lecture de la pièce et de ses arbitrages : fait (09/11/2026 ; empreinte `314b569f…e7a1` conforme).
- Lecture du livre au texte, chapitres 11 à 14 et note méthodologique (p. 137-194, 220-222), édition du 17/10/2026
  (`88e8703e…`) : fait (09/11/2026) ; relevé des hypothèses, mécanismes et chiffres dans le dossier de session
  (`NOTE_LECTURE_LIVRE.md`).
- Plan d'outils (`outils_du_produit.py ressource`) : fait (09/11/2026) ; retenus : méthode ressource-site, séries
  statistiques (MCP `sources`), vérificateur de références (droit de l'Union, textes cités), relecture de langue,
  recette, panel, contrôle des figures ; MAGNIFIER en finition seulement ; votes du Parlement sans objet (aucun vote cité).
- Protocole du type, partie juridique : en cours. Règlement (UE) 2024/1263, articles 1 à 26 lus au texte (EUR-Lex,
  CELEX 32024R1263, texte SHA-256 `f0fa50e5…102e`) : période d'ajustement de quatre ans, prolongeable de trois en échange
  de réformes et d'investissements (art. 2 § 8, art. 14) ; baisse moyenne minimale du ratio de 1 point par an au-dessus
  de 90 %, comptée depuis l'année précédant la trajectoire de référence ou depuis la sortie de la procédure de déficit
  excessif, la plus tardive (art. 7) ; art. L. 213-22-1 CMF lu (clauses d'action collective, titres d'avant 2013 exclus) ; marge de résilience de 1,5 point sous 3 % (art. 8) ; clauses dérogatoires générale et nationale (art. 25, 26) ;
  aucune exclusion de l'investissement vert du calcul, contrairement au « pilier 1 » du livre. Articles 27 à 38 et
  considérants non lus. Reste à lire : articles 123, 125 et 126 TFUE, protocole n° 12, décision du Conseil sur le plan
  français (2025), règlement NextGenerationEU (base juridique de l'emprunt commun), lex monetae (Zettelmeyer 2017).
- Analyses de soutenabilité de la Commission : lues au texte (DSM 2025, Institutional Paper 332, 12/02/2026, archivé
  `84f9872a…` ; encadré 2.1, tableau 2.2, chapitre 1) ; fiche France lue (`2b0486b1…`).
- Test décisif : fait (09/11/2026), `RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\test_decisif\` ; deux témoins passent,
  mutation mordue sur T2, seuil de T1 trop large (dit).
- Scénarios d'architecture : fait (trois, ci-dessus).
- Panel avant : non fait (motif : l'architecture dépend de l'arbitrage de phase A ; à décider ensuite).
- Contre-expertise de phase A : paquet préparé (09/11/2026), audit `PRO-20261109-063209`, REASONING_AUDIT, SHA-256
  `B0222086…6AF0`, source hors OUTBOX `D:\PRO\.claude\external-audits\PAQUET_QUELS_FUTURS_DETTE_PHASE_A_2026-11-09.md` ;
  sas `D:\CONTRE_EXPERTISE\PRO\PRO-20261109-063209\A_TRANSMETTRE\` ; statut AWAITING_MANUAL_SEND (envoi par l'auteur).
  Dix points soumis (moteur, découverte, règle d'or, leviers de stock, témoin institutionnel, écart avec le livre, type,
  architecture, droit, recevabilité) et six hypothèses H1-H6. Réponse archivée (SHA-256 `85DB7E6D…B982`), **arbitrée
  le 09/11/2026** (`.claude/external-audits/ARBITRATIONS/PRO-20261109-063209_arbitrage.md`) : GO pour l'architecture
  A+ (enquête courte, témoin, sensibilités, matrice par régime dans un ordre institutionnel, technologie, robustesse,
  conclusion) ; type `["quantitatif", "juridique-institutionnel"]` confirmé ; C écartée. NO-GO pour publier les
  sensibilités avant un moteur conforme à l'annexe A2.2 du DSM et deux tests de reproduction supplémentaires, même cadre (« historical SPB »,
  « financial stress »), tolérances écrites d'abord ; H3 reformulée ; seuil de la règle d'or retiré ; leviers de stock en
  deux temps et sur une échelle séparée ; FMI en second témoin ; droit qualifié opération par opération (corpus élargi).
  Affirmations du contradicteur non lues au texte marquées NON_VERIFIE dans l'arbitrage.
- Contre-arbitrage reçu hors navette (« Dette-04 », 09/11/2026, SHA-256 `2d15ad7f…f4f2`), arbitré le même jour
  (`.claude/external-audits/ARBITRATIONS/ENTRANTE_2026-11-09_Dette-04_arbitrage.md`) : fiche mise en cohérence (rivales
  en trois mécanismes, sans attribution aux institutions ; quatre formules contraires à la H3 retirées ; H3 séparée en clé
  comptable et hypothèse économique, quatre issues possibles par levier ; « preuve décisive » rétrogradée ; solde
  structurel et composante conjoncturelle ajoutés au protocole ; investissement en trajectoire de niveau ; singularité :
  cartographie « ce qui change, qui supporte, qui décide »). Point 7b (note publique de correction du livre) : décision
  de l'auteur requise, hors de ce chantier.
- Phase B, étape 1 — moteur v2 selon l'annexe A2.2 : fait (09/11/2026), protocole et tolérances écrits avant le calcul
  (`RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\test_decisif\PROTOCOLE_MOTEUR_A22.md`), résultats dans
  `RESULTATS_MOTEUR_A22.md`. R1 « adverse r-g » et R2 « financial stress » passent ; la mutation « passage immédiat des
  taux » les fait échouer tous deux. R3 « lower SPB » échoue sur le calendrier des années de prévision 2026-2027 (dette
  2035 juste à 0,15 point) ; R4 « historical SPB » échoue sur le niveau (écart de millésime AMECO de 0,125 point, soit un
  point de dette en 2035). Les mutations M2-M4 ne peuvent pas être vues mordre. Conséquence : leviers de taux et de
  croissance chiffrés au point près ; leviers de solde appliqués à partir de 2028, affichés à 2035 avec leur limite.
  Une erreur d'implémentation (emprunt net) est corrigée et déclarée ; aucune tolérance n'a été modifiée.
- Correctif du livre (décision de l'auteur, 09/11/2026 : « si nous avons une erreur, nous modifions et nous mettons en
  ligne ») : point A1 corrigé dans l'édition du 09/11/2026, paquet `03_LIVRES\dette-publique\03_LIVRABLES\_A_TELEVERSER_2026-11-09\`
  (journal du livre, § 0y). Le point 7b de « Dette-04 » est ainsi tranché par l'auteur : correction de l'édition en vente,
  non une note publique.
- Phase B, étape 1 — lectures au texte : fait en partie (09/11/2026), `RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\NOTE_SOURCES_PHASE_B.md`.
  Lus : art. 122, 123, 125, 136, 311 TFUE, art. 48 TUE, décision 2020/2053 (art. 5), règlement 2024/1263 (art. 1-26),
  art. L. 213-22-1 CMF ; avis 2026-5 du HCFP (prévision du Gouvernement : 119,3 % en 2026, 121,7 % en 2027 ; retour sous
  3 % en 2029 jugé « très peu vraisemblable »). Le « rapport du FMI de juillet 2026 » cité par la pièce Dette-04 n'existe
  pas selon la page pays du FMI (dernière consultation : juillet 2025) : chiffre écarté tant qu'il n'est pas lu. Non lus
  (sites qui refusent les scripts, navigateur sans résultat utile) : texte des deux recommandations du Conseil de janvier
  2025 (contenu connu par le HCFP), rapport du Trésor sur la dette annexé au PLF 2027 ; art. 124, 126, 310 TFUE,
  règlement 2024/1264, directive 2024/1265.
- Phase B, étape 2 — tests du moteur : fait (09/11/2026), protocole écrit avant (`test_decisif\PROTOCOLE_ETAPE2.md`),
  résultats `RESULTATS_ETAPE2.md`. Témoin extérieur au cadre de la Commission : sensibilité publiée par l'AFT (+100 pb :
  +3,4 / +8,1 / +19,2 Md€ en années 1, 2, 5) ; moteur +5,8 / +8,8 / +19,1 Md€ : échec sur l'année 1 (calendrier
  d'émission, sens prévu), à 9 % et 1 % près ensuite ; la mutation mord. Proportionnalité : échec de peu (5,3 % contre
  5 %), relation croissante avec la taille du choc ; chaque choc calculé directement. Choc de solde dès 2028 : pas de
  témoin, pas de test. Une erreur du script de test (choc d'un an au lieu d'un choc permanent) est corrigée et déclarée.
  Conséquence : leviers de taux affichés à partir de la deuxième année ; leviers de solde comptables.
- PSMT 2025-2029 et annexes du PLF 2027 (rapport sur la dette, RESF) téléchargés et lus (`NOTE_SOURCES_PHASE_B.md`) :
  trajectoire promise en 2024 (116,5 % en 2027) contre prévision de 2026 (121,7 %).
- Phase B, étape 3 — générateur : fait (09/11/2026), `scripts/update_dette_futurs.py` et `scripts/moteur_dette_futurs.py`
  (mécanique du moteur testé reprise à l'identique ; référence reproduite à 140,808 %). Logique prospective
  probabiliste (consigne de l'auteur) : distribution stochastique publiée par la Commission (centiles 10 à 90 jusqu'en
  2030, probabilité 95 % que la dette de 2030 dépasse 2025), trajectoires du Gouvernement placées dans cette distribution
  (prévision du PLF 2027 pour 2030 : 20e centile en niveau, 24e en variation ; promesse du PSMT pour 2029 : sous le 10e
  centile en niveau, 12e en variation, résultat marqué « dépend du point de départ ») ; aucune probabilité attribuée à un
  choix politique. Sensibilités : taux −20 pb ≈ −1,0 point en 2035 (−8 Md€ d'intérêts), croissance ±0,5 point ≈ ∓6 points ;
  solde en illustration comptable. Pièces : `scripts/sources_futurs/` (rapport sur la dette du PLF 2027 ; extrait du PSMT
  avec l'empreinte du PDF entier) ; fiche du DSM lue dans `sources_generations/` (une pièce, deux générateurs). Témoins
  rejoués à chaque exécution : R1, R2, AFT (années 2 et 5), cohérences de la distribution ; `--temoin` : deux mutations,
  toutes deux arrêtées ; rien réécrit à données identiques ; `check-all --ci` à 0. Non fait : workflow de mise à jour
  (calendrier : DSM en février, PLF en octobre, PSMT au printemps) ; le générateur « générations » garde son propre
  lecteur du DSM (factorisation reportée : générateur en ligne, gain faible, risque de régression).
- Maquettes de la figure signature : trois concurrentes (A éventail, B leviers, C leviers face à l'incertitude),
  `06_PROMOTION\MAQUETTES_FIGURE_QUELS_FUTURS_2026-11-09\` ; contre-expertise `PRO-20261109-092834` (réponse Dette-06,
  `C2B9CF72…`), arbitrée le 09/11/2026 : **A figure signature, B figure analytique, C écartée** (dispersion et
  déplacements n'ont pas le même statut) ; « qui porte » retiré des figures (matrice) ; pas de centile dans l'étiquette du
  PLF, note « ce n'est pas la probabilité que la trajectoire du Gouvernement se réalise » ; « plan budgétaire d'octobre
  2024 » au lieu de « promesse » ; éventail limité à 2025-2030, 2035 hors éventail ; leviers par mécanisme. Maquettes A2
  et B2 produites (`maquettes_v2.py`), contrôle automatique à 0, rendus regardés. Téléphone et anglais : à la production.
- Contre-lecture A2/B2 (pièce Dette-07, `12dec1fb…`, arbitrée le 09/11/2026, `ENTRANTE_2026-11-09_Dette-07_arbitrage.md`) :
  effet du solde calculé par l'identité (−8,2 en 2035 au lieu de la somme 8,0) ; trois points de départ dits sous A2 ;
  « trajectoire proposée dans le PLF 2027 » ; titre de B2 « ce que changent le solde, les taux et la croissance » ;
  symétrie des chocs de taux testée (+20 pb : +1,047 ; −20 pb : −1,030 en 2035). Fin des tours de maquettes ; effort
  porté sur la matrice.
- Intégration des figures : fait (09/11/2026), `scripts/figures_dette_futurs.py` appelé par `update_dette_futurs.py` :
  `static/img/dette-futurs-{eventail,leviers}{,-en}{,-m}.{svg,png}` (8 SVG, 8 PNG), pied commun `pied_figure`, contrôle
  de parité téléphone/bureau bloquant, SVG et PNG ensemble ou pas du tout ; `check-figures.py` 0 défaut ; rendus regardés
  (FR bureau et téléphone, EN bureau) : unité ajoutée sur téléphone, note longue réservée au bureau (la page la reprendra
  sous la figure sur téléphone), licence courte sur téléphone. Deux contrôleurs indépendants : non fait (au stade de la
  page, avant publication). Slug anglais `/en/public-debt-what-futures/` provisoire, inscrit dans la licence des figures :
  à confirmer avant publication.
- Matrice institutionnelle : projet écrit (09/11/2026), `RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\MATRICE_INSTITUTIONNELLE.md` ;
  neuf opérations en ordre institutionnel (solde, allongement, règle d'or, emprunt commun, mutualisation, conversion des
  titres de l'Eurosystème, restructuration, impôt sur les patrimoines, sortie de l'euro) et la croissance en variable
  transversale ; chaque case marquée [lu], [calc], [site] ou [non établi] ; art. 126 TFUE et base du règlement 2024/1263
  (art. 121 § 6, procédure législative ordinaire) lus. Contre-expertise `PRO-20261109-095636` préparée (envoi par
  l'auteur).
- Arbitrage de la matrice : fait (09/11/2026), `PRO-20261109-095636` (Dette-08), tous points acceptés ; matrice v2 (v1 en
  `_ARCHIVE\`) : statut [inféré] ajouté, robustesse en trois statuts (calculée / mécanisme documenté / non déterminée),
  règle d'or en trois variantes (la troisième relève du droit primaire et du protocole n° 12), −1,0 point retiré de
  l'emprunt commun (hypothèse de taux), mutualisation en quatre instruments, conversion et annulation séparées, seuils
  des clauses d'action collective en vigueur (D. 213-25-13, lus), sortie de l'euro « non déterminée » ; constat 2 retiré,
  découverte provisoire : « une même réforme peut réduire la dette mesurée, déplacer des charges ou modifier les
  risques selon ses conditions ». Forme publique : option C (fiches courtes, tableau complet téléchargeable). Lectures
  restant avant publication : protocole n° 12, Pringle, décret 2025-1413 et D. 213-25-1, lignes de l'AFT, art. 130 et
  textes de l'Eurosystème, FMI WEO 2014 ch. 3, évaluations de l'impôt sur les patrimoines, art. 63 TFUE, art. 50 TUE.
- Lectures P0 : faites (09/11/2026), `RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\NOTE_LECTURES_P0.md`, pièces et empreintes
  dans `_SOURCES\lectures_P0_2026-11-09\` ; matrice v3. Apports : une conversion qui garde le nominal ne baisse pas la
  dette au sens du protocole n° 12 (inféré du texte) ; Pringle trace la frontière prêter / répondre des dettes ; 86,3 %
  des OAT (nominal) portent des clauses d'action collective, 13 lignes d'avant 2013 non (calcul sur les 76 fiches de
  l'AFT) ; FMI 2014 conditionnel ; impôt sur les grands patrimoines : rendement non établi (1 à 25 Md€ selon deux
  hypothèses nommées). Canaux : navigateur pour l'AFT et EUR-Lex (refus des scripts), copie archivée du PDF du FMI (lien
  officiel en 404) contrôlée par le WP 15/95. Restes : textes de l'Eurosystème sur une conversion, traitement Eurostat
  d'une perpétuelle, art. 65 TFUE.
- Contre-expertise des lectures P0 : faite (09/11/2026), `PRO-20261109-104650`, arbitrée : option A (publication après
  corrections) ; matrice v4 : conversion à nominal constant rendue conditionnelle (SEC 2010 § 5.90 lu), Pringle reformulé,
  86,3 % libellé comme reconstitution nominale des lignes soumises en principe aux clauses, impôt sur les patrimoines
  présenté par convention sans fourchette, FMI 2014 confronté au DP 204 de la Commission (2024). Restes P1 : arrêtés des
  trois OAT€i, art. 65 TFUE.
- Données structurées de la matrice : faites (09/11/2026). Source écrite à la main sans montant saisi :
  `scripts/sources_futurs/matrice_institutionnelle.yaml` (9 opérations × 7 dimensions, FR et EN, statut par champ,
  bloc `valeurs` des données transcrites avec empreinte de la pièce). Module `scripts/matrice_dette_futurs.py`, appelé
  par `update_dette_futurs.py` : jetons résolus (calculs du moteur ; part des lignes soumises aux clauses recalculée sur
  la pièce `sources_futurs/aft_lignes_2026-11-09.csv`, 76 lignes longues et 35 BTF ; jeux `annulation_bdf` et
  `dette_generations`), accords par `langue_generee`. Sorties : bloc `matrice` de `data/dette_futurs.json` (fiches
  courtes = ce qui change, effet, qui décide, issue ; analyse = droit, répartition, robustesse) et
  `static/dette_futurs_matrice.csv` (129 lignes). Gardes : structure, listes fermées, montant en clair interdit, jeton
  inconnu, sens des effets, divergences loi / fiche AFT limitées aux trois écarts déclarés ; trois mutations ajoutées
  au `--temoin`, toutes arrêtées ; `check-all --ci` à 0 ; seconde exécution : rien écrit. Témoin AFT : même résultat
  que le relevé indépendant du matin (2 282,2 / 362,4 / 215,7 Md€).
- Page FR et EN : écrites (09/11/2026), `content/dette-publique-quels-futurs/_index.md` et `_index.en.md`
  (`/en/public-debt-what-futures/`, slug confirmé). Architecture A+ arbitrée : trajectoire (éventail, résultat en une
  phrase, promesse 2024 contre prévision 2026 et point de départ), leviers (figure, solde comptable, taux lus à partir
  de la deuxième année, croissance ; méthode en repli), matrice (shortcode `futurs-matrice` : neuf fiches, analyse en
  repli, ancres `#op-<clé>`), constats (découverte provisoire en tête), limites, hypothèse de l'auteur en encadré séparé
  (`canonical-definition`), synthèse, FAQ (3), pastilles, livre (`appel-livre`, surtitre « Les quatre scénarios,
  racontés sur dix ans », `avis="non"`), sources, Réutiliser. Organes ajoutés : `futurs-val`, jetons `{futurs.*}` dans
  `desc-figures.html`, `_dette-futurs.scss`, `data/figures_futurs.json` (fiches lues dans les SVG), carte de partage et
  vignette (`og_dossier_dette.py --futurs`, contraste contrôlé), sixième onglet (`data/dossier_dette.yaml`,
  `dossier-dette.html` : volet `futurs`, six volets exigés). Gardes de prose nouvelles dans `affichage()` (moitié basse
  de l'éventail, promesse sous le 10e centile, rang dépendant du départ, promesse 2027 dépassée, probabilité > 90 %,
  sens des sensibilités). Contrôles : build sans erreur, `typo_build` 0, `check-all --ci` 0,
  `check-rendu-ressources` conforme, `audit-liens-build` 0 critique, `check-dates-build` 0. Barre à six onglets :
  rangée naturelle 1 064 px (936 à cinq) ; bascule vers les libellés courts assurée par le script de la barre, vérifiée
  à 1 100 / 1 050 / 1 000 / 970 px ; seuil CSS commun (968 px) inchangé, motif dans `_reutiliser.scss`. Rendu bureau
  regardé (fiches, replis, ancre sous la barre collante).
  Non fait (phase B, à suivre) : recette 320-1600 (Chrome ne descend pas sous sa largeur minimale), deux contrôleurs
  indépendants des figures, panel après, gate éditorial, relecture phrase à phrase FR et EN du texte servi et
  instantané (`check-relecture` bloquera le déploiement sans lui), confrontation à la recherche, raccords réciproques
  (phrase en fin de « Peut-elle baisser ? », FAQ « engrenage » de « Qui paie », formules du débat), fiche D0 à la
  feuille de route, contre-expertise de la page, accord de l'auteur.
- Recette 320 / 390 / 768 / 1 280 / 1 600 px, FR et EN : FAITE (09/11/2026, Playwright sans interface sur le serveur
  local). Aucun débordement horizontal ; 21 ancres par page, aucune sous la barre collante ; 25 tabulations, aucun focus
  invisible ou sans contour ; aucune erreur de console ni ressource en échec ; figures chargées après défilement (chargement
  différé). Page entière regardée à 320 px, haut à 1 000 px (libellés courts et « Plus » sur une rangée). Deux fausses
  alertes écartées : apostrophes droites du serveur local (redressées par `typo_build.py` au build, 0 défaut) ; éléments
  hors cadre à 1 280 px = panneau « Plus » de la barre, identique sur les autres volets.
- Contrôle des figures (skill `controle-figures`) : FAIT, deux contrôleurs indépendants en quatre passages, jusqu'à zéro
  défaut nouveau (dernier passage : un cosmétique par contrôleur, corrigés et vérifiés). Trouvé et corrigé :
  **double arrondi** des sensibilités (« 6,0 » imprimé pour 5,947 dans la figure, la page et la matrice ; `sensibilites()`
  rend désormais les valeurs brutes, `sens_ecrit()` arrondit à l'écriture) ; contresens anglais (« no effect on growth ») ;
  formule ambiguë du solde (« un point de plus chaque année » → « solde primaire supérieur d'un point de PIB chaque
  année », figure, page et matrice) ; « sans effet de l'ajustement » dans la matrice FR ; prévision du PLF en trait plein
  (charte : tirets ; carte de partage comprise) ; clé des couleurs, signes +, valeurs au bout des barres, grille sous les
  barres ; bandes, départs 2025 et absence de valeur 2026 de l'engagement dits en note ; un seul nom par trajectoire
  (« Commission, politique inchangée », « Prévision du PLF 2027 », « Engagement d'octobre 2024 ») ; libellés décollés
  de l'axe et des grilles ; libellé de la Commission en trois lignes (au bord du cadre en gras) ; téléphone : marques des
  points, graduations, échantillons de trait, valeur 2035 hors graphique ; texte alternatif sans nombre saisi et exact ;
  « percentile » dans la page anglaise ; « ni … ni » agrammatical. Organe commun `pied_figure.coupe` : nombre + point(s)/pb,
  sigle + année, année + draft/commitment/plan/budget, mois français + année soudés (273 figures du site : 0 défaut).
  Témoin source relu sans filtre par les contrôleurs (DSM 2025 xlsx, PLF 2027 p. 5, PSMT). Limites déclarées : les
  sensibilités de taux n'ont pas de témoin extérieur hors ceux du générateur ; le séparateur « · » qui passe à la ligne avec
  le mot suivant est la règle du site (04/11), non rouverte ; les autres générateurs bénéficieront des nouvelles soudures à
  leur prochaine régénération (aucune figure publiée régénérée ici).
- Panel « après » (consigne `CONSIGNE_PANEL_RESSOURCE.md` mot pour mot, cinq lecteurs isolés, texte servi) et gate
  éditorial : FAITS (09/11/2026), détail et tableaux dans
  `D:\PRO_PROMOTION\RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\PANEL_ET_GATE_PAGE_2026-11-09.md`. Constat : la première
  section (« Lire l'éventail », rang en variation) arrêtait ou perdait trois des quatre lecteurs non spécialistes ; le
  connaisseur y voyait l'apport le plus original. Gate v1 : clarté et progression partielles (P1). Corrigé : phrase utile
  d'abord, rang en variation en repli sur la même URL, centile glosé par jeton, « promesse » → « engagement », Commission
  située (« qui parle et d'où »), « en l'état des traités », mécanisme taux-croissance, renvoi à « Qui gagne, qui paie »,
  fiche 2 réécrite, « émissions » → « nouveaux emprunts de l'État », badges de robustesse dédoublonnés. Panel de contrôle
  (Thomas, Julien) : Thomas répond juste aux trois questions de compréhension. Gate franchi (aucun P0, P1 traité).
- Pièce Dette-10 (contradicteur, 09/11/2026, SHA-256 `83d8ddac…0404`) : ARBITRÉE
  (`D:\PRO\.claude\external-audits\ARBITRATIONS\ENTRANTE_2026-11-09_Dette-10_arbitrage.md`). Chapô corrigé (il présumait
  que toute opération déplace le coût, contre les issues de la matrice ; la synthèse et le résumé aussi) ; fiche 8 complétée
  par l'estimation de la DG Trésor (3,5 à 5,5 Md€, Sénat, rapport n° 760 du 17/06/2026, lu sur senat.fr et archivé
  `42802bfb…`) ; « dans 80 % des simulations » ; identité taux-croissance précisée ; avis du Conseil d'État n° 410182 inscrit
  « non lu ». Gate de publication à valider sur la version finale.
- Relecture phrase à phrase FR et EN du texte servi (build `hugo --minify` + `typo_build`) : FAITE (09/11/2026). Corrigé,
  entre autres : « mesures qu'il n'a pas toutes votées » (le Gouvernement ne vote pas) ; « nouveaux emprunts de l'État » →
  « publics » (périmètre des administrations publiques) ; « investissement emprunté » sans « chaque année » ; deux
  deux-points dans une phrase ; pronoms ambigus de la fiche 1 ; « Non établie » ; « Un ratio n'est pas un bien-être » ;
  anglais calqué (« would be neutral », « has already known », « unestablished », « does not tell ») ; **sources de la
  matrice en français sur la page anglaise** → `sources_en` obligatoire par fiche, de même longueur (garde vue mordre :
  « sortie_euro : sources_en absente ou de longueur différente ») ; « les fiches concernées le disent » rendu vrai pour
  l'avis du Conseil d'État (fiche 8, droit). Instantanés écrits : `docs/relectures/dette-publique-quels-futurs.txt` (407
  phrases) et `en__public-debt-what-futures.txt` (399).
- Contre-expertise de la page construite : FAITE (PRO-20261109-135050, réponse archivée `5E6EEBF5…` avant lecture) et
  ARBITRÉE (`ARBITRATIONS\PRO-20261109-135050_arbitrage.md`). Verdict : publiable après corrections, liste fermée appliquée
  FR et EN : « parce que » causal du 20e centile retiré ; projection / prévision / sensibilité distinguées (limites et
  résumé) ; synthèse chiffrée avec le sens des variations ; « hors ajustements flux-stock » ; FAQ des clauses d'action
  collective alignée sur l'art. D. 213-25-13 ; « peut aussi changer qui décide », « principalement des institutions
  françaises, sous surveillance européenne » ; ordre « de la plus courante à la plus rare » retiré ; « la matrice examine
  les conditions juridiques connues » ; observatoire nommé. Non retenu : titre anglais (facultatif). Contrôles à 0,
  instantanés de relecture réécrits.
- Pièce Dette-11 (clôture de la contre-expertise, SHA-256 `0f301de8…a11a4`) : ARBITRÉE
  (`ARBITRATIONS\ENTRANTE_2026-11-09_Dette-11_arbitrage.md`). Quorum des clauses d'action collective lu sur Légifrance
  (art. D. 213-25-12 : deux tiers du principal en circulation pour une modification substantielle), archivé `c5bae69e…` ;
  FAQ FR/EN et fiche 7 complétées. Le contradicteur clôt les itérations : GO sous réserve de l'accord de l'auteur, des
  raccords, de la fiche D0 et du diff.
- Raccords réciproques : FAITS (09/11/2026, FR et EN). « Peut-elle baisser ? » : phrase de fin de synthèse (« Ce que
  changeraient ici, d'ici 2035, … est l'objet de … ») et pastille ; « Qui paie », FAQ « engrenage » : renvoi en clair (le
  champ de FAQ ne rend pas de lien) et « déplacent la charge » nuancé en « ne font pas porter la charge aux mêmes groupes »
  (cohérence avec la pièce Dette-10) ; décision déléguée par l'auteur (« arbitre au profit de la clarté et la fluidité ») ;
  section annulation non touchée ; « Formules du débat » : suite de la phrase sur la baisse. Écartés avec motif :
  comparaison internationale, inflation, générations futures (voir « Raccords »). Instantanés réécrits pour « Formules du
  débat » FR/EN (seule phrase changée) ; non réécrits pour « Peut-elle baisser ? » : onze des douze phrases changées y
  viennent d'une autre session (Cour des comptes), relecture à faire par elle (alerte non bloquante).
- Fiche D0 : ÉCRITE dans `06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` (09/11/2026, avant publication).
- Publication : `d92acb8` poussé le 09/11/2026 ; déploiement Pages réussi par le commit vide `fde159c` après trois échecs
  côté GitHub ; version servie attestée (texte, CSV et PNG identiques, SVG identiques en nombres et en textes).
- Pièces Dette-12 (revue éditoriale de la page publiée, `de1ff828…7331`) et Dette-13 (avis sur la maquette,
  `f09a7b9d…2006`) : ARBITRÉES (`ARBITRATIONS\ENTRANTE_2026-11-09_Dette-12_arbitrage.md` et `…Dette-13…`), maquette
  `06_PROMOTION\RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\MAQUETTE_DETTE-12_2026-11-09.html`. APPLIQUÉ (FR et EN) :
  - carte d'entrée « Trois questions pour examiner chaque opération » ;
  - « Le résultat en une phrase » ramené à une phrase, le rang du Gouvernement et sa réserve passés en tête de « Lire
    l'éventail » ;
  - légende de l'éventail : les points de départ différents ;
  - figure des leviers : parenthèse « financement commun » retirée, quatre versions régénérées, `check-figures` à 0,
    rendus regardés ;
  - matrice : trois familles en H3 et opérations en H4 (impôt passé en 2, ancres inchangées, garde des familles vue
    mordre), issue provisoire en tête de fiche au style neutre, statuts plus contrastés ;
  - premier niveau de l'impôt et de la règle d'or : le fait du désaccord et sa nature, les estimations et études dans le
    repli, sous le champ nouveau « Les estimations publiées » ;
  - mutualisation : quatre instruments en liste ; sortie de l'euro : les questions qui décideraient ;
  - tableau « Cinq distinctions pour comprendre ces opérations » ;
  - contrôles : `check-all --ci` 0, témoins 5/5, build, `typo_build` 0, rendu, dates, liens ; recette à 1280 et 390 px
    (FR, EN, aucun débordement) ; phrases modifiées relues sur le texte servi ; instantanés réécrits.

  Le chantier éditorial est clos (Dette-13, point 9).
- Gardes vues mordre, figures téléphone, relecture de langue, recette 320-1600, panel après, gate éditorial, relecture
  phrase à phrase FR et EN, instantané de relecture, contre-expertise de la page, accord de l'auteur : non fait (phase B,
  après l'arbitrage).
