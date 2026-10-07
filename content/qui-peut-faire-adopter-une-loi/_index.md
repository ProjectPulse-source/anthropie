---
title: "Qui peut faire adopter une loi ?"
description: "Le Parlement vote la loi, mais qui en a l'initiative, combien de propositions arrivent en séance, et que change l'article 49.3 ? L'origine des lois promulguées sous les trois dernières législatures complètes, rapprochée loi par loi entre l'Assemblée nationale, le Sénat et le Journal officiel, le sort des propositions de loi déposées et les engagements de responsabilité. Données ouvertes."
chapo: "Le Parlement vote la loi, et l'initiative appartient au Premier ministre comme aux parlementaires. Hors lois de finances, de financement de la sécurité sociale et organiques, et hors traités, {ado.P14} des {ado.N14} lois promulguées sous la XIVe législature sont d'origine parlementaire, {ado.P15} sur {ado.N15} sous la XVe et {ado.P16} sur {ado.N16} sous la XVIe. Cette origine dit qui a déposé le texte, non qui l'a façonné ni quels textes déposés ont échoué : dans chacune de ces législatures, plus de la moitié des propositions de loi ordinaires déposées à l'Assemblée sont restées sans examen en séance observé avant sa fin. La voie ordinaire fait intervenir les deux assemblées ; à l'Assemblée nationale, l'article 49, alinéa 3 permet en outre au Gouvernement d'engager sa responsabilité pour qu'un texte soit considéré comme adopté à l'étape concernée, sauf censure."
date: 2026-10-06
lastmod: 2026-10-06
donnees: [promesses_adopter]
og_title: "Qui peut faire adopter une loi ? — l'origine des lois, les propositions sans séance et l'article 49.3 — S. Lalut"
og_image: "images/og-adopter-promesse.jpg"
og_image_alt: "Carte de partage : qui est à l'origine des lois promulguées du champ étudié, par législature, de la XIVe à la XVIe : projets du Gouvernement, propositions déposées à l'Assemblée nationale et au Sénat."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_adopter"
  nom: "Origine des lois promulguées de 2012 à 2026, propositions de loi déposées à l'Assemblée et engagements de responsabilité (art. 49, al. 3)"
  description: "Origine formelle au dépôt initial (projet du Gouvernement, proposition déposée à l'Assemblée nationale ou au Sénat) des lois promulguées de la XIVe à la XVIIe législature, hors traités, lois de finances, de financement de la sécurité sociale et organiques, rapprochée loi par loi entre les données de l'Assemblée nationale, la base Dosleg du Sénat et le Journal officiel ; propositions de loi ordinaires déposées à l'Assemblée et restées sans examen en séance avant la fin de la législature, avec la borne du pire cas face aux bulletins statistiques ; engagements de responsabilité du Gouvernement sur un texte (art. 49, al. 3) par législature."
  couverture_temporelle: "2012/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Lois promulguées par origine", unite: "lois"}
    - {nom: "Propositions de loi déposées et sans examen en séance", unite: "textes"}
    - {nom: "Engagements de responsabilité (art. 49, al. 3)", unite: "engagements"}
  sources:
    - "https://data.assemblee-nationale.fr/"
    - "https://data.senat.fr/dosleg/"
    - "https://www.legifrance.gouv.fr/constitution"
  mots: ["loi", "proposition de loi", "projet de loi", "Parlement", "article 49.3", "article 45", "Assemblée nationale", "Sénat", "promesses"]
  fichiers: ["promesses_adopter.csv", "promesses_adopter.json"]
  doi: "10.5281/zenodo.23212665"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Qui peut proposer une loi en France ?"
    answer: "Selon l'article 39 de la Constitution, « {ado.cit_art39} » Un texte du Gouvernement est un projet de loi ; un texte d'un député ou d'un sénateur est une proposition de loi. Hors lois de finances, de financement de la sécurité sociale et organiques, et hors traités, {ado.P16} des {ado.N16} lois promulguées sous la XVIe législature étaient issues d'une proposition, {ado.G16} d'un projet."
  - question: "Parmi les lois promulguées, quelle part vient d'un projet du Gouvernement ?"
    answer: "Cela varie selon la législature. Dans le champ étudié (hors traités, lois de finances, de financement de la sécurité sociale et organiques), {ado.G14} des {ado.N14} lois promulguées venaient d'un projet du Gouvernement sous la XIVe législature, {ado.G15} sur {ado.N15} sous la XVe et {ado.G16} sur {ado.N16} sous la XVIe. C'est l'origine au dépôt du texte : elle ne mesure pas l'influence du Gouvernement sur une proposition, ni les amendements du Parlement sur un projet."
  - question: "Combien de propositions de loi arrivent en séance ?"
    answer: "Moins de la moitié. Sous la XIVe législature, {ado.Z14} des {ado.NZ14} propositions de loi ordinaires déposées à l'Assemblée nationale sont restées sans examen en séance observé avant la fin de la législature ; {ado.Z15} sur {ado.NZ15} sous la XVe ; {ado.Z16} sur {ado.NZ16} sous la XVIe. Ces décomptes dépassent légèrement ceux des bulletins de l'Assemblée ; même en retirant tout l'excès, plus de la moitié restent sans examen dans chaque législature."
  - question: "Combien de fois l'article 49.3 a-t-il été utilisé ?"
    answer: "Le Gouvernement a engagé sa responsabilité sur un texte {ado.E14} fois sous la XIVe législature, sur {ado.Etextes14} projets de loi, {ado.E15} fois sous la XVe et {ado.E16} fois sous la XVIe, dont {ado.Efin16} sur un projet de loi de finances ou de financement de la sécurité sociale, en comptant un engagement par texte et par étape de lecture. Aucune motion de censure n'a été adoptée sur ces engagements ; sous la XVIIe législature, une motion a été adoptée après l'engagement du {ado.censure_date}."
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

