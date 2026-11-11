---
title: "Parcoursup : quelles sont vraiment vos chances d'être admis ?"
description: "Le taux d'accès affiché par Parcoursup décrit la session précédente, pas vos chances. Comparaison formation par formation sur les sessions {psup.sessions} : de {psup.d_de} à {psup.d_a}, {psup.d_absmed_frac} a vu son taux varier de {psup.d_absmed_pts} ou moins, mais {psup.d_t9099_b20_frac} de celles qui affichaient {psup.d_t9099_lib} en a perdu {psup.seuil_baisse_pts} ou plus. Figures, données et méthode."
chapo: "Le taux d'accès affiché par Parcoursup ne mesure pas vos chances d'être admis : il dit quelle part des candidats de l'année précédente ont pu recevoir une proposition. D'une année à la suivante, ce taux reste proche pour {psup.d_absmed_frac} ({psup.d_absmed_pts} d'écart ou moins de {psup.d_de} à {psup.d_a}) ; il change parfois beaucoup, même au-dessus de {psup.seuil_reste} %. C'est un repère utile, pas une promesse."
date: 2026-11-11
lastmod: 2026-11-11
journal:  # révisions qui changent la lecture de la page (registre interne, jamais affiché)
  - {date: 2026-11-11, texte: "Correction : dans les données ouvertes, la répartition par type de bac porte sur les élèves de terminale en position de recevoir une proposition, et non sur tous les candidats (libellé de la variable, vérifié sur le fichier) ; quatre passages corrigés le jour de la publication."}
og_title: "Parcoursup : quelles sont vraiment vos chances d'être admis ? Ce que vaut le taux d'accès — S. Lalut"
og_image: "images/og-parcoursup.jpg"
og_image_alt: "Carte de partage : « Parcoursup : quelles sont vraiment vos chances d'être admis ? » — pour quatre tranches de taux d'accès une année, une barre montre où se situait le taux des mêmes formations l'année suivante : chaque barre déborde largement sa tranche de départ."
# Quatrième onglet du bloc « École, lycée et université ». Recherche :
# D:\PRO\06_PROMOTION\RECHERCHE_RESSOURCE_UNIVERSITE_2026-11-03 (sept contre-expertises arbitrées, panel avant, protocole).
# Aucun chiffre saisi : jetons {psup.*} et shortcode psup-val (scripts/update_parcoursup.py, exports et témoin dans
# scripts/sources_parcoursup/). Les seuils (90 %, 20 points…) sont des paramètres du calcul : en jetons seuil_* dans les
# blocs citables, écrits en clair dans les titres et le corps. Français seulement : procédure et débat français
# (exclusion déclarée). À RELIRE contre les fiches Parcoursup 2027 à l'ouverture de la carte (17/12/2026) : intitulé
# « Visualiser les chiffres d'accès » et numéros d'étapes du quatrième mouvement.
lang_repli: "/en/resources/"  # pas de version anglaise (exclusion déclarée) : cible de l'onglet EN, partials/lang-cible.html
donnees: [parcoursup]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "parcoursup"
  nom: "Stabilité du taux d'accès des formations de Parcoursup d'une session à la suivante, {psup.s_premiere}-{psup.s_derniere}"
  description: "Taux d'accès publiés par le ministère chargé de l'enseignement supérieur, repris sans recalcul et comparés formation par formation entre deux sessions successives ({psup.p_n} formations de {psup.p_de} à {psup.p_a}, {psup.d_n} de {psup.d_de} à {psup.d_a}) : par tranche de taux de départ, 1er décile, médiane et 9e décile du taux de l'année suivante ; parts des formations restées à {psup.seuil_reste} % ou plus et de celles qui ont perdu {psup.seuil_baisse_pts} ou plus ; variation médiane par filière ; formations écartées de la comparaison, comptées par motif ; contrôles de sensibilité et cohorte des formations comparées sur les trois sessions."
  couverture_temporelle: "2023/2025"
  couverture_spatiale: "France"
  variables:
    - {nom: "Taux d'accès de l'année suivante par tranche de taux de départ", unite: "%", description: "1er décile, médiane et 9e décile ; part des formations entre les deux déciles ; deux transitions"}
    - {nom: "Part des formations restées à un taux élevé ou ayant fortement baissé", unite: "% des formations", description: "par tranche ; avec les effectifs"}
    - {nom: "Variation du taux d'accès par filière", unite: "points de pourcentage", description: "médiane et moyenne des variations, part des formations en baisse, corrélation des taux d'une session à l'autre"}
    - {nom: "Sens des variations de l'ensemble des formations comparées", unite: "% des formations", description: "en baisse, en hausse, inchangées ; ensemble des formations comparées et cohorte des trois sessions"}
    - {nom: "Formations écartées de la comparaison", unite: "formations", description: "par motif : nouvelle, disparue, intitulé changé, taux non publié, aucun candidat classé"}
  sources:
    - "https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup/"
    - "https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup_2024/"
    - "https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup_2023/"
  mots: ["Parcoursup", "taux d'accès", "chances d'admission", "vœux", "lycéens", "terminale", "classes préparatoires", "BTS", "BUT", "licence", "orientation", "enseignement supérieur"]
  fichiers: ["parcoursup.csv", "parcoursup.json"]
  apropos: "taux d'accès des formations de Parcoursup en France"
