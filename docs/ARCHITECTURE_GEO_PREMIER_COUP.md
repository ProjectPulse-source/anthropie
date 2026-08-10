# Architecture GEO — *La Société du premier coup*

`ARCHITECTURE_GEO_PREMIER_COUP — OPTION_1_5_ADOPTÉE` · 2026-07-29

Arbitrage issu de trois pièces : la proposition initiale (auteur), l'arbitrage
`Amelioration_chaine_editoriale-128.txt`, et le contrôle sur l'architecture réelle
(dépôt du site + BAT du livre) qui a tranché entre les deux.

---

## 1. Quatre objets, quatre fonctions — jamais deux fois la même

| URL | Fonction | Public | Dans la nasse&nbsp;? |
|---|---|---|---|
| `/reversibilite-sociale/` | **racine conceptuelle** — répond à la question | lecteur curieux | **oui** (maille, `faq:`) |
| `/awp/awp-08/` | **formalisation scientifique** — DOI, méthode | chercheur | oui (hub) |
| `/livres/la-societe-du-premier-coup/` | **objet éditorial et commercial** | acheteur | non (catalogue) |
| `/premier-coup/` | **compagnon du lecteur** — preuves réutilisables | lecteur du livre, journaliste | **non** |

> **Le concept sur la maille · la démonstration dans l'AWP · les preuves réutilisables
> dans le compagnon · le récit dans le livre.**

### Pourquoi `/premier-coup/` n'a pas de `faq:`

Ce n'est pas un oubli, c'est le mécanisme. La doctrine **GEO-04** est déjà écrite dans le
dépôt et **déjà démontrée par une red team** sur un autre livre : *« la question “qui paie
la dette publique&nbsp;?” est la propriété exclusive de la page pont
`/qui-paie-la-dette-publique/` — cannibalisation démontrée — ne jamais l'ajouter ici »*
(`content/livres/dette-publique-qui-paie-vraiment.md`).

Deux pages du même domaine qui répondent à la même question se concurrencent. Le titre du
livre n'a par ailleurs aucun volume de requête — c'est un nom de marque, comme
«&nbsp;anthropie&nbsp;», dont les audits GEO ont établi que le volume est quasi nul.

**Conséquence technique** : l'absence de `faq:` tient la page hors du recensement des
mailles dans `scripts/check-geo-coverage.py`. Le linter et la doctrine disent la même
chose. Ne pas ajouter de FAQ conceptuelle à cette page.

---

## 2. Ce qui a été corrigé de part et d'autre

**Corrigé chez moi** — une page absente du menu principal **n'est pas du cloaking**. Le
cloaking consiste à servir un contenu *différent* selon le user-agent. `/premier-coup/`
est publique, identique pour tous, dans le sitemap. Ce qu'il faut éviter n'est pas la
discrétion, c'est **l'orphelinat** : une page sans lien entrant ne peut recevoir aucune
citation tierce, et c'est de citations tierces que vient la bascule GEO.

> Pas dans le menu ≠ page cachée. **Pas de lien du tout = page orpheline.**

**Corrigé dans -128, sur des faits qu'il ne pouvait pas voir :**

1. **`?source=broche` est irréalisable.** Le livre est gelé (`BAT_FINAL`). La page&nbsp;105
   imprime `stephane-lalut.com/premier-coup` **en clair, sans QR**&nbsp;; le seul QR du
   volume est page&nbsp;106 et pointe vers `/a-propos/`. Aucun support ne peut porter le
   paramètre. → **aucun paramètre de provenance.** (`?source=kindle` serait techniquement
   possible dans l'EPUB, mais un seul canal mesuré donne un chiffre qu'on interprète mal.)

2. **Mettler est exclu des repères de la V1.** C'est la seule réserve ouverte du
   certificat documentaire : l'attribution «&nbsp;21 politiques / 96&nbsp;%&nbsp;» à
   Mettler &amp; Sides, *NYT*, 24 septembre 2012, dont **aucune page n'a pu être ouverte**.
   Un repère citable est fait pour le copier-coller — **et les réserves ne survivent pas au
   copier-coller**. Publier cet item, c'est fabriquer l'outil qui propagera l'attribution
   non vérifiée, vers des journalistes. Il entrera si la réserve tombe.

3. **La sélection se fait par densité probatoire mesurée**, pas par mémorabilité du récit.
   La liste de -128 proposait «&nbsp;prime d'activité&nbsp;» (1 occurrence dans les notes),
   «&nbsp;minimum vieillesse&nbsp;» et «&nbsp;écoles de la deuxième chance&nbsp;» (2), quand
   «&nbsp;non-recours&nbsp;» y figure 13 fois et «&nbsp;Visale&nbsp;»/«&nbsp;Garantie
   jeunes&nbsp;» 5 fois.

**Deux anomalies signalées par -128, tranchées par le contrôle local :**

