# Fiche de conception — Enseigner la vérification des citations en français : une activité de Première

Page : `/enseignants/litterature/` (FR) · pas de version anglaise (exclusion déclarée, comme la page mère
`/citations-celebres-verifiees/`) · ouverte le 2026-11-04

Demande de l'auteur du 04/11/2026 : l'atelier de la page des citations devient, dans « Pour enseigner », la première page
de la discipline Littérature ; la page mère reste dans « Idées et méthode ».

## Forme

`usage` : une activité pour la classe. Critères : rattachement au programme cité à la source ; fiche élève imprimable
sans corrigé ; corrigé qui ne dit rien que la source ne dise ; durée et matériel indiqués ; aucune question ne demande de
juger une personne.

## Fiche de conception

### Question centrale

Une phrase célèbre est-elle authentique, retouchée ou introuvable chez l'auteur à qui on la prête ?

### Enjeu

Apprendre à citer : une phrase prise sans son livre, sa page et sa forme exacte change de sens ou d'auteur.

### Croyance initiale

Une citation célèbre attribuée à un grand auteur est de lui, sous cette forme.

### Découverte principale

Sur cinq phrases, deux ne sont pas établies chez l'auteur, une est une variante, deux sont établies ; l'une des établies
change de sens quand on la cite sans son vers suivant.

### Mécanisme explicatif

La phrase circule seule ; elle prend le nom qui la rend vraisemblable, se simplifie, ou perd ce qui l'entourait.

### Preuve décisive

Les passages et éditions donnés par les fiches de la page mère, liés depuis le corrigé.

### Pouvoir discriminant

Sans objet : page sans données. Le corrigé départage les hypothèses des élèves par le texte de l'œuvre.

### Limite

Les statuts valent pour les sources consultées par la page mère ; « non établie » ne veut pas dire « fausse ». Les
œuvres au programme changent chaque année : la page ne cite que les objets d'étude.

### Valeur finale

Une séance prête à l'emploi, sans préparation, dont chaque réponse renvoie à sa source.

### Singularité

Cette page donne, pour la classe, une fiche imprimable et un corrigé sourcé ; la page mère, lue, donne les fiches, pas la
séance.

### Raccords

Page mère `/citations-celebres-verifiees/` : retenue (chaque réponse y renvoie). *Livresque des mots* : retenu, une phrase
en fin de page. Définition de l'anthropie et working papers : écartés, sans lien avec l'activité.

## Fiche D0

Résultat visé : des enseignants de français et des animateurs (Alliances françaises, écoles FLAM) utilisent la fiche ;
diagnostic : visites de la page et clics vers la page mère. État initial au 04/11/2026 : page neuve, aucune visite.

## Étapes de la méthode

- Plan d'outils : non fait (motif : activité courte, sans figure ni données).
- Protocole du type `usage` : fait (04/11/2026) ; programme relu sur Éduscol (juin 2021), le Bulletin officiel refusant le script.
- Scénarios d'architecture : fait (04/11/2026) ; page propre dans « Pour enseigner » retenue, déplacement de la page mère écarté.
- Panel avant, contre-expertise de phase A : non fait (motif : reprise d'un contenu vérifié, sans fait nouveau).
- Gardes vues mordre : sans objet (aucun chiffre).
- Affichage à 320 et 390 px : fait (04/11/2026), sans débordement ; rendu relu à 1 920 px.
- Relecture de langue (`check_langue.py`) : faite (04/11/2026), 8 signalements dus à l'analyse des apostrophes codées, aucun ne bloque.
- Refonte « à l'heure de l'IA » : faite (10/11/2026). Contre-expertise externe sur paquet autoportant, réponse archivée
  (SHA-256 `86c03d23…`) et arbitrée : `D:\CONTRE_EXPERTISE\2026-11-10_LITTERATURE_IA\ARBITRAGE.md`. Sixième citation-piège
  rejetée ; hypothèse sans écran d'abord ; deux réponses rédigées pour l'exercice, dites telles ; deux régimes de preuve
  (attestation, non-attestation) ; cadre d'usage de l'IA cité sur ses seuls passages lus (affiche Éduscol, le site du
  ministère refusant le script).
- Seconde contre-expertise : faite et arbitrée (10/11/2026, réponse SHA-256 `980d1ece…`, `ARBITRAGE-01.md` du même
  dossier). Corrigé précisé (vérifiable ≠ vérifié ; absence dans un corpus lu ≠ inexistence) ; question de traduction (A) ;
  fin de la fable relue sur Wikisource (éd. 1874, texte validé) ; dossier documentaire de cinq extraits ; numérotation du
  corrigé réparée (la liste ordonnée renumérotait « 1. et 2. » et décalait les réponses, défaut déjà en ligne) ; deux
  boutons d'impression mesurés en PDF A4 : fiche élève 2 pages (fiche, puis dossier), corrigé 2 pages. Licence du texte
  des fiches : décision de l'auteur, en attente.
- Troisième relecture externe : faite et arbitrée (10/11/2026, `a4dbbcb7…`, `ARBITRAGE-02.md`). « Ce que les élèves
  découvrent » sous le titre, bloc enseignant après la fiche et le dossier, intertitres au style des surtitres ; dossier
  présenté comme pièces d'une enquête déjà menée ; conclusion négative sur Hugo bornée au corpus et aux formes cherchées ;
  question 6 de synthèse (mots, source, sens). Impressions remesurées : 2 pages chacune.
- Quatrième relecture externe : faite et arbitrée (10/11/2026, `6d8fec44…`, `ARBITRAGE-03.md`). Document A pour tous ;
  fable intégrale en C (Wikisource, éd. 1874, relue) ; réponses « justes sur ce qu'elles affirment » ; lettre de Hall
  citée d'après sa publication ; « Première » retiré de l'intertitre. Impressions : 2 pages chacune.
- Cinquième relecture externe : faite et arbitrée (10/11/2026, `f4731716…`, `ARBITRAGE-04.md`). Citation D relue sur le
  fac-similé du *Sottisier* de 1880, p. 99 (Internet Archive) : conforme mot pour mot, rien à changer. Chaque élève a la
  fiche et le dossier entier ; mise en commun par citation, cinq rapporteurs ; pièces lues et recherche rapportée
  distinguées (question 3) ; les trois vérifications nommées dans l'encadré, absent des impressions.
- Sixième relecture externe, sur le fichier de relecture de `70a87af` : faite et arbitrée (10/11/2026, `dd795ab3…`,
  `ARBITRAGE-05.md`). Corrigé de la question 2 : « n'est pas de Voltaire » des deux réponses dit plus que la preuve (même
  doctrine que la question 4) ; conclusion 7 min, mise en commun 13 min. Révisions de fond closes.
- Relecture phrase à phrase par l'auteur : faite et validée (10/11/2026), sur le texte servi de `462e4d8`, 122 phrases
  (`D:\CONTRE_EXPERTISE\2026-11-10_LITTERATURE_IA\Relecture_page_litterature.txt`, SHA-256 `05fbc169…`). Instantané
  `check-relecture` : sans objet (l'outil ne suit que les pages marquées `refonte`, aucune page « Pour enseigner » ne l'est).
- Prochain test : retour d'usage d'une séance réelle, pas une relecture de plus.
- Accord de l'auteur : demande du 04/11/2026.