faq:
  - question: "Le taux d'accès est-il ma chance d'être admis ?"
    answer: "Non. Il dit quelle part des candidats de la session précédente ont pu recevoir une proposition, tous profils confondus : il ne tient compte ni de votre bac, ni de vos résultats. Et il décrit une année passée : de {psup.d_de} à {psup.d_a}, {psup.d_absmed_frac} a vu son taux varier de {psup.d_absmed_pts} ou moins, mais {psup.d_t9099_b20_frac} de celles qui affichaient {psup.d_t9099_lib} en a perdu {psup.seuil_baisse_pts} ou plus."
  - question: "Un taux d'accès de 100 % garantit-il une place ?"
    answer: "Non. Il signifie qu'à la fin de la phase principale de la session précédente, aucun candidat n'était encore en attente dans cette formation. Parmi les formations à {psup.d_t100_lib} en {psup.d_de}, {psup.d_t100_reste} % étaient encore à {psup.seuil_reste} % ou plus en {psup.d_a}, et {psup.d_t100_b20} % avaient perdu {psup.seuil_baisse_pts} ou plus."
  - question: "Un candidat resté sur liste d'attente est-il compté dans le taux d'accès ?"
    answer: "Cela dépend du moment. Un candidat encore en attente à la fin de la phase principale est compté parmi les candidats, pas parmi ceux dont le rang permettait de recevoir une proposition. Un candidat d'abord en attente, puis appelé avant la fin de cette phase, est compté parmi eux. Ce qui se passe après la phase principale n'entre pas dans le calcul du taux."
  - question: "Taux d'accès et taux d'admission, est-ce la même chose ?"
    answer: "Non. Le taux d'accès compte les candidats qui ont pu recevoir une proposition, qu'ils l'aient acceptée ou non ; la part des candidats finalement admis est bien plus faible. Exemple tiré des données publiques : dans un BUT de l'{psup.ex_etab}, en {psup.ex_session}, le taux d'accès était de {psup.ex_taux} %, et {psup.ex_adm} candidats sur {psup.ex_cand} ont été admis, soit {psup.ex_adm_part} %."
  - question: "Où trouver les chiffres qui correspondent à mon bac ?"
    answer: "Sur la fiche de la formation, dans Parcoursup, à la rubrique « Visualiser les chiffres d'accès » : elle donne le taux d'accès par type de bac, puis les possibilités d'accès selon la série et le niveau de moyenne. Les sites qui reprennent les données publiques ne disposent que de la répartition par bac des élèves de terminale qui pouvaient recevoir une proposition : une composition, pas une chance."
  - question: "Le taux affiché cette année vaudra-t-il l'an prochain ?"
    answer: "Rien ne le garantit. D'une session à la suivante, les taux d'accès sont fortement corrélés ({psup.p_pearson} de {psup.p_de} à {psup.p_a}, {psup.d_pearson} de {psup.d_de} à {psup.d_a}), mais les écarts peuvent être grands : parmi les formations à {psup.d_t6075_court} en {psup.d_de}, {psup.d_t6075_dans_frac} se situaient entre {psup.d_t6075_d1} et {psup.d_t6075_d9} % en {psup.d_a}. Ces mesures décrivent le passé ; elles ne prévoient pas la session suivante."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/parcoursup-quelles-chances-d-etre-admis.md"  # fiche de conception (règle 12)
  refonte: "2026-11-11"  # page de données nouvelle : née refondue (relecture phrase à phrase à attester avant publication)
  bloc: "ecole"
  livres: ["la-societe-du-premier-coup"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 40
  nature: "Taux d'accès publiés par le ministère, repris et comparés formation par formation sur trois sessions ; conseils courants mis à l'épreuve"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Parcoursup : quelles sont vraiment vos chances ?"
  court: "Parcoursup"
  role: "taux d'accès, 2023-2025"
reperes:  # trois repères sous le chapô, à partir de 600 px de large (partials/reperes-page.html ; maquette B+ validée par
  # l'auteur le 11/11/2026, pièces 09 et 10). Chacun reprend un résultat écrit dans sa section, avec sa période ; au
  # téléphone ils ne s'affichent pas. Aucun nombre saisi : jetons gardés par le générateur (garde 6).
  - ancre: "d-une-annee-sur-l-autre"
    fort: "{psup.d_absmed_frac}"
    texte: "a vu son taux d'accès varier de {psup.d_absmed_pts} ou moins, de {psup.d_de} à {psup.d_a}"
    precision: "{psup.d_part_absmed} % des {psup.d_n} formations comparées"
  - ancre: "au-dessus-de-90"
    fort: "{psup.d_t9099_b20_frac}"
    texte: "des formations qui affichaient {psup.d_t9099_lib} en {psup.d_de} a perdu {psup.seuil_baisse_pts} ou plus en {psup.d_a}"
    precision: "{psup.d_t9099_b20} %, soit {psup.d_t9099_b20_n} sur {psup.d_t9099_n}"
  - ancre: "selon-la-filiere"
    fort: "{psup.d_f_cpge_med_pts}"
    texte: "en classes préparatoires : la moitié des formations ont perdu {psup.d_f_cpge_perte_pts} ou plus, de {psup.d_de} à {psup.d_a}"
    precision: "{psup.d_f_cpge_n} classes comparées"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données mises à jour le {{< psup-val "date_donnees" >}}</span> Ministère chargé de l'enseignement supérieur, données ouvertes Parcoursup, sessions {{< psup-val "sessions" >}}&nbsp;; calcul de l'auteur.

## Peut-on se fier au taux d'accès de l'année précédente&nbsp;? {#se-fier-au-taux-d-acces}

Le taux d'accès est le chiffre que Parcoursup affiche sur la fiche de chaque formation. Il se rapporte à l'année précédente. Chaque formation classe ses candidats, puis les appelle dans l'ordre de ce classement, à mesure que des places se libèrent&nbsp;: le taux d'accès est la part des candidats dont le rang permettait de recevoir une proposition avant la fin de la phase principale.

<div class="encadre-exemple">
<div>
<p class="surtitre-bloc">Un exemple</p>

Un taux d'accès de {{< psup-val "ex_taux" >}}&nbsp;% signifie que, sur cent candidats, {{< psup-val "ex_taux" >}} avaient un rang qui leur permettait de recevoir une proposition. Cela ne veut pas dire que les {{< psup-val "ex_taux" >}} l'ont reçue, ni qu'ils l'ont acceptée&nbsp;: certains avaient déjà renoncé à ce vœu, d'autres ont préféré une autre formation. Pour les autres candidats, l'appel n'est pas allé jusqu'à leur rang, ou la formation ne les avait pas classés.

</div>
<div>
{{< psup-cent "ex_taux" >}}
<p class="legende-bloc">Sur 100&nbsp;candidats que le ministère retient pour ce calcul, {{< psup-val "ex_taux" >}} (cases pleines) avaient un rang qui leur permettait de recevoir une proposition.</p>
</div>
</div>

**Le taux d'accès donne donc une information sur une formation, une année passée&nbsp;; il ne donne pas de réponse sur votre candidature.** Pour s'en servir, il faut savoir à quel point il varie d'une année à l'autre, puis le rapporter à son propre profil. Nous avons comparé le taux d'accès de chaque formation d'une session à la suivante, sur les sessions {{< psup-val "sessions" >}}.

Première réponse&nbsp;: les formations les plus accessibles une année tendent à le rester l'année suivante, comme les plus sélectives. Cette stabilité d'ensemble n'empêche pas certaines formations de varier fortement. **Et elle porte sur les formations&nbsp;: elle ne dit rien de l'issue d'une candidature.**

## Que deviennent les taux d'une année sur l'autre&nbsp;? {#d-une-annee-sur-l-autre}

La comparaison porte sur {{< psup-val "p_n" >}} formations de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}} et sur {{< psup-val "d_n" >}} formations de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}&nbsp;: celles que l'on retrouve sous le même code et le même intitulé deux années de suite, et non toutes les formations proposées. Pour chaque tranche de taux d'accès une année, la figure montre où se situait le taux des mêmes formations l'année suivante.

