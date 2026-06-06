# Notes de référence — Publications et SCSS

> **À lire avant** : ajout de publication, modification de vignette, 
> ou intervention sur le SCSS de cartes BEM.
> Dernière mise à jour : mai 2026 (après bascule complète du corpus en typographique).

## 1. Front matter publication — checklist

Toute fiche dans `content/publications/*.md` suit ce front matter :

```yaml
---
title: "Titre de l'article"
date: 2026-MM-DD
revue: "Nom canonique de la revue"      # voir table §2
source_type: "Catégorie"                  # voir table §2 — UNIQUEMENT si image_type: logo
url_externe: "https://..."
image: "/img/publications/..."
image_type: "photo"                        # OU "logo"
chapo: "Chapô français."
chapo_en: "English chapeau."
related: [awp-XX]
related_book: [slug-livre]
---
```

### Règles

0. **Par défaut, toutes les nouvelles publications utilisent `image_type: logo`**
   (rendu typographique). Le mode `image_type: photo` reste techniquement
   supporté mais désormais déprécié — ne l'utiliser qu'en cas de décision
   éditoriale explicite (ex. visuel d'article particulièrement signifiant
   que l'on souhaite mettre en avant).
1. **`image_type: logo`** → `source_type` OBLIGATOIRE, valeur tirée de §2.
2. **Revue absente de §2** → suivre la procédure §3 avant publication.
3. **Revue universitaire à comité de lecture** → catégorie réservée 
   « Académique », à activer avec accord explicite (voir §4).
4. **`image_type: photo` (mode déprécié)** → ne PAS remplir `source_type`
   (champ ignoré).
5. **Synchronisation `data/works.yaml`** → publier une fiche
   `content/publications/*.md` implique de mettre à jour, **dans le même
   commit**, l'entrée correspondante de `data/works.yaml` (`status`
   `accepted_pending`/`in_review` → `published`, renseigner `url`,
   `publication_date`, `source_type`, `chapo.fr/.en`) et de bumper
   `meta.last_updated`. Le registre étant maintenu manuellement, c'est le
   seul garde-fou contre sa dérive par rapport au contenu en ligne.
   *(Classe de défaut constatée mai 2026 : entrées EAN restées
   `accepted_pending` après publication.)*
