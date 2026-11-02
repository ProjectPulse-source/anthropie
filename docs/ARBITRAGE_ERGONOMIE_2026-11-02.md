# Arbitrage ergonomique du site — 02/11/2026

Pièce arbitrée : `D:\CONTRE_EXPERTISE\2026-11-02_ERGONOMIE_SITE\Arbitrage ergonomique du site.pdf`, 4 pages, SHA-256
`19afb2095130630390f9d77ec3b8c7b6a3b416b4ebeb73630bd01a6f9c3a606d`. Son auteur précise n'avoir reproduit aucune mesure
en navigateur. Les points ci-dessous ont été vérifiés sur le site en ligne le 02/11/2026 ; rien n'est encore modifié.

**Finalité** : crédibilité durable et diffusion des travaux. **Objectif intermédiaire** : des pages qu'on lit jusqu'au bout
et dont on comprend les preuves. **Mécanisme** : une ligne trop longue fait perdre le retour à la ligne, donc la lecture
suivie ; une figure lisible porte la démonstration. Ce mécanisme repose sur des repères d'usage, pas sur une mesure de
notre audience.

## Décision finale de l'auteur (02/11/2026)

Après essai de la maquette sur son écran, l'auteur retient la **version D** : structure actuelle, texte de 18 px borné à
880 px (environ 121 signes par ligne), contenu sur 1 216 px, ronds retirés sous le contenu. Elle prime sur la colonne de
600 px et l'ordre d'exécution ci-dessous. Le sommaire latéral et la régénération des figures ne sont pas engagés.

## Le fait nouveau, absent des deux diagnostics

Mesure ligne par ligne, à 1 440 px : sur les pages du dossier dette, seul le chapô tient dans 720 px. **Le texte courant
occupe 992 px, soit environ 147 signes par ligne** (137 à 161), près du double du repère de 80. Sur 129 pages à texte
long, 81 ont plus de la moitié de leur texte au-delà de 760 px (`/quest-ce-que-lanthropie/`, `/premier-coup/`,
`/a-propos/`, enseignants, EN compris). Le chiffre de 110 signes portait donc sur le chapô, et la limite de 720 px
annoncée dans mon diagnostic ne vaut que pour lui.

## Décisions, point par point