<div class="figure-lecture">
<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/parcoursup-tranches-m.svg" width="300" height="1200">
    <img src="/img/parcoursup-tranches.svg" alt="Pour chaque tranche de taux d'accès en {{< psup-val "d_de" >}}, intervalle contenant au moins huit formations sur dix et médiane du taux d'accès des mêmes formations en {{< psup-val "d_a" >}}. {{< psup-val "d_t100_lib" >}} en {{< psup-val "d_de" >}} : de {{< psup-val "d_t100_d1" >}} à {{< psup-val "d_t100_d9" >}} %, médiane {{< psup-val "d_t100_med" >}} %. {{< psup-val "d_t9099_lib" >}} : de {{< psup-val "d_t9099_d1" >}} à {{< psup-val "d_t9099_d9" >}} %, médiane {{< psup-val "d_t9099_med" >}} %. {{< psup-val "d_t7590_lib" >}} : de {{< psup-val "d_t7590_d1" >}} à {{< psup-val "d_t7590_d9" >}} %, médiane {{< psup-val "d_t7590_med" >}} %. {{< psup-val "d_t6075_lib" >}} : de {{< psup-val "d_t6075_d1" >}} à {{< psup-val "d_t6075_d9" >}} %, médiane {{< psup-val "d_t6075_med" >}} %. {{< psup-val "d_t4060_lib" >}} : de {{< psup-val "d_t4060_d1" >}} à {{< psup-val "d_t4060_d9" >}} %, médiane {{< psup-val "d_t4060_med" >}} %. {{< psup-val "d_t2040_lib" >}} : de {{< psup-val "d_t2040_d1" >}} à {{< psup-val "d_t2040_d9" >}} %, médiane {{< psup-val "d_t2040_med" >}} %. {{< psup-val "d_t0020_lib" >}} : de {{< psup-val "d_t0020_d1" >}} à {{< psup-val "d_t0020_d9" >}} %, médiane {{< psup-val "d_t0020_med" >}} %. La même mesure de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}} est tracée en gris." width="720" height="629" loading="lazy">
  </picture>
  <figcaption>Taux d'accès l'année suivante, selon le taux de l'année de départ (ministère chargé de l'enseignement supérieur, calcul de l'auteur).</figcaption>
</figure>
<div class="figure-lecture__texte">
<div class="resultat-phrase">

**Le résultat en une phrase.** Un taux d'accès n'est pas une promesse pour l'année suivante&nbsp;: parmi les formations à {{< psup-val "d_t6075_court" >}} en {{< psup-val "d_de" >}}, {{< psup-val "d_t6075_dans_frac" >}} se situaient entre {{< psup-val "d_t6075_d1" >}} et&nbsp;{{< psup-val "d_t6075_d9" >}}&nbsp;% en {{< psup-val "d_a" >}}.

</div>

Deux choses sont à retenir, et elles vont ensemble.

<div class="cartes-paire">
<div class="carte-point">
<p class="carte-point__titre">Le taux change peu pour beaucoup de formations</p>

Pour {{< psup-val "d_absmed_frac" >}}, l'écart d'une session à la suivante est de {{< psup-val "d_absmed_pts" >}} ou moins&nbsp;: {{< psup-val "p_part_absmed" >}}&nbsp;% des formations de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}}, {{< psup-val "d_part_absmed" >}}&nbsp;% de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}.

</div>
<div class="carte-point">
<p class="carte-point__titre">Il change parfois beaucoup</p>

Parmi les formations à {{< psup-val "d_t6075_court" >}} en {{< psup-val "d_de" >}}, {{< psup-val "d_t6075_bas_frac" >}} s'est retrouvée à {{< psup-val "d_t6075_d1" >}}&nbsp;% ou moins en {{< psup-val "d_a" >}}.

</div>
</div>
</div>
</div>

**Ces intervalles décrivent ce qui s'est passé, pas ce qui se passera.** Ils se déplacent eux aussi d'une année à l'autre&nbsp;: de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}}, {{< psup-val "p_t6075_dans_frac" >}} des formations de la même tranche se situaient entre {{< psup-val "p_t6075_d1" >}} et {{< psup-val "p_t6075_d9" >}}&nbsp;% (barres grises de la figure). Et ils décrivent des groupes de formations&nbsp;: aucune barre ne dit où se trouvera, l'an prochain, une formation précise.

## Un taux supérieur à 90&nbsp;% est-il rassurant&nbsp;? {#au-dessus-de-90}

