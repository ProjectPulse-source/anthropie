# Fiche de conception — Qui peut faire face à une dépense imprévue ?

<!-- Page de données née de l'arbitrage PRO-20261026-033434 (graphe G1, scénario S2 : page de faits distincte, reliée à
la notion de réversibilité sociale par une phrase) et du comité de lecteurs du même jour. Fiche écrite AVANT le texte
de la page, après le test décisif sur les données (relevé direct de l'API Eurostat, 26/10/2026). -->

Page : `/qui-peut-faire-face-a-une-depense-imprevue/` (FR) · `/en/who-can-cope-with-an-unexpected-expense/` (EN) ·
ouverte le 2026-10-26

## Forme

`quantitatif` : une série officielle (Eurostat, enquête SILC, jeu `ilc_mdes04`), relevée par un générateur, modèle
complet des pages de données (jetons, gardes vues mordre, JSON et CSV, figure SVG et PNG avec version téléphone, carte de
partage et vignette, `Dataset`, « Réutiliser », mise à jour au calendrier de la source). Critères : définitions et
périmètres (personnes, non ménages ; seuil de 60 % du revenu médian équivalent ; « dépense imprévue » au sens de
l'enquête), millésimes (année d'enquête), dénominateurs, changements de série (UE à 27 depuis 2010 seulement), aucune
lecture anthropique dans l'exposé des constats (décision verrouillée).

## Fiche de conception

### Question centrale

Qui, en France, ne pourrait pas faire face à une dépense imprévue — et le revenu suffit-il à le dire ?

### Enjeu

Les politiques sociales et le débat public classent les ménages par le revenu (pauvres ou non). Si la capacité d'encaisser
un choc dépend aussi, fortement, de la composition du foyer, une partie des personnes vulnérables échappe à ce classement.

### Croyance initiale

Ne pas pouvoir faire face à une dépense imprévue, c'est être pauvre ; au-dessus du seuil de pauvreté, on s'en sort.

### Découverte principale

Au-dessus du seuil de pauvreté, être le seul adulte d'un foyer avec enfants va de pair avec une vulnérabilité au choc
nettement plus forte : en France en 2025, 46,9 % des ménages d'un adulte avec enfants dépendants au-dessus du seuil ne pourraient pas faire face à une
dépense imprévue, contre 18,6 % des ménages de deux adultes avec un enfant dépendant (catégories d'Eurostat : R1-5, R2-8) (chiffres à afficher par jetons, jamais saisis).

### Mécanisme explicatif

Un seul revenu et un seul filet (épargne, entourage, second salaire) pour un foyer qui porte des charges d'enfants : le
seuil de pauvreté, calculé sur un revenu par unité de consommation, ne dit rien de la réserve disponible ni du nombre
d'adultes qui pourraient la reconstituer. Mécanisme proposé, non mesuré par la série : la page le dit. Relecture R1-2 : la position juste au-dessus du seuil est documentée par Eurostat (ilc_li03 : 22,8 % contre 4,9 %) ; « le revenu ne dit pas tout » se restreint à la position au seuil (IM-1, à arbitrer). Relecture des sources du 12/11/2026 : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\SOURCES\qui-peut-faire-face-a-une-depense-imprevue_SYNTHESE.md`.

### Preuve décisive

Le témoin à une seule variable : à présence d'enfants constante, le passage de deux adultes à un seul ajoute de 21 à 29
points (France, 2015-2025, au-dessus du seuil) ; sans enfants, le même passage n'en ajoute que 9 à 13. Même ordre dans
l'UE à 27 (20 à 24 contre 10 à 11). La lecture tient chaque année de la série.

### Pouvoir discriminant

- **Explications rivales réellement soutenues.** (a) La vulnérabilité au choc est d'abord une affaire de revenu : c'est la
  lecture implicite des indicateurs de pauvreté monétaire. (b) La composition du foyer pèse en elle-même, au-delà du
  revenu par unité de consommation (travaux de l'Insee et de la Drees sur les familles monoparentales : à lire et citer
  avant publication, NON_VERIFIE à ce jour).
- **Témoin à une variable.** Parent seul contre couple avec un enfant (le nombre d'adultes change, la présence d'enfants
  reste) ; adulte seul contre couple sans enfant (même changement, sans enfants) ; le tout de chaque côté du seuil.
- **Que révèle le graphe qu'une série isolée ne montre pas ?** Que l'écart lié à la composition est le plus grand
  au-dessus du seuil, là où le classement par le revenu dit « pas pauvre ».
- **Quelles explications départage-t-il ?** Il dément (a) prise seule : à revenu relatif du même côté du seuil, la
  composition change fortement la part exposée. Il ne départage pas (b) d'une troisième lecture : les parents seuls
  au-dessus du seuil pourraient être plus proches du seuil que les couples (position dans la tranche) ; le jeu ne
  ventile pas par décile. La page l'écrit au contact du chiffre.
- **Une variable, à une nuance près.** La catégorie d'Eurostat « un adulte avec enfants dépendants » compte un enfant ou plus ;
  la variante « couple avec deux enfants » (écart maintenu) montre que le nombre d'enfants ne suffit pas à expliquer l'écart.
  La page le dit au lieu d'annoncer des foyers qui « ne diffèrent que d'une chose » (relecture du 26/10/2026).
- **Robustesse, montrée par une variante calculée.** Chaque année de 2015 à 2025 (et depuis 2004 pour l'écart principal),
  France et UE à 27 ; couple avec un enfant et couple avec deux enfants.
- **Levier ou risque éclairé.** Un ciblage des aides par le seul revenu laisse de côté une part des foyers où un seul
  adulte porte les charges ; la page le dit comme question, sans recommander une politique.

### Limite

Déclaratif (« le ménage pourrait-il faire face… ») ; un indicateur de la capacité financière d'absorber un choc, une
seule part de ce que l'auteur appelle « réversibilité sociale » (ni le tarif de l'échec, ni la réadmission) ;
association, non cause ; montant de la dépense imprévue fixé par pays dans l'enquête ; personnes, non ménages.

### Valeur finale

Un chiffre citable et sourcé, un graphe qui montre ce que le classement par le revenu ne montre pas, et la question qui
reste ouverte (la position dans la tranche de revenu).

### Singularité

Cette page existe parce qu'elle croise seuil de pauvreté et composition du foyer en ne changeant qu'une variable, ce que
le lecteur ne trouve pas, à notre connaissance, dans les publications d'Eurostat et de l'Insee sur l'indicateur
(recherche du 26/10/2026 : Eurostat publie la part des personnes seules avec enfants, 56 % en 2019, communiqué du
05/05/2020, et l'Observatoire des inégalités 56 % des familles monoparentales, tous deux sans le seuil de pauvreté ;
aucun croisement trouvé — une recherche n'est pas exhaustive ; à revoir si une publication le donne). Apport d'analyse
ajouté après la seconde réponse de PRO-20261026-045248 : la question française porte sur 1 000 €, environ 17 % sous le
douzième du seuil que fixe la règle d'Eurostat (1 209 € pour l'enquête 2025) ; le niveau français se compare donc aux
autres pays sur une question plus facile. Niveau atteint par la figure : descriptive, discriminante en partie (elle
écarte « le revenu suffit », n'isole pas l'effet de la composition du foyer) ; pas décisionnelle.

### Raccords

- Définition de l'anthropie — écartée du corps de la page (page de faits, décision verrouillée) ; la notion de
  réversibilité sociale renvoie à cette page par une phrase, et non l'inverse dans l'exposé des constats.
- Livre — retenu : *La Société du premier coup* (inégalités et possibilités de recommencer), appel en fin de page,
  `ressource.livres`.
- Working paper — retenu dans un bloc séparé : AWP-08, qui propose la capacité de repli comme une composante de la
  réversibilité sociale (hypothèse de l'auteur, « non testée ici »).
- Pages voisines — `/reversibilite-sociale/` (phrase de renvoi ajoutée dans la notion) ; `/premier-coup/`.

## Fiche D0

Résultat visé au plus près de la finalité : la page citée pour son croisement (enseignants, presse, chercheurs) et lue
jusqu'à la limite. Diagnostics : vues, sources d'arrivée, citations ; test de compréhension par trois lecteurs réels
(décision D2). État initial : page nouvelle, aucune vue ; relevé au J+60 de l'architecture des ressources.

## Étapes de la méthode

- Plan d'outils : fait le 26/10/2026 (méthode, LanguageTool, recette, séries statistiques).
- Protocole du type `quantitatif` : fait — définitions (personnes, seuil, déclaratif), millésime affiché, ruptures de
  série lues dans les drapeaux d'Eurostat (France 2020 et 2022) et citées par jeton, aucune lecture anthropique dans les
  constats (hypothèse de l'auteur dans un encadré séparé).
- Scénarios d'architecture : tranché par l'arbitrage PRO-20261026-033434 (S2, page distincte, renvoi depuis la notion).
- Panel avant : comité de lecteurs simulés du 26/10/2026 (D1, D2, témoin à une variable).
- Contre-expertise de phase A : faite (PRO-20261026-033434, arbitrée).
- Gardes vues mordre : faites — 12 gardes de prose et 1 bande de plausibilité, chacune mutée
  (`--mutation=total|dessus|dessous|ratio|ecarts|chaque|serre|ue|deux|majorite|rupture|annee`), toutes ont mordu.
- Figures téléphone : faites — versions `-m` recomposées, parité contrôlée par `pied_figure.parite`, hauteurs déclarées
  dans les deux pages contrôlées par le générateur.
- Relecture de langue : faite (LanguageTool FR et EN sur le texte servi ; signalements tranchés : accords justes,
  artefact d'extraction, titre français, orthographe britannique).
- Recette 320-1280 : faite (`recette.py`, 12/12) après correction du composant « Réutiliser » (marge de défilement des
  ancres intérieures, 1,5rem → 5rem, pour toutes les pages).
- Gate éditorial — **auto-évaluation, non indépendante** : exactitude *tenu* (gardes, témoin, limite au contact du
  chiffre) ; clarté *tenu* ; accroche *tenu* (question et contre-intuition en chapô) ; progression *tenu* (constat →
  test → Europe → limites) ; originalité *partiel* (croisement non trouvé publié, recherche non exhaustive) ; valeur
  finale *tenu* (chiffre citable, question ouverte). Cinq fonctions remplies ; aucun bloc sans apport repéré.
- Relecture phrase à phrase FR et EN du texte servi : faite le 26/10/2026 ; six corrections (nuance « une variable »,
  nombre d'enfants, bandeau des années, pronom, redondance, « as high »).
- Instantané de relecture : fait (`docs/relectures/`, FR 99 phrases, EN 92).
- Test de compréhension par trois lecteurs réels (D2) : non fait (recrutement par l'auteur).
- Contre-expertise de la page : faite (PRO-20261026-045248, arbitrée le 26/10/2026, `ARBITRATIONS\PRO-20261026-045248_arbitrage.md`) ;
  corrections : écart en points dans le résultat, association et facteurs concurrents écrits, « personnes, non ménages »,
  garde `peu_fiables` (drapeau « u » d'Eurostat) vue mordre ; recette 12/12 et LanguageTool refaits. Restent ouverts :
  définition Eurostat du montant (vérifiée depuis : ligne suivante), test par de vrais lecteurs (auteur).
- Seconde réponse de la contre-expertise (26/10/2026) : arbitrée. Montant de la question (1 000 €, Insee) et règle
  d'Eurostat (HS060, p. 154) lus à la source ; seuil `ilc_li01` lu par le générateur ; gardes `montant` et `enquete` vues
  mordre (15 gardes) ; limite sur les drapeaux complétée ; phrase de méthode de la FAQ corrigée ; page datée au fond.
- Accord de l'auteur : demandé avec le diff du 26/10/2026.

## Test de compréhension simulé (26/10/2026)

Demandé par l'auteur. Trois lecteurs simulés, isolés, recevant le seul texte servi de la page (figures décrites par leur
texte alternatif) et les questions de la décision D2 ; aucun ne connaissait les réponses attendues. Limite : un lecteur
simulé partage les présupposés du modèle qui l'écrit ; ce test ne remplace pas les trois lecteurs réels (D2, ouvert).

| Lecteur | Ce que montre le graphe | Ce qu'il ne montre pas | Question ouverte | Contresens |
|---|---|---|---|---|
| Professeure de SES, lecture attentive | juste (46,9 contre 18,6 au-dessus du seuil ; majorité exposée en dessous) | juste (association, déclaratif, personnes et non ménages) | juste (position dans la tranche) | aucun |
| Artisan, lecture rapide | juste | juste (« ça va ensemble, c'est tout ») | juste | aucun ; amplification mineure : « une **grosse** facture surprise » (la page ne donne pas le montant) |
| Journaliste économique | juste | juste | juste (« microdonnées, ou découpage par déciles ») | aucun ; phrase publiable exacte, avec source |

Décision : aucune correction de fond. Le montant de la dépense imprévue n'est pas donné (définition non vérifiée à la
source) ; à préciser si la définition d'Eurostat est lue.

### Reprise du lot « guides » (12/11/2026)

Méthode `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\METHODE_REPRISE_RESSOURCE.md` ; dossier `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\` (rapport
`RAPPORTS\qui-peut-faire-face-a-une-depense-imprevue.md`, état `LOT.md`).

- Relecture des sources : faite le 12/11/2026, deux relecteurs indépendants et les sondes de la session
  (`SOURCES\qui-peut-faire-face-a-une-depense-imprevue_R1.md`, `_R2.md`, `_SYNTHESE.md`, `SONDES_SESSION.md`) : « le revenu
  ne dit pas tout » corrigé (seule la position au seuil est montrée insuffisante) ; catégories d'Eurostat rendues exactes
  (un adulte avec un ou plusieurs enfants dépendants, deux adultes avec un enfant, couple ou non) ; position juste au-dessus du
  seuil documentée par Eurostat (`ilc_li03`), non exploitée (point ouvert).
- Interventions : `specs\qui-peut-faire-face-a-une-depense-imprevue.py`, 153 remplacements (FR et EN), dont trois
  explications (IM-1a, IM-1b, IM-1e) tranchées par le contradicteur externe en faveur de la version proposée ; témoin : la
  spécification appliquée à la page d'origine (`c2b25c2`) redonne cette page, en-tête de publication, sujet du jeu de données
  et organe de forme (`figure-lecture`) à part.
- Contradicteur externe `PRO-20261112-140721` (réponse archivée avant lecture, SHA-256 `A71FAC4D…`) : version proposée
  retenue sauf le passage 13 ; décisions 20 à 25 appliquées. Décisions de l'auteur du 12/11/2026 : « capacité individuelle de
  repli » gardée (terme d'AWP-08), l'indicateur, fondé sur la déclaration du ménage, n'en saisissant que le volet financier ;
  « Deux explications, un test » remplacé par la réécriture du contradicteur (« Ce que la comparaison permet — et ne permet
  pas — de dire »), nombres repris des jetons. Aussi : « le nombre d'enfants ne suffit pas à expliquer l'écart » corrigé (les
  catégories ne mesurent pas l'effet du nombre d'enfants) ; réserve de causalité en tête de la réponse de FAQ ; « le lien
  avec le revenu est fort » remplacé par l'écart de part et d'autre du seuil.
- Générateur (`scripts/update_menages_imprevu.py`) : titre du contradicteur ; note (déclaration du ménage, montant, « un
  adulte avec enfants » = un ou plusieurs enfants, groupes non comparés à revenu égal) ; description intégrée et texte
  réutilisable avec la réserve ; « Un adulte sans enfant » ; accolade sans « + » et décalée ; colonne des libellés élargie
  (« Deux adultes sans enfant » était mordu par sa barre dans le PNG, sans alerte du verrou) ; garde « chaque année … deux à
  trois fois » étendue à toutes les années de la fenêtre (elle ne testait que la dernière ; témoin `--mutation=ecarts_debut`
  vu mordre). Carte (`scripts/og_imprevu_menages.py`) : sujet dans le titre, même nom de barre que la figure, légende en
  personnes, « association, non cause, pas à revenu égal », orange du texte de la charte, garde d'échelle de 0 à 60 %.
- Figure : `check-figures` 0 défaut ; contrôleur de géométrie et de données (API d'Eurostat relue : 684 cellules identiques
  au jeu) et contrôleur de lecture, puis un passage sur l'état corrigé (trois cosmétiques nouveaux, corrigés) ; troisième
  passage : aucun défaut nouveau sur la figure, les cartes et la page ; un constat d'outillage (le témoin d'une garde
  masqué par la garde élargie), corrigé et vu mordre (`JUGE\FIGURE_DEPENSE_CONTROLE_{GEOMETRIE,LECTURE,2,3}.md`).
- Relecture de langue phrase à phrase du texte servi, FR (124 phrases : 2 fautes, 21 maladresses) et EN (118 : 5 erreurs,
  25 maladresses) : corrigées. Points de fond tranchés au passage : fourchettes annuelles écrites comme telles ; groupe
  européen exact ; « non un effet mesuré de la composition du foyer » (« non un effet isolé » inversait la réserve) ; FAQ
  lue seule (pays, année, montant) ; « peut dépendre du montant demandé » ; « foyer monoparental » nommé comme le terme de la
  page, non d'Eurostat ; « aides sociales reçues ». Relecture de contrôle des phrases changées
  (`JUGE\RELECTURE_LANGUE_DEPENSE_CONTROLE.md`) : deux défauts nécessaires (apostrophe de la carte, réserve de la
  description intégrée), corrigés.
- Données structurées : sujet du jeu de données déclaré (`apropos`). Dates : le 07/11/2026 ajouté à l'historique des dates
  de la page (`data/dates_affichage.json`), l'entrée du journal de ce jour étant une modification de fond.
- Contrôles : `check-all --ci` 0 ; build et `typo_build` 0 défaut ; rendu 0 ; liens 0 critique ; dates 83/83, 0 bloc sans
  période ; couverture : 15 signaux, aucun nouveau.
- Envois : la page est citée par deux courriels non partis de la campagne ANTHROPY-EN (LOT5, Lusardi ; LOT6, Nieuwenhuis) ;
  leur texte est mis en cohérence avec la page publiée (décision de l'auteur du 12/11/2026), réapprobation des lots par
  l'auteur.
- Instantané de relecture : fait le 12/11/2026 (125 phrases FR, 119 EN) ; `refonte` porté au 12/11/2026 ; journal : entrée du 12/11/2026.
- Mise en ligne : poussée sur le mandat de l'auteur, le 12/11/2026 (commit d76e866) ; déploiement `hugo.yml`
  n° 43292354304 réussi (build, relecture, deploy, contrôle de fumée de la production).
- Attestation de la version servie : faite le 12/11/2026 vers 20 h 41 (heure de Paris). HTML servi identique au build
  contrôlé (arbre propre extrait de l'index), aux empreintes de cache des feuilles et scripts près, en FR et en EN ; les
  quatre SVG de la figure, le PNG du bureau, les deux cartes de partage et leurs vignettes, le JSON et le CSV servis
  identiques, octet pour octet, au commit.
- Laissés à l'auteur : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\A_ARBITRER.md`.

### Reprise du style (13/11/2026)

- Consigne de l'auteur (13/11/2026) : une mise en page « ultra lisible », au niveau de la page Parcoursup (règle 17
  du `CLAUDE.md` du site), adaptée au sujet. Étude, choix et mesures :
  `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\ETUDE_STYLE.md`. Organes existants seulement
  (`_ressource-relief.scss`, `reperes-page.html`) ; les phrases ne changent pas, elles prennent une forme.
- Organes : trois repères (28,8 % ; 65,9 % sous le seuil contre 21,6 % au-dessus ; 46,9 % contre 18,6 %, dans les deux
  cas au-dessus du seuil, avec la réserve de la page sur les deux groupes) ; grille « environ deux tiers » / « environ une
  sur cinq » de part et d'autre du seuil, barres sur une même échelle (même indicateur, même année) ; deux paragraphes
  coupés. Pas de repère européen (montant de la question française plus bas). `imp-val` reçoit la variante « css » de
  `psup-val`.
- Inchangés : titre, adresse, ancres, chapô, figures, nombres, réserves, questions fréquentes, sources, « Réutiliser ».
  Aucune modification de fond : `lastmod`, journal et `data/dates_affichage.json` inchangés ; `refonte` reste au
  12/11/2026 (instantané du 13/11, postérieur).
- Contrôles : `check-all --ci` 19/19 à 0 ; build CI et `typo_build` 0 défaut ; liens 0 critique ; rendu 0 ; dates 83/83,
  0 bloc sans période ; 0 débordement sur onze largeurs de 320 à 1 440 px, avec et sans JavaScript ; aucun texte des
  blocs sous 12 px ; repères absents sous 600 px ; lecture à côté de la figure dans la limite. Lettre : texte servi avant
  et après, phrase à phrase ; seules changent les phrases mises en forme ; nombres inchangés. Langue et fidélité : la
  session, puis un relecteur indépendant (aucun P0 ; P1 traités). Premier écran : deux tours de lecteurs neufs (FR, EN) et un témoin trompeur vu mordre
  (`LOTS\guides\P\premier_ecran_style.md`) ; constats sur le chapô, inchangé : `LOTS\guides\A_ARBITRER.md`.
- Instantané de relecture refait le 13/11/2026.