| Point | Décision | Motif vérifié |
|---|---|---|
| 18 px ramène à 85-90 signes | **ACCEPTÉ** (correction) | 110 × 16/18 ≈ 98 ; mon chiffre était faux |
| Texte à environ 18 px | **ACCEPTÉ AVEC MODIFICATION** | 16 px partout aujourd'hui ; hausse progressive selon l'écran, téléphone à tester à part |
| Interligne 1,55-1,7 | **ACCEPTÉ** | déjà 1,7 (27,2 px) ; à recaler après la hausse de taille |
| Colonne de 650-680 px | **ACCEPTÉ AVEC MODIFICATION** | donne 88-93 signes, au-dessus de l'exigence de confort qu'il pose pour les longs textes ; mesuré sur maquette avec Newsreader à 18 px : 632 px = 88 signes, 600 px = 82-83 ; colonne de 600 px, cible ≤ 85 |
| Trois largeurs distinctes (lecture, démonstration, navigation) | **ACCEPTÉ** | c'est le socle, et il corrige les 81 pages |
| Ne pas remplacer 1 120 par 1 280 partout | **ACCEPTÉ** | un remplacement global élargirait encore le texte à 992 px et plus |
| 1 280 px ne remplit pas 2 560 px | **ACCEPTÉ** | calcul exact (50 %) ; remplir l'écran n'est pas l'objectif |
| Figures, priorité majeure | **ACCEPTÉ AVEC MODIFICATION** | priorité seconde : le texte à 147 signes passe avant |
| Risque de flou des PNG | **REJETÉ, sans objet** | les figures de données sont en SVG (21 fichiers), sans PNG de figure |
| Figures à 1 000-1 200 px | **ACCEPTÉ AVEC MODIFICATION** | agrandir un SVG grossit tout sans montrer plus : 720 × 413 devient 1 100 × 631. Le gain vient d'un format plus large, régénéré par `dette_cout_figures.py` et les générateurs voisins, figure par figure, séries longues d'abord |
| Tableaux pleine largeur, défilement local | **ACCEPTÉ** | déjà 960 px ; à reprendre avec la grille |
| Sommaire latéral sur dossiers longs seulement | **ACCEPTÉ AVEC MODIFICATION** | 63 pages ont déjà « Dans cette page » : transformer cet organe, ne pas en ajouter un |
| Schéma sommaire + figure de 1 000-1 200 px | **REJETÉ en l'état** | dans 1 216 px, colonne et sommaire laissent environ 250 px : la figure large passe sur le sommaire. Prototype sur une page avant décision |
| Bandeau « décalé de 112 px » : corrigé en écart symétrique | **ACCEPTÉ** | même axe, 1 216 contre 992 px ; mon mot « décalé » était inexact. Le nom et le titre restent à 112 px l'un de l'autre |
| Bandeau secondaire | **ACCEPTÉ AVEC MODIFICATION** | la correction vient gratuitement : le bandeau vaut 1 280 px moins 32 px par côté ; le contenu cumule deux marges de 2 rem (`.site-main` et `.home-section`). Conteneur de 1 280 px à marge simple = 1 216 px, même grille |
| Fond conservé, moins présent sous le contenu | **ACCEPTÉ** | à régler après la grille : un rond entoure aujourd'hui le badge EN |
| Modèles distincts : accueil, ressources, AWP | **ACCEPTÉ** | AWP déjà à 604 px et 84 signes, avec barre latérale : le modèle existe |
| « Quatre livres » sur l'accueil | **ACCEPTÉ** | l'accueil renvoie vers 6 livres ; écrire « quatre livres du corpus », FR et EN (`layouts/index.html`) |
| Contrôle à 375-2 560 px, zoom 200 %, clavier | **ACCEPTÉ** | largeurs 320 et 390 px conservées en plus |
| Critère 1.4.8 du W3C (80 caractères) | **ACCEPTÉ comme repère** | niveau AAA, pas une obligation |
| Mesurer l'effet par les données de consultation | **DÉCISION HUMAINE REQUISE** | GoatCounter enregistre le trafic, mais le jeton de lecture n'est pas sur le poste |
| Note de 8/10 et conclusion générale | **SANS EFFET** | ni l'une ni l'autre ne porte une décision vérifiable |

## Conflit à ne pas masquer

La demande de départ était d'occuper mieux l'écran. Le correctif le plus utile resserre le texte de 992 à 600 px :
sur grand écran, les marges peuvent paraître plus vides. Le conflit se traite par la taille du texte, les figures et le
sommaire ; il se juge sur capture à 1 920 px avant publication. La lecture prime si le conflit persiste.

## Ordre d'exécution

1. **Lecture** : variables des trois largeurs, colonne, taille du texte ; les 81 pages sont le critère de réussite.
2. **Grille** : conteneur de 1 280 px à marge simple, bandeau aligné. Essai à comparer : colonne alignée à gauche ou centrée.
3. **Figures** : dossier dette d'abord, par les générateurs, sans changer une donnée.
4. **Fond** : éloigner les ronds du contenu.
5. **Sommaire** : prototype sur une page longue, puis décision.
6. **Accueil** : formulation des livres (peut partir dès le lot 1).

Chaque lot se contrôle sur un build servi entièrement en local (mémoire `feedback_test_affichage_build_local`), toutes
largeurs, avec les contrôles habituels. Une mesure ligne par ligne vérifie la cible de signes. Aucun contrôle permanent
n'est ajouté à ce stade.

## Limites

- Mesures à 1 440 et 1 920 px sur le site en ligne, en navigateur headless ; le comptage des 81 pages repose sur la
  largeur des paragraphes et listes de plus de 200 signes, à 1 440 px.
- Maquette : `D:\CONTRE_EXPERTISE6-11-02_ERGONOMIE_SITE\MAQUETTE\ouvrir.html`, cinq vraies pages, surcharge CSS et JS.
  Figures agrandies, pas régénérées. Mesures ci-dessus à confirmer sur le build final.
- La part des grands écrans dans l'audience n'est pas connue.
- Le fond n'a fait l'objet d'aucune mesure de coût de rendu.