6. **Typographie des chapôs — titres d'œuvres en italique.** Les chapôs
   (`chapo` / `chapo_en`) sont rendus en **texte brut** par
   `layouts/partials/publication-card.html` (sortie `| safeHTML`, **non
   markdownifiée**). Pour mettre un titre de livre en italique — convention
   éditoriale française — utiliser `<em>Titre</em>`, **jamais** d'astérisques
   markdown `*Titre*` (qui s'afficheraient littéralement sur la carte).
   Appliquer le même balisage dans l'entrée `data/works.yaml` miroir.
   Contrôle post-build : `grep "&lt;em&gt;" public/publications/index.html`
   doit renvoyer `0`.
   *(Bug constaté mai 2026 : astérisques littérales sur la carte Welgryn.)*

## 2. Table de mapping revue → source_type

Établie d'après l'auto-définition officielle de chaque source 
(rubrique « Qui sommes-nous » + Wikipédia), validée mai 2026.

| Nom canonique             | source_type   | Note                                        |
|---------------------------|---------------|---------------------------------------------|
| Alternatives Économiques  | `Magazine`    | Mensuel + site, auto-désigné magazine       |
| En attendant Nadeau       | `Revue`       | Choix éditorial Stéphane (Wikipédia : journal) |
| La Grande Conversation    | `Revue`       | Auto-désignée « la revue intellectuelle et politique de Terra Nova » |
| La Vie des Idées          | `Revue`       | Auto-désigné « la revue » sur leur site     |
| Le Temps                  | `Quotidien`   | Quotidien suisse romand                     |
| Lectures                  | `Revue`       | Revue électronique OpenEdition              |
| Mediapart                 | `Journal`     | Journal en ligne, auto-désigné              |
| Nonfiction                | `Portail`     | Slogan officiel : « Le portail des livres » |
| Revue de la régulation    | `Revue`       | Le terme est dans le titre                  |
| Terrestres                | `Revue`       | Slogan : « La revue des écologies radicales » |

### Catégories actuelles
`Revue` · `Magazine` · `Quotidien` · `Journal` · `Portail`

### Catégorie réservée
`Académique` — pour revues universitaires à comité de lecture 
(à activer avec accord explicite, voir §4).

## 3. Qualification d'une nouvelle source

Quand une publication paraît dans une revue absente de §2 :

1. Ouvrir la rubrique « Qui sommes-nous » officielle de la source.
2. Croiser avec la fiche Wikipédia francophone.
3. Identifier le terme dominant et auto-défini (revue, journal, 
   magazine, quotidien, portail, site…).
4. Choisir le `source_type` qui correspond à ce terme dans nos 
   catégories existantes.
5. Si aucune catégorie existante ne convient, NE PAS inventer — 
   demander arbitrage avant publication.
6. Une fois validé, ajouter la ligne à la table §2.

## 4. Bascule vers « Académique »

La catégorie `Académique` est réservée aux revues universitaires à 
comité de lecture (peer-reviewed). Quand la première fiche concernée 
arrive (ex. Droit et Société, Revue économique, Annales HSS) :

- NE PAS basculer unilatéralement.
- Demander arbitrage : faut-il reclasser rétroactivement Lectures 
  et Revue de la régulation (qui sont objectivement académiques) 
  ou maintenir leur étiquette `Revue` par cohérence d'usage ?
- Une fois la décision prise, mettre à jour §2 ET les fiches existantes 
  concernées en un seul commit atomique.

## 5. Règle d'or SCSS BEM

**Bug identifié en mai 2026 :** la syntaxe imbriquée `&__element` 
à l'intérieur d'un sélecteur modifier `--variant` produit une 
concaténation indésirable.

### ❌ INCORRECT

```scss
.pub-thumb--logo {
  &__name { font-size: 22px; }
  // compile en .pub-thumb--logo__name
  // → classe INEXISTANTE dans le HTML
  // → règle ne s'applique JAMAIS
}
```

### ✅ CORRECT

```scss
.pub-thumb--logo {
  .pub-thumb__name { font-size: 22px; }
  // compile en .pub-thumb--logo .pub-thumb__name
  // → sélecteur descendant qui MATCHE le HTML
}
```

### Vérification rapide après build

Quand on intervient sur un sélecteur modifier BEM, ouvrir le CSS 
compilé et chercher la classe attendue :

```bash
grep -E "pub-thumb--logo[^ ]*\.pub-thumb__" public/css/style.*.css
```

Si la classe attendue est absente ou compile vers un nom inattendu 
(ex. `.parent--mod__element`), c'est ce piège.

## 6. Règles d'or préservées

Ces règles sont intangibles et ont précédence sur toute optimisation :

- **Cadre vignette** : `.pub-thumb` à 160×107px, `border-radius: 8px`. 
  Ne JAMAIS modifier width/height/radius.
- **Vignettes-photos** : ne jamais affecter le rendu de `image_type: photo`
  lors de modifications sur les logos.
- **Meta sociales et Schema.org** : `og:image`, `twitter:image`, JSON-LD 
  ne dépendent pas de `Params.image` des publications (ils pointent vers 
  l'image globale du site). Préserver ce comportement.
- **Hreflang et badge `In French`** sur /en/ : ne pas casser lors de 
  refontes sur les listes.

---

*Ce fichier est versionné dans le repo. Toute modification de la 
table §2 ou des règles §1, §3, §4 doit faire l'objet d'un commit 
atomique séparé avec préfixe `docs:` dans le message.*
