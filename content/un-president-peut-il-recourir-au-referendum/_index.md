---
title: "Un président peut-il recourir au référendum ?"
description: "Qui peut soumettre un texte au référendum, par quelle voie (articles 11, 89 et 88-5 de la Constitution) et sur quels sujets ; ce qu'ont décidé les {ref.N} référendums nationaux de la Ve République, arrêtés au {ref.arrete}, et ce que sont devenues les {ref.S} propositions d'initiative partagée examinées par le Conseil constitutionnel, motifs cités. Registre du Conseil constitutionnel, vérifié contre le Journal officiel ; données ouvertes."
chapo: "Un président peut-il soumettre une réforme aux électeurs quand il le veut ? La Constitution lui en donne le pouvoir par trois voies, et chacune a ses conditions : pour un projet de loi, une proposition du Gouvernement ou des deux assemblées, et un sujet que l'article 11 délimite ; pour une révision de la Constitution, un vote des deux assemblées en termes identiques ; pour l'adhésion d'un État à l'Union européenne, le référendum est la règle, sauf si le Parlement en décide autrement. Du 4 octobre 1958 au {ref.arrete}, {ref.N} référendums nationaux ont eu lieu, le dernier le {ref.dernier}. Depuis {ref.rip_depuis}, des parlementaires soutenus par des électeurs peuvent aussi engager une procédure qui peut y conduire : elle n'a conduit à aucun scrutin."
date: 2026-10-06
lastmod: 2026-10-12
donnees: [promesses_referendum]
og_title: "Un président peut-il recourir au référendum ? — le registre des référendums de la Ve République et l'initiative partagée — S. Lalut"
og_image: "images/og-referendum-promesse.jpg"
og_image_alt: "Carte de partage : « Neuf référendums nationaux depuis le 4 octobre 1958 » — frise des référendums nationaux, avec la part des oui parmi les suffrages exprimés ; sept adoptés, deux rejetés (1969 et 2005) ; aucun depuis le 29 mai 2005, arrêté au 5 octobre 2026."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_referendum"
  nom: "Référendums nationaux de la Ve République et référendum d'initiative partagée : registre arrêté au 5 octobre 2026"
  description: "Registre des référendums nationaux proclamés par le Conseil constitutionnel depuis 1958 (inscrits, votants, suffrages exprimés, oui, non, issue, article de la Constitution), rapproché scrutin par scrutin du Journal officiel (décret de soumission, loi promulguée) ; décisions du Conseil constitutionnel sur les propositions de loi présentées au titre de l'article 11, alinéa 3 (solution, condition non remplie, motifs cités avec leur considérant, soutiens recueillis). Source : stock CONSTIT de la DILA, arrêté au {ref.arrete}."
  couverture_temporelle: "1958/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Référendums nationaux : inscrits, votants, suffrages exprimés, oui, non", unite: "électeurs"}
    - {nom: "Propositions de loi au titre de l'article 11 : solution du Conseil constitutionnel, condition de l'article 45-2, motifs cités, soutiens recueillis", unite: "décisions ; électeurs"}
  sources:
    - "https://echanges.dila.gouv.fr/OPENDATA/CONSTIT/"
    - "https://www.conseil-constitutionnel.fr/"
    - "https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006071194"
  mots: ["référendum", "article 11", "article 89", "article 88-5", "référendum d'initiative partagée", "Conseil constitutionnel", "Ve République", "promesses"]
  fichiers: ["promesses_referendum.csv", "promesses_referendum.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Le président de la République peut-il organiser un référendum quand il le veut ?"
    answer: "Non, pas seul et pas sur tout sujet. Selon l'article 11 de la Constitution, il peut soumettre au référendum un projet de loi « {ref.cit_art11_1} », et seulement sur les sujets que l'article énumère. Une révision de la Constitution (article 89) doit d'abord être votée en termes identiques par les deux assemblées. Pour la ratification d'un traité d'adhésion d'un État à l'Union européenne (article 88-5), le référendum est la règle, sauf si les deux assemblées votent une motion à la majorité des trois cinquièmes."
  - question: "Le président doit-il soumettre au référendum une proposition qu'on lui adresse ?"
    answer: "Pour l'article 11, le texte dit qu'il « {ref.cit_art11_peut} » sur proposition du Gouvernement ou des deux assemblées : la proposition est nécessaire, et l'article n'en fait pas une obligation. Pour l'initiative partagée, quand la proposition a réuni le soutien d'un dixième des électeurs et que les deux assemblées ne l'ont pas examinée dans le délai, l'article 11 dispose que « {ref.cit_art11_soumet} ». Pour un projet de révision voté par les deux assemblées, l'article 89 lui laisse le choix du Congrès au lieu du référendum."
  - question: "Le référendum d'initiative partagée permet-il aux citoyens de déclencher un référendum ?"
    answer: "Pas seuls. L'initiative appartient à un cinquième des membres du Parlement ; les électeurs inscrits la soutiennent, et il en faut un dixième. Le Conseil constitutionnel contrôle d'abord la proposition. De {ref.rip_depuis} au {ref.arrete}, il en a examiné {ref.S} ; {ref.C} a été jugée conforme et a recueilli {ref.soutiens} soutiens pour {ref.seuil} requis. Aucune n'a été soumise au référendum."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "promesses"
  rang: 60
  prolongement: true
  nature: "Registre du Conseil constitutionnel, vérifié contre le Journal officiel ; données ouvertes"
  refonte: "2026-10-12"
onglet:  # panneau « Prolongements » de la barre du dossier (partials/barre-bloc.html)
  long: "Un président peut-il recourir au référendum ?"
  court: "Référendum"
  role: "registre et initiative partagée"
---

{{< reutiliser-ancre >}}

Promettre de soumettre une réforme aux électeurs, c'est promettre de passer par une autre voie que le seul vote du Parlement. La Constitution l'organise&nbsp;: «&nbsp;{{< ref-val "cit_art3" >}}&nbsp;» (art.&nbsp;3). Cette page dit qui peut soumettre un texte au référendum, par quelle voie et sur quels sujets, puis ce qu'ont décidé les scrutins qui ont eu lieu et ce que sont devenues les initiatives partagées, à partir du registre du Conseil constitutionnel, rapproché scrutin par scrutin du Journal officiel. Elle s'appuie sur la lettre des textes, les décisions citées et les documents officiels lus, et sépare ce que disent les textes, ce qui a été appliqué et ce que le Conseil constitutionnel en a déduit&nbsp;; elle ne tient pas lieu de consultation juridique.

## Qui peut soumettre un texte au référendum&nbsp;? {#qui-peut}

Trois articles de la Constitution permettent de soumettre un texte au référendum&nbsp;: l'article&nbsp;11 pour un projet de loi, l'article&nbsp;89 pour une révision de la Constitution, l'article&nbsp;88-5 pour l'adhésion d'un État à l'Union européenne. Ils ne laissent pas au président la même latitude&nbsp;: selon la voie, il décide sur une proposition qu'il ne fait pas lui-même, après un vote des deux assemblées (l'Assemblée nationale et le Sénat), ou parce que l'article dispose que le projet «&nbsp;est soumis&nbsp;» au référendum. Trois articles, mais quatre modalités&nbsp;: l'article&nbsp;11 ouvre aussi l'initiative partagée, où des parlementaires soutenus par des électeurs engagent la procédure ([plus bas](#initiative-partagee)).

