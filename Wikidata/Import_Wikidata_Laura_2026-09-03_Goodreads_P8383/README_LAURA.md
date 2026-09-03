# Wikidata — navette du 2026-09-03, **2ᵉ lot** (6 lignes, un seul Run) : l'identifiant d'œuvre Goodreads sur les six livres

Laura — rien à créer. On ajoute **une** déclaration `P8383` (*Goodreads work ID*)
sur chacun des six items livres, qui n'en portent aucune.

| Item | Livre | ISBN (P212, déjà sur l'item) | Œuvre Goodreads |
|---|---|---|---|
| **Q138911733** | L'Odyssée des idées | 978-2-9586347-4-2 | `215006210` |
| **Q138827344** | ANTHROPIE — Ordre ici. Dette ailleurs | 978-2-9586347-2-8 | `260328868` |
| **Q140645013** | ANTHROPY (édition anglaise) | 978-2-9586347-5-9 | `299046023` |
| **Q138910896** | Dette Publique : Qui paie vraiment ? | 978-2-9586347-3-5 | `266484445` |
| **Q140517745** | Livresque des mots | 978-2-9586347-0-4 | `99837927` |
| **Q141072263** | La Société du premier coup | 978-2-9586347-6-6 | `301000264` |

## Comment faire — UN CLIC

1. Ouvrir le lien du fichier **`deeplink.txt`** : il charge les 6 commandes dans
   QuickStatements (connectée à ton compte).
2. **Vérifier le preview** : six **ajouts de déclaration `P8383`**, chacun avec sa
   référence. Si une ligne annonce autre chose — une modification d'une déclaration
   existante, ou un item que tu ne reconnais pas — ne pas lancer et me le dire.
3. **Run**, puis me confirmer.

Repli si le lien ne s'ouvre pas — coller `batch_quickstatements.txt` en mode
Import V1, en retirant les lignes `//`.

## Pourquoi ce lot n'existait pas hier

Sur Goodreads, deux livres étaient éclatés en **deux œuvres** chacun : *L'Odyssée
des idées* (le broché 2026 vivait à part du reste) et *La Société du premier coup*
(le Kindle à part du broché). Poser un identifiant d'œuvre dans cet état aurait figé
dans Wikidata la moitié d'un livre. Les deux réunions ont été faites le 03/09 et
vérifiées : la page auteur Goodreads rend maintenant **six livres, un par œuvre**,
les deux œuvres orphelines (`297251964`, `301009614`) répondent 404.

## Ce qui a été contrôlé avant d'écrire ce lot

**Le rattachement est établi par ISBN, jamais par le titre.** Pour chacune des six
œuvres, la page `work/editions/<id>` a été relue et contient bien l'ISBN que l'item
Wikidata déclare en `P212` :

| Œuvre | éditions | ISBN-13 trouvé | ISBN-10 trouvé |
|---|---|---|---|
| 215006210 | 3 | 9782958634742 ✓ | 2958634742 ✓ |
| 260328868 | 2 | 9782958634728 ✓ | 2958634728 ✓ |
| 299046023 | 2 | 9782958634759 ✓ | 2958634752 ✓ |
| 266484445 | 2 | 9782958634735 ✓ | 2958634736 ✓ |
| 99837927 | 4 | 9782958634704 ✓ | 2958634701 ✓ |
| 301000264 | 2 | 9782958634766 ✓ | 2958634760 ✓ |

⚠ La première lecture de `301000264` a rendu **zéro occurrence** de son ISBN — une
lecture transitoire juste après la réunion, pas une absence. La relecture donne
2 éditions et l'ISBN présent. *Une absence de trace n'est pas une absence de fait* :
ne pas conclure d'un seul relevé.

Vérifié aussi : aucun des six items ne porte déjà `P8383` ni `P2969`.

## Ce qui reste ouvert sur ce graphe

- **`P268` (BnF)** : toujours impossible, les notices n'existent pas.
- **`P2963`** (identifiant auteur Goodreads) : ✅ posé par toi le 03/09 à 01h16 UTC,
  relu à l'API — l'item auteur est passé de 17 à 18 propriétés.
- **Traductions FR ↔ EN** : Goodreads recommande explicitement de réunir les
  traductions d'un même livre dans une seule œuvre (« we've made the decision to
  combine them all »). ANTHROPIE et ANTHROPY sont aujourd'hui **deux** œuvres.
  Les réunir ferait converger notes et avis — décision éditoriale, non prise ici.
  ⛔ Ne pas exécuter sans arbitrage de l'auteur : ce lot suppose les deux œuvres
  séparées, et une réunion invaliderait l'un des six identifiants.

Merci !