Une promesse qui nécessite une loi doit franchir l'étape parlementaire. La Constitution le dit en une phrase&nbsp;: «&nbsp;{{< ado-val "cit_art24" >}}&nbsp;» (art.&nbsp;24). Elle partage l'initiative&nbsp;: «&nbsp;{{< ado-val "cit_art39" >}}&nbsp;» (art.&nbsp;39). Cette page compte, loi par loi, qui a déposé les lois promulguées depuis 2012, combien de propositions de loi arrivent en séance, et combien de fois le Gouvernement a engagé sa responsabilité sur un texte au titre de l'article&nbsp;49, alinéa&nbsp;3. Tous les nombres viennent des données publiques de l'Assemblée nationale, du Sénat et du Journal officiel, rapprochées loi par loi, et aucun n'est saisi à la main.

**Réponse courte.** Le Parlement vote la loi, mais le texte voté peut venir du Gouvernement ou d'un parlementaire. Hors lois de finances, de financement de la sécurité sociale et organiques, et hors traités, {{< ado-val "P16" >}} des {{< ado-val "N16" >}} lois promulguées sous la XVIe législature étaient issues d'une proposition de loi. Mais plus de la moitié des propositions de loi déposées à l'Assemblée restent sans examen en séance observé avant la fin de la législature. Et le Gouvernement peut engager sa responsabilité sur un texte&nbsp;: à l'étape concernée, le texte est alors considéré comme adopté, sauf si une motion de censure est votée.

## Qui est à l'origine des lois promulguées&nbsp;? {#origine-des-lois}

{{< figure-svg fichier="adopter-origine" alt="Barres horizontales par législature, de la XIVe à la XVIIe en cours : lois issues d'un projet du Gouvernement, d'une proposition déposée à l'Assemblée nationale, d'une proposition déposée au Sénat ; un trait marque la moitié des lois. La part d'origine parlementaire est sous la moitié pour la XIVe et au-dessus pour les suivantes. Les valeurs sont dans le tableau sous la figure." >}}Lois promulguées, rattachées à la législature de leur promulgation, selon l'origine du texte au dépôt initial. Champ étudié&nbsp;: hors lois autorisant un traité, lois de finances, lois de financement de la sécurité sociale et lois organiques.{{< /figure-svg >}}

{{< fig-actions id="origine" >}}

