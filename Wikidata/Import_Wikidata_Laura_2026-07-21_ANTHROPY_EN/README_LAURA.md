# Wikidata — édition anglaise ANTHROPY + rappel fusion Livresque (2026-07-21)

Laura — deux choses à faire « dans la foulée », l'une nouvelle, l'autre restée
en attente depuis juillet. J'ai vérifié l'état réel de Wikidata avant d'écrire :
il **n'existe aucun doublon** de l'item ANTHROPIE (`Q138827344` est seul), et
**aucun item ANTHROPY** n'a encore été créé. Le seul doublon en attente, c'est
Livresque (tâche B ci-dessous).

---

## Tâche A — créer l'item « ANTHROPY » (édition anglaise)

Le livre fondateur a désormais une **édition anglaise publiée** (Amazon, 2026-07-21) :

| | |
|---|---|
| Titre | **ANTHROPY — A Big History of Civilization's Hidden Costs** |
| Œuvre d'origine | ANTHROPIE — Ordre ici. Dette ailleurs (**Q138827344**) |
| Auteur | Stéphane Lalut (**Q138909233**) |
| Langue | anglais (**Q1860**) |
| ISBN-13 | 9782958634759 |
| ASIN broché | 2958634752 (= ISBN-10) · **ASIN Kindle** B0H9QMR1CN |
| Pages | 632 · Publication | 2026-07-21 |
| Page site | https://stephane-lalut.com/en/livres/anthropie-ordre-ici-dette-ailleurs/ |

**Comment faire** : ouvrir **QuickStatements** (https://quickstatements.toolforge.org/),
mode *Import* → coller le contenu de **`batch_quickstatements.txt`** (dossier joint),
retirer les lignes commençant par `//`, lancer.

> L'item est relié à l'œuvre française par **P629 (traduction de) → Q138827344**.
> C'est ce qui les distingue proprement : deux éditions d'une même œuvre, pas un
> doublon. Ne PAS fusionner ANTHROPY avec ANTHROPIE.

**Après l'import (3 étapes manuelles, détaillées en bas du .txt)** :
1. noter le QID créé, l'envoyer à Stéphane ;
2. sur `Q138827344`, ajouter **P747 (a pour édition/traduction) = \<QID créé\>** ;
3. (recommandé) corriger le **libellé anglais** de `Q138827344`, qui recopie
   aujourd'hui le libellé français.

**⚠ Une décision revient à Stéphane** (ligne `P655` laissée en commentaire dans
le .txt) : faut-il créditer un **traducteur** ? La traduction EN vient du moteur
interne + relecture auteur (déclaration IA côté KDP). Par défaut : rien poser.

---

## Tâche B — appliquer la fusion Livresque restée en attente

En vérifiant Wikidata, je constate que le **doublon Livresque** signalé le
2026-07-16 est **toujours actif** : `Q138911600` (« Livresque des Mots »,
majuscule) n'a pas été fusionné dans `Q140517745`. La consigne complète, déjà
prête, est ici :

**`Wikidata/Fusion_Livresque_2026-07-16/README_LAURA.md`**

Rappel express (tout est dans ce fichier) :
1. vider les descriptions FR + EN de **Q138911600** (sinon la fusion échoue) ;
2. **Special:MergeItems** — from `Q138911600`, to `Q140517745` ;
3. vérifier que `Q138911600` redirige et que `Q140517745` garde ISBN/ASIN/pages.

*(Si tu l'avais déjà faite et qu'elle a échoué, c'est presque sûrement l'étape
« vider les descriptions » qui manquait — c'est le point de blocage classique.)*

---

## Bonus repéré (à ton rythme, non urgent)

`Q138911733` (L'Odyssée des idées) porte **trois** valeurs « instance de » (P31)
contradictoires : Q571 (livre), Q3331189 (édition/traduction) **et** Q47461344
(œuvre écrite). Garder Q571 + Q47461344, **retirer Q3331189**.

---
*Préparé le 2026-07-21. Nouvel item = ANTHROPY (édition EN, traduction de
Q138827344). Fusion Livresque = Q138911600 → Q140517745 (toujours en attente).*