Le conseil est courant&nbsp;: au-dessus de 90&nbsp;%, un vœu serait «&nbsp;réaliste&nbsp;». Une activité que l'Onisep propose aux élèves de terminale, [«&nbsp;Évaluer son niveau d'ambition dans MonProjetSup&nbsp;»](https://reso-avenirs.onisep.fr/connaissance-de-soi-et-construction-de-son-projet/monprojetsup/evaluer-son-niveau-d-ambition-dans-monprojetsup), l'écrit à propos de ce qu'elle appelle le taux d'admission, à côté d'autres critères (le profil de l'élève, les attendus de la formation)&nbsp;: au-dessus de ce seuil, «&nbsp;on peut imaginer que ce choix de formation est réaliste&nbsp;».

Que sont devenues, un an plus tard, les formations dont le taux d'accès était de {{< psup-val "d_t9099_lib" >}}&nbsp;?

<div class="grille-reperes" role="table" aria-label="Formations dont le taux d'accès était de {{< psup-val "d_t9099_lib" >}}, un an plus tard">
<div class="grille-reperes__rang grille-reperes__tete" role="row"><span role="columnheader"></span><span role="columnheader">de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}}</span><span role="columnheader">de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}</span></div>
<div class="grille-reperes__rang" role="row"><span role="rowheader">encore à 90&nbsp;% ou plus, un an après</span><span class="grille-reperes__val" role="cell"><b>{{< psup-val "p_t9099_reste_frac" >}}</b><small>{{< psup-val "p_t9099_reste" >}}&nbsp;%, <span>soit {{< psup-val "p_t9099_reste_n" >}} sur {{< psup-val "p_t9099_n" >}}</span></small><span class="barre-part barre-part--avant" style="--v:{{< psup-val "p_t9099_reste" "css" >}}" aria-hidden="true"><i></i></span></span><span class="grille-reperes__val" role="cell"><b>{{< psup-val "d_t9099_reste_frac" >}}</b><small>{{< psup-val "d_t9099_reste" >}}&nbsp;%, <span>soit {{< psup-val "d_t9099_reste_n" >}} sur {{< psup-val "d_t9099_n" >}}</span></small><span class="barre-part" style="--v:{{< psup-val "d_t9099_reste" "css" >}}" aria-hidden="true"><i></i></span></span></div>
<div class="grille-reperes__rang" role="row"><span role="rowheader">ont perdu 20&nbsp;points ou plus</span><span class="grille-reperes__val" role="cell"><b>{{< psup-val "p_t9099_b20_frac" >}}</b><small>{{< psup-val "p_t9099_b20" >}}&nbsp;%, <span>soit {{< psup-val "p_t9099_b20_n" >}} sur {{< psup-val "p_t9099_n" >}}</span></small><span class="barre-part barre-part--avant" style="--v:{{< psup-val "p_t9099_b20" "css" >}}" aria-hidden="true"><i></i></span></span><span class="grille-reperes__val" role="cell"><b>{{< psup-val "d_t9099_b20_frac" >}}</b><small>{{< psup-val "d_t9099_b20" >}}&nbsp;%, <span>soit {{< psup-val "d_t9099_b20_n" >}} sur {{< psup-val "d_t9099_n" >}}</span></small><span class="barre-part" style="--v:{{< psup-val "d_t9099_b20" "css" >}}" aria-hidden="true"><i></i></span></span></div>
</div>

**Le seuil de 90&nbsp;% garde donc une valeur de repère, et il ne garantit rien.** Passer sous 90&nbsp;% ne veut pas dire tomber bas&nbsp;: de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}, la moitié de ces formations étaient encore à {{< psup-val "d_t9099_med" >}}&nbsp;% ou plus, et neuf sur dix à {{< psup-val "d_t9099_d1" >}}&nbsp;% ou plus. Mais {{< psup-val "p_t9099_b20_frac" >}}, puis {{< psup-val "d_t9099_b20_frac" >}}, a perdu 20&nbsp;points ou plus. **Ces résultats décrivent des formations&nbsp;: ils ne disent pas si un vœu est réaliste pour un candidat donné**, ce qui dépend aussi de son dossier.

Les formations à 100&nbsp;% bougent moins&nbsp;: {{< psup-val "p_t100_reste" >}}&nbsp;% puis {{< psup-val "d_t100_reste" >}}&nbsp;% sont restées à 90&nbsp;% ou plus, et {{< psup-val "p_t100_b20" >}}&nbsp;% puis {{< psup-val "d_t100_b20" >}}&nbsp;% ont perdu 20&nbsp;points ou plus. Un taux de 100&nbsp;% signifie qu'aucun candidat n'était encore en attente à la fin de la phase principale&nbsp;; il baisse dès que l'appel ne va plus jusqu'au dernier candidat classé.

À l'autre bout, les formations très sélectives le restent&nbsp;: parmi celles dont le taux était inférieur à 20&nbsp;%, {{< psup-val "p_cp_n" >}} sur {{< psup-val "p_cp_tot" >}}, puis {{< psup-val "d_cp_n" >}} sur {{< psup-val "d_cp_tot" >}}, atteignaient 40&nbsp;% ou plus l'année suivante.

### Selon la filière {#selon-la-filiere}

En {{< psup-val "d_a" >}}, le mouvement d'ensemble a été une baisse&nbsp;: {{< psup-val "d_baisse" >}}&nbsp;% des formations comparées ont vu leur taux d'accès reculer et {{< psup-val "d_hausse" >}}&nbsp;% l'ont vu augmenter, contre {{< psup-val "p_baisse" >}}&nbsp;% et {{< psup-val "p_hausse" >}}&nbsp;% un an plus tôt. Ce recul n'a pas été le même partout.

De {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}, la moitié des classes préparatoires ont perdu {{< psup-val "d_f_cpge_perte_pts" >}} de taux d'accès ou plus, et {{< psup-val "d_f_cpge_baisse_frac" >}} ont vu leur taux baisser ({{< psup-val "d_f_cpge_baisse" >}}&nbsp;%). En BTS, la moitié des formations ont perdu {{< psup-val "d_f_bts_perte_pts" >}} ou plus&nbsp;; en BUT, {{< psup-val "d_f_but_perte_pts" >}} ou plus&nbsp;; en licence, la variation médiane est nulle. Un an plus tôt, la variation médiane ne dépassait {{< psup-val "p_f_absmax_pts" >}} dans aucune filière.

