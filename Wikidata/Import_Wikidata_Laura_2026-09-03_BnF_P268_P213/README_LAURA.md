# Wikidata — navette du 2026-09-03, **4ᵉ lot** (5 lignes, un seul Run) : BnF + ISNI

Laura — rien à créer. On ajoute `P268` (identifiant BnF) sur l'auteur et trois livres,
et `P213` (ISNI) sur l'auteur.

| Item | Propriété | Valeur | Notice BnF |
|---|---|---|---|
| **Q138909233** Stéphane Lalut | `P268` | `17672810m` | autorité personne, `cb17672810m` |
| **Q138909233** Stéphane Lalut | `P213` ISNI | `0000000518014301` | déclaré dans cette même notice |
| **Q138827344** ANTHROPIE | `P268` | `488150518` | `cb488150518` |
| **Q138910896** Dette Publique | `P268` | `488150471` | `cb488150471` |
| **Q140517745** Livresque des mots | `P268` | `474815054` | `cb474815054` |

⚠ **Deux pièges de format, vérifiés sur les propriétés elles-mêmes avant d'écrire :**
`P268` se stocke **sans le préfixe `cb`** — la *formatter URL* de Wikidata est
`catalogue.bnf.fr/ark:/12148/cb$1`, donc l'ARK `cb17672810m` donne la valeur
`17672810m`. `P213` s'écrit **sans espaces** : `0000000518014301`, pas
`0000 0005 1801 4301`.

## Comment faire — UN CLIC

1. Ouvrir le lien du fichier **`deeplink.txt`**.
2. **Vérifier le preview** : cinq **ajouts de déclaration**, quatre `P268` et un `P213`,
   chacun avec sa référence. Si une ligne annonce autre chose, ne pas lancer et me le dire.
3. **Run**, puis me confirmer.

Repli : coller `batch_quickstatements.txt` en mode Import V1, sans les lignes `//`.

## Pourquoi ce lot existe alors que la BnF était réputée bloquée

La mémoire du projet portait « BnF : notices inexistantes, `P268` impossible ». **C'était
faux.** Interrogation de l'API SRU du Catalogue général le 03/09 : l'auteur a une **notice
d'autorité personne depuis octobre 2024** (`cb17672810m`, Lalut, Stéphane, 1966-....),
qui cite *L'odyssée des idées* et *Livresque des mots* comme sources, et qui **déclare
elle-même l'ISNI** en zone 001. Trois livres sur six ont leur notice bibliographique.

📌 *Un point réputé bloqué se revérifie à la source, pas dans la note qui le déclare
bloqué.* Celui-ci l'était depuis dix mois.

## ⛔ L'Odyssée n'est pas dans ce lot, et ce n'est pas un oubli

`Q138911733` déclare l'ISBN **978-2-9586347-4-2** — la nouvelle édition 2026. Le
Catalogue général BnF n'en a **aucune notice** : le dépôt légal n'a pas encore eu lieu.
La seule notice existante, `cb47481513r`, est celle de la **première édition, dépubliée**.
Y rattacher l'item contredirait son propre `P212`.

C'est le même refus que celui opposé le même jour à Goodreads et à Babelio : **on ne pose
pas un identifiant qui désigne une autre génération de l'objet.**

## État du dépôt légal au 03/09 — mesuré, pas supposé

| Livre | ISBN | Notice BnF |
|---|---|---|
| Livresque des mots | 978-2-9586347-0-4 | ✅ `cb474815054` |
| L'Odyssée des idées, 1ʳᵉ éd. **dépubliée** | 978-2-9586347-1-1 | ✅ `cb47481513r` |
| ANTHROPIE | 978-2-9586347-2-8 | ✅ `cb488150518` |
| Dette Publique | 978-2-9586347-3-5 | ✅ `cb488150471` |
| **L'Odyssée des idées, éd. 2026** | 978-2-9586347-4-2 | ⛔ **aucune** |
| **ANTHROPY** (édition anglaise) | 978-2-9586347-5-9 | ⛔ **aucune** |
| **La Société du premier coup** | 978-2-9586347-6-6 | ⛔ **aucune** |

**Trois livres ne sont pas déposés, pas un seul.** Chaque dépôt fait ouvrira une ligne
`P268` de plus, et pour l'Odyssée débloquera aussi la fusion des fiches Babelio.

Merci !
