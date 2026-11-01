# Fiche de conception — Combien de temps une erreur reste-t-elle inscrite ?

Page : `/combien-de-temps-une-erreur-reste-inscrite/` (FR) · pas de version anglaise (exclusion déclarée : droit français, et
*La Société du premier coup* n'existe qu'en français) · ouverte le 2026-11-01

Programme « sujets → livres », matrice sujet → livre (`06_PROMOTION/PLAN_SUJETS_LIVRES_2026-11/MATRICE_SUJET_LIVRE.md`,
§ 3, vague 1) ; commande de l'auteur du 01/11/2026 (« fais la page effacement des erreurs »).

## Forme

`juridique-institutionnel`, avec ses critères :
- distinguer qui inscrit, qui consulte, qui efface, et dans quel délai ;
- références datées, lues dans la version en vigueur, avec leurs conditions et exceptions ;
- changements déjà publiés et à venir signalés (FICP au 20/11/2026 ; casier au 01/01/2029) ;
- aucun jeu de données fabriqué : les durées sont des règles, non des séries.

## Fiche de conception

### Question centrale

Combien de temps une erreur — un crédit impayé, un chèque sans provision, une condamnation, une infraction routière, un
accident responsable, une maladie — reste-t-elle inscrite, et qu'est-ce qui l'efface ?

### Enjeu

La question est d'abord pratique : quelqu'un fiché à la Banque de France, condamné, ou qui a perdu des points veut savoir
quand la porte se rouvre. Elle est aussi celle de *La Société du premier coup* : le coût d'une erreur dépend moins de
l'erreur que du temps pendant lequel elle reste lisible par ceux qui décident d'un prêt, d'un emploi ou d'un contrat.

### Croyance initiale

Une erreur réparée — dette payée, peine exécutée, maladie guérie — cesse aussitôt de compter. Ou, à l'inverse, un fichage
« suit à vie ».

### Découverte principale

Les durées vont de six mois (un point de permis) à quarante ans (le bulletin n° 1 du casier). Surtout, ce qui efface
n'est pas le temps seul, et l'effacement s'obtient de quatre manières différentes :
- automatiquement : réhabilitation légale, points, malus, droit à l'oubli ;
- sur démarche de la personne : justifier la régularisation d'un chèque, demander l'exclusion d'une mention du B2,
  demander un déréférencement ;
- par un tiers : la radiation du FICP dépend de la déclaration du créancier ;
- ou collectivement, d'un trait : l'indicateur « 040 » des dirigeants, supprimé par décret en 2013.

Le même registre oublie aussi à des vitesses différentes selon le sens. Un malus revient au plus à 1 après deux ans sans
sinistre ; le bonus maximal demande treize ans ; le relevé d'informations garde cinq ans de sinistres.

### Mécanisme explicatif

La durée d'une trace est fixée par un texte, pour un usage (protéger un prêteur, un employeur, des mineurs, un assureur).
Elle se mesure donc à ce qu'elle protège encore, non à la gravité initiale seule. C'est la thèse du chapitre 5 du livre
(« la durée d'une trace n'est pas une propriété de l'échec. C'est un choix »), que la page expose comme thèse, après les
règles.

### Preuve décisive

