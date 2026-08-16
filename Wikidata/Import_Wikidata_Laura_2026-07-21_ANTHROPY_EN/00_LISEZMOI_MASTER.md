# Chantier Wikidata + OpenLibrary — état consolidé au 2026-07-21

État vérifié en ligne (SPARQL Wikidata + API OpenLibrary) le 2026-07-21. Ce fichier
est l'index maître ; les consignes détaillées sont dans les sous-dossiers.

---

## 1. ANTHROPY (édition anglaise d'ANTHROPIE) — ✅ CRÉÉE : Q140645013

Livre publié sur Amazon le 2026-07-21. Item FR = **Q138827344**.

- **Wikidata** : ✅ item EN créé le 2026-07-21 = **Q140645013** (vérifié : P629
  traduction de → Q138827344, P407 anglais, P212/P957, P577, P648 OL62342580M,
  titre/sous-titre). ✅ **Réciproque posée** le 21/07 : `Q138827344 P747
  Q140645013` (vérifiée en ligne) → lien **bidirectionnel** P629↔P747 COMPLET.
  Optionnel restant : corriger le libellé anglais de Q138827344 (il duplique le
  FR). Décision Stéphane : crédit traducteur (P655 volontairement absent).
- **Open Library** : édition EN **DÉJÀ créée = `OL62342580M`**, rattachée au Work
  `OL45424565W`. ⚠ L'enrichissement (langue anglais, 632 p., format Paperback,
  lien « traduction de », sous-titre) a été **bloqué par un reCAPTCHA** au save
  (compte OL neuf) → **à finir par Stéphane** : *Modifier* la fiche `OL62342580M`,
  compléter, résoudre le CAPTCHA, *Enregistrer*.
- Le QS inclut déjà `P648 OL62342580M` pour lier l'item Wikidata EN à Open Library.

---

## 2. Livresque — FUSION Wikidata TOUJOURS EN ATTENTE

Doublon Wikidata **`Q138911600` → `Q140517745`** préparé le 2026-07-16 mais
**jamais appliqué** (Q138911600 encore actif, vérifié SPARQL 2026-07-21).
Consigne complète : dossier **`Fusion_Livresque/README_LAURA.md`** (joint).
Rappel : `Special:MergeItems`, PAS QuickStatements ; vider d'abord les
descriptions FR+EN de Q138911600.

---

## 3. Odyssée — nettoyage Wikidata (à ton rythme)

`Q138911733` porte **3 valeurs P31 contradictoires** : garder Q571 (livre) +
Q47461344 (œuvre écrite), **retirer Q3331189**. Par ailleurs l'item pointe encore
l'ancienne édition (ISBN 978-2-9586347-1-1) ; la nouvelle (978-2-9586347-4-2) est
un autre chantier (hors périmètre ici).

---

## 4. Open Library — DOUBLONS DE WORKS à fusionner (2026-07-21)

Les 4 livres sont **déjà** sur Open Library (rien à créer). Mais 2 ont un **Work
en double** visible sur la page auteur (`OL16378291A`). Fusionner en **gardant
l'ID que Wikidata référence en P648** (sinon on casse le lien Wikidata↔OpenLibrary) :

| Livre | GARDER (= P648 Wikidata) | ABSORBER (doublon) | Édition du doublon | QID |
|---|---|---|---|---|
| ANTHROPIE | `OL45424565W` (porte FR + édition EN) | `OL45424564W` | `OL61896276M` (FR, ISBN …728) | Q138827344 |
| Dette Publique | `OL45424600W` | `OL45424599W` | — | Q138910896 |

*(Livresque : le 2ᵉ Work `OL45424545W` n'apparaît pas sur la page auteur ; sa
vraie fusion est côté **Wikidata**, cf. §2. L'Odyssée n'a pas de doublon —
`OL45424562W` seul, mais c'est l'ANCIENNE édition ISBN …711 ; ajouter la nouvelle
…742 = autre chantier.)*

### ⚠ Réalité opérationnelle (constaté le 2026-07-21)
- **On ne SUPPRIME pas** une fiche sur Open Library (wiki) : pas de bouton
  *Delete* sur les éditions (vérifié : la page d'édition n'a que reCAPTCHA +
  *Enregistrer*). Un doublon se résorbe **uniquement par FUSION** (→ redirection).
- L'outil *Merge works* (`https://openlibrary.org/works/merge?records=<garder>,<absorber>`)
  renvoie **« Forbidden »** pour un compte sans le rôle **librarian**. Le compte
  utilisé (`un_jour_peut-_tre`) ne l'a pas.

### Comment faire (3 voies)
1. **Compte principal** : se reconnecter avec le compte `Stephane Lalut` (celui qui
   a édité les fiches) — il a peut-être déjà les droits.
2. **Demander la fusion à la communauté** OpenLibrary (librarians) en donnant les
   paires ci-dessus (garder / absorber).
3. **Obtenir le rôle librarian** : `https://openlibrary.org/librarians-in-training`
   (promotion par un admin, quelques jours), puis fusionner soi-même.

### Couverture de l'édition EN
`OL62342580M` n'a pas d'image. Une fois le site déployé (fait — push 2026-07-21),
ajouter par URL : `https://stephane-lalut.com/images/livres/anthropie-ordre-ici-dette-ailleurs.en.jpg`
(nécessite aussi de résoudre le reCAPTCHA).

### Priorité
**Non bloquant / cosmétique.** Les doublons pointent le même livre réel (aucune
perte), et Wikidata référence déjà les fiches canoniques. À faire au calme quand
les droits sont là.

---

## 5. Récapitulatif des liens P648 (déjà tous posés — RIEN à ajouter)

| Livre | Wikidata | P648 (Open Library) |
|---|---|---|
| ANTHROPIE (FR) | Q138827344 | OL45424565W ✅ |
| ANTHROPY (EN) | *à créer* | OL62342580M (dans le QS) |
| Dette Publique | Q138910896 | OL45424600W ✅ |
| Livresque | Q140517745 | OL45424544W ✅ |
| L'Odyssée | Q138911733 | OL45424562W ✅ |

---
*Consolidé le 2026-07-21. Sources : SPARQL Wikidata (P50/P648) + API OpenLibrary
(search.json author). Rien d'inféré : tous les QID/OLID sont vérifiés en ligne.*
