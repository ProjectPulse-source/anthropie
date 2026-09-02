# Wikidata — navette du 2026-09-02 (6 lignes, un seul Run) : références sur deux recensions *Lectures* + deux descriptions de l'item auteur

> ⏳ **À exécuter.** Une fois fait, remplacer ce bloc par ✅ + readback API
> (`P50` et `P356` doivent porter **1 référence** chacun sur les deux items ; toujours
> **8 propriétés** par item — aucune déclaration nouvelle ; descriptions es/de de
> `Q138909233` remplacées, rien d'autre touché sur l'item auteur).

Laura — rien à créer : on **source** deux items qui existent déjà (créés par toi le
15/08, même lot que `Q141072263`). Le modèle RFSE (`Q140892752`) portait une référence
`S854` + `S813` sur l'auteur et sur le DOI ; ces deux items n'en ont pas.

| Item | Recension | Déclarations à sourcer | Référence (URL OpenEdition + date de consultation) |
|---|---|---|---|
| **Q141072264** | Arnaud Kaba, *La main et l'esprit* | `P50` Q138909233 · `P356` `10.4000/162F0` | https://journals.openedition.org/lectures/70897 · 2026-09-02 |
| **Q141072265** | Valéry Ridde, *La financiarisation de la santé au Sénégal* | `P50` Q138909233 · `P356` `10.4000/16IHM` | https://journals.openedition.org/lectures/71869 · 2026-09-02 |

## Et deux descriptions à corriger sur l'item auteur

Relecture API du 02/09 : les descriptions **espagnole** et **allemande** de `Q138909233`
portent des fautes (« francès », « antropico » ; « ükonom under forscher », minuscules).
Les deux lignes `Des` / `Dde` du lot les **remplacent** (une description par langue,
QuickStatements écrase) : rien d'autre n'est touché sur cet item.

## Comment faire — UN CLIC

1. Ouvrir le lien du fichier **`deeplink.txt`** : il charge les 6 commandes dans
   QuickStatements (connectée à ton compte).
2. **Vérifier le preview** : chaque ligne doit apparaître comme un **ajout de référence**
   sur une déclaration existante — pas comme une nouvelle déclaration `P50`/`P356` ;
   les deux dernières lignes doivent apparaître comme des changements de description.
   Si une ligne annonce une nouvelle déclaration, ne pas lancer et me le dire.
3. **Run**, puis me confirmer.

Repli si le lien ne s'ouvre pas — coller `batch_quickstatements.txt` en mode Import V1,
en retirant les lignes `//`.

## Pourquoi c'est fait comme ça

- Les valeurs répètent **exactement** ce qui est en place (DOI en majuscules, tel que
  stocké) : c'est la condition pour que QuickStatements rattache la référence à la
  déclaration existante au lieu d'en créer une seconde.
- Même forme que la navette RFSE du 05/08 : `S854` = URL de la page OpenEdition,
  `S813` = date de consultation. Pas de `S248` : un compte rendu porteur de son DOI se
  source par sa page.
- Aucune autre propriété touchée ; les items restent à 8 propriétés.

Merci !