<div class="figure-lecture">
<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/parcoursup-filieres-m.svg" width="300" height="1091">
    <img src="/img/parcoursup-filieres.svg" alt="Variation médiane du taux d'accès par filière, en points de pourcentage, de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}} puis de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}. Classes préparatoires : {{< psup-val "p_f_cpge_med" >}} puis {{< psup-val "d_f_cpge_med" >}}. BTS : {{< psup-val "p_f_bts_med" >}} puis {{< psup-val "d_f_bts_med" >}}. BUT : {{< psup-val "p_f_but_med" >}} puis {{< psup-val "d_f_but_med" >}}. Licences accès santé : {{< psup-val "p_f_las_med" >}} puis {{< psup-val "d_f_las_med" >}}. Soins infirmiers : {{< psup-val "p_f_ifsi_med" >}} puis {{< psup-val "d_f_ifsi_med" >}}. Autres formations : {{< psup-val "p_f_autre_med" >}} puis {{< psup-val "d_f_autre_med" >}}. Parcours accès santé : {{< psup-val "p_f_pass_med" >}} puis {{< psup-val "d_f_pass_med" >}}. Travail social : {{< psup-val "p_f_efts_med" >}} puis {{< psup-val "d_f_efts_med" >}}. Licences hors accès santé : {{< psup-val "p_f_licence_med" >}} puis {{< psup-val "d_f_licence_med" >}}. Écoles d'ingénieurs : {{< psup-val "p_f_ing_med" >}} puis {{< psup-val "d_f_ing_med" >}}. Écoles de commerce : {{< psup-val "p_f_com_med" >}} puis {{< psup-val "d_f_com_med" >}}." width="720" height="626" loading="lazy">
  </picture>
  <figcaption>Variation médiane du taux d'accès selon la filière, d'une session à la suivante (ministère chargé de l'enseignement supérieur, calcul de l'auteur).</figcaption>
</figure>
<div class="figure-lecture__texte">

Une médiane nulle ne veut pas dire que rien n'a bougé&nbsp;: en licence, {{< psup-val "d_f_licence_baisse" >}}&nbsp;% des formations ont vu leur taux baisser de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}.

**Pourquoi cette baisse est-elle plus forte en classes préparatoires&nbsp;? Ces données ne permettent pas de le dire, ni de savoir si elle se reproduira.** Le taux d'accès dépend des places, des candidatures, des classements et des choix des candidats, y compris de leurs renoncements&nbsp;: des résultats agrégés par formation ne séparent pas ces mécanismes.

</div>
</div>

## Et pour un candidat avec mon bac et mes résultats&nbsp;? {#mon-bac-et-mes-resultats}

Le taux d'accès d'une formation vaut pour l'ensemble de ses candidats. Les chiffres qui correspondent le mieux à un profil sont sur la fiche de la formation, dans Parcoursup. Ouvrez la rubrique «&nbsp;Visualiser les chiffres d'accès&nbsp;»&nbsp;:

<div class="fiche-etapes">
<p class="surtitre-bloc">Sur la fiche de la formation&nbsp;: «&nbsp;Visualiser les chiffres d'accès&nbsp;»</p>
<ol>
<li><span class="fiche-etapes__n">Étape&nbsp;1</span><span>Tous les candidats&nbsp;: combien ont été classés, ont pu recevoir une proposition et ont intégré la formation</span></li>
<li><span class="fiche-etapes__n">Étape&nbsp;2</span><span>Le taux d'accès pour votre type de bac (général, technologique, professionnel)</span></li>
<li><span class="fiche-etapes__n">Étape&nbsp;3</span><span>Les possibilités d'accès selon votre série et votre niveau de moyenne, calculées sur trois&nbsp;ans</span></li>
<li><span class="fiche-etapes__n">Étape&nbsp;4</span><span>Le profil des candidats admis</span></li>
</ol>
</div>

**Aucun de ces chiffres n'est la probabilité qu'un candidat en particulier soit admis.** Ils disent ce qui est arrivé à des candidats qui vous ressemblent sur un ou deux critères.

Deux autres pourcentages circulent sur les sites qui reprennent les données publiques. Ils ne se lisent pas comme une chance.

<div class="cartes-paire">
<div class="carte-point">
<p class="carte-point__titre">La part des candidats admis</p>

Exemple tiré des données publiques&nbsp;: en {{< psup-val "ex_session" >}}, un BUT de l'{{< psup-val "ex_etab" >}} comptait {{< psup-val "ex_cand" >}} candidats en phase principale, et {{< psup-val "ex_adm" >}} candidats y ont été admis, soit {{< psup-val "ex_adm_part" >}}&nbsp;%. C'est la part des candidats qui ont fini par choisir cette formation, pas la part de ceux qui pouvaient y entrer&nbsp;: son taux d'accès était de {{< psup-val "ex_taux" >}}&nbsp;%.

<div class="indicateurs-distincts">
<div class="indicateur-encadre">
<p class="surtitre-bloc">Indicateur du ministère</p>
<p class="indicateur-encadre__val">{{< psup-val "ex_taux" >}}&nbsp;%</p>
<p class="indicateur-encadre__txt">Taux d'accès&nbsp;: part des candidats dont le rang permettait de recevoir une proposition avant la fin de la phase principale. Le ministère le calcule sur les candidats scolarisés en France ou de nationalité européenne.</p>
</div>
<div class="indicateur-encadre">
<p class="surtitre-bloc">Admissions constatées</p>
<p class="indicateur-encadre__val">{{< psup-val "ex_adm" >}} sur {{< psup-val "ex_cand" >}}</p>
<p class="indicateur-encadre__txt">Soit {{< psup-val "ex_adm_part" >}}&nbsp;% des candidats de la phase principale, tous candidats confondus, d'après le fichier public arrêté en septembre.</p>
</div>
</div>
<p class="legende-bloc legende-bloc--large">Deux indicateurs, deux populations, deux dates&nbsp;: ils ne mesurent pas la même chose, et aucun n'est la chance d'un candidat.</p>
</div>
<div class="carte-point">
<p class="carte-point__titre">La part d'un type de bac</p>

