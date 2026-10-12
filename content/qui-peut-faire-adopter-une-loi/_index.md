---
title: "Qui peut faire adopter une loi ?"
description: "Déposer un texte, le faire venir en séance, obtenir le dernier mot : la Constitution répartit ces clés entre le Gouvernement, les parlementaires et les deux assemblées. Elle confie le vote de la loi au Parlement, et trois situations sont à distinguer (article 49.3, ordonnances budgétaires, référendum). L'origine des lois promulguées depuis 2012, rapprochée loi par loi entre l'Assemblée nationale, le Sénat et le Journal officiel, le sort des propositions de loi déposées et les engagements de responsabilité. Données ouvertes."
chapo: "Les lois viennent-elles surtout du Gouvernement ? Depuis la XVe législature (2017-2022), la majorité des lois ordinaires promulguées, hors traités, est issue d'une proposition de député ou de sénateur ; pour la XVe, c'est de peu (au moins {ado.Pmin15} lois sur {ado.N15}). Ce résultat dépend de ce qu'on compte : en y ajoutant les lois à procédure propre (budgets de l'État et de la sécurité sociale, lois qui complètent ou modifient la Constitution), la majorité parlementaire n'apparaît qu'avec la XVIe (2022-2024). Pourtant, environ {ado.Zdix} propositions de loi sur dix déposées à l'Assemblée nationale n'ont pas été examinées en séance avant la fin de leur législature. Les deux constats tiennent ensemble parce que faire adopter une loi demande plusieurs clés, que la Constitution répartit : le Premier ministre comme les parlementaires peuvent déposer, mais le Gouvernement a des priorités à l'ordre du jour et peut seul demander à l'Assemblée nationale de statuer définitivement. Le vote de la loi appartient au Parlement, et trois situations sont à distinguer : l'adoption d'un texte à une étape sans vote de l'Assemblée nationale sur celui-ci (article 49, alinéa 3), la mise en vigueur de dispositions budgétaires par ordonnance sans loi votée (articles 47 et 47-1) et l'adoption d'une loi par référendum (article 11)."
date: 2026-10-06
lastmod: 2026-10-12
donnees: [promesses_adopter]
og_title: "Qui peut faire adopter une loi ? — l'origine des lois, les propositions sans séance, l'ordre du jour et l'article 49.3 — S. Lalut"
og_image: "images/og-adopter-promesse.jpg"
og_image_alt: "Carte de partage : qui est à l'origine des lois promulguées ? Lois ordinaires, par législature, de la XIVe à la XVIIe (en cours au 06/10/2026) : projets du Gouvernement, propositions déposées à l'Assemblée nationale et au Sénat."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_adopter"
  nom: "Origine des lois promulguées de 2012 à 2026, propositions de loi déposées à l'Assemblée et engagements de responsabilité (art. 49, al. 3)"
  description: "Origine formelle au dépôt initial (projet du Gouvernement, proposition déposée à l'Assemblée nationale ou au Sénat) des lois promulguées de la XIVe à la XVIIe législature, rapprochée loi par loi entre les données de l'Assemblée nationale, la base Dosleg du Sénat et le Journal officiel : lois ordinaires (hors traités, lois de finances, de financement de la sécurité sociale, organiques et constitutionnelles), toutes natures hors traités, et lois promulguées entre deux législatures ; propositions de loi ordinaires déposées à l'Assemblée et restées sans examen en séance avant la fin de la législature, avec la borne du pire cas face aux bulletins statistiques ; engagements de responsabilité du Gouvernement sur un texte (art. 49, al. 3) par législature, et lois financières promulguées qui en ont fait l'objet."
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
  mots: ["loi", "proposition de loi", "projet de loi", "Parlement", "ordre du jour", "article 49.3", "article 45", "Assemblée nationale", "Sénat", "promesses"]
  fichiers: ["promesses_adopter.csv", "promesses_adopter.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Qui peut proposer une loi en France ?"
    answer: "Selon l'article 39 de la Constitution, « {ado.cit_art39} » Un texte du Gouvernement est un projet de loi ; un texte d'un député ou d'un sénateur est une proposition de loi. Dans le champ étudié ({ado.champ}), {ado.P16} des {ado.N16} lois promulguées sous la XVIe législature étaient issues d'une proposition, {ado.G16} d'un projet. Une proposition n'est toutefois pas recevable si elle crée ou aggrave une charge publique, ni si elle diminue les ressources publiques sans compenser la perte par une autre recette (article 40, tel que l'Assemblée nationale l'applique)."
  - question: "Une loi peut-elle être adoptée sans vote du Parlement sur son texte ?"
    answer: "Trois situations sont à distinguer : l'engagement de responsabilité du Gouvernement, qui fait considérer un texte comme adopté à une étape sans vote des députés sur lui, sauf censure (articles 49, alinéa 3, et 50) ; la mise en vigueur d'un budget par ordonnance si le Parlement ne s'est pas prononcé dans les délais, sans loi votée (articles 47 et 47-1) ; l'adoption d'une loi par référendum (article 11)."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "promesses"
  rang: 20
  refonte: "2026-10-12"
  nature: "Données de l'Assemblée nationale, du Sénat et du Journal officiel, rapprochées loi par loi ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Qui peut faire adopter une loi ?"
  court: "Adopter"
  role: "dépôt, séance, dernier mot, 49.3"
---

{{< reutiliser-ancre >}}

La Constitution confie le vote de la loi au Parlement&nbsp;: «&nbsp;{{< ado-val "cit_art24" >}}&nbsp;» (art.&nbsp;24). Trois situations s'en distinguent. L'engagement de responsabilité du Premier ministre fait considérer un texte comme adopté à une étape, sauf si une motion de censure est adoptée (art.&nbsp;49, al.&nbsp;3). Si le Parlement ne s'est pas prononcé dans les délais, les dispositions d'un projet de loi de finances ou de financement de la sécurité sociale (le budget de l'État ou celui de la sécurité sociale) peuvent être mises en vigueur par ordonnance, sans devenir une loi votée (art.&nbsp;47 et 47-1). Enfin, une loi peut être adoptée par référendum (art.&nbsp;11). Cette page suit la voie que prennent presque toutes les lois, celle du Parlement&nbsp;: qui a déposé, loi par loi, les lois promulguées depuis 2012, ce que sont devenues les propositions de loi déposées à l'Assemblée nationale, combien de fois la responsabilité du Gouvernement a été engagée sur un texte.

**Réponse courte.** Faire adopter une loi demande quatre clés. Déposer&nbsp;: «&nbsp;{{< ado-val "cit_art39" >}}&nbsp;» (art.&nbsp;39). Venir en séance&nbsp;: chaque assemblée fixe son ordre du jour, mais le Gouvernement y dispose de priorités (art.&nbsp;48). Conclure&nbsp;: il faut un texte identique des deux assemblées, ou, à défaut, le dernier mot de l'Assemblée nationale, que seul le Gouvernement peut lui demander (art.&nbsp;45). Et le Premier ministre peut engager la responsabilité du Gouvernement sur un texte, au risque d'une censure (art.&nbsp;49 et 50). Le Gouvernement ne fait donc pas adopter les lois seul, et les parlementaires, qui déposent la majorité des lois promulguées depuis 2017 dans le champ étudié, ne tiennent pas seuls les autres clés.

## Qui est à l'origine des lois promulguées&nbsp;? {#origine-des-lois}

Les lois viennent-elles surtout du Gouvernement&nbsp;? L'origine de chaque loi promulguée, au dépôt du texte, permet de le vérifier. Un texte du Gouvernement est un projet de loi&nbsp;; un texte d'un député ou d'un sénateur, une proposition de loi. Le compte porte sur les lois ordinaires, celles qui suivent la procédure commune. Il laisse de côté les lois qui ont leur procédure ou leur origine propre&nbsp;: {{< ado-val "champ_def" >}}.

{{< figure-svg fichier="adopter-origine" alt="Barres à 100 % par législature, de la XIVe à la XVIIe en cours : part des lois issues d'une proposition déposée à l'Assemblée nationale, d'une proposition déposée au Sénat, d'un projet du Gouvernement ; des pointillés marquent la moitié, un triangle la borne basse quand l'origine de certaines lois ne repose que sur une source. La part d'origine parlementaire est sous la moitié pour la XIVe et au-dessus pour les suivantes ; à droite, la part toutes natures hors traités. Les valeurs sont dans le tableau sous la figure." >}}Lois promulguées, rattachées à la législature de leur promulgation, selon l'origine du texte au dépôt initial. Champ étudié&nbsp;: lois ordinaires, {{< ado-val "champ" >}}.{{< /figure-svg >}}

{{< fig-actions id="origine" >}}

{{< ado-tableau "lois" "Les valeurs de la figure en tableau" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Dans le champ étudié, la part des lois promulguées issues d'une proposition de parlementaire est de {{< ado-val "Ppct14" >}}&nbsp;% sous la XIVe législature (2012-2017), puis dépasse la moitié&nbsp;: {{< ado-val "Ppct15" >}}&nbsp;% sous la XVe (au moins {{< ado-val "Pminpct15" >}}&nbsp;%), {{< ado-val "Ppct16" >}}&nbsp;% sous la XVIe et {{< ado-val "Ppct17" >}}&nbsp;% sous la XVIIe, en cours au {{< ado-val "releve" >}}.

</div>

**Ce que l'origine ne dit pas.** Elle dit qui a déposé le texte, non qui l'a voulu ni ce qu'il est devenu. Une proposition de loi peut avoir été préparée avec un ministère ou soutenue par le Gouvernement&nbsp;; un projet peut être profondément modifié par le Parlement. La hausse de la part des propositions ne mesure donc pas une autonomie croissante des parlementaires&nbsp;: aucune de ces séries n'observe ces influences.

**Le champ change-t-il la réponse&nbsp;?** Pour la XVe législature, oui. Sous la XVe, {{< ado-val "Ppct15" >}}&nbsp;% des lois du champ étudié sont d'origine parlementaire, mais {{< ado-val "Ptotpct15" >}}&nbsp;% seulement toutes natures réunies hors traités ({{< ado-val "Ptot15" >}} lois sur {{< ado-val "Ntot15" >}}). Ce second compte réintègre les lois financières, organiques et constitutionnelles&nbsp;; il donne aussi {{< ado-val "Ptotpct14" >}}&nbsp;% sous la XIVe, {{< ado-val "Ptotpct16" >}}&nbsp;% sous la XVIe et {{< ado-val "Ptotpct17" >}}&nbsp;% sous la XVIIe. **La majorité parlementaire de la XVe dépend donc du champ retenu.** Celle des XVIe et XVIIe n'en dépend pas.

Ces lois sont écartées du compte principal parce que leur origine ou leur procédure est fixée à part. Les articles&nbsp;47 et 47-1 de la Constitution ne parlent que de projets de loi de finances ou de financement de la sécurité sociale, et toutes ces lois viennent ici d'un projet du Gouvernement. Les lois organiques suivent leurs propres règles (art.&nbsp;46)&nbsp;: faute d'accord entre les deux assemblées, l'Assemblée nationale ne peut les adopter en dernière lecture qu'à la majorité absolue de ses membres, et celles qui concernent le Sénat doivent être votées dans les mêmes termes par les deux assemblées. Les lois autorisant un traité, toutes issues d'un projet, ne sont comptées nulle part.

<details class="repli"><summary>La lettre de l'article&nbsp;46</summary>

Article&nbsp;46&nbsp;: «&nbsp;{{< ado-val "cit_art46c" >}}&nbsp;» Et&nbsp;: «&nbsp;{{< ado-val "cit_art46d" >}}&nbsp;»

</details>

{{< ado-tableau "natures" "Toutes natures hors traités, par législature" >}}

Enfin, {{< ado-val "HLn" >}} lois promulguées en {{< ado-val "HLmois" >}}, après la dissolution de l'Assemblée et avant la XVIIe législature, ne relèvent d'aucune législature&nbsp;: elles ont leur ligne dans le tableau, et toutes sont d'origine parlementaire.

<details class="repli"><summary>Ce qui a été vérifié, et comment</summary>

Chaque loi promulguée depuis juin 2012 est rapprochée, par son numéro au Journal officiel, entre les données ouvertes de l'Assemblée nationale et la base Dosleg du Sénat. Quand les deux sources la connaissent, elles donnent la même origine pour toutes les lois. Certaines lois de la XIVe et de la XVe législatures manquent aux fichiers de l'Assemblée, parce que leur dossier a été ouvert sous la législature précédente&nbsp;: leur origine ne repose que sur le Sénat, d'où la borne «&nbsp;au moins&nbsp;» du tableau et le triangle de la figure.

Deux contrôles viennent d'ailleurs. Session par session, de 2017-2018 à 2024-2025, le nombre de lois promulguées hors traités est exactement celui que compte le baromètre de l'application des lois, publié par l'Assemblée nationale à partir des données de la DILA. Et le Sénat écrit, pour 2024-2025&nbsp;: «&nbsp;{{< ado-val "cit_senat_origine" >}}&nbsp;»&nbsp;; le décompte loi par loi donne {{< ado-val "s2425_P" >}} lois d'origine parlementaire sur {{< ado-val "s2425_N" >}}. Pour 2023-2024, il donne {{< ado-val "s2324_P" >}} sur {{< ado-val "s2324_N" >}}, soit {{< ado-val "s2324_pct" >}}&nbsp;%, que le tableau arrondit à {{< ado-val "s2324_arr" >}}&nbsp;%&nbsp;; le Sénat, cité ci-dessus, donne l'unité inférieure. Le Sénat parle de lois adoptées, ce relevé de lois promulguées&nbsp;: les deux comptes coïncident pour 2024-2025.

{{< ado-tableau "sessions" "Par session, toutes natures sauf les traités" >}}

</details>

## Combien de propositions de loi arrivent en séance&nbsp;? {#propositions-en-seance}

Peu. Dans chacune des trois législatures closes, environ {{< ado-val "Zdix" >}} propositions de loi ordinaires sur dix déposées en premier lieu à l'Assemblée nationale n'avaient pas été examinées en séance à la fin de la législature, d'après les données de l'Assemblée&nbsp;: {{< ado-val "Z14" >}} sur {{< ado-val "NZ14" >}} sous la XIVe ({{< ado-val "Zpct14" >}}&nbsp;%), {{< ado-val "Z15" >}} sur {{< ado-val "NZ15" >}} sous la XVe ({{< ado-val "Zpct15" >}}&nbsp;%), {{< ado-val "Z16" >}} sur {{< ado-val "NZ16" >}} sous la XVIe ({{< ado-val "Zpct16" >}}&nbsp;%). La XVIIe, en cours, n'est pas comptée.

Une proposition sans examen en séance n'a été ni rejetée ni interdite, et son contenu n'a pas forcément disparu&nbsp;: il peut être repris par un autre texte, ou par un amendement. Ces fractions ne se comparent pas non plus d'une législature à l'autre comme des taux&nbsp;: la XVIe, écourtée par la dissolution, a laissé aux textes un temps d'examen plus de deux fois plus court (durée médiane entre dépôt et fin de législature&nbsp;: {{< ado-val "med16" >}} jours, contre {{< ado-val "med14" >}} sous la XIVe).

<details class="repli"><summary>Le pire cas&nbsp;: les dépôts que les bulletins de l'Assemblée ne comptent pas</summary>

Ces nombres comptent les dépôts dans les données ouvertes de l'Assemblée. Ses bulletins statistiques en comptent un peu moins&nbsp;: {{< ado-val "exces14" >}}, {{< ado-val "exces15" >}} et {{< ado-val "exces16" >}} propositions de moins selon la législature, sans liste qui permette d'identifier les textes en cause. En retirant tout cet excès à la fois du total et des propositions restées sans examen, il en reste {{< ado-val "Zw14" >}} sur {{< ado-val "Nw14" >}}, {{< ado-val "Zw15" >}} sur {{< ado-val "Nw15" >}} et {{< ado-val "Zw16" >}} sur {{< ado-val "Nw16" >}}&nbsp;: toujours environ {{< ado-val "Zdix" >}} sur dix.

{{< ado-tableau "e1" "Les valeurs en tableau, avec la borne du pire cas" >}}

</details>

**Comment ces deux constats tiennent-ils ensemble&nbsp;?** Ils ne se contredisent pas, parce qu'ils ne portent pas sur les mêmes textes. Le premier part des lois promulguées, propositions du Sénat comprises, rattachées à la législature de leur promulgation&nbsp;; le second part des propositions déposées à l'Assemblée, rattachées à la législature de leur dépôt. Une petite part de propositions qui aboutissent peut fournir la majorité des lois promulguées, parce que les propositions sont bien plus nombreuses que les projets&nbsp;: selon les bulletins de l'Assemblée, {{< ado-val "bul14" >}} propositions de loi y ont été déposées en première lecture sous la XIVe législature, contre {{< ado-val "pjl14" >}} projets, et l'écart dépasse un facteur cinq dans chacune des trois législatures closes.

| Ce que ces mesures établissent | Ce qu'elles n'établissent pas |
|---|---|
| Qui a déposé chaque loi promulguée, au dépôt initial | Qui a voulu ou rédigé le texte, ni ce que les amendements en ont fait |
| Que la plupart des propositions déposées à l'Assemblée n'ont pas été examinées en séance avant la fin de leur législature | Pourquoi&nbsp;: aucune donnée ne relie ce sort à une décision d'ordre du jour, ni à l'article&nbsp;40 |
| Le nombre d'engagements de responsabilité et les textes qui en ont fait l'objet | Le contenu des lois qui en sont issues, ou ce qu'un vote aurait donné |

## Qui décide de ce qui vient en séance&nbsp;? {#ordre-du-jour}

Chaque assemblée, d'abord&nbsp;: selon l'article&nbsp;48, «&nbsp;{{< ado-val "cit_art48a" >}}&nbsp;» Le même article réserve au Gouvernement deux semaines de séance sur quatre, pour les textes et les débats dont il demande l'inscription, dans l'ordre qu'il fixe. Il lui donne aussi, s'il le demande, une priorité pour certains textes, dont les projets de budget de l'État et de la sécurité sociale. Et il garantit un jour de séance par mois aux groupes d'opposition et aux groupes minoritaires.

L'ordre du jour est donc partagé, et une priorité d'ordre du jour ne garantit pas l'adoption d'un texte. Une autre règle limite ce que les parlementaires peuvent proposer&nbsp;: leurs propositions et amendements ne sont pas recevables si leur adoption diminuait les ressources publiques, ou créait ou aggravait une charge publique (art.&nbsp;40). L'Assemblée nationale n'admet aucune compensation d'une charge, mais admet une perte de recettes compensée par une autre recette, le «&nbsp;gage&nbsp;». Les données de cette page ne disent pas lequel de ces filtres a écarté telle ou telle proposition&nbsp;: elles ne contiennent ni les décisions d'inscription à l'ordre du jour, ni les déclarations d'irrecevabilité.

<details class="repli"><summary>La lettre des articles&nbsp;48 et 40</summary>

Article&nbsp;48, alinéa&nbsp;2&nbsp;: «&nbsp;{{< ado-val "cit_art48" >}}&nbsp;» Alinéa&nbsp;3&nbsp;: «&nbsp;{{< ado-val "cit_art48c" >}}&nbsp;» Alinéa&nbsp;5&nbsp;: «&nbsp;{{< ado-val "cit_art48e" >}}&nbsp;»

Article&nbsp;40&nbsp;: «&nbsp;{{< ado-val "cit_art40" >}}&nbsp;»

Selon la fiche de synthèse n°&nbsp;52 de l'Assemblée nationale (septembre 2023), à propos des «&nbsp;ressources publiques&nbsp;», au pluriel&nbsp;: «&nbsp;{{< ado-val "cit_fiche52" >}}&nbsp;» Pour «&nbsp;une charge publique&nbsp;», au singulier, «&nbsp;{{< ado-val "cit_fiche52b" >}}&nbsp;».

</details>

## Qui a le dernier mot entre les deux assemblées&nbsp;? {#voie-ordinaire}

Le principe est l'accord&nbsp;: «&nbsp;{{< ado-val "cit_art45a" >}}&nbsp;» (Constitution, art.&nbsp;45). Quand l'accord ne vient pas, l'article&nbsp;45 fixe une séquence, et chaque étape a son acteur.

1. Une commission mixte paritaire, composée de députés et de sénateurs en nombre égal, peut être réunie pour proposer un texte sur les points encore en discussion. Elle peut l'être après deux lectures dans chaque assemblée, ou après une seule si le Gouvernement a engagé la procédure accélérée sans que les Conférences des présidents des deux assemblées s'y opposent conjointement. La réunir revient au Premier ministre ou, pour une proposition de loi, aux présidents des deux assemblées agissant conjointement.
2. Le texte de cette commission passe par le Gouvernement&nbsp;: c'est lui qui peut le soumettre aux deux assemblées, et aucun amendement n'y est recevable sans son accord.
3. En cas d'échec, le dernier mot de l'Assemblée nationale ne peut venir que du Gouvernement&nbsp;: si la commission n'aboutit pas à un texte commun, ou si ce texte n'est pas adopté, il peut, après une nouvelle lecture dans chaque assemblée, demander à l'Assemblée nationale de statuer définitivement. C'est vrai aussi d'une proposition de loi. Le Gouvernement peut ouvrir cette procédure&nbsp;; il ne garantit pas que l'Assemblée vote le texte.

Le Gouvernement dispose enfin d'un outil de séance, le vote unique (art.&nbsp;44)&nbsp;: s'il le demande, l'assemblée se prononce par un seul vote sur tout ou partie du texte, en ne retenant que les amendements qu'il a proposés ou acceptés. L'assemblée vote toujours, mais sur le texte tel que le Gouvernement l'accepte.

<details class="repli"><summary>La lettre des articles&nbsp;45 et 44</summary>

Article&nbsp;45, alinéa&nbsp;2&nbsp;: «&nbsp;{{< ado-val "cit_art45d" >}}&nbsp;» Alinéa&nbsp;3&nbsp;: «&nbsp;{{< ado-val "cit_art45e" >}}&nbsp;» Alinéa&nbsp;4&nbsp;: «&nbsp;{{< ado-val "cit_art45f" >}}&nbsp;»

Article&nbsp;44, alinéa&nbsp;3&nbsp;: «&nbsp;{{< ado-val "cit_art44c" >}}&nbsp;»

</details>

## Que change l'article 49, alinéa 3&nbsp;? {#article-49-3}

Il permet au Premier ministre, après délibération du Conseil des ministres, d'engager la responsabilité du Gouvernement devant l'Assemblée nationale sur un texte&nbsp;: le texte est alors considéré comme adopté à cette étape de son examen, sans que les députés votent sur lui, sauf si une motion de censure, déposée dans les vingt-quatre heures qui suivent, est votée. L'alinéa vise les projets de loi de finances et de financement de la sécurité sociale&nbsp;; hors de ces textes, le Premier ministre ne peut y recourir que pour un autre projet ou une proposition de loi par session. Le texte n'est pas pour autant adopté définitivement&nbsp;: l'engagement vaut pour une étape, et l'examen continue. Un même projet peut recevoir plusieurs engagements, y compris au cours d'une même lecture&nbsp;; chacun est compté une fois.

La motion de censure vise le Gouvernement, et l'alinéa&nbsp;2 ne la laisse adopter qu'à la majorité des membres composant l'Assemblée, seuls les votes favorables étant recensés. Si elle est adoptée, le texte n'est pas considéré comme adopté à cette étape, et le Gouvernement doit remettre sa démission (art.&nbsp;50).

<details class="repli"><summary>La lettre des articles&nbsp;49 et 50</summary>

Article&nbsp;49, alinéa&nbsp;3&nbsp;: «&nbsp;{{< ado-val "cit_art49a" >}}&nbsp;» Et&nbsp;: «&nbsp;{{< ado-val "cit_art49b" >}}&nbsp;» Alinéa&nbsp;2&nbsp;: «&nbsp;{{< ado-val "cit_art49c" >}}&nbsp;»

Article&nbsp;50&nbsp;: «&nbsp;{{< ado-val "cit_art50" >}}&nbsp;»

</details>

{{< figure-svg fichier="adopter-493" alt="Barres horizontales par législature : engagements de responsabilité sur un projet de loi de finances ou de financement de la sécurité sociale, et sur un autre projet ou une proposition, avec sous chaque barre le nombre de textes distincts et les motions de censure adoptées. Ceux de la XIVe et de la XVe portent sur d'autres projets ; ceux de la XVIe portent en majorité, et ceux de la XVIIe en cours en totalité, sur des projets de loi de finances ou de financement de la sécurité sociale. Les valeurs sont dans le tableau sous la figure." >}}Engagements de responsabilité du Gouvernement sur un texte, chacun compté une fois, selon les catégories de l'article&nbsp;49, alinéa&nbsp;3&nbsp;: la loi de programmation des finances publiques y relève d'«&nbsp;un autre projet&nbsp;». Ce relevé porte sur tous les textes, lois de finances comprises.{{< /figure-svg >}}

{{< fig-actions id="493" >}}

{{< ado-tableau "engagements" "Les valeurs de la figure en tableau" >}}

Sous la XIVe législature, la responsabilité du Gouvernement a été engagée {{< ado-val "E14" >}} fois, sur {{< ado-val "Etextes14" >}} projets de loi qui n'étaient ni des projets de loi de finances ni de financement de la sécurité sociale&nbsp;; sous la XVe, {{< ado-val "Efois15" >}}&nbsp;; sous la XVIe, {{< ado-val "E16" >}} fois sur {{< ado-val "Etextes16" >}} textes, dont {{< ado-val "Efin16" >}} engagements sur des projets de loi de finances ou de financement de la sécurité sociale et {{< ado-val "Eautre16" >}} sur la loi de programmation des finances publiques&nbsp;; sous la XVIIe, en cours, {{< ado-val "E17" >}} fois sur {{< ado-val "Etextes17" >}} textes, tous financiers. La fiche de l'Assemblée nationale consacrée à cette procédure donne les mêmes totaux jusqu'à la XVIe&nbsp;: «&nbsp;{{< ado-val "cit_fiche64" >}}&nbsp;»

Compter en lois plutôt qu'en engagements change l'image. Sous la XVIe législature, {{< ado-val "Lfineng16" >}} des {{< ado-val "Lfin16" >}} lois de finances ou de financement de la sécurité sociale promulguées ont fait l'objet d'au moins un engagement, à une étape au moins de leur examen&nbsp;; les autres n'en ont eu aucun. Sous la XVIIe, en cours, c'est {{< ado-val "Lfineng17" >}} sur {{< ado-val "Lfin17" >}}. Ces nombres décrivent la procédure suivie, non le contenu des textes ni ce qu'un vote aurait donné, et ils n'expliquent pas pourquoi l'usage diffère d'une législature à l'autre.

Aucune motion de censure n'a été adoptée sur ces engagements, de la XIVe à la XVIe législature. Le {{< ado-val "censure_date" >}}, la responsabilité du Gouvernement a été engagée sur le {{< ado-val "censure_etape" >}} du {{< ado-val "censure_texte" >}}&nbsp;; selon la même fiche, «&nbsp;{{< ado-val "cit_censure" >}}&nbsp;». Le texte n'a pas été considéré comme adopté à cette étape, et le Gouvernement a dû remettre sa démission.

**Les deux autres situations.** Si le Parlement ne s'est pas prononcé dans le délai que fixe la Constitution, les dispositions du projet de budget de l'État (art.&nbsp;47) ou de celui de la sécurité sociale (art.&nbsp;47-1) peuvent être mises en vigueur par ordonnance. Ces ordonnances ne font pas une loi votée&nbsp;: elles mettent en vigueur les dispositions d'un projet. Le référendum, lui, adopte une loi sans vote du Parlement sur son texte&nbsp;: si le résultat est favorable au texte, le Président de la République promulgue la loi (art.&nbsp;11). Quand il est organisé sur proposition du Gouvernement, le Parlement débat sans voter&nbsp;: le Gouvernement fait devant chaque assemblée une déclaration suivie d'un débat. La page [Un président peut-il recourir au référendum&nbsp;?](/un-president-peut-il-recourir-au-referendum/) en fait le compte.

<details class="repli"><summary>La lettre des articles&nbsp;47, 47-1 et 11</summary>

Article&nbsp;47&nbsp;: «&nbsp;{{< ado-val "cit_art47c" >}}&nbsp;» Article&nbsp;47-1&nbsp;: «&nbsp;{{< ado-val "cit_art471c" >}}&nbsp;»

Article&nbsp;11&nbsp;: «&nbsp;{{< ado-val "cit_art11a" >}}&nbsp;» Et&nbsp;: «&nbsp;{{< ado-val "cit_art11b" >}}&nbsp;»

</details>

<details class="repli"><summary>Ce qui a été vérifié, et comment</summary>

Les engagements sont lus dans les dossiers législatifs de l'Assemblée nationale, et comptés deux fois par deux voies différentes du même producteur, avec les mêmes dates. Ils sont comparés, session par session, aux bulletins statistiques de l'Assemblée&nbsp;: mêmes nombres d'engagements et de motions. Une seule date diffère, d'un jour, pour un engagement de novembre 2022&nbsp;; le compte rendu officiel de la séance confirme la date des données. Pour quelques motions, les données ne contiennent pas l'acte de vote&nbsp;; les bulletins donnent leurs scrutins, tous sous la majorité requise. Les lois financières concernées sont retrouvées par l'identifiant de dossier de l'Assemblée, commun aux deux fichiers&nbsp;; le script vérifie que chaque engagement classé sur un projet de loi de finances ou de financement de la sécurité sociale porte sur une loi de cette nature, et aucun autre.

</details>

## Comment juger une promesse qui demande une loi&nbsp;? {#trois-questions}

Trois questions suffisent à situer une promesse de loi, sans rien supposer de son contenu.

1. **Qui déposera le texte&nbsp;?** Le Gouvernement ou un parlementaire. Une proposition ou un amendement de parlementaire ne peut créer ou aggraver une charge publique, et une perte de recettes doit y être compensée par une autre recette (art.&nbsp;40, tel que l'Assemblée nationale l'applique)&nbsp;; cette règle ne vise pas les textes du Gouvernement.
2. **Qui l'inscrira à l'ordre du jour&nbsp;?** Le Gouvernement sur ses semaines prioritaires, une assemblée sur les siennes, un groupe d'opposition ou minoritaire sur son jour mensuel (art.&nbsp;48).
3. **Qui aura le dernier mot&nbsp;?** L'accord des deux assemblées&nbsp;; à défaut, l'Assemblée nationale, si le Gouvernement le lui demande (art.&nbsp;45)&nbsp;; ou un engagement de responsabilité, au risque d'une censure (art.&nbsp;49 et 50).

Une loi adoptée n'est pas encore une loi appliquée&nbsp;: la page [Une loi votée s'applique-t-elle tout de suite&nbsp;?](/une-loi-votee-s-applique-t-elle-tout-de-suite/) prend le relais. Et la page [Que peut décider le président seul&nbsp;?](/pouvoirs-du-president-de-la-republique/) traite de ce qu'il décide sans passer par la loi.

## Ce que cette page ne dit pas {#limites}

Elle ne mesure pas l'influence du Gouvernement sur les propositions de loi, ni celle du Parlement sur les projets&nbsp;: l'origine d'une loi n'est pas son contenu, et les amendements ne sont pas comptés. Elle ne relie pas le nombre d'engagements de responsabilité à la composition de l'Assemblée&nbsp;: une coïncidence de dates n'établit pas un lien. Elle ne dit pas ce que deviennent les propositions sans examen en séance, ni pourquoi elles n'y sont pas venues. Les décomptes de dépôts ne concordent pas texte par texte avec les bulletins de l'Assemblée&nbsp;: la phrase sur les propositions ne s'appuie que sur la borne du pire cas. Elle ne compte ni les ordonnances budgétaires ni les lois référendaires.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Ce qu'il faut faire voter" avis="non" >}}
Cette page dit qui dépose les lois, qui les fait venir en séance, qui a le dernier mot et ce que permet l'article 49.3. Le livre suit neuf promesses écrites, datées et signées, le long de la chaîne qui va de la décision à son résultat&nbsp;: ce qu'un président décide dans sa propre chaîne de pouvoir, ce qu'il doit faire voter, ce qu'il doit négocier, et ce qui ne dépendra jamais de lui. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Assemblée nationale**, données ouvertes des dossiers législatifs des XIVe à XVIIe législatures (version du {{< ado-val "releve" >}})&nbsp;; bulletins statistiques annuels&nbsp;; fiches de synthèse n°&nbsp;64 sur l'engagement de la responsabilité du Gouvernement et n°&nbsp;52 sur la recevabilité financière des initiatives parlementaires.

**Sénat**, base Dosleg (version du {{< ado-val "releve" >}})&nbsp;; rapport d'information n°&nbsp;802 (2025-2026) sur l'application des lois, p.&nbsp;44.

**Journal officiel**, données de la DILA&nbsp;; **Constitution**, art.&nbsp;11, 24, 39, 40, 44, 45, 46, 47, 47-1, 48, 49 et 50, lus sur Légifrance (API).

Les chiffres, les citations, les contrôles et les figures sont produits par un script unique. Il lit l'origine des lois, les propositions et les engagements dans les données de l'Assemblée nationale, du Sénat et du Journal officiel, et retrouve chaque citation mot pour mot dans son document archivé. Les dépôts comptés par les bulletins statistiques de l'Assemblée, publiés en image, sont transcrits à la main et ne servent qu'au calcul du pire cas&nbsp;; les engagements des bulletins, lus dans leur texte, servent de témoin. Le script s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_adopter.csv), en format long&nbsp;; [JSON](/promesses_adopter.json), avec les définitions et le compte rendu des contrôles. Ce jeu est aussi archivé sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent à citer&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664)&nbsp;; la version archivée ne contient pas encore les séries ajoutées le 12/10/2026 (toutes natures, lois entre deux législatures, lois financières concernées par un engagement).

{{< reutiliser figures="figures_adopter" jeu="promesses_adopter" sources="Assemblée nationale, Sénat (Dosleg), Journal officiel, Légifrance" donnees="L'origine des lois promulguées par législature, par nature et par session, les propositions de loi déposées à l'Assemblée et restées sans examen en séance, et les engagements de responsabilité de l'article 49, alinéa 3 ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Dans le champ étudié ({{< ado-val "champ" >}}), la part des lois promulguées issues d'une proposition de parlementaire est de {{< ado-val "Ppct14" >}}&nbsp;% sous la XIVe législature, {{< ado-val "Ppct15" >}}&nbsp;% sous la XVe (au moins {{< ado-val "Pminpct15" >}}&nbsp;%), {{< ado-val "Ppct16" >}}&nbsp;% sous la XVIe et {{< ado-val "Ppct17" >}}&nbsp;% sous la XVIIe en cours&nbsp;; toutes natures hors traités, la XVe passe sous la moitié ({{< ado-val "Ptotpct15" >}}&nbsp;%). Environ {{< ado-val "Zdix" >}} propositions de loi ordinaires sur dix déposées à l'Assemblée n'ont pas été examinées en séance avant la fin de leur législature, de la XIVe à la XVIe, pire cas compris. La responsabilité du Gouvernement a été engagée sur un texte {{< ado-val "E16" >}} fois sous la XVIe législature, dont {{< ado-val "Efin16" >}} sur des projets de loi de finances ou de financement de la sécurité sociale.
{{< /reutiliser >}}