{{< ado-tableau "lois" "Les valeurs de la figure en tableau" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Hors lois de finances, de financement de la sécurité sociale et organiques, et hors traités, {{< ado-val "P14" >}} des {{< ado-val "N14" >}} lois promulguées sous la XIVe législature sont d'origine parlementaire, {{< ado-val "P15" >}} sur {{< ado-val "N15" >}} sous la XVe et {{< ado-val "P16" >}} sur {{< ado-val "N16" >}} sous la XVIe.

</div>

La part d'origine parlementaire est inférieure à la moitié sous la XIVe législature et supérieure à la moitié sous la XVe et la XVIe, même en ne retenant, pour la XVe, que les {{< ado-val "Pmin15" >}} lois dont l'origine est établie par les deux sources. Ces proportions décrivent les lois finalement promulguées&nbsp;; elles ne mesurent pas le sort des textes déposés, que la section suivante examine. Les lois de finances et de financement de la sécurité sociale, hors du champ, viennent toutes d'un projet du Gouvernement.

**Ce que l'origine ne dit pas.** Elle dit qui a déposé le texte, non qui l'a voulu ni ce qu'il est devenu. Une proposition de loi peut être soutenue, amendée ou réécrite à la demande du Gouvernement&nbsp;; un projet peut être profondément modifié par le Parlement. Les textes déposés mais non adoptés sont absents de ce décompte. Aucune de ces séries ne mesure ces influences.

<details class="repli"><summary>Ce qui a été vérifié, et comment</summary>

Chaque loi promulguée depuis juin 2012 est rapprochée, par son numéro au Journal officiel, entre les données ouvertes de l'Assemblée nationale et la base Dosleg du Sénat. Quand les deux sources la connaissent, elles donnent la même origine pour toutes les lois. Certaines lois de la XIVe et de la XVe législatures manquent aux fichiers de l'Assemblée, parce que leur dossier a été ouvert sous la législature précédente&nbsp;: leur origine ne repose que sur le Sénat, d'où la borne «&nbsp;au moins&nbsp;» du tableau.

Deux contrôles viennent d'ailleurs. Session par session, de 2017-2018 à 2024-2025, le nombre de lois promulguées hors traités est exactement celui que compte le baromètre de l'application des lois, publié par l'Assemblée nationale à partir des données de la DILA. Et le Sénat écrit, pour 2024-2025&nbsp;: «&nbsp;{{< ado-val "cit_senat_origine" >}}&nbsp;»&nbsp;; le décompte loi par loi donne {{< ado-val "s2425_P" >}} lois d'origine parlementaire sur {{< ado-val "s2425_N" >}}.

{{< ado-tableau "sessions" "Par session, toutes natures sauf les traités" >}}

</details>

## Combien de propositions de loi arrivent en séance&nbsp;? {#propositions-en-seance}

Moins de la moitié. Sous la XIVe législature, {{< ado-val "Z14" >}} des {{< ado-val "NZ14" >}} propositions de loi ordinaires déposées en premier lieu à l'Assemblée nationale sont restées sans examen en séance observé avant la fin de la législature&nbsp;; {{< ado-val "Z15" >}} sur {{< ado-val "NZ15" >}} sous la XVe&nbsp;; {{< ado-val "Z16" >}} sur {{< ado-val "NZ16" >}} sous la XVIe.

{{< ado-tableau "e1" "Les valeurs en tableau, avec la borne du pire cas" >}}

Ces nombres comptent les dépôts dans les données ouvertes de l'Assemblée. Ses bulletins statistiques en comptent un peu moins&nbsp;: {{< ado-val "exces14" >}}, {{< ado-val "exces15" >}} et {{< ado-val "exces16" >}} propositions de moins selon la législature, sans liste qui permette d'identifier les textes en cause. Même en retirant tout cet excès à la fois du total et des propositions restées sans examen, plus de la moitié des propositions de loi ordinaires déposées restent sans examen en séance observé avant la fin de la législature, dans chacune des trois législatures&nbsp;: {{< ado-val "Zw14" >}} sur {{< ado-val "Nw14" >}}, {{< ado-val "Zw15" >}} sur {{< ado-val "Nw15" >}}, {{< ado-val "Zw16" >}} sur {{< ado-val "Nw16" >}}.

Une proposition sans examen en séance n'est pas forcément perdue&nbsp;: son contenu peut être repris par un autre texte, ou par un amendement. Et ces fractions ne se comparent pas d'une législature à l'autre comme des taux&nbsp;: la XVIe, écourtée par la dissolution, a laissé aux textes un temps d'examen plus de deux fois plus court (durée médiane entre dépôt et fin de législature&nbsp;: {{< ado-val "med16" >}} jours, contre {{< ado-val "med14" >}} sous la XIVe).

## Comment une loi est-elle adoptée par la voie ordinaire&nbsp;? {#voie-ordinaire}

«&nbsp;{{< ado-val "cit_art45a" >}}&nbsp;» (Constitution, art.&nbsp;45). En cas de désaccord persistant entre les deux assemblées, le Premier ministre ou, pour une proposition de loi, les présidents des deux assemblées «&nbsp;{{< ado-val "cit_art45b" >}}&nbsp;» Si cet accord échoue, «&nbsp;{{< ado-val "cit_art45c" >}}&nbsp;»

L'initiative n'épuise pas les leviers de procédure&nbsp;: selon l'article&nbsp;48, «&nbsp;{{< ado-val "cit_art48" >}}&nbsp;» Cette priorité d'ordre du jour ne garantit pas l'adoption d'un texte.

## Que change l'article 49, alinéa 3&nbsp;? {#article-49-3}

Il permet au Gouvernement d'engager sa responsabilité sur un texte devant l'Assemblée nationale. Selon l'article&nbsp;49 de la Constitution, «&nbsp;{{< ado-val "cit_art49a" >}}&nbsp;» Hors de ces textes, «&nbsp;{{< ado-val "cit_art49b" >}}&nbsp;» Le texte n'est pas voté à cette étape&nbsp;: il est considéré comme adopté, sauf si une motion de censure l'est. Ce relevé porte sur tous les textes, lois de finances comprises, que le compte de l'origine des lois laisse de côté.

{{< figure-svg fichier="adopter-493" alt="Barres horizontales par législature : engagements de responsabilité sur un projet de loi de finances ou de financement de la sécurité sociale, et sur un autre projet ou une proposition. Ceux de la XIVe et de la XVe portent sur d'autres projets ; ceux de la XVIe portent en majorité sur des projets de loi de finances ou de financement de la sécurité sociale. Les valeurs sont dans le tableau sous la figure." >}}Engagements de responsabilité du Gouvernement sur un texte, un par texte et par étape de lecture, selon les catégories de l'article&nbsp;49, alinéa&nbsp;3&nbsp;: la loi de programmation des finances publiques y relève d'«&nbsp;un autre projet&nbsp;».{{< /figure-svg >}}

{{< fig-actions id="493" >}}

{{< ado-tableau "engagements" "Les valeurs de la figure en tableau" >}}

Sous la XIVe législature, le Gouvernement a engagé sa responsabilité {{< ado-val "E14" >}} fois, sur {{< ado-val "Etextes14" >}} projets de loi qui n'étaient ni des projets de loi de finances ni de financement de la sécurité sociale&nbsp;; sous la XVe, {{< ado-val "E15" >}} fois&nbsp;; sous la XVIe, {{< ado-val "E16" >}} fois, dont {{< ado-val "Efin16" >}} sur des projets de loi de finances ou de financement de la sécurité sociale et {{< ado-val "Eautre16" >}} sur la loi de programmation des finances publiques. La fiche de l'Assemblée nationale consacrée à cette procédure donne les mêmes totaux&nbsp;: «&nbsp;{{< ado-val "cit_fiche64" >}}&nbsp;» Ces nombres décrivent la nature des textes sur lesquels la responsabilité a été engagée&nbsp;; ils n'expliquent pas pourquoi l'usage diffère d'une législature à l'autre.

Aucune motion de censure n'a été adoptée sur ces engagements, de la XIVe à la XVIe législature. Sous la XVIIe, après l'engagement du {{< ado-val "censure_date" >}}, «&nbsp;{{< ado-val "cit_censure" >}}&nbsp;» (même fiche)&nbsp;: le texte n'a pas été considéré comme adopté sur le fondement de l'article&nbsp;49, alinéa&nbsp;3, à cette étape.

<details class="repli"><summary>Ce qui a été vérifié, et comment</summary>

Les engagements sont lus dans les dossiers législatifs de l'Assemblée nationale, et comptés deux fois par deux voies différentes du même producteur, avec les mêmes dates. Ils sont comparés, session par session, aux bulletins statistiques de l'Assemblée&nbsp;: mêmes nombres d'engagements et de motions. Une seule date diffère, d'un jour, pour un engagement de novembre 2022&nbsp;; le compte rendu officiel de la séance confirme la date des données. Pour quelques motions, les données ne contiennent pas l'acte de vote&nbsp;; les bulletins donnent leurs scrutins, tous sous la majorité requise.

</details>

## Ce que cette page ne dit pas {#limites}

Elle ne mesure pas l'influence du Gouvernement sur les propositions de loi, ni celle du Parlement sur les projets&nbsp;: l'origine d'une loi n'est pas son contenu, et les amendements ne sont pas comptés. Elle ne relie pas le nombre d'engagements de responsabilité à la composition de l'Assemblée&nbsp;: une coïncidence de dates n'établit pas un lien. Elle ne dit pas ce que deviennent les propositions sans examen en séance, ni si leur contenu a été repris ailleurs. Les décomptes de dépôts ne concordent pas texte par texte avec les bulletins de l'Assemblée&nbsp;: la phrase sur les propositions ne s'appuie que sur la borne du pire cas.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Ce qu'il faut faire voter" avis="non" >}}
Cette page dit qui dépose les lois, combien de propositions arrivent en séance et ce que permet l'article 49.3. Le livre suit neuf promesses écrites, datées et signées, le long de la chaîne qui va de la décision à son résultat&nbsp;: ce qu'un président décide dans sa propre chaîne de pouvoir, ce qu'il doit faire voter, ce qu'il doit négocier, et ce qui ne dépendra jamais de lui. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Assemblée nationale**, données ouvertes des dossiers législatifs des XIVe à XVIIe législatures (version du {{< ado-val "releve" >}})&nbsp;; bulletins statistiques annuels&nbsp;; fiche de synthèse n°&nbsp;64 sur l'engagement de la responsabilité du Gouvernement.

**Sénat**, base Dosleg (version du {{< ado-val "releve" >}})&nbsp;; rapport d'information n°&nbsp;802 (2025-2026) sur l'application des lois, p.&nbsp;44.

**Journal officiel**, données de la DILA&nbsp;; **Constitution**, art.&nbsp;24, 39, 45, 48 et 49, lus sur Légifrance (API).

Les chiffres, les citations, les contrôles et les figures sont produits par un script unique&nbsp;; chaque citation est vérifiée mot pour mot dans son document, et aucun chiffre de cette page n'est saisi à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_adopter.csv), en format long&nbsp;; [JSON](/promesses_adopter.json), avec les définitions et le compte rendu des contrôles. Ce jeu est aussi archivé sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent à citer&nbsp;: [doi:10.5281/zenodo.23212665](https://doi.org/10.5281/zenodo.23212665).

{{< reutiliser figures="figures_adopter" jeu="promesses_adopter" sources="Assemblée nationale, Sénat (Dosleg), Journal officiel, Légifrance" donnees="L'origine des lois promulguées par législature et par session, les propositions de loi déposées à l'Assemblée et restées sans examen en séance, et les engagements de responsabilité de l'article 49, alinéa 3 ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Dans le champ étudié (hors traités, lois de finances, de financement de la sécurité sociale et organiques), {{< ado-val "P14" >}} des {{< ado-val "N14" >}} lois promulguées sous la XIVe législature sont d'origine parlementaire, {{< ado-val "P15" >}} sur {{< ado-val "N15" >}} sous la XVe et {{< ado-val "P16" >}} sur {{< ado-val "N16" >}} sous la XVIe&nbsp;; c'est l'origine au dépôt, non l'influence. Plus de la moitié des propositions de loi ordinaires déposées à l'Assemblée restent sans examen en séance observé avant la fin de la législature, même sous la borne du pire cas. Le Gouvernement a engagé sa responsabilité sur un texte {{< ado-val "E16" >}} fois sous la XVIe législature, dont {{< ado-val "Efin16" >}} sur des projets de loi de finances ou de financement de la sécurité sociale.
{{< /reutiliser >}}
