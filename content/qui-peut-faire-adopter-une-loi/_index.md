---
title: "Qui peut faire adopter une loi ?"
description: "Le Parlement vote la loi, mais qui en a l'initiative ? L'origine des lois ordinaires promulguées sous les trois dernières législatures complètes, rapprochée loi par loi entre l'Assemblée nationale, le Sénat et le Journal officiel, et les engagements de responsabilité de l'article 49, alinéa 3. Données ouvertes."
chapo: "Le Parlement vote la loi ; l'initiative appartient concurremment au Premier ministre et aux parlementaires. Parmi les lois ordinaires promulguées, {ado.P14} sur {ado.N14} sont d'origine parlementaire sous la XIVe législature, {ado.P15} sur {ado.N15} sous la XVe et {ado.P16} sur {ado.N16} sous la XVIe. Le Gouvernement peut aussi faire considérer un texte comme adopté sans vote sur l'ensemble, en engageant sa responsabilité : sous la XVIe législature, il l'a fait {ado.E16} fois, toujours sur des textes financiers."
date: 2026-10-06
lastmod: 2026-10-06
donnees: [promesses_adopter]
og_title: "Qui peut faire adopter une loi ? — l'origine des lois votées et l'article 49.3 — S. Lalut"
og_image: "images/og-adopter-promesse.jpg"
og_image_alt: "Carte de partage : qui est à l'origine des lois ordinaires promulguées, par législature, de la XIVe à la XVIe : projets du Gouvernement, propositions déposées à l'Assemblée nationale et au Sénat."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_adopter"
  nom: "Origine des lois promulguées de 2012 à 2026 et engagements de responsabilité (art. 49, al. 3)"
  description: "Origine formelle au dépôt initial (projet du Gouvernement, proposition déposée à l'Assemblée nationale ou au Sénat) des lois ordinaires promulguées de la XIVe à la XVIIe législature, rapprochée loi par loi entre les données de l'Assemblée nationale, la base Dosleg du Sénat et le Journal officiel ; lois par session de 2017-2018 à 2024-2025 ; engagements de responsabilité du Gouvernement sur un texte (art. 49, al. 3) et motions de censure, par législature."
  couverture_temporelle: "2012/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Lois ordinaires promulguées par origine", unite: "lois"}
    - {nom: "Engagements de responsabilité (art. 49, al. 3)", unite: "engagements"}
  sources:
    - "https://data.assemblee-nationale.fr/"
    - "https://data.senat.fr/dosleg/"
    - "https://www.legifrance.gouv.fr/constitution"
  mots: ["loi", "proposition de loi", "projet de loi", "Parlement", "article 49.3", "Assemblée nationale", "Sénat", "promesses"]
  fichiers: ["promesses_adopter.csv", "promesses_adopter.json"]
faq:
  - question: "Qui peut proposer une loi en France ?"
    answer: "Selon l'article 39 de la Constitution, « {ado.cit_art39} » Un texte du Gouvernement est un projet de loi ; un texte d'un député ou d'un sénateur est une proposition de loi. Sous la XVIe législature, {ado.P16} des {ado.N16} lois ordinaires promulguées étaient issues d'une proposition, {ado.G16} d'un projet."
  - question: "Les lois votées viennent-elles surtout du Gouvernement ?"
    answer: "Cela dépend de la législature. Parmi les lois ordinaires promulguées, {ado.G14} sur {ado.N14} venaient d'un projet du Gouvernement sous la XIVe législature, {ado.G15} sur {ado.N15} sous la XVe et {ado.G16} sur {ado.N16} sous la XVIe. C'est l'origine formelle, au dépôt du texte : elle ne mesure pas l'influence du Gouvernement sur une proposition, ni les amendements du Parlement sur un projet."
  - question: "Combien de fois l'article 49.3 a-t-il été utilisé ?"
    answer: "Le Gouvernement a engagé sa responsabilité sur un texte {ado.E14} fois sous la XIVe législature, sur {ado.Etextes14} projets de loi, {ado.E15} fois sous la XVe et {ado.E16} fois sous la XVIe, toutes sur des textes financiers, en comptant un engagement par texte et par étape de lecture. Aucune motion de censure n'a été adoptée sur ces engagements ; sous la XVIIe législature, une motion a été adoptée sur l'engagement du {ado.censure_date}."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 20
  nature: "Données de l'Assemblée nationale, du Sénat et du Journal officiel, rapprochées loi par loi ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Qui peut faire adopter une loi ?"
  court: "Adopter"
  role: "initiative, vote et 49.3"
---

{{< reutiliser-ancre >}}

Une promesse qui passe par la loi doit trouver une majorité. La Constitution le dit en une phrase&nbsp;: «&nbsp;{{< ado-val "cit_art24" >}}&nbsp;» (art.&nbsp;24). Elle partage l'initiative&nbsp;: «&nbsp;{{< ado-val "cit_art39" >}}&nbsp;» (art.&nbsp;39). Cette page compte, loi par loi, qui a déposé les lois promulguées depuis 2012, et combien de fois le Gouvernement a fait adopter un texte en engageant sa responsabilité. Tous les nombres viennent des données publiques de l'Assemblée nationale, du Sénat et du Journal officiel, rapprochées loi par loi, et aucun n'est saisi à la main.