Les textes en vigueur, lus sur Légifrance le 01/11/2026 (outil `sources`, versions et dates de chaque article) :
- C. consom., L. 752-1 (version jusqu'au 19/11/2026 et version du 20/11/2026) et L. 752-3 ;
- CMF, L. 131-73 et L. 131-78 ;
- C. pén., art. 133-13 (version en vigueur jusqu'au 31/12/2028) et 133-16 ;
- CPP, art. 769 et 775-1 (version du 20/08/2026) ;
- C. route, L. 223-6 ;
- C. assur., A. 121-1-1 et annexe à A. 121-1 (version du 24/07/2025, art. 4, 5, 12) ;
- CSP, L. 1141-5 ;
- décret n° 2013-799 ;
- Service-public F14710 (bulletins du casier, vérifiée le 20/08/2026) et F31802 (effacement, vérifiée le 20/10/2025).

### Pouvoir discriminant

Sans objet (page sans série).

### Limite

La page décrit des règles générales, sans conseil juridique. Les points de départ des délais et les exceptions
(récidive, infractions de l'art. 706-47 CPP, peines complémentaires définitives) sont résumés. Les fichiers privés
(assureurs, bailleurs, opérateurs) ne sont pas couverts. Les versions des articles du casier publiées pour le 01/01/2029
ne sont pas décrites.

### Valeur finale

Le lecteur sait, pour chaque registre, combien de temps l'inscription dure au plus, ce qui l'efface plus tôt, et s'il doit
agir lui-même. Il peut vérifier chaque règle dans son texte.

### Singularité

Cette page met côte à côte des durées que les sources officielles et les sites pratiques donnent une par une, chacune
sur sa page (Service-public : une fiche par registre). Elle les compare par la manière d'effacer, automatique, sur
démarche, par un tiers ou collective, et par l'asymétrie bonus-malus. Elle signale le changement du FICP au 20/11/2026.
Témoin lu le 01/11/2026 : les fiches Service-public F14710, F31802 et F2655 traitent chacune un registre et ne comparent
pas les durées entre eux.

### Raccords

- Définition de l'anthropie : écartée (page de faits juridiques ; aucune lecture anthropique dans l'exposé, règle 4).
- Livre : *La Société du premier coup*, retenu. Le chapitre 5 (« La trace ») et le chapitre 8 (« Les erreurs qui
  disparaissent ») sont exposés comme la lecture du livre, après les règles ; `appel-livre` en fin de page,
  `ressource.livres`.
- Working paper : AWP-08 (réversibilité sociale), retenu en une phrase par la notion (lien vers `/reversibilite-sociale/`).
- Pages voisines : `/premier-coup/`, retenue (repères FICP, casier, « 040 », et piste « aucune trace sans rendez-vous »).
  `/qui-peut-faire-face-a-une-depense-imprevue/`, retenue (même livre, le coût d'un imprévu). `/reversibilite-sociale/`,
  retenue (la notion).

## Test de contribution marginale (arbitrage PRO-20261101-060949, point 7)

- Qu'apprend-on de neuf ? Les durées comparées et classées selon la manière d'effacer. L'asymétrie bonus-malus. Le
  changement du FICP au 20/11/2026 (qui déclare le paiement quand le crédit a été cédé).
- Quelles sources ? Les textes en vigueur, lus le 01/11/2026, et deux fiches Service-public pour le casier.
- Pourquoi le livre est-il un prolongement ? Il explique pourquoi ces durées pèsent inégalement : ce qu'un fichier vous
  coûte dépend de ce qui vous attend pendant qu'il court, et certaines erreurs ne s'inscrivent jamais (chapitre 8).

## Fiche D0

- **Résultat visé** : être la page lue (et citée par les moteurs de réponse) sur « combien de temps fiché Banque de
  France », « effacer son casier », « récupérer ses points », « durée du malus », et y conduire vers *La Société du
  premier coup*. Finalités : diffusion du livre, crédibilité (exactitude juridique).
- **Diagnostics** : Search Console (requêtes FICP, casier, points, malus) ; demandes d'exemplaire
  `?src=consultation-combien-de-temps-une-erreur-reste-inscrite`.
- **État initial (01/11/2026)** : page inexistante.
- **Relevé** : J+60, le 31/12/2026 ; relecture des textes après le 20/11/2026 (FICP). Pas de mesure des IA (décision
  de l'auteur du 01/11/2026).

## Étapes de la méthode

- Plan d'outils : fait pour le programme le 01/11/2026.
- Protocole du type : fait le 01/11/2026 (textes lus dans leur version en vigueur, versions futures repérées).
- Scénarios d'architecture : fait. (A) Tableau d'abord, puis une section par registre, puis la lecture du livre : retenu,
  le lecteur vient pour une durée. (B) Par manière d'effacer : écarté comme plan (le lecteur cherche un registre), gardé
  comme colonne du tableau et comme synthèse. (C) Une page par registre : écarté (une question, une page mère).
- Panel avant / après : non fait (motif : page juridique ; la contre-expertise en tient lieu).
- Gardes vues mordre, figures téléphone : sans objet.
- Relecture de langue : faite le 01/11/2026 (`check_langue.py` sur le texte servi : 0 signalement).
- Relecture phrase à phrase du texte servi : faite le 01/11/2026. Corrections de fond :
  - « cinq ans pour un crédit remboursé tardivement » est faux (un crédit remboursé est radié aussitôt), devenu
    « incident de crédit non régularisé » ;
  - « 10 ans au plus » du permis limité aux contraventions des quatre premières classes ;
  - « sans rechute » retiré (absent de l'art. L. 1141-5) ;
  - parties à la convention non vérifiées, donc retirées ;
  - le relevé d'informations est remis à la résiliation ou sur demande ;
  - le B2 n'est remis vierge qu'à l'employeur.
- Recette 320-1600 : faite le 01/11/2026 (RECETTE OK). Elle a révélé un défaut ancien de `/premier-coup/` (tableau des
  versions en cartes sans libellé, de 320 à 768 px), corrigé dans la même session (liste à la place du tableau).
- Gate éditorial (01/11/2026) — exactitude : tenu (textes en vigueur relus, versions futures signalées). Clarté : tenu
  (tableau d'abord, une section par registre). Accroche : tenu (chapô qui répond). Progression : tenu. Originalité : tenu
  (manière d'effacer, asymétrie bonus-malus, changement du 20/11/2026). Valeur finale : tenu. Fonctions : remplies.
- Instantané de relecture : fait le 01/11/2026 ; `refonte` posé.
- Contrôles : `check-all --ci` 0 ; build 0 ; liens 0 critique ; dates conformes ; rendu conforme.
- Contre-expertise de la page : faite le 01/11/2026 (`PRO-20261101-091535`, réponse archivée SHA-256 061B38FC…).
  Arbitrage `ARBITRATIONS/PRO-20261101-091535_arbitrage.md` : option B. P0 acceptés : tableau à six colonnes (nature des
  délais), transitoire du FICP (ordonnance 2025-880, art. 99, lu dans le navigateur, Légifrance refusant les scripts),
  conditions AERAS et L. 113-2-1, permis invalidé et probatoire (L. 223-1). P1 acceptés sauf la rectification FICP
  (arrêté non lu). Synthèse : quatre manières d'oublier. Contrôles relancés à 0, recette OK, instantané refait.
- Correction du chapô et de « Qui efface compte autant que le délai » (01/11/2026), sur la contre-expertise du lot de
  diffusion (`D:\PRO\06_PROMOTION\CAMPAGNES\2026-11-01_EFFACEMENT\_PIECES_RECUES\2026-11-01_resources.txt`, SHA-256
  adcfcf76…a42b) : « le permis, le malus et la réhabilitation s'effacent seuls ; le chèque sans provision et l'exclusion
  du bulletin n° 2 demandent une démarche » simplifiait les sections. L'interdiction de chéquier tombe seule au bout de
  cinq ans (la régularisation l'abrège) ; l'exclusion du bulletin n° 2 se décide au tribunal, dans le jugement ou sur
  requête (art. 775-1, déjà lu) ; ce qui revient sans démarche, ce sont les points, le malus et la réhabilitation. Les
  sections et la FAQ, exactes, sont inchangées. `check-all --ci` 0, build 0, liens 0 critique, dates conformes,
  `check_langue` sur les deux phrases servies (2 faux positifs), instantané refait.
- Correction du délai probatoire (01/11/2026), sur la seconde contre-expertise du lot
  (`…\2026-11-01_EFFACEMENT\_PIECES_RECUES\2026-11-01_Messages.txt`, SHA-256 da757d81…98b9) : « tant qu'aucune infraction
  n'a été commise » élargissait la condition ; le Code de la route, art. L. 223-1 (relu par le MCP `sources`, version en
  vigueur depuis le 30/03/2018), dit « aucune infraction ayant donné lieu à un retrait de points ». Phrase corrigée.