Dans la même formation, sur cent élèves de terminale qui pouvaient recevoir une proposition, {{< psup-val "ex_tec" >}} préparaient un bac technologique et {{< psup-val "ex_gen" >}} un bac général. Ces nombres décrivent la composition de ce groupe, pas la chance d'un élève de terminale technologique&nbsp;: pour la connaître, il faudrait savoir combien d'élèves de terminale technologique étaient candidats. C'est le taux d'accès par type de bac, à l'étape&nbsp;2 de la fiche, qui répond à cette question&nbsp;: il ne se confond pas avec la part de ces élèves parmi ceux qui pouvaient recevoir une proposition.

<p class="legende-bloc">Sur cent élèves de terminale qui pouvaient recevoir une proposition&nbsp;:</p>
<div class="barre-composition" aria-hidden="true"><span style="--v:{{< psup-val "ex_tec" "css" >}}">{{< psup-val "ex_tec" >}} · bac technologique</span><span style="--v:{{< psup-val "ex_gen" "css" >}}">{{< psup-val "ex_gen" >}} · bac général</span></div>
</div>
</div>

## Que permettent réellement de décider ces chiffres&nbsp;? {#ce-que-ces-chiffres-permettent}

Pour chaque formation de votre liste, trois vérifications évitent de faire dire au taux d'accès plus qu'il ne dit.

<div class="liste-cartes">

1. **Situer son taux d'accès.** Regardez dans quelle tranche il se trouve, et où se sont retrouvées, un an après, les formations de cette tranche (première figure). Une formation à 95&nbsp;%, par exemple, appartient à une tranche de formations dont {{< psup-val "d_t9099_reste_frac" >}} est restée à 90&nbsp;% ou plus de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}, et dont {{< psup-val "d_t9099_b20_frac" >}} a perdu 20&nbsp;points ou plus.
2. **Lire les chiffres de votre profil sur sa fiche**&nbsp;: le taux d'accès pour votre type de bac, puis les possibilités selon votre série et votre moyenne.
3. **Regarder sa filière.** Parmi les classes préparatoires, {{< psup-val "d_f_cpge_baisse_frac" >}} ont vu leur taux baisser de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}&nbsp;; en licence, la variation médiane est nulle.

</div>

Ces vérifications ne donnent ni votre probabilité d'être admis, ni la façon de composer votre liste. **Un taux élevé est un indice favorable&nbsp;; ce n'est jamais une garantie, même à 100&nbsp;%**&nbsp;: {{< psup-val "p_t100_reste" >}}&nbsp;% puis {{< psup-val "d_t100_reste" >}}&nbsp;% des formations à 100&nbsp;% étaient encore à 90&nbsp;% ou plus l'année suivante. [Parcoursup recommande](https://www.parcoursup.gouv.fr/faq/thematiques/fonctionnement-de-parcoursup/formuler-ses-voeux) de ne pas formuler un seul vœu et de diversifier ses vœux entre formations sélectives et non sélectives&nbsp;; les résultats de cette page ne démontrent aucune stratégie de vœux.

## Comment avons-nous vérifié ces résultats&nbsp;? {#verification}

Les données sont celles que le ministère chargé de l'enseignement supérieur publie chaque année pour toutes les formations de Parcoursup, hors apprentissage. Deux sessions successives sont comparées formation par formation. Une formation est retenue si elle garde le même code et le même intitulé, si son taux d'accès est publié et si elle a classé des candidats les deux années&nbsp;: c'est le cas de {{< psup-val "p_n" >}} formations sur {{< psup-val "p_entrees" >}} de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}} ({{< psup-val "p_part_app" >}}&nbsp;%), et de {{< psup-val "d_n" >}} sur {{< psup-val "d_entrees" >}} de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}} ({{< psup-val "d_part_app" >}}&nbsp;%).

**Les résultats portent sur ces formations comparées, pas sur toutes.**

**Les intervalles d'une année ne se retrouvent qu'imparfaitement l'année suivante.** Appliqués aux formations de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}, les intervalles mesurés de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}} contenaient de {{< psup-val "val_min" >}} à {{< psup-val "val_max" >}}&nbsp;% des formations selon la tranche, alors qu'ils en contenaient de {{< psup-val "val_ref_min" >}} à {{< psup-val "val_ref_max" >}}&nbsp;% l'année où ils ont été mesurés. Pour la tranche {{< psup-val "d_t9099_lib" >}}, par exemple&nbsp;: {{< psup-val "p_t9099_dans" >}}&nbsp;% puis {{< psup-val "d_t9099_val" >}}&nbsp;%.

Trois contrôles en précisent la portée&nbsp;: la comparaison des mêmes formations sur les trois sessions, le retrait des petites formations, le retrait de celles dont le nombre de places a beaucoup changé. Ils déplacent peu les résultats, sauf pour les formations à 100&nbsp;%.

<details class="repli"><summary>Le détail des contrôles</summary>

**Qui est écarté de la comparaison.** Les formations écartées (nouvelles, disparues, renommées, sans taux publié ou sans candidat classé) sont comptées motif par motif, dans le détail des sources. Celles qui ont disparu ou changé d'intitulé étaient plus petites et plus accessibles que les formations comparées&nbsp;: leur taux d'accès médian allait de {{< psup-val "sel_taux_min" >}} à {{< psup-val "sel_taux_max" >}}&nbsp;%, contre {{< psup-val "d_sel_app_taux" >}}&nbsp;%.