**Réponse courte.** Le Parlement vote la loi, mais le texte voté peut venir du Gouvernement ou d'un parlementaire. Sous la XVIe législature, {{< ado-val "P16" >}} des {{< ado-val "N16" >}} lois ordinaires promulguées étaient issues d'une proposition de loi. Et le Gouvernement peut faire considérer un texte comme adopté sans vote sur l'ensemble, sauf si une motion de censure le renverse.

## Qui est à l'origine des lois votées&nbsp;? {#origine-des-lois}

{{< figure-svg fichier="adopter-origine" alt="Barres horizontales par législature, de la XIVe à la XVIIe en cours : lois ordinaires issues d'un projet du Gouvernement, d'une proposition déposée à l'Assemblée nationale, d'une proposition déposée au Sénat ; un trait marque la moitié des lois. La part d'origine parlementaire est sous la moitié pour la XIVe et au-dessus pour les suivantes. Les valeurs sont dans le tableau sous la figure." >}}Lois ordinaires promulguées, rattachées à la législature de leur promulgation, selon l'origine du texte au dépôt initial. Les lois qui autorisent un traité sont exclues&nbsp;; les lois de finances, de financement de la sécurité sociale et organiques sont présentées à part.{{< /figure-svg >}}

{{< fig-actions id="origine" >}}