- `/livres/` titré «&nbsp;Publications&nbsp;» → **non confirmée**. L'artefact déployé rend
  `<title>Livres — Anthropie — Stéphane Lalut</title>`. Ce qui a été lu vient d'un **index
  périmé**, pas du site — ce qui renforce au contraire l'argument sur IndexNow.
- «&nbsp;displace&nbsp;» répété sur la home EN → **confirmée, mal diagnostiquée**. 15
  occurrences de la racine sur la page rendue, dont **une seule** dans la source de la
  home&nbsp;: effet d'agrégation des cartes, pas coquille.

**Déjà satisfait, sans rien faire :** `robots.txt` autorise explicitement `OAI-SearchBot`,
`Claude-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `GPTBot`, `ClaudeBot`,
`Google-Extended`, `CCBot`. Et **IndexNow est automatisé** par
`.github/workflows/indexnow.yml` à chaque push touchant `content/**`.

---

## 3. Séquence de publication — par nature, pas par date

L'auteur proposait de tout construire et de ne révéler qu'à la mise en vente. **Écarté** :
une page publiée le jour du lancement a zéro autorité ce jour-là — crawl, indexation et
citations tierces prennent des semaines, et l'ancienneté d'une URL ne se rattrape pas.
Or les repères sont **vrais indépendamment du livre**. Et la page&nbsp;105 promet une
«&nbsp;adresse permanente&nbsp;» : si un lecteur du premier tirage tombe sur rien, la
promesse imprimée est rompue.

| Vague | Déclencheur | Contenu |
|---|---|---|
| **0** — faite | — | `/premier-coup/` et la fiche livre écrites en `draft: true`. Rien en ligne. |
| **1** | relecture auteur close | `/premier-coup/` seule passe en ligne. Mention «&nbsp;à paraître&nbsp;», **aucun lien d'achat**. IndexNow part au push. |
| **2** | livres **en vente** sur Amazon | fiche livre (paratexte + `/dp/` par marché) + les huit liens de maillage ci-dessous. |

### Les huit liens de la vague 2

```
/reversibilite-sociale/  →  fiche livre        (porte hors catalogue — gate 2 du linter)
/reversibilite-sociale/  →  /awp/awp-08/       (existe déjà)
fiche livre              →  /premier-coup/
fiche livre              →  /reversibilite-sociale/
/awp/awp-08/             →  fiche livre
/premier-coup/           →  fiche livre
/premier-coup/           →  /reversibilite-sociale/   (existe déjà)
/premier-coup/           →  /awp/awp-08/              (existe déjà)
```

Pas de lien dans le menu principal. Un lien discret en pied de page
«&nbsp;Ressources associées aux livres&nbsp;» est admis.

---

## 4. Ce qui reste dû

| | Fournisseur |
|---|---|
| Paratexte (description, promesse, FAQ book-scoped) | auteur, après relecture |
| ASIN broché + Kindle, liens `/dp/` par marché, prix | KDP, à la publication |
| Décision : DOI Zenodo pour le compagnon&nbsp;? | auteur — un dépôt est un acte public |
| ~~Mise en ligne du *Répertoire*~~ | ✅ **fait le 09/08** — 5&nbsp;634 mots intégrés en ligne dans `/premier-coup/`, section ①. La page passe de 1&nbsp;922 à **7&nbsp;543 mots**. Pas de cinquième objet&nbsp;: le livre promet «&nbsp;accessibles à l'adresse&nbsp;», et quatre objets suffisent. |

**Rappel de la condition -124**, qui gouverne tout le paratexte : il doit vendre *une grille
qui rend visible une dimension insuffisamment mesurée des inégalités*. **Jamais** une loi
cachée démontrée, une mesure statistique déjà construite, une causalité générale établie,
ni un programme de réforme.

---

## 5. Le bandeau d'identité — pourquoi il existe (09/08)

`/premier-coup/` est **imprimée page 105** et annoncée permanente : l'adresse est donc gelée,
courte et tapable depuis un exemplaire en main. Le contrôle a montré que la page s'ouvrait
malgré cela sur un mur de texte, **sans couverture ni titre** : le lecteur qui vient de refermer
le livre ne reconnaissait pas l'ouvrage.

Réparé sans toucher à l'URL — `layouts/premier-coup/list.html` pose un bandeau
couverture + titre + sous-titre + lien vers la fiche. **Le bandeau identifie et oriente ; il ne
vend pas.** Prix, boutons d'achat et `schema.org` restent la propriété de
`/livres/la-societe-du-premier-coup/` : une seule page vend. Le lien vers la fiche est gardé par
`{{ if not .Draft }}` — il apparaît de lui-même en vague 2.

⚠ **Trou trouvé au passage** : `assets/images/livres/` ne contenait **aucune** couverture pour ce
livre. Ce n'était donc pas le compagnon qui manquait d'image, c'était le livre entier — la fiche
elle-même s'affichait sans photo. Produite depuis le master, 1000×1599, ratio 5×8 respecté
(les autres titres sont en 6×9, ne pas déformer pour uniformiser).

`pages:` corrigé 134 → **136** dans la fiche livre.
