# Arborescence et liens du dossier dette publique — FR / EN (contre-expertise)

Relevé du 30/09/2026 (parties 1 à 4 régénérées après les corrections de traduction du même jour), sur signalement de l'auteur : « *Why does public debt rise?* renvoie sur la page française ;
d'autres problèmes de lien sur la page anglaise des ressources ». Parties 1 à 4 **générées** depuis le site
construit localement (`docs/audit-liens/arborescence_dossier_dette.py`), jamais écrites à la main.

## 0. Diagnostic : ce que voit le lecteur en ligne, et pourquoi

| | Site **en ligne** (dernier déploiement `b73b3cc`) | Site **local** (`d99f9d9`, après corrections de traduction) |
|---|---|---|
| `/en/why-does-public-debt-rise/` | **404** | page anglaise |
| `/en/who-really-pays-public-debt/` | **404** | page anglaise |
| `/en/resources/` → « Why does public debt rise? » | lien vers **`/pourquoi-la-dette-publique-augmente/`** (français, marqué « in French ») | lien vers `/en/why-does-public-debt-rise/` |
| `/en/resources/` → « Who pays », « Elsewhere » | liens vers les pages **françaises** | liens vers les pages anglaises |
| Barre d'onglets de `/en/cost-of-french-public-debt/` | volets 1, 3 et 4 **en français** | volets 1, 3 et 4 en anglais |

**Cause unique** : la version anglaise du dossier (commit `77898a7`) n'est pas encore publiée. Le site en ligne
applique fidèlement l'état antérieur — trois volets n'existaient qu'en français, l'index et la barre les
signalaient « in French ». Rien n'est cassé en ligne ; tout ce qui manque arrive avec le push.

## Corrections faites pendant cet audit

1. **Lien vers le livre depuis une page anglaise** : le livre n'existe qu'en français ; le gabarit
   `appel-livre.html` déclare désormais `hreflang` dès que la fiche du livre n'est pas dans la langue de la page
   (4 pages du dossier EN, et toute page future).
2. **Sélecteur « Version française / English version » du pied de page** : `hreflang` ajouté
   (`partials/footer.html`), sur tout le site.
3. Avant l'audit, pendant l'intégration : terme unique « interest-growth effect » (page et figures) ;
   `en_francais` retiré des trois pages françaises désormais traduites.

## Points laissés, et pourquoi

- **Deux liens de texte** de `/en/who-really-pays-public-debt/` vers les Prolongements français (collectivités,
  générations futures) : Markdown ne porte pas `hreflang` ; la mention **« (in French) »** suit chaque lien. Les
  cartes « Prolongements » de la même page portent, elles, `hreflang="fr"`.
