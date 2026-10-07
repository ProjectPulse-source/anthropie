---
title: "Un président peut-il recourir au référendum ?"
description: "Qui peut soumettre un texte au référendum, sur quels sujets, et qu'ont décidé ceux qui ont eu lieu : les {ref.N} référendums nationaux de la Ve République, arrêtés au {ref.arrete}, et les {ref.S} propositions soumises au Conseil constitutionnel au titre du référendum d'initiative partagée. Registre du Conseil constitutionnel, vérifié contre le Journal officiel ; données ouvertes."
chapo: "La Constitution permet au président de soumettre un projet de loi au référendum, à des conditions qu'elle fixe : une proposition du Gouvernement pendant la durée des sessions ou une proposition conjointe des deux assemblées, et un objet qu'elle délimite. Du 4 octobre 1958 au {ref.arrete}, {ref.N} référendums nationaux ont été organisés ; {ref.A} ont adopté le texte soumis, {ref.R} l'ont rejeté, et le dernier date du {ref.dernier}. La voie ouverte en 2015 à l'initiative d'un cinquième des parlementaires, soumise ensuite au soutien d'un dixième des électeurs, n'a encore conduit à aucun scrutin."
date: 2026-10-06
lastmod: 2026-10-06
donnees: [promesses_referendum]
og_title: "Un président peut-il recourir au référendum ? — le registre des référendums de la Ve République et l'initiative partagée — S. Lalut"
og_image: "images/og-referendum-promesse.jpg"
og_image_alt: "Carte de partage : « Neuf référendums nationaux depuis le 4 octobre 1958 » — frise des référendums nationaux, avec la part des oui parmi les suffrages exprimés ; sept adoptés, deux rejetés (1969 et 2005) ; aucun depuis le 29 mai 2005, arrêté au 5 octobre 2026."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_referendum"
  nom: "Référendums nationaux de la Ve République et référendum d'initiative partagée : registre arrêté au 5 octobre 2026"
  description: "Registre des référendums nationaux proclamés par le Conseil constitutionnel depuis 1958 (inscrits, votants, suffrages exprimés, oui, non, issue, article de la Constitution), rapproché scrutin par scrutin du Journal officiel (décret de soumission, loi promulguée) ; décisions du Conseil constitutionnel sur les propositions de loi présentées au titre de l'article 11, alinéa 3 (solution, condition non remplie, soutiens recueillis). Source : stock CONSTIT de la DILA, arrêté au {ref.arrete}."
  couverture_temporelle: "1958/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Référendums nationaux : inscrits, votants, suffrages exprimés, oui, non", unite: "électeurs"}
    - {nom: "Propositions de loi au titre de l'article 11 : solution du Conseil constitutionnel, soutiens recueillis", unite: "décisions ; électeurs"}
  sources:
    - "https://echanges.dila.gouv.fr/OPENDATA/CONSTIT/"
    - "https://www.conseil-constitutionnel.fr/"
    - "https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006071194"
  mots: ["référendum", "article 11", "article 89", "référendum d'initiative partagée", "Conseil constitutionnel", "Ve République", "promesses"]
  fichiers: ["promesses_referendum.csv", "promesses_referendum.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Le président de la République peut-il organiser un référendum quand il le veut ?"
    answer: "Non, pas seul et pas sur tout sujet. Selon l'article 11 de la Constitution, il peut soumettre au référendum un projet de loi « {ref.cit_art11_1} », et seulement un projet « {ref.cit_art11_objet} ». La révision de la Constitution suit l'article 89 : pour un projet de révision voté en termes identiques par les deux assemblées, le président choisit entre le référendum et le Parlement réuni en Congrès ; une proposition de révision, d'origine parlementaire, n'a pas cette seconde voie : « {ref.cit_art89_ref} »"
  - question: "Combien de référendums ont eu lieu sous la Ve République ?"
    answer: "Du 4 octobre 1958 au {ref.arrete}, {ref.N} référendums nationaux, dont les résultats ont été proclamés par le Conseil constitutionnel : {ref.A} ont adopté le texte soumis, {ref.R} l'ont rejeté (en 1969 et en 2005). Le dernier date du {ref.dernier}. Ce compte exclut le référendum du 28 septembre 1958, qui a adopté la Constitution, et les consultations locales."
  - question: "Le référendum d'initiative partagée a-t-il déjà été utilisé ?"
    answer: "De {ref.rip_depuis} au {ref.arrete}, le Conseil constitutionnel a été saisi de {ref.S} propositions de loi au titre de l'article 11 ; {ref.C} a été jugée conforme, celle sur les aérodromes de Paris, et elle a recueilli {ref.soutiens} soutiens, pour {ref.seuil} requis (un dixième des électeurs inscrits). Aucune n'a été soumise au référendum."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 60
  prolongement: true
  nature: "Registre du Conseil constitutionnel, vérifié contre le Journal officiel ; données ouvertes"
onglet:  # panneau « Prolongements » de la barre du dossier (partials/barre-bloc.html)
  long: "Un président peut-il recourir au référendum ?"
  court: "Référendum"
  role: "registre et initiative partagée"
---

{{< reutiliser-ancre >}}

Promettre de soumettre une réforme aux électeurs, c'est promettre de passer par une autre voie que le seul vote du Parlement. La Constitution l'organise&nbsp;: «&nbsp;{{< ref-val "cit_art3" >}}&nbsp;» (art.&nbsp;3). Cette page dit qui peut soumettre un texte au référendum, sur quels sujets, et ce qu'ont décidé les scrutins qui ont eu lieu, à partir du registre du Conseil constitutionnel, qui en proclame les résultats, rapproché scrutin par scrutin du Journal officiel. Aucun chiffre n'est saisi à la main.

**Réponse courte.** Le président peut soumettre au référendum un projet de loi, sur proposition du Gouvernement pendant la durée des sessions ou sur proposition conjointe des deux assemblées, et sur les seuls sujets que fixe l'article&nbsp;11&nbsp;; selon l'article&nbsp;89, un projet de révision de la Constitution d'abord voté en termes identiques par les deux assemblées est soumis au référendum, sauf si le président choisit de le soumettre au Parlement réuni en Congrès. Du 4&nbsp;octobre 1958 au {{< ref-val "arrete" >}}, {{< ref-val "N" >}} référendums nationaux ont été organisés, et aucun depuis le {{< ref-val "dernier" >}}.

## Qui peut soumettre un texte au référendum&nbsp;? {#qui-peut}

Deux articles de la Constitution ouvrent la voie, à des conditions différentes.

- **L'article 11** permet au président de soumettre au référendum un projet de loi, «&nbsp;{{< ref-val "cit_art11_1" >}}&nbsp;». Le sujet est délimité&nbsp;: un projet «&nbsp;{{< ref-val "cit_art11_objet" >}}&nbsp;».
- **L'article 89** organise la révision de la Constitution. Un projet de révision voté par les deux assemblées est en principe soumis au référendum, «&nbsp;Toutefois, {{< ref-val "cit_art89_voies" >}}&nbsp;», où il doit réunir les trois cinquièmes des suffrages exprimés. Une proposition de révision, d'origine parlementaire, n'a pas cette seconde voie&nbsp;: «&nbsp;{{< ref-val "cit_art89_ref" >}}&nbsp;»

L'acte par lequel le président soumet un projet au référendum (art.&nbsp;11) n'a pas besoin du contreseing du Premier ministre&nbsp;: c'est l'une des exceptions de l'article&nbsp;19 (voir [ce que le président peut décider seul](/pouvoirs-du-president-de-la-republique/)). Mais il ne peut pas l'accomplir sans la proposition qui le précède, et c'est le corps électoral qui adopte ou rejette le texte. Le Conseil constitutionnel veille à la régularité des opérations&nbsp;; selon l'article&nbsp;60, «&nbsp;{{< ref-val "cit_art60" >}}&nbsp;»

## Combien de référendums ont eu lieu, et qu'ont-ils décidé&nbsp;? {#registre}

{{< figure-svg fichier="referendum-registre" alt="Frise de 1958 à 2026 : une tige par référendum national, dont la hauteur donne la part des oui parmi les suffrages exprimés, pleine pour un texte adopté, vide pour un texte rejeté ; une ligne marque la moitié des exprimés ; une zone grisée couvre les années depuis le dernier scrutin, en 2005. Les valeurs sont dans le tableau sous la figure." >}}Référendums nationaux dont le Conseil constitutionnel a proclamé les résultats, du 4&nbsp;octobre 1958 au {{< ref-val "arrete" >}}. Hors référendum du 28&nbsp;septembre 1958 (adoption de la Constitution, avant la création du Conseil) et consultations locales.{{< /figure-svg >}}

{{< fig-actions id="registre" >}}

{{< ref-tableau "registre" "Les scrutins en tableau" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Du 4&nbsp;octobre 1958 au {{< ref-val "arrete" >}}, {{< ref-val "N" >}} référendums nationaux ont été organisés&nbsp;; {{< ref-val "A" >}} ont adopté le texte soumis, {{< ref-val "R" >}} l'ont rejeté, et le dernier date du {{< ref-val "dernier" >}}.

</div>

{{< ref-val "n_loi" >}} scrutins ont eu lieu sur le fondement de l'article&nbsp;11, {{< ref-val "n_rev" >}} sur celui de l'article&nbsp;89&nbsp;: le quinquennat, en 2000. Deux projets soumis au titre de l'article&nbsp;11 portaient pourtant sur la Constitution elle-même&nbsp;: celui de 1962, adopté, qui modifie ses articles&nbsp;6 et&nbsp;7 pour faire élire le président au suffrage universel direct (loi n°&nbsp;62-1292 du 6&nbsp;novembre 1962), et celui de 1969, rejeté. Ce recours à l'article&nbsp;11 pour réviser la Constitution a été contesté&nbsp;: saisi de la loi de 1962 par le président du Sénat, le Conseil constitutionnel s'est déclaré incompétent (décision n°&nbsp;62-20&nbsp;DC du 6&nbsp;novembre 1962)&nbsp;; selon l'Assemblée nationale, cette pratique n'a plus été employée depuis l'échec de 1969. La participation a varié de {{< ref-val "part_min" >}}&nbsp;% des inscrits ({{< ref-val "part_min_an" >}}) à {{< ref-val "part_max" >}}&nbsp;% ({{< ref-val "part_max_an" >}}). Les deux textes rejetés l'ont été en 1969 (régions et Sénat) et en 2005 (traité établissant une Constitution pour l'Europe), avec {{< ref-val "non_2005" >}}&nbsp;% de non parmi les suffrages exprimés.

<details class="repli"><summary>Ce qui a été vérifié</summary>

**Le registre.** Les décisions du Conseil constitutionnel sont lues dans le stock que publie la DILA (fichiers ouverts, arrêtés au {{< ref-val "arrete" >}}). Parmi les décisions classées «&nbsp;référendum&nbsp;», seules les proclamations de résultats entrent au registre&nbsp;; les autres sont des désignations de délégués, des réponses à des requêtes et des observations. Pour chaque scrutin, les nombres d'inscrits, de votants, de suffrages exprimés, de oui et de non sont lus dans la proclamation, et leur cohérence est contrôlée (oui et non font les exprimés&nbsp;; exprimés, votants et inscrits sont dans l'ordre). Les pourcentages de cette page sont recalculés à partir de ces nombres et arrondis au plus proche&nbsp;; le tableau récapitulatif du Conseil constitutionnel les donne tronqués, d'où des écarts d'un centième de point sur certains scrutins.

**Le témoin du Journal officiel.** Chaque scrutin a été rapproché du Journal officiel&nbsp;: le décret par lequel le président soumet le texte, à la date que donne la proclamation, et, pour chaque texte adopté, la loi promulguée. Les {{< ref-val "A" >}} lois existent&nbsp;; aucune loi n'existe pour les {{< ref-val "R" >}} textes rejetés. Un seul décret n'a pas été retrouvé dans le fonds de Légifrance, celui du 2&nbsp;octobre 1962, dont la loi est publiée. La recherche par titre dans le Journal officiel ne fait apparaître aucun scrutin absent du registre.

**Les limites.** Les nombres de voix n'ont pas de second producteur pour 1961-1988&nbsp;: ils sont contrôlés par leur cohérence, pas par une autre source. Les résultats publiés par le ministère de l'Intérieur pour 1992, 2000 et 2005 précèdent les rectifications du Conseil&nbsp;: même scrutin, autre définition, donc pas un témoin.

</details>

## Le référendum d'initiative partagée a-t-il déjà abouti&nbsp;? {#initiative-partagee}

Depuis la révision de 2008, une autre voie existe&nbsp;: un référendum peut être organisé «&nbsp;{{< ref-val "cit_art11_rip" >}}&nbsp;». La proposition de loi est transmise au Conseil constitutionnel, qui vérifie qu'elle est signée par un cinquième des parlementaires, qu'elle porte sur un objet de l'article&nbsp;11 et qu'aucune de ses dispositions n'est contraire à la Constitution&nbsp;; si elle est conforme, les soutiens sont recueillis pendant neuf mois. Si elle réunit ses soutiens et que les deux assemblées ne l'examinent pas dans le délai fixé, l'article&nbsp;11 dispose&nbsp;: «&nbsp;{{< ref-val "cit_art11_soumet" >}}&nbsp;». La procédure est en vigueur depuis le 1er&nbsp;janvier {{< ref-val "rip_depuis" >}}.

{{< figure-svg fichier="referendum-rip" alt="Quatre barres en entonnoir, chacune avec son nombre : propositions soumises au Conseil constitutionnel, jugées conformes, ayant réuni le soutien d'un dixième des inscrits, soumises au référendum ; dessous, une jauge montre les soutiens recueillis par la proposition sur les aérodromes de Paris, rapportés au seuil requis." >}}Propositions de loi présentées au titre de l'article&nbsp;11, alinéa&nbsp;3, dont le Conseil constitutionnel a été saisi, de {{< ref-val "rip_depuis" >}} au {{< ref-val "arrete" >}}, et ce qu'elles sont devenues.{{< /figure-svg >}}

{{< fig-actions id="rip" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** De {{< ref-val "rip_depuis" >}} au {{< ref-val "arrete" >}}, le Conseil constitutionnel a été saisi de {{< ref-val "S" >}} propositions de loi au titre de l'article&nbsp;11&nbsp;; {{< ref-val "C" >}} a été jugée conforme et n'a pas réuni le soutien d'un dixième des électeurs inscrits ({{< ref-val "soutiens" >}} soutiens pour {{< ref-val "seuil" >}} requis)&nbsp;; aucune n'a été soumise au référendum.

</div>

{{< ref-tableau "rip" "Les décisions en tableau" >}}

Les {{< ref-val "non_conformes" >}} autres propositions ont été jugées non conformes, pour deux raisons que le Conseil nomme lui-même. {{< ref-val "cond2_maj" >}} ne portaient pas sur un objet de l'article&nbsp;11&nbsp;: pour la retraite à 62&nbsp;ans, par exemple, la proposition «&nbsp;{{< ref-val "cit_motif_2023_4" >}}&nbsp;» (décision 2023-4 RIP). {{< ref-val "cond3_maj" >}} contenaient une disposition contraire à la Constitution (2021-2 et 2024-6 RIP). La page ne juge pas ces décisions&nbsp;; elle rapporte leurs motifs.

**{{< ref-val "depots_sans_saisine_maj" >}} autres propositions** ont été déposées «&nbsp;en application de l'article 11&nbsp;» sans qu'aucune décision du Conseil constitutionnel ne les concerne dans le registre consulté&nbsp;: au Sénat, n°&nbsp;459 (20&nbsp;avril 2018, contrôle de l'immigration)&nbsp;; à l'Assemblée nationale, n°&nbsp;1749 (6&nbsp;mars 2019, mesures contre les djihadistes français ayant combattu en Irak et en Syrie) et n°&nbsp;5203 (5&nbsp;avril 2022, mauvais traitements envers les animaux). Elles portaient la signature de {{< ref-val "depots_auteurs" >}} parlementaires, quand l'article&nbsp;11 prévoit l'initiative d'un cinquième des membres du Parlement. Elles ne sont donc pas comptées parmi les {{< ref-val "S" >}} saisines. La loi organique prévoit que la proposition est transmise au Conseil constitutionnel&nbsp;; les sources consultées ne permettent pas d'établir ce qu'il est advenu de ces textes.

## Ce qu'un référendum décide, et ce qu'il ne fait pas {#ce-qu-il-decide}

Le référendum tranche le texte soumis&nbsp;: adopté, un projet de loi de l'article&nbsp;11 devient une loi, que le président promulgue, et un projet de révision de l'article&nbsp;89 modifie la Constitution. Il ne garantit pas, à lui seul, la mise en œuvre de ce texte ni le résultat auquel une promesse l'associe. Une loi adoptée par référendum peut appeler des [mesures d'application](/une-loi-votee-s-applique-t-elle-tout-de-suite/), ne raccourcit pas une [formation de dix ans](/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/), et ne choisit pas [l'indicateur](/comment-savoir-si-une-promesse-est-tenue/) qui dira si la promesse est tenue. La proclamation dit combien de bulletins portaient oui et non&nbsp;; elle ne dit pas pourquoi.

## Que s'est-il passé après le rejet de 2005&nbsp;? {#apres-2005}

Le 29&nbsp;mai 2005, le projet de loi autorisant la ratification du traité établissant une Constitution pour l'Europe a été rejeté. Le traité de Lisbonne, signé ensuite, est un autre traité&nbsp;: comme le dit son intitulé, «&nbsp;traité de Lisbonne modifiant le traité sur l'Union européenne et le traité instituant la Communauté européenne&nbsp;», il modifie les traités existants. Il a été soumis au Conseil constitutionnel, qui a jugé que l'autorisation de le ratifier «&nbsp;{{< ref-val "cit_2007_560" >}}&nbsp;» (décision n°&nbsp;2007-560&nbsp;DC du 20&nbsp;décembre 2007). Le 4&nbsp;février 2008, le Parlement réuni en Congrès a adopté le projet de loi constitutionnelle modifiant le titre&nbsp;XV de la Constitution, dans les conditions de l'article&nbsp;89 ([scrutin du Congrès](https://www.assemblee-nationale.fr/13/scrutins/jo9000.asp))&nbsp;; c'est la loi constitutionnelle n°&nbsp;2008-103 du même jour. La ratification du traité de Lisbonne a ensuite été autorisée par la loi n°&nbsp;2008-125 du 13&nbsp;février 2008. Aucun référendum n'a été organisé en 2008. La page s'en tient à cette succession d'actes.

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas si le référendum est un bon ou un mauvais instrument, ni pourquoi aucun n'a été organisé depuis 2005&nbsp;: aucune source ne l'établit, et une intention ne se lit pas dans un acte. Elle ne compte ni le référendum du 28&nbsp;septembre 1958, antérieur au Conseil constitutionnel, ni les consultations locales (Nouvelle-Calédonie, Corse, outre-mer), proclamées par d'autres autorités. Elle lit la Constitution en vigueur, sans doctrine ni jurisprudence au-delà des décisions citées. Le registre est arrêté au {{< ref-val "arrete" >}}.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Ce qu'un vote décide" avis="non" >}}
Cette page montre que le référendum tranche un texte, pas ses suites. Le livre suit neuf promesses écrites, datées et signées jusqu'à leur dernier obstacle, et consacre sa clôture au référendum de 2005 et à ce qu'il en est advenu. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Constitution** du 4&nbsp;octobre 1958, art.&nbsp;3, 11, 60 et 89, texte en vigueur (Légifrance). **Ordonnance** n°&nbsp;58-1067 du 7&nbsp;novembre 1958, art.&nbsp;45-1 et 45-2&nbsp;; **loi organique** n°&nbsp;2013-1114 du 6&nbsp;décembre 2013 portant application de l'article&nbsp;11.

**Conseil constitutionnel**, proclamations des résultats des référendums (décisions 61-4, 62-7, 62-9, 69-10, 72-11, 88-14, 92-19, 2000-29, 2005-38) et décisions sur les propositions de loi de l'article&nbsp;11 (2019-1 et 2019-1-8, 2021-2, 2022-3, 2023-4, 2023-5, 2024-6, 2026-7 RIP), lues dans le stock CONSTIT que publie la DILA, arrêté au {{< ref-val "arrete" >}}&nbsp;; décision n°&nbsp;2007-560&nbsp;DC.

**Journal officiel** (Légifrance), décrets de soumission au référendum et lois adoptées par référendum&nbsp;; **Assemblée nationale**, données ouvertes des législatures XV à XVII (dépôts au titre de l'article&nbsp;11).

Les chiffres, les contrôles et les figures sont produits par un script unique, qui relit les décisions et les articles archivés et refuse d'écrire si une donnée cesse de soutenir une phrase&nbsp;; aucun chiffre de cette page n'est saisi à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_referendum.csv), en format long&nbsp;; [JSON](/promesses_referendum.json), avec les identifiants des décisions et le compte rendu des contrôles. Ce jeu est aussi archivé sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent à citer&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_referendum" jeu="promesses_referendum" sources="Conseil constitutionnel et Journal officiel" donnees="Le registre des référendums nationaux (inscrits, votants, exprimés, oui, non, article, issue), les décisions sur le référendum d'initiative partagée et les dépôts sans décision ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Un président peut soumettre un projet de loi au référendum, sur proposition du Gouvernement pendant la durée des sessions ou sur proposition conjointe des deux assemblées, et sur les sujets que fixe l'article&nbsp;11 de la Constitution. Du 4&nbsp;octobre 1958 au {{< ref-val "arrete" >}}, {{< ref-val "N" >}} référendums nationaux ont été organisés&nbsp;; {{< ref-val "A" >}} ont adopté le texte soumis, {{< ref-val "R" >}} l'ont rejeté, et le dernier date du {{< ref-val "dernier" >}}. Le référendum d'initiative partagée, ouvert en {{< ref-val "rip_depuis" >}}, n'a encore conduit à aucun scrutin.
{{< /reutiliser >}}
