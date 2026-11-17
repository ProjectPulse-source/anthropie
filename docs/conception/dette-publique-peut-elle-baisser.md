# Fiche de conception — La dette publique peut-elle baisser ?

<!-- Fiche écrite le 16/11/2026 pendant la reprise du lot « dette-a », APRÈS la relecture des sources :
LOTS\dette-a\SOURCES\dette-publique-peut-elle-baisser_R1a.md (lignes 1-247 du texte servi, « R1a ») et _R1b.md (lignes
248-545, « R1b »). La page existait depuis le 02/10/2026 sans fiche ; celle-ci dit son état réel au 16/11. -->

Page : `/dette-publique-peut-elle-baisser/` (FR) · `/en/can-public-debt-come-down/` (EN) · ouverte le 2026-10-02 (fiche
écrite le 2026-11-16, après la relecture des sources)

## Forme

Données (`quantitatif`) : jeu `dette_baisse` (JSON, CSV), jetons sans chiffre saisi (le dernier nombre écrit en dur,
« dix-neuf pays », devient le jeton `ze_n`), gardes vues mordre, figures en SVG et PNG avec version téléphone, Réutiliser,
Dataset. La page décompose et compare ; elle ne recommande pas de trajectoire.

## Fiche de conception

### Question centrale

Le poids de la dette publique dans le PIB peut-il baisser, et par quels termes a-t-il baissé là où il a baissé ?

### Enjeu

Le débat oppose « la dette ne baisse jamais » et « il suffit de croissance ». Les deux confondent le montant et le ratio,
et ignorent par quel terme les pays de la zone euro ont réellement réduit le leur. La réponse conditionne ce qu'un
excédent primaire, la croissance ou les taux peuvent faire.

### Croyance initiale

« La dette ne peut pas baisser » (son montant monte presque toujours), ou « la croissance suffit ».

### Découverte principale

Le ratio peut baisser même quand le montant monte, et il a baissé ailleurs : sur la dernière décennie, les pays de la
zone euro qui ont réduit leur ratio cumulent des excédents primaires et une croissance nominale plus forte, quand la France
a connu la plus forte hausse du groupe avec le déficit primaire moyen le plus élevé. Porté par R1a § 1 (l. 25-80 :
décompositions par décennie et comparaison des pays, recalculées à l'identique depuis Eurostat par le relecteur) et R1a
§ 2, P2 l. 67 (« Leur croissance du PIB nominal a, elle, été plus forte », non exclusive : les excédents comptent aussi).

### Mécanisme explicatif

La même identité que la page « Pourquoi la dette publique augmente-t-elle ? » : variation du ratio = effet des taux et de
la croissance + déficit primaire + ajustements flux-stock. Le ratio baisse quand le solde primaire dépasse le solde
stabilisant, qui dépend de l'écart entre taux implicite et croissance nominale. En France, l'écart au repère s'est refermé
par le repère (taux bas), pas par le solde (R1b § 2, P1-2, l. 271 : le solde primaire s'est lui aussi abaissé).

### Preuve décisive

Le témoin des pays de la zone euro (21 pays, une décennie, Eurostat) : même identité, mêmes sources, et des trajectoires
opposées selon le solde primaire et la croissance nominale ; R1b reproduit tous les nombres calculés depuis Eurostat,
AMECO, l'OCDE et le FMI (R1b, bilan).

### Pouvoir discriminant

Rivales soutenues : la croissance seule (lecture répandue), l'excédent primaire (Cour des comptes, direction générale du
Trésor), l'écart taux–croissance favorable (travaux r < g). Le témoin des pays ne change qu'un terme à la fois : à
déficit primaire moyen, l'Espagne, l'Italie et la Belgique finissent la décennie à peu près à leur niveau de départ malgré
un effet des taux et de la croissance favorable ; ceux qui réduisent leur ratio ont des excédents. La comparaison ne porte
que sur une décennie et la page le dit ; l'accès au marché n'est pas mesuré par la page, la Cour en suit les indicateurs
(R1b § 2, P0-1). Levier visible : le solde primaire ; risque : la quasi-égalité de 2025 entre taux et croissance.

### Limite

Décomposition comptable sur une décennie ; elle ne dit pas pourquoi les déficits ont existé. Le solde stabilisant dépend
d'hypothèses de taux et de croissance. Deux lignes restent NON VÉRIFIÉES (R1b § 3).

### Valeur finale

Le lecteur distingue le montant du ratio, sait par quels termes d'autres pays ont réduit leur dette, et voit ce qu'il
faudrait de solde primaire pour stabiliser celle de la France selon chaque source.

### Singularité

Cette page existe parce qu'elle révèle, sur 21 pays et une même identité, par quels termes le ratio a baissé là où il a
baissé, que le lecteur ne découvre pas dans le rapport de la Cour des comptes de juin 2025, lu (R1b), qui compare quatre
grands pays et réunit taux et croissance dans l'effet « boule de neige ».

### Raccords

Retenus : `/pourquoi-la-dette-publique-augmente/` (même identité) ; `/dette-publique-comparaison-internationale/` ; livre
*Dette publique : qui paie vraiment ?* (bloc d'appel). Écarté : le renvoi vers l'AWP-09 (absence actée par l'auteur,
feuille de route GEO, l. 546 au 16/11/2026).

## Fiche D0

Fiches D0 existantes : `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`, page (l. 394 et suivantes au 16/11/2026)
et section `#soutenable` (l. 432 et suivantes), écrites le 03/10 avant publication : objet, requêtes, relevés. Relevé
suivant : à la publication de la version reprise.

## Étapes de la méthode

- Plan d'outils : non fait dans cette reprise (outils déjà câblés) ; à lancer à la publication.
- Relecture des sources : fait (16/11/2026, R1a et R1b, FR et EN : 1 P0, 7 P1, 41 P2 au total).
- Scénarios d'architecture : sans objet (organes existants).
- Panel avant : non fait ; premier écran testé par des lecteurs qui ne voient que lui (rapport du lot).
- Gardes vues mordre : existantes (93 gardes du générateur passées le 16/11) ; aucune garde nouvelle.
- Figures téléphone : fait (`--check` du générateur) ; texte alternatif périmé corrigé (sonde S1-1).
- Relecture de langue : fait (`RAPPORTS\langue\`, aucun blocage).
- Recette 320-1440 : fait par `captures.py` (0 débordement) ; `recette.py` non lancé.
- Panel après, gate éditorial : non faits (préparation de nuit).
- Instantané de relecture : non fait (à refaire à la publication).
- Contre-expertise de la page : paquet du lot préparé le 16/11, à envoyer par l'auteur.
- Accord de l'auteur : non obtenu (préparation seule).