**Le recul de {{< psup-val "d_a" >}} subsiste lorsqu'on compare exactement les mêmes formations sur les trois sessions.** Parmi les {{< psup-val "coh_n" >}} formations comparées les deux fois, {{< psup-val "coh_d_baisse" >}}&nbsp;% ont vu leur taux baisser de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}, contre {{< psup-val "coh_p_baisse" >}}&nbsp;% de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}}&nbsp;; sans les classes préparatoires, {{< psup-val "coh_sc_d_baisse" >}}&nbsp;% contre {{< psup-val "coh_sc_p_baisse" >}}&nbsp;%. Ce recul ne s'explique donc ni par la seule modification du périmètre des formations comparées, ni par les seules classes préparatoires. Cette comparaison ne dit rien des candidats, dont le nombre et les vœux changent chaque année.

**Les petites formations et les changements de capacité ne font pas ces résultats.** Sans les formations de moins de {{< psup-val "seuil_cand" >}} candidats, la part des formations perdant 20&nbsp;points ou plus bouge de moins d'un point dans chaque tranche, sauf pour les formations à 100&nbsp;% (de {{< psup-val "d_t100_b20" >}} à {{< psup-val "d_t100_b20_50" >}}&nbsp;% de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}). Sans les formations dont le nombre de places a varié de plus de {{< psup-val "seuil_capa" >}}&nbsp;% ({{< psup-val "p_capa_n" >}} puis {{< psup-val "d_capa_n" >}}), les repères de la première figure se déplacent d'un point au plus.

**Classes préparatoires.** De {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}, le nombre médian de candidats par classe préparatoire est passé de {{< psup-val "d_f_cpge_cand0" >}} à {{< psup-val "d_f_cpge_cand1" >}}, et le nombre médian de places est resté de {{< psup-val "d_f_cpge_places1" >}}. Ces deux médianes décrivent&nbsp;; elles ne permettent d'écarter aucune explication de la baisse.

</details>

## Ce que ces données ne disent pas {#limites}

<div class="liste-colonnes">

- **Aucune prévision, ni pour un dossier, ni pour la session de 2027.** Trois sessions décrivent une variabilité passée&nbsp;; une variation passée ne mesure pas l'incertitude à venir.
- **Le taux d'accès est repris, pas recalculé.** Le fichier public ne permet pas de le refaire. Selon le ministère, qui produit l'indicateur, son mode de calcul est le même pour les trois sessions.
- **Trois sessions seulement, dont une de recul d'ensemble.** Les causes d'une variation (places, nombre de candidats, autres vœux, renoncements) ne se séparent pas dans des données agrégées par formation.
- **Même code et même intitulé ne garantissent pas une formation inchangée**&nbsp;: ses groupes de classement, son recrutement ou ses modalités ont pu changer.
- **Une baisse de taux n'est pas un échec de candidats**&nbsp;: une formation à 80&nbsp;% place encore quatre candidats sur cinq en position de recevoir une proposition.
- **L'accès n'est pas la réussite.** Rien ici sur ce que deviennent les étudiants une fois admis&nbsp;; pour la licence, l'activité [«&nbsp;Après une première année de licence&nbsp;»](/enseignants/ecole-et-parcours/#terminale-licence) le suit sur les données du ministère.

</div>

## Questions fréquentes {#questions}

{{< faq-visible colonnes="2" >}}

{{< appel-livre slug="la-societe-du-premier-coup" sur="Ce qu'un premier choix engage dépend de ce qu'il permet de rattraper" avis="non" >}}
Cette page mesure ce que vaut un chiffre au moment de choisir&nbsp;; elle ne dit pas ce que coûte un premier choix manqué. Ce coût dépend de ce que l'on peut rattraper ensuite&nbsp;: pourquoi certains disposent-ils de plusieurs chances quand d'autres jouent leur avenir dès la première tentative&nbsp;? C'est cette inégalité qu'explore le livre.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

Ministère chargé de l'enseignement supérieur, données ouvertes Parcoursup des sessions {{< psup-val "sessions" >}}&nbsp;: le taux d'accès de chaque formation, repris tel qu'il est publié. Le détail des sources, des formations écartées et des contrôles est ci-dessous.

<details class="repli"><summary>Le détail des sources et de la méthode</summary>

**Données.** Ministère chargé de l'enseignement supérieur, sous-direction des systèmes d'information et des études statistiques (SIES), «&nbsp;Parcoursup&nbsp;: vœux de poursuite d'études et de réorientation dans l'enseignement supérieur et réponses des établissements&nbsp;», sessions [2023](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup_2023/), [2024](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup_2024/) et [2025](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup/), licence ouverte 2.0. Une ligne par formation, hors apprentissage. Les trois exports sont archivés avec leurs empreintes.

**Taux d'accès.** Définition du ministère ([méthodologie des données ouvertes, 2025](https://data.enseignementsup-recherche.gouv.fr/api/datasets/1.0/fr-esr-parcoursup/attachments/methodologie_opendata_2025pdf))&nbsp;: rapport entre le nombre de candidats dont le rang de classement ne dépasse pas celui du dernier appelé de leur groupe et le nombre de candidats ayant validé un vœu pour la formation en phase principale. Seuls les candidats scolarisés en France ou de nationalité européenne entrent dans ce calcul. Le ministère précise que ce taux ne peut pas être recalculé à partir du fichier, et que son mode de calcul est identique d'une session à l'autre pour {{< psup-val "sessions" >}}. Selon Boyer et Gossa («&nbsp;Si Parcoursup m'était compté&nbsp;», *Éducation et Socialisation*, n°&nbsp;72, 2024), il avait été modifié en 2022&nbsp;: la comparaison porte sur les trois sessions qui suivent.

**Formations écartées de la comparaison**, de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}} puis de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}&nbsp;: nouvelles, {{< psup-val "p_m_nouv" >}} puis {{< psup-val "d_m_nouv" >}}&nbsp;; disparues, {{< psup-val "p_m_disp" >}} puis {{< psup-val "d_m_disp" >}}&nbsp;; intitulé changé, {{< psup-val "p_m_intit" >}} puis {{< psup-val "d_m_intit" >}}&nbsp;; taux d'accès non publié, {{< psup-val "p_m_tauxabs" >}} puis {{< psup-val "d_m_tauxabs" >}}&nbsp;; aucun candidat classé, {{< psup-val "p_m_nonclasse" >}} puis {{< psup-val "d_m_nonclasse" >}}. De {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}, {{< psup-val "d_sel_intit_bts" >}}&nbsp;% des formations dont l'intitulé change sont des BTS, dont plusieurs diplômes ont changé de nom.