{{< ado-tableau "lois" "Les valeurs de la figure en tableau" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Parmi les lois ordinaires promulguées, {{< ado-val "P14" >}} sur {{< ado-val "N14" >}} sont d'origine parlementaire sous la XIVe législature, {{< ado-val "P15" >}} sur {{< ado-val "N15" >}} sous la XVe et {{< ado-val "P16" >}} sur {{< ado-val "N16" >}} sous la XVIe.

</div>

C'est moins de la moitié sous la XIVe législature, plus de la moitié sous la XVe et la XVIe, même en ne retenant, pour la XVe, que les {{< ado-val "Pmin15" >}} lois dont l'origine est établie par les deux sources. Les lois de finances et de financement de la sécurité sociale, elles, viennent toutes d'un projet du Gouvernement.

**Ce que l'origine ne dit pas.** Elle dit qui a déposé le texte, non qui l'a voulu ni ce qu'il est devenu. Une proposition de loi peut être soutenue, amendée ou réécrite à la demande du Gouvernement&nbsp;; un projet peut être profondément modifié par le Parlement. Aucune de ces séries ne mesure ces influences.

<details class="repli"><summary>Ce qui a été vérifié, et comment</summary>

Chaque loi promulguée depuis juin 2012 est rapprochée, par son numéro au Journal officiel, entre les données ouvertes de l'Assemblée nationale et la base Dosleg du Sénat. Quand les deux sources la connaissent, elles donnent la même origine pour toutes les lois. Certaines lois de la XIVe et de la XVe législatures manquent aux fichiers de l'Assemblée, parce que leur dossier a été ouvert sous la législature précédente&nbsp;: leur origine ne repose que sur le Sénat, d'où la borne «&nbsp;au moins&nbsp;» du tableau.

Deux contrôles viennent d'ailleurs. Session par session, de 2017-2018 à 2024-2025, le nombre de lois promulguées hors traités est exactement celui que compte le baromètre de l'application des lois, publié par l'Assemblée nationale à partir des données de la DILA. Et le Sénat écrit, pour 2024-2025&nbsp;: «&nbsp;{{< ado-val "cit_senat_origine" >}}&nbsp;»&nbsp;; le décompte loi par loi donne {{< ado-val "s2425_P" >}} lois d'origine parlementaire sur {{< ado-val "s2425_N" >}}.

{{< ado-tableau "sessions" "Par session, toutes natures sauf les traités" >}}

</details>

## Le Gouvernement peut-il faire adopter un texte sans vote&nbsp;? {#article-49-3}

Oui, à une condition&nbsp;: que l'Assemblée ne le renverse pas. Selon l'article&nbsp;49 de la Constitution, «&nbsp;{{< ado-val "cit_art49a" >}}&nbsp;» Hors de ces textes, «&nbsp;{{< ado-val "cit_art49b" >}}&nbsp;»

{{< figure-svg fichier="adopter-493" alt="Barres horizontales par législature : engagements de responsabilité sur un texte financier et sur un autre texte. Les engagements de la XIVe et de la XVe portent sur d'autres textes ; ceux de la XVIe et de la XVIIe en cours portent tous sur des textes financiers. Les valeurs sont dans le tableau sous la figure." >}}Engagements de responsabilité du Gouvernement sur un texte, un par texte et par étape de lecture. Texte financier&nbsp;: loi de finances, de financement de la sécurité sociale ou de programmation des finances publiques.{{< /figure-svg >}}

{{< fig-actions id="493" >}}

{{< ado-tableau "engagements" "Les valeurs de la figure en tableau" >}}

Sous la XIVe législature, le Gouvernement a engagé sa responsabilité {{< ado-val "E14" >}} fois, sur {{< ado-val "Etextes14" >}} projets de loi qui n'étaient pas des textes financiers&nbsp;; sous la XVe, {{< ado-val "E15" >}} fois&nbsp;; sous la XVIe, {{< ado-val "E16" >}} fois, toutes sur des textes financiers. La fiche de l'Assemblée nationale consacrée à cette procédure donne les mêmes nombres&nbsp;: «&nbsp;{{< ado-val "cit_fiche64" >}}&nbsp;»

Aucune motion de censure n'a été adoptée sur ces engagements, de la XIVe à la XVIe législature. Sous la XVIIe, après l'engagement du {{< ado-val "censure_date" >}}, «&nbsp;{{< ado-val "cit_censure" >}}&nbsp;» (même fiche)&nbsp;: le texte n'a pas été adopté par cette voie.

<details class="repli"><summary>Ce qui a été vérifié, et comment</summary>

Les engagements sont lus dans les dossiers législatifs de l'Assemblée nationale, et comptés deux fois par deux voies différentes du même producteur, avec les mêmes dates. Ils sont comparés, session par session, aux bulletins statistiques de l'Assemblée&nbsp;: mêmes nombres d'engagements et de motions. Une seule date diffère, d'un jour, pour un engagement de novembre 2022&nbsp;; le compte rendu officiel de la séance confirme la date des données. Pour quelques motions, les données ne contiennent pas l'acte de vote&nbsp;; les bulletins donnent leurs scrutins, tous sous la majorité requise.

</details>

## Ce que cette page ne dit pas {#limites}

Elle ne mesure pas l'influence du Gouvernement sur les propositions de loi, ni celle du Parlement sur les projets&nbsp;: l'origine d'une loi n'est pas son contenu. Elle ne relie pas le nombre d'engagements de responsabilité à la composition de l'Assemblée&nbsp;: une coïncidence de dates n'établit pas un lien. Elle ne dit pas encore combien de propositions de loi n'arrivent jamais en séance&nbsp;: le décompte des dépôts à l'Assemblée ne concorde pas exactement avec celui de ses bulletins statistiques, et rien n'est publié tant que l'écart n'est pas expliqué.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Ce qu'il faut faire voter" avis="non" >}}
Cette page dit qui dépose les lois et comment le Gouvernement peut les faire adopter. Le livre suit neuf promesses écrites, datées et signées, le long de la chaîne qui va de la décision à son résultat&nbsp;: ce qu'un président décide dans sa propre chaîne de pouvoir, ce qu'il doit faire voter, ce qu'il doit négocier, et ce qui ne dépendra jamais de lui. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Assemblée nationale**, données ouvertes des dossiers législatifs des XIVe à XVIIe législatures (version du {{< ado-val "releve" >}})&nbsp;; bulletins statistiques annuels&nbsp;; fiche de synthèse n°&nbsp;64 sur l'engagement de la responsabilité du Gouvernement.

**Sénat**, base Dosleg (version du {{< ado-val "releve" >}})&nbsp;; rapport d'information n°&nbsp;802 (2025-2026) sur l'application des lois, p.&nbsp;44.

**Journal officiel**, données de la DILA&nbsp;; **Constitution**, art.&nbsp;24, 39, 48 et 49, lus sur Légifrance (API).

Les chiffres, les citations, les contrôles et les figures sont produits par un script unique&nbsp;; chaque citation est vérifiée mot pour mot dans son document, et aucun chiffre de cette page n'est saisi à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_adopter.csv), en format long&nbsp;; [JSON](/promesses_adopter.json), avec les définitions et le compte rendu des contrôles.

{{< reutiliser figures="figures_adopter" jeu="promesses_adopter" sources="Assemblée nationale, Sénat (Dosleg), Journal officiel, Légifrance" donnees="L'origine des lois ordinaires promulguées par législature et par session, et les engagements de responsabilité de l'article 49, alinéa 3 ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Parmi les lois ordinaires promulguées, {{< ado-val "P14" >}} sur {{< ado-val "N14" >}} sont d'origine parlementaire sous la XIVe législature, {{< ado-val "P15" >}} sur {{< ado-val "N15" >}} sous la XVe et {{< ado-val "P16" >}} sur {{< ado-val "N16" >}} sous la XVIe&nbsp;; c'est l'origine au dépôt, non l'influence. Le Gouvernement a engagé sa responsabilité sur un texte {{< ado-val "E16" >}} fois sous la XVIe législature, toutes sur des textes financiers, et aucune motion de censure n'a été adoptée sur ces engagements.
{{< /reutiliser >}}