- **Hors dossier** : fiches des livres (26 liens depuis l'accueil et « À propos » anglais, pages qui n'existent
  qu'en français, souvent étiquetées « In French ») ; boutons « FR » des AWP anglais (16) ; `/premier-coup/` (1).
  Aucun ne mène à une mauvaise page ; ils ne déclarent pas `hreflang`.
- **Couverture GEO** : « Pourquoi » et « Et ailleurs », FR et EN, sans lien source vers `/awp/` ou `/livres/`
  (l'appel au livre passe par un shortcode que `check-geo-coverage.py` ne lit pas) — signal préexistant.

## Questions posées à la contre-expertise

1. L'arborescence (4 volets × 2 langues, index par langue, Prolongements en français seulement) est-elle
   cohérente pour un lecteur anglophone ? Les Prolongements doivent-ils être traduits, ou retirés des pages
   anglaises ?
2. Un lien anglais vers une page qui n'existe qu'en français (livre, Prolongements) : suffit-il de l'étiqueter
   « (in French) » + `hreflang`, ou faut-il une page d'atterrissage anglaise ?
3. Que manque-t-il au contrôle ci-dessous pour être tenu pour complet ?

**Décision déjà prise, non à rouvrir sauf erreur** : l'URL `/en/why-does-public-debt-rise/` (sans « French »,
alors que le titre dit « Why does French public debt rise? ») est gardée — même forme que les deux autres volets
traduits (`/en/who-really-pays-public-debt/`, `/en/public-debt-international-comparison/`) ; seule la page Coût,
antérieure, porte « french ». Figures, cartes de partage et barre d'onglets la citent déjà.


## 1. Les pages et leurs paires de langue

| Volet | Page FR | Titre FR | Page EN | Titre EN | alternate FR→EN | alternate EN→FR | carte FR | carte EN |
|---|---|---|---|---|---|---|---|---|
| 1. Pourquoi elle augmente | `/pourquoi-la-dette-publique-augmente/` | Pourquoi la dette publique augmente-t-elle ? | `/en/why-does-public-debt-rise/` | Why does French public debt rise? | ✅ | ✅ | `/images/og-dette-dynamique.jpg` | `/images/og-dette-dynamique-en.jpg` |
| 2. Combien coûte | `/cout-de-la-dette-publique/` | Combien coûte la dette publique ? | `/en/cost-of-french-public-debt/` | What does French public debt actually cost? | ✅ | ✅ | `/images/og-cout-dette.jpg` | `/images/og-cout-dette-en.jpg` |
| 3. Qui paie | `/qui-paie-la-dette-publique/` | Qui paie vraiment la dette publique ? | `/en/who-really-pays-public-debt/` | Who really pays for public debt? | ✅ | ✅ | `/images/og-qui-paie-dette.jpg` | `/images/og-qui-paie-dette-en.jpg` |
| 4. Et ailleurs | `/dette-publique-comparaison-internationale/` | Dette publique : pourquoi 100 % du PIB ne pèse pas partout de la même façon | `/en/public-debt-international-comparison/` | Public debt: why 100% of GDP does not carry the same burden everywhere | ✅ | ✅ | `/images/og-dette-monde.jpg` | `/images/og-dette-monde-en.jpg` |

## 2. Barre d'onglets et liens entre volets (chaque page → les trois autres)

| Page | → volet 1 | → volet 2 | → volet 3 | → volet 4 | même langue ? |
|---|---|---|---|---|---|
| `/pourquoi-la-dette-publique-augmente/` | (page) | ✅ /cout-de-la-dette-publique/ | ✅ /qui-paie-la-dette-publique/ | ✅ /dette-publique-comparaison-internationale/ | ✅ |
| `/en/why-does-public-debt-rise/` | (page) | ✅ /en/cost-of-french-public-debt/ | ✅ /en/who-really-pays-public-debt/ | ✅ /en/public-debt-international-comparison/ | ✅ |
| `/cout-de-la-dette-publique/` | ✅ /pourquoi-la-dette-publique-augmente/ | (page) | ✅ /qui-paie-la-dette-publique/ | ✅ /dette-publique-comparaison-internationale/ | ✅ |
| `/en/cost-of-french-public-debt/` | ✅ /en/why-does-public-debt-rise/ | (page) | ✅ /en/who-really-pays-public-debt/ | ✅ /en/public-debt-international-comparison/ | ✅ |
| `/qui-paie-la-dette-publique/` | ✅ /pourquoi-la-dette-publique-augmente/ | ✅ /cout-de-la-dette-publique/ | (page) | ✅ /dette-publique-comparaison-internationale/ | ✅ |
| `/en/who-really-pays-public-debt/` | ✅ /en/why-does-public-debt-rise/ | ✅ /en/cost-of-french-public-debt/ | (page) | ✅ /en/public-debt-international-comparison/ | ✅ |
| `/dette-publique-comparaison-internationale/` | ✅ /pourquoi-la-dette-publique-augmente/ | ✅ /cout-de-la-dette-publique/ | ✅ /qui-paie-la-dette-publique/ | (page) | ✅ |
| `/en/public-debt-international-comparison/` | ✅ /en/why-does-public-debt-rise/ | ✅ /en/cost-of-french-public-debt/ | ✅ /en/who-really-pays-public-debt/ | (page) | ✅ |

## 3. Prolongements, livre, index des ressources

| Page | Prolongements (collectivités, générations) | Livre | Index des ressources de la même langue |
|---|---|---|---|
| `/pourquoi-la-dette-publique-augmente/` | — | sans hreflang | ✅ |
| `/en/why-does-public-debt-rise/` | — | hreflang | ✅ |
| `/cout-de-la-dette-publique/` | — | sans hreflang | ✅ |
| `/en/cost-of-french-public-debt/` | — | hreflang | ✅ |
| `/qui-paie-la-dette-publique/` | /dette-publique-collectivites-locales/, /dette-publique-generations-futures/ | sans hreflang | ✅ |
| `/en/who-really-pays-public-debt/` | /dette-publique-collectivites-locales/, /dette-publique-collectivites-locales/ (hreflang), /dette-publique-generations-futures/, /dette-publique-generations-futures/ (hreflang) | hreflang | ✅ |
| `/dette-publique-comparaison-internationale/` | — | sans hreflang | ✅ |
| `/en/public-debt-international-comparison/` | — | hreflang | ✅ |

### Index des ressources : entrées du dossier dette

- `/ressources/` :
  - ✅ `/pourquoi-la-dette-publique-augmente/` — Pourquoi la dette publique augmente-t-elle ? 
  - ✅ `/cout-de-la-dette-publique/` — Combien coûte la dette publique ? 
  - ✅ `/qui-paie-la-dette-publique/` — Qui paie vraiment la dette publique ? 
  - ✅ `/dette-publique-comparaison-internationale/` — Dette publique : pourquoi 100 % du PIB ne pèse pas 
- `/en/resources/` :
  - ✅ `/en/why-does-public-debt-rise/` — Why does French public debt rise? 
  - ✅ `/en/cost-of-french-public-debt/` — What does French public debt actually cost? 
  - ✅ `/en/who-really-pays-public-debt/` — Who really pays for public debt? 
  - ✅ `/en/public-debt-international-comparison/` — Public debt: why 100% of GDP does not carry the sa 

## 4. Audit de tous les liens du site construit

- Pages lues : **107**.
- Liens internes cassés (page ou fichier absent) : **0**.
- Ancres absentes dans la page cible : **0**.
- Alternates de langue non réciproques ou vers une page absente : **0**.
- Liens d'une page anglaise vers une page française **sans `hreflang`** : **45**, répartis ainsi :
  - autre : **1**
  - dossier dette : **2** — `/en/who-really-pays-public-debt/` → `/dette-publique-generations-futures/` (« Is public debt a burden on future generations ») ; `/en/who-really-pays-public-debt/` → `/dette-publique-collectivites-locales/` (« Public debt: why are local authorities the ad »)
  - fiches des livres (français seulement) : **26**
  - sélecteurs « FR » des AWP anglais : **16**

## Méthode

- **Audit** : `docs/audit-liens/audit_liens.py <build> <sortie.json>` lit toutes les pages HTML d'un build
  `hugo --minify` (107 pages) : pour chaque lien interne, cible présente dans le build, ancre présente dans la page
  cible, langue de la cible (attribut `lang` de `<html>`) comparée à celle de la page source, présence de
  `hreflang` ; réciprocité des `<link rel=alternate hreflang>`. Aucun réseau.
- **Témoin positif** : trois défauts injectés dans une copie du build (lien vers une page inexistante, ancre
  fantôme, image absente) → **3 détectés** (2 cibles absentes, 1 ancre). Le « 0 lien cassé » est donc un
  résultat, non un silence.
- **Arborescence** : `docs/audit-liens/arborescence_dossier_dette.py <build> <audit.json> <sortie.md>` produit les
  parties 1 à 4 à partir du même build.
- **Rendu mobile** (mesuré le 30/09, cadre de 390 px, feuille de style chargée) : 4 pages anglaises du dossier sans
  débordement horizontal, replis ouverts.
- **Limite** : l'audit porte sur le build local ; le site en ligne a été relevé à part (partie 0) par requêtes
  HTTP. Les liens **externes** ne sont pas contrôlés ici.
- **Condition de mort** des deux scripts : ils servent ce relevé et sa contre-expertise ; ils ne sont branchés sur
  aucun contrôle bloquant. À retirer une fois l'arbitrage exécuté, sauf décision de les promouvoir en contrôle
  (R2 : qu'ils prouvent alors leur utilité présente).