**Filières.** Une formation compte dans une filière si le ministère la classe dans cette filière les deux années. Les formations qu'il a classées dans une autre filière d'une session à l'autre ({{< psup-val "p_recl_n" >}} puis {{< psup-val "d_recl_n" >}}) sont comptées à part et ne figurent pas dans la seconde figure. «&nbsp;Licences&nbsp;» s'entend hors licences accès santé&nbsp;; «&nbsp;Autres formations&nbsp;» est la catégorie du ministère pour les formations qui n'entrent dans aucune autre.

**Tranches et intervalles.** Les tranches sont définies sur le taux de l'année de départ. L'intervalle va du 1er au 9e&nbsp;décile du taux de l'année suivante, bornes comprises&nbsp;: il contient au moins huit formations sur dix, et neuf sur dix dans les deux tranches du haut, où il touche 100&nbsp;%. Une variation s'exprime en points de pourcentage&nbsp;: un taux qui perd {{< psup-val "d_f_cpge_perte_pts" >}} passe, {{< psup-val "d_f_cpge_exemple" >}}.

**Corrélation.** D'une session à la suivante, la corrélation entre les taux d'accès est de {{< psup-val "p_pearson" >}} puis de {{< psup-val "d_pearson" >}}&nbsp;; calculée sur les rangs, de {{< psup-val "p_spearman" >}} puis de {{< psup-val "d_spearman" >}}&nbsp;; sans les formations à 0 ou 100&nbsp;%, de {{< psup-val "p_pearson_int" >}} puis de {{< psup-val "d_pearson_int" >}}. En classes préparatoires, elle passe de {{< psup-val "p_f_cpge_pearson" >}} à {{< psup-val "d_f_cpge_pearson" >}}&nbsp;; en licence, de {{< psup-val "p_f_licence_pearson" >}} à {{< psup-val "d_f_licence_pearson" >}}.

**Exemple.** {{< psup-val "ex_etab" >}}, {{< psup-val "ex_formation" >}}, session {{< psup-val "ex_session" >}}&nbsp;: nombres du fichier public, arrêtés en septembre et portant sur tous les candidats. La fiche de la formation sur Parcoursup, arrêtée à la fin de la phase principale, en donne d'autres. La répartition par type de bac est celle du fichier publié ({{< psup-val "ex_gen" >}}&nbsp;% en terminale générale, {{< psup-val "ex_tec" >}}&nbsp;% en terminale technologique, {{< psup-val "ex_pro" >}}&nbsp;% en terminale professionnelle). D'après le libellé de la variable et d'après ses valeurs dans le fichier, elle porte sur les seuls élèves de terminale en position de recevoir une proposition, alors que la définition donnée par la notice du ministère parle des candidats. Cette notice, qui prend la même formation en exemple, indique 49&nbsp;%, 50&nbsp;% et 1&nbsp;% (notice de la session 2025, lue le 11&nbsp;novembre 2026). Les autres nombres de l'exemple sont les mêmes dans les deux documents.

**Conseils cités.** Onisep, activité «&nbsp;Évaluer son niveau d'ambition dans MonProjetSup&nbsp;», lue le 10&nbsp;novembre 2026. Parcoursup, foire aux questions «&nbsp;Formuler ses vœux&nbsp;» et fiche d'une formation (rubrique «&nbsp;Visualiser les chiffres d'accès&nbsp;»), lues les 10 et 11&nbsp;novembre 2026.

Les chiffres de cette page sont **lus par un script** dans les trois exports du ministère, à l'exception des seuils (90&nbsp;%, 20&nbsp;points, 50&nbsp;candidats, 25&nbsp;% de places), qui sont des paramètres du calcul, et des taux de 95&nbsp;% et de 80&nbsp;% pris en exemple. Le taux d'accès est repris, jamais recalculé. Chaque résultat est refait par un second programme, écrit séparément et sur une autre copie du fichier de 2023&nbsp;; le script qui produit la page s'arrête si un écart dépasse un dixième de point, ou si une donnée ne remplit plus les conditions dont dépendent les principales phrases.

</details>

{{< reutiliser figures="figures_parcoursup" jeu="parcoursup" sources="ministère chargé de l'enseignement supérieur, données ouvertes Parcoursup" donnees="Par tranche de taux d'accès de l'année de départ et pour deux transitions : effectif, 1er décile, médiane et 9e décile du taux de l'année suivante, parts des formations restées à un taux élevé ou ayant fortement baissé, contrôles de sensibilité ; par filière : variation médiane et moyenne, part des formations en baisse, corrélations ; formations écartées par motif ; cohorte des formations comparées sur les trois sessions ; le même contenu existe en CSV, au format long." >}}
D'une session à la suivante, le taux d'accès d'une formation de Parcoursup varie de {{< psup-val "d_absmed_pts" >}} ou moins pour {{< psup-val "d_absmed_frac" >}}, et les taux des deux années sont fortement corrélés ({{< psup-val "p_pearson" >}} de {{< psup-val "p_de" >}} à {{< psup-val "p_a" >}}, {{< psup-val "d_pearson" >}} de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}}). Mais un taux n'est pas une promesse&nbsp;: parmi les formations affichant {{< psup-val "d_t9099_lib" >}}, {{< psup-val "p_t9099_b20_frac" >}} puis {{< psup-val "d_t9099_b20_frac" >}} ont perdu {{< psup-val "seuil_baisse_pts" >}} ou plus l'année suivante, et de {{< psup-val "d_de" >}} à {{< psup-val "d_a" >}} la moitié des classes préparatoires ont perdu {{< psup-val "d_f_cpge_perte_pts" >}} ou plus. Ces mesures décrivent des groupes de formations sur {{< psup-val "n_sessions" >}} sessions&nbsp;; elles ne prévoient ni le taux d'une formation, ni l'admission d'un candidat.
{{< /reutiliser >}}