**L'article 11, pour un projet de loi.** La proposition vient du Gouvernement, quand le Parlement est en session, ou des deux assemblées ensemble&nbsp;; elle est publiée au Journal officiel. Le président décide ensuite&nbsp;: il «&nbsp;{{< ref-val "cit_art11_peut" >}}&nbsp;», sur l'un des sujets que l'article énumère (l'organisation des pouvoirs publics, des réformes de politique économique, sociale ou environnementale et les services publics qui y concourent, la ratification de certains traités). Quand c'est le Gouvernement qui propose, il fait devant chaque assemblée une déclaration suivie d'un débat. L'article dit «&nbsp;peut&nbsp;»&nbsp;: la proposition est nécessaire, et le texte n'en fait pas une obligation pour le président. Celui-ci signe seul l'acte de soumission&nbsp;: l'article&nbsp;19 le range parmi les exceptions au contreseing, c'est-à-dire à la signature du Premier ministre (et, le cas échéant, des ministres responsables) ajoutée à celle du président (voir [ce que le président peut décider seul](/pouvoirs-du-president-de-la-republique/)). Si le texte est adopté, le président promulgue la loi dans les quinze jours.

<details class="repli"><summary>L’article 11, mot pour mot</summary>

Le président «&nbsp;{{< ref-val "cit_art11_peut" >}}&nbsp;», mais seulement «&nbsp;{{< ref-val "cit_art11_1" >}}&nbsp;», et sur un sujet que l'article délimite&nbsp;: «&nbsp;{{< ref-val "cit_art11_objet" >}}&nbsp;». Lorsque le référendum est organisé sur proposition du Gouvernement, «&nbsp;{{< ref-val "cit_art11_decl" >}}&nbsp;». Si le texte est adopté, «&nbsp;{{< ref-val "cit_art11_promulgue" >}}&nbsp;».

</details>

**L'article 89, pour une révision de la Constitution.** Le texte peut venir du Gouvernement&nbsp;: le président le présente sur proposition du Premier ministre, et il s'appelle alors un projet de révision. Il peut aussi venir de députés ou de sénateurs&nbsp;: c'est une proposition de révision. Dans les deux cas, il doit être «&nbsp;{{< ref-val "cit_art89_identiques" >}}&nbsp;», puis approuvé par référendum. Le projet du Gouvernement, et lui seul, a une seconde voie&nbsp;: le président peut le soumettre au Parlement réuni en Congrès, où il doit obtenir les trois cinquièmes des suffrages exprimés. Une proposition venue des parlementaires ne peut donc aboutir que par référendum. La décision de convoquer le Congrès ne figure pas dans la liste des exceptions de l'article&nbsp;19&nbsp;; par la lettre de cet article, elle est contresignée.

<details class="repli"><summary>L’article 89, mot pour mot</summary>

«&nbsp;{{< ref-val "cit_art89_init" >}}&nbsp;» Le projet ou la proposition doit être «&nbsp;{{< ref-val "cit_art89_identiques" >}}&nbsp;». Une fois le texte voté, «&nbsp;{{< ref-val "cit_art89_ref" >}}&nbsp;» Toutefois, «&nbsp;{{< ref-val "cit_art89_voies" >}}&nbsp;», où il doit réunir les trois cinquièmes des suffrages exprimés. L'article borne enfin toute révision&nbsp;: «&nbsp;{{< ref-val "cit_art89_limites" >}}&nbsp;»

</details>

**L'article 88-5, pour l'adhésion d'un État à l'Union européenne.** Le référendum est ici la règle&nbsp;: le projet de loi qui autorise la ratification d'un traité d'adhésion est soumis au référendum par le président. Le Parlement peut l'éviter si chaque assemblée vote, aux trois cinquièmes, une même motion&nbsp;: le projet passe alors par le Congrès, aux trois cinquièmes des suffrages exprimés. L'article ne vaut pas pour toutes les adhésions&nbsp;: la loi constitutionnelle du 23&nbsp;juillet 2008 (art.&nbsp;47) en exclut certaines, selon la date de la conférence qui les a préparées. L'acte de soumission n'est pas non plus dans la liste de l'article&nbsp;19&nbsp;: il est contresigné. Aucun des {{< ref-val "N" >}} scrutins du registre n'a eu lieu sur ce fondement. Ce que la France décide seule ou avec les autres États membres est l'objet d'une [autre page de ce dossier](/ce-que-la-france-peut-decider-dans-l-union-europeenne/).

<details class="repli"><summary>L’article 88-5 et sa clause de 2004, mot pour mot</summary>

«&nbsp;{{< ref-val "cit_art88_5_1" >}}&nbsp;» Toutefois, «&nbsp;{{< ref-val "cit_art88_5_2" >}}&nbsp;», c'est-à-dire par le Congrès, aux trois cinquièmes des suffrages exprimés. La loi constitutionnelle du 23&nbsp;juillet 2008 (art.&nbsp;47) dispose que l'article «&nbsp;{{< ref-val "cit_clause_2004" >}}&nbsp;».

</details>

**Le Conseil constitutionnel contrôle, il ne soumet rien.** «&nbsp;{{< ref-val "cit_art60" >}}&nbsp;» (art.&nbsp;60). L'article&nbsp;61 lui fait aussi examiner «&nbsp;{{< ref-val "cit_art61" >}}&nbsp;»&nbsp;: c'est la voie de l'initiative partagée, plus bas.

## Combien de référendums ont eu lieu, et qu'ont-ils décidé&nbsp;? {#registre}

{{< figure-svg fichier="referendum-registre" alt="Frise de 1958 à 2026 : une tige par référendum national, dont la hauteur donne la part des oui parmi les suffrages exprimés, pleine pour un texte adopté, vide pour un texte rejeté ; une ligne marque la moitié des exprimés ; une zone grisée couvre les années depuis le dernier scrutin, en 2005. Les valeurs sont dans le tableau sous la figure." >}}Référendums nationaux dont le Conseil constitutionnel a proclamé les résultats, du 4&nbsp;octobre 1958 au {{< ref-val "arrete" >}}. Hors référendum du 28&nbsp;septembre 1958 (adoption de la Constitution, avant la création du Conseil) et consultations locales. Le oui y est une part des suffrages exprimés, la participation une part des inscrits&nbsp;: en 2000, {{< ref-val "oui_2000" >}}&nbsp;% de oui parmi les exprimés, pour une participation de {{< ref-val "part_2000" >}}&nbsp;% des inscrits.{{< /figure-svg >}}

{{< fig-actions id="registre" >}}

{{< ref-tableau "registre" "Les scrutins en tableau" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Du 4&nbsp;octobre 1958 au {{< ref-val "arrete" >}}, {{< ref-val "N" >}} référendums nationaux ont été organisés&nbsp;; {{< ref-val "A" >}} ont adopté le texte soumis, {{< ref-val "R" >}} l'ont rejeté, et le dernier date du {{< ref-val "dernier" >}}.

</div>

{{< ref-val "n_loi" >}} scrutins ont eu lieu sur le fondement de l'article&nbsp;11, {{< ref-val "n_rev" >}} sur celui de l'article&nbsp;89&nbsp;: le quinquennat, en 2000. Deux projets soumis au titre de l'article&nbsp;11 portaient pourtant sur la Constitution elle-même&nbsp;: celui de 1962, adopté, qui modifie ses articles&nbsp;6 et&nbsp;7 pour faire élire le président au suffrage universel direct (loi n°&nbsp;62-1292 du 6&nbsp;novembre 1962), et celui de 1969, rejeté. Ce recours à l'article&nbsp;11 pour réviser la Constitution a été contesté&nbsp;: saisi de la loi de 1962 par le président du Sénat, le Conseil constitutionnel s'est déclaré incompétent (décision n°&nbsp;62-20&nbsp;DC du 6&nbsp;novembre 1962)&nbsp;; selon l'Assemblée nationale, cette pratique n'a plus été employée depuis l'échec de 1969.

La participation a varié de {{< ref-val "part_min" >}}&nbsp;% ({{< ref-val "part_min_an" >}}) à {{< ref-val "part_max" >}}&nbsp;% ({{< ref-val "part_max_an" >}}). Les deux textes rejetés l'ont été en 1969 (régions et Sénat), avec {{< ref-val "non_1969" >}}&nbsp;% de non parmi les suffrages exprimés, et en 2005 (traité établissant une Constitution pour l'Europe), avec {{< ref-val "non_2005" >}}&nbsp;%.

## Le référendum d'initiative partagée a-t-il déjà abouti&nbsp;? {#initiative-partagee}

Une autre voie, créée par la révision de 2008, s'applique depuis le 1er&nbsp;janvier {{< ref-val "rip_depuis" >}}&nbsp;: un référendum peut être organisé «&nbsp;{{< ref-val "cit_art11_rip" >}}&nbsp;». Ce n'est pas une initiative des citoyens&nbsp;: le texte vient de parlementaires, les électeurs le soutiennent.

Le parcours s'est toujours arrêté avant le vote&nbsp;: de {{< ref-val "rip_depuis" >}} au {{< ref-val "arrete" >}}, {{< ref-val "S" >}} propositions ont été soumises au Conseil constitutionnel, {{< ref-val "C" >}} a été jugée conforme, aucune n'a réuni le soutien d'un dixième des inscrits, et aucune n'a donc été soumise au référendum. Ce seuil franchi, un dernier filtre resterait&nbsp;: il suffit que chaque assemblée examine la proposition une fois, même sans l'adopter, pour que la condition de sa soumission au référendum ne soit pas remplie. La procédure tient en quatre étapes.

1. Un cinquième au moins des membres du Parlement dépose une proposition de loi&nbsp;; «&nbsp;{{< ref-val "cit_lo1" >}}&nbsp;» (loi organique du 6&nbsp;décembre 2013, art.&nbsp;1er).
2. Le Conseil vérifie, «&nbsp;{{< ref-val "cit_o45_2_delai" >}}&nbsp;», que le cinquième est atteint, que l'objet relève de l'article&nbsp;11 et respecte deux délais, et qu'aucune disposition n'est contraire à la Constitution (ordonnance du 7&nbsp;novembre 1958, art.&nbsp;45-2). Les deux délais sont ceux de l'article&nbsp;11&nbsp;: la proposition «&nbsp;{{< ref-val "cit_art11_abrog" >}}&nbsp;», et, après un rejet par le peuple, «&nbsp;{{< ref-val "cit_art11_deux_ans" >}}&nbsp;».
3. Si elle est conforme, les électeurs inscrits peuvent la soutenir&nbsp;: «&nbsp;{{< ref-val "cit_lo4" >}}&nbsp;» (loi organique, art.&nbsp;4).
4. Si un dixième des inscrits l'a soutenue, le Conseil constitutionnel le déclare, et chacune des deux assemblées a six mois, à compter de la publication de cette décision au Journal officiel, pour examiner la proposition&nbsp;; «&nbsp;{{< ref-val "cit_lo9_susp" >}}&nbsp;» (loi organique, art.&nbsp;9). Si l'une d'elles ne l'a pas examinée dans ce délai, le président la soumet au référendum. Pour qu'il n'y ait pas de référendum, il suffit donc que chaque assemblée examine la proposition au moins une fois, même sans l'adopter. Pour cette étape, l'article&nbsp;11 emploie l'indicatif&nbsp;: «&nbsp;{{< ref-val "cit_art11_soumet" >}}&nbsp;», là où son premier alinéa dit «&nbsp;peut soumettre&nbsp;».

<details class="repli"><summary>L’article 9 de la loi organique, mot pour mot</summary>

Le président soumet la proposition au référendum si elle «&nbsp;{{< ref-val "cit_lo9" >}}&nbsp;». «&nbsp;{{< ref-val "cit_lo9_susp" >}}&nbsp;»

</details>

{{< figure-svg fichier="referendum-rip" alt="Quatre barres en entonnoir, chacune avec son nombre : propositions soumises au Conseil constitutionnel, jugées conformes, ayant réuni le soutien d'un dixième des inscrits, soumises au référendum ; dessous, une jauge montre les soutiens recueillis par la proposition sur les aérodromes de Paris, rapportés au seuil requis." >}}Propositions de loi présentées au titre de l'article&nbsp;11, alinéa&nbsp;3, dont le Conseil constitutionnel a été saisi, de {{< ref-val "rip_depuis" >}} au {{< ref-val "arrete" >}}, et ce qu'elles sont devenues.{{< /figure-svg >}}

{{< fig-actions id="rip" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** De {{< ref-val "rip_depuis" >}} au {{< ref-val "arrete" >}}, le Conseil constitutionnel a été saisi de {{< ref-val "S" >}} propositions de loi au titre de l'article&nbsp;11&nbsp;; {{< ref-val "C" >}} a été jugée conforme et a recueilli {{< ref-val "soutiens" >}} soutiens pour {{< ref-val "seuil" >}} requis, soit {{< ref-val "part_seuil" >}}&nbsp;% du seuil&nbsp;; aucune n'a été soumise au référendum.

</div>

{{< ref-tableau "rip" "Les décisions en tableau, avec leurs motifs" >}}

Les {{< ref-val "non_conformes" >}} autres propositions ont été jugées non conformes. {{< ref-val "cond3_maj" >}} contenaient une disposition contraire à la Constitution (2021-2 et 2024-6 RIP). {{< ref-val "cond2_maj" >}} ne remplissaient pas la condition d'objet. Le Conseil dit pourquoi, et la page le cite sans juger ses raisons&nbsp;; le tableau ci-dessus donne, décision par décision, les motifs et leurs considérants.

**Les propositions sur la retraite à 62&nbsp;ans.** À la date de la saisine, constate le Conseil, «&nbsp;{{< ref-val "m23_7" >}}&nbsp;» (décision 2023-4 RIP, consid.&nbsp;{{< ref-val "m23_7_n" >}}). La proposition, qui interdisait de fixer cet âge au-delà, «&nbsp;{{< ref-val "m23_8" >}}&nbsp;» (consid.&nbsp;{{< ref-val "m23_8_n" >}}), et son adoption par référendum n'y changerait rien, car «&nbsp;{{< ref-val "m23_9" >}}&nbsp;» (consid.&nbsp;{{< ref-val "m23_9_n" >}}). Le Conseil en conclut qu'«&nbsp;{{< ref-val "m23_10" >}}&nbsp;» (consid.&nbsp;{{< ref-val "m23_10_n" >}}). La seconde proposition, déposée au Sénat (2023-5 RIP), est écartée pour la même raison&nbsp;; de la hausse de prélèvement qu'elle ajoutait sur des revenus du patrimoine et des produits de placement, le Conseil relève&nbsp;: «&nbsp;{{< ref-val "m235_10" >}}&nbsp;» (consid.&nbsp;{{< ref-val "m235_10_n" >}}).

**La proposition sur la fin de vie.** La décision 2026-7 RIP repose d'abord sur un autre motif, fondé sur les travaux préparatoires de la révision constitutionnelle de 1995&nbsp;: «&nbsp;{{< ref-val "m26_7" >}}. {{< ref-val "m26_7b" >}}.&nbsp;» (consid.&nbsp;{{< ref-val "m26_7_n" >}}). C'est l'interprétation que le Conseil donne de ces travaux&nbsp;: l'article&nbsp;11 ne mentionne pas les «&nbsp;questions de société&nbsp;». La décision porte sur les objets que le premier alinéa de l'article&nbsp;11 ouvre au référendum&nbsp;; elle ne se prononce pas sur une révision de la Constitution (art.&nbsp;89). La proposition portant sur la fin de vie, le Conseil juge qu'«&nbsp;{{< ref-val "m26_9" >}}&nbsp;» (consid.&nbsp;{{< ref-val "m26_9_n" >}}). La décision ajoute ensuite le motif retenu pour les retraites&nbsp;: la proposition «&nbsp;{{< ref-val "m26_11" >}}&nbsp;» (consid.&nbsp;{{< ref-val "m26_11_n" >}}), donc «&nbsp;{{< ref-val "m26_13" >}}&nbsp;» (consid.&nbsp;{{< ref-val "m26_13_n" >}}).

**{{< ref-val "depots_sans_saisine_maj" >}} autres propositions** ont été déposées «&nbsp;en application de l'article 11&nbsp;» sans qu'aucune décision du Conseil constitutionnel ne les concerne dans le registre consulté&nbsp;: au Sénat, n°&nbsp;459 (20&nbsp;avril 2018, contrôle de l'immigration)&nbsp;; à l'Assemblée nationale, n°&nbsp;1749 (6&nbsp;mars 2019, mesures contre les djihadistes français ayant combattu en Irak et en Syrie) et n°&nbsp;5203 (5&nbsp;avril 2022, mauvais traitements envers les animaux). Elles ne sont pas comptées parmi les {{< ref-val "S" >}} saisines, dont l'unité est la décision du Conseil. Elles portaient respectivement la signature de {{< ref-val "depots_auteurs" >}} parlementaires. L'article&nbsp;11 prévoit l'initiative d'un cinquième des membres du Parlement. La loi organique prévoit que la proposition est transmise au Conseil constitutionnel par le président de l'assemblée saisie&nbsp;; les sources consultées ne permettent pas d'établir ce qu'il est advenu de ces textes.

## Ce qu'un référendum décide, et ce qu'il ne fait pas {#ce-qu-il-decide}

Le référendum tranche le texte soumis&nbsp;: adopté, un projet de loi de l'article&nbsp;11 devient une loi, que le président promulgue dans les quinze jours, et un projet de révision de l'article&nbsp;89 modifie la Constitution. Le scrutin ne garantit pas, à lui seul, la mise en œuvre de ce texte ni le résultat auquel une promesse l'associe. Une loi adoptée par référendum reste une loi&nbsp;: le législateur peut ensuite la modifier ou l'abroger, comme le rappelle le Conseil constitutionnel dans la décision 2023-4 RIP citée plus haut. Certaines de ses dispositions peuvent attendre des textes d'application, car le code civil dispose que, pour les lois, «&nbsp;{{< ref-val "cit_cc1" >}}&nbsp;» (art.&nbsp;1er&nbsp;; voir [une loi votée s'applique-t-elle tout de suite&nbsp;?](/une-loi-votee-s-applique-t-elle-tout-de-suite/)). Le scrutin ne raccourcit pas non plus le temps qu'une mesure met à produire ses effets ([une promesse peut-elle produire ses effets en cinq ans&nbsp;?](/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/)), et ne choisit pas [l'indicateur](/comment-savoir-si-une-promesse-est-tenue/) qui dira si la promesse est tenue. La proclamation dit combien de bulletins portaient oui et non&nbsp;; elle ne dit pas pourquoi.

## Que s'est-il passé après le rejet de 2005&nbsp;? {#apres-2005}

Le 29&nbsp;mai 2005, le projet de loi autorisant la ratification du traité établissant une Constitution pour l'Europe a été rejeté. En 2008, la ratification d'un autre traité, celui de Lisbonne, a été autorisée par une loi, après une révision de la Constitution approuvée par le Congrès&nbsp;; aucun référendum n'a eu lieu.

Le traité de Lisbonne, signé après le rejet de 2005, est un autre traité&nbsp;; son intitulé, «&nbsp;traité de Lisbonne modifiant le traité sur l'Union européenne et le traité instituant la Communauté européenne&nbsp;», dit qu'il modifie les traités existants. Le Conseil constitutionnel a jugé que l'autorisation de le ratifier «&nbsp;{{< ref-val "cit_2007_560" >}}&nbsp;» (décision n°&nbsp;2007-560&nbsp;DC du 20&nbsp;décembre 2007). Le 4&nbsp;février 2008, le Parlement réuni en Congrès a approuvé le projet de loi constitutionnelle modifiant le titre&nbsp;XV de la Constitution «&nbsp;{{< ref-val "cit_congres_2008" >}}&nbsp;» ([scrutin du Congrès](https://www.assemblee-nationale.fr/13/scrutins/jo9000.asp))&nbsp;; c'est la loi constitutionnelle n°&nbsp;2008-103 du même jour. La ratification du traité de Lisbonne a ensuite été autorisée par la loi n°&nbsp;2008-125 du 13&nbsp;février 2008.

Trois plans se distinguent ici. **En droit**, l'article&nbsp;53 dispose que les traités qu'il énumère «&nbsp;{{< ref-val "cit_art53" >}}&nbsp;»&nbsp;; l'article&nbsp;11 permet de soumettre au référendum un projet de loi autorisant la ratification de certains traités, mais le texte dit que le président «&nbsp;peut&nbsp;» le faire, sans en faire une obligation. **Sur le contenu**, l'intitulé établit la forme du traité de Lisbonne, pas le rapport entre son contenu et celui du texte rejeté, que cette page ne compare pas. **En politique**, la page s'en tient à deux votes publiés. Le {{< ref-val "congres_date" >}}, le Congrès a approuvé la révision par {{< ref-val "congres_pour" >}} voix contre {{< ref-val "congres_contre" >}}, pour une majorité requise de {{< ref-val "congres_majorite" >}}, les trois cinquièmes des suffrages exprimés. Le {{< ref-val "motion_date" >}}, l'Assemblée nationale a rejeté, par {{< ref-val "motion_contre" >}} voix contre {{< ref-val "motion_pour" >}}, une motion présentée par M.&nbsp;Ayrault et plusieurs de ses collègues, tendant à soumettre au référendum le projet de loi autorisant la ratification ([scrutin n°&nbsp;82](https://www.assemblee-nationale.fr/13/scrutins/jo0082.asp)).

**Une révision annoncée avec un référendum, en 2020 et 2021.** Le {{< ref-val "declaration_2020" >}}, devant la Convention citoyenne pour le climat, le président de la République s'est dit favorable à la réécriture de l'article premier de la Constitution qu'elle proposait, pour y introduire la biodiversité, l'environnement et la lutte contre le réchauffement climatique, et a déclaré&nbsp;: «&nbsp;{{< ref-val "cit_elysee" >}}&nbsp;» (texte publié par l'Élysée). Le projet de loi constitutionnelle complétant l'article&nbsp;1er et relatif à la préservation de l'environnement a été déposé à l'Assemblée nationale le {{< ref-val "e2021_depot" >}}. Adopté par l'Assemblée le {{< ref-val "e2021_an1" >}}, modifié par le Sénat le {{< ref-val "e2021_se1" >}}, adopté avec modifications par l'Assemblée le {{< ref-val "e2021_an2" >}}, il a été de nouveau modifié par le Sénat le {{< ref-val "e2021_se2" >}}&nbsp;: c'est la dernière étape du dossier législatif du Sénat. Les deux assemblées ne l'ont donc jamais voté en termes identiques, ce que l'article&nbsp;89 exige avant tout référendum.

Ce cas montre une condition de l'article&nbsp;89 qui n'a pas été remplie&nbsp;; il n'explique pas pourquoi aucun référendum n'a eu lieu depuis 2005.

## Que demander à une promesse de référendum&nbsp;? {#grille}

1. **Sur quoi&nbsp;?** Un projet de loi sur un sujet de l'article&nbsp;11, une révision de la Constitution, ou l'adhésion d'un État à l'Union européenne&nbsp;: chaque objet a sa voie, et pour l'initiative partagée le Conseil constitutionnel contrôle l'objet avant tout recueil de soutiens.
2. **Par quelle voie&nbsp;?** Article&nbsp;11, article&nbsp;89, article&nbsp;88-5, ou initiative partagée.
3. **Avec qui&nbsp;?** Le Gouvernement ou les deux assemblées, qui proposent (art.&nbsp;11)&nbsp;; les deux assemblées, qui votent le texte en termes identiques (art.&nbsp;89)&nbsp;; un cinquième des parlementaires et un dixième des électeurs (initiative partagée).
4. **Quelles conditions restent à franchir, et qui les vérifie&nbsp;?** Une proposition publiée, une déclaration suivie d'un débat, un vote identique des deux assemblées, ou le contrôle du Conseil constitutionnel et le recueil des soutiens&nbsp;; le Conseil veille ensuite à la régularité du scrutin.
5. **Pour obtenir quoi&nbsp;?** Le scrutin tranche un texte&nbsp;: une loi, que le président promulgue dans les quinze jours, ou une révision de la Constitution. Ses mesures d'application et ses effets viennent ensuite, et se jugent à part.

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas si le référendum est un bon ou un mauvais instrument, ni pourquoi aucun n'a été organisé depuis 2005&nbsp;: les sources consultées (registre du Conseil constitutionnel, Journal officiel, dossiers législatifs, déclaration de 2020) ne l'établissent pas, et une intention ne se lit pas dans un acte. Elle ne compte ni le référendum du 28&nbsp;septembre 1958, antérieur au Conseil constitutionnel, ni les consultations locales. Elle lit la Constitution en vigueur et les décisions citées, sans doctrine ni autre jurisprudence, et ne tient pas lieu de consultation juridique. Le registre est arrêté au {{< ref-val "arrete" >}}&nbsp;; le cas de 2020 et 2021 repose sur des pages consultées le 12&nbsp;octobre 2026.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Ce qu'un vote décide" avis="non" >}}
Cette page montre que le référendum tranche un texte, pas ses suites. Le livre suit neuf promesses écrites, datées et signées jusqu'à leur dernier obstacle, et consacre sa clôture au référendum de 2005 et à ce qu'il en est advenu. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Constitution** du 4&nbsp;octobre 1958, art.&nbsp;3, 11, 19, 53, 60, 61, 88-5 et 89, texte en vigueur (Légifrance). **Loi constitutionnelle** n°&nbsp;2008-724 du 23&nbsp;juillet 2008, art.&nbsp;47 (texte adopté par le Congrès le 21&nbsp;juillet 2008, publié par le Sénat)&nbsp;; **loi constitutionnelle** n°&nbsp;2008-103 du 4&nbsp;février 2008 (texte adopté par le Congrès le même jour, publié par le Sénat)&nbsp;; **loi** n°&nbsp;2008-125 du 13&nbsp;février 2008. **Ordonnance** n°&nbsp;58-1067 du 7&nbsp;novembre 1958, art.&nbsp;45-2&nbsp;; **loi organique** n°&nbsp;2013-1114 du 6&nbsp;décembre 2013 portant application de l'article&nbsp;11, art.&nbsp;1er, 4 et 9&nbsp;; **code civil**, art.&nbsp;1er.

**Conseil constitutionnel**, proclamations des résultats des référendums (décisions 61-4, 62-7, 62-9, 69-10, 72-11, 88-14, 92-19, 2000-29, 2005-38) et décisions sur les propositions de loi de l'article&nbsp;11 (2019-1 et 2019-1-8, 2021-2, 2022-3, 2023-4, 2023-5, 2024-6, 2026-7 RIP), lues dans le stock CONSTIT que publie la DILA, arrêté au {{< ref-val "arrete" >}}&nbsp;; décision n°&nbsp;2007-560&nbsp;DC.

**Journal officiel** (Légifrance), décrets de soumission au référendum et lois adoptées par référendum&nbsp;; **Assemblée nationale**, données ouvertes des législatures XV à XVII (dépôts au titre de l'article&nbsp;11), et analyses du scrutin du Congrès du 4&nbsp;février 2008 et du scrutin n°&nbsp;82 du 6&nbsp;février 2008 (XIIIe législature), consultées le 12&nbsp;octobre 2026&nbsp;; **Sénat**, proposition de loi n°&nbsp;459 (2017-2018) et dossier législatif du projet de loi constitutionnelle n°&nbsp;449 (2020-2021), consultés le 12&nbsp;octobre 2026&nbsp;; **Présidence de la République**, discours du 29&nbsp;juin 2020 devant la Convention citoyenne pour le climat (elysee.fr), consulté le 12&nbsp;octobre 2026.

<details class="repli"><summary>Comment le registre des référendums a été vérifié</summary>

**Le registre.** Les décisions du Conseil constitutionnel sont lues dans le stock que publie la DILA (fichiers ouverts, arrêtés au {{< ref-val "arrete" >}}). Parmi les décisions classées «&nbsp;référendum&nbsp;», seules les proclamations de résultats entrent au registre&nbsp;; les autres sont des désignations de délégués, des réponses à des requêtes et des observations. Pour chaque scrutin, les nombres d'inscrits, de votants, de suffrages exprimés, de oui et de non sont lus dans la proclamation, et leur cohérence est contrôlée (oui et non font les exprimés&nbsp;; exprimés, votants et inscrits sont dans l'ordre). Les pourcentages de cette page sont recalculés à partir de ces nombres et arrondis au plus proche&nbsp;; le tableau récapitulatif du Conseil constitutionnel les donne tronqués, d'où des écarts d'un centième de point sur certains scrutins.

**Le témoin du Journal officiel.** Chaque scrutin a été rapproché du Journal officiel&nbsp;: le décret par lequel le président soumet le texte, à la date que donne la proclamation, et, pour chaque texte adopté, la loi promulguée. Les {{< ref-val "A" >}} lois existent&nbsp;; aucune loi n'existe pour les {{< ref-val "R" >}} textes rejetés. Un seul décret n'a pas été retrouvé dans le fonds de Légifrance, celui du 2&nbsp;octobre 1962, dont la loi est publiée. La recherche par titre dans le Journal officiel ne fait apparaître aucun scrutin absent du registre.

**Les limites.** Les nombres de voix n'ont pas de second producteur pour 1961-1988&nbsp;: ils sont contrôlés par leur cohérence, pas par une autre source. Les résultats publiés par le ministère de l'Intérieur pour 1992, 2000 et 2005 précèdent les rectifications du Conseil&nbsp;: même scrutin, autre définition, donc pas un témoin.

</details>

Les chiffres, les contrôles et les figures sont produits par un script unique. Il relit les décisions et les textes archivés et s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases. Il retrouve mot pour mot chaque citation de la Constitution, de l'ordonnance, de la loi organique et du code civil, et chaque motif de décision dans le considérant indiqué&nbsp;; il vérifie l'empreinte des pages du Sénat, de l'Élysée et de l'Assemblée archivées, y retrouve les passages cités et les dates du dossier de 2021, et lit dans les deux scrutins de 2008 les nombres de voix que la page donne. La liste des propositions déposées sans décision est contrôlée contre les données de l'Assemblée et du Sénat&nbsp;; le nombre de leurs signataires, transcrit dans le script, est relu dans ces données et dans le texte déposé au Sénat. Les objets des scrutins et des propositions sont rédigés à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_referendum.csv), en format long&nbsp;; [JSON](/promesses_referendum.json), avec les identifiants des décisions, les motifs cités et le compte rendu des contrôles. Une version antérieure de ce jeu, sans les motifs cités ajoutés le 12&nbsp;octobre 2026, est archivée sur Zenodo avec les six autres de la même série et leur note de méthode, sous un identifiant permanent&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_referendum" jeu="promesses_referendum" sources="Conseil constitutionnel et Journal officiel" donnees="Le registre des référendums nationaux (inscrits, votants, exprimés, oui, non, article, issue), les décisions sur le référendum d'initiative partagée avec leurs motifs cités et les dépôts sans décision ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Un président peut soumettre un projet de loi au référendum sur proposition du Gouvernement ou des deux assemblées, et sur les sujets que fixe l'article&nbsp;11 de la Constitution&nbsp;; une révision de la Constitution (article&nbsp;89) et l'adhésion d'un État à l'Union européenne (article&nbsp;88-5) ont leurs propres voies. Du 4&nbsp;octobre 1958 au {{< ref-val "arrete" >}}, {{< ref-val "N" >}} référendums nationaux ont été organisés&nbsp;; {{< ref-val "A" >}} ont adopté le texte soumis, {{< ref-val "R" >}} l'ont rejeté, et le dernier date du {{< ref-val "dernier" >}}. Le référendum d'initiative partagée, ouvert en {{< ref-val "rip_depuis" >}}, n'a encore conduit à aucun scrutin.
{{< /reutiliser >}}
