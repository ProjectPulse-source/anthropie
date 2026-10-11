---
title: "Que peut décider le président de la République seul ?"
description: "Ce que la Constitution permet au président de faire sans contreseing, à quelles conditions, et qui d'autre intervient : les {pv.n_renvois} dispositions de l'article 19 lues acte par acte, chaque élément appuyé sur une citation exacte. Données ouvertes."
chapo: "Le président nomme le Premier ministre. Peut-il le révoquer ? Non : la Constitution prévoit que ses fonctions prennent fin sur présentation de la démission du Gouvernement. En règle générale, un acte du président porte aussi la signature d'un ministre : c'est le contreseing. L'article 19 en dispense les actes de {pv.n_renvois} dispositions ; même là, le texte fait le plus souvent intervenir quelqu'un d'autre, avant ou après le président. Ses pouvoirs les plus visibles (armées, grâce, traités, nominations) ne sont pas dans cette liste : ils sont contresignés."
date: 2026-09-30
lastmod: 2026-10-11
donnees: [pouvoirs_president_donnees]
og_title: "Que peut décider le président de la République seul ? — le texte, citation par citation — S. Lalut"
og_image: "images/og-pouvoirs-president.jpg"
og_image_alt: "Carte de partage : « Décider seul : ce que dit le texte » — une matrice de douze lignes, une par acte que contiennent les huit dispositions dispensées de contreseing par l'article 19 de la Constitution, et quatre colonnes : exigé avant l'acte, autre acteur pour la suite, pouvoir partagé, autre cadre écrit ; case pleine quand l'article contient une citation exacte de l'élément."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "pouvoirs_president_donnees"
  nom: "Les actes du président de la République dispensés de contreseing : inventaire de l'article 19, acte par acte, en citations"
  description: "Pour chacun des actes que contiennent les huit dispositions que l'article 19 de la Constitution dispense de contreseing (art. 8 al. 1, 11, 12, 16, 18, 54, 56, 61) : l'acte, ce que le texte exige avant lui (proposition, consultation ou acte d'un autre acteur), l'autre acteur appelé à intervenir pour la suite, les autres autorités disposant d'un pouvoir de même nature et l'autre encadrement écrit, chacun appuyé sur une citation exacte de l'article, vérifiée contre le texte en vigueur lu sur Légifrance, avec sa temporalité, son caractère facultatif et la justification de son classement ; et les articles qui attribuent la loi et le règlement (art. 13, 19, 21, 34, 37, 38, 47, 49)."
  couverture_temporelle: "2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Attribut de l'acte (acte, condition, autre acteur, partage, limite)", unite: "présent ou absent dans le texte de l'article"}
    - {nom: "Citation exacte de l'article", unite: "texte"}
    - {nom: "Temporalité, caractère facultatif et justification du classement", unite: "texte"}
  sources:
    - "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/"
  mots: ["président de la République", "contreseing", "article 19", "Constitution de 1958", "pouvoirs du président", "domaine de la loi"]
  fichiers: ["pouvoirs_president_donnees.csv", "pouvoirs_president_donnees.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Que peut décider le président de la République seul ?"
    answer: "La Constitution ne parle pas de décider seul. L'article 19 dispense du contreseing du Premier ministre les actes de {pv.n_renvois} dispositions : nommer le Premier ministre et mettre fin à ses fonctions, soumettre un texte au référendum, dissoudre l'Assemblée nationale, exercer les pouvoirs exceptionnels, s'adresser au Parlement, saisir le Conseil constitutionnel d'un traité ou d'une loi, nommer au Conseil constitutionnel. Sur les {pv.n_actes} actes qu'elles contiennent, {pv.n_encadres_acte} font intervenir, dans leur propre article, un autre acteur avant ou après le président : une proposition pour le référendum, une consultation puis des élections pour la dissolution. Ses autres actes sont contresignés."
  - question: "Le président peut-il renvoyer le Premier ministre ?"
    answer: "Non. L'article 8 décrit une seule voie : le président met fin aux fonctions du Premier ministre « sur la présentation par celui-ci de la démission du Gouvernement ». L'article 50 décrit le cas où cette démission devient obligatoire : lorsque l'Assemblée nationale adopte une motion de censure ou désapprouve le programme ou une déclaration de politique générale du Gouvernement. Cette obligation naît d'un vote de l'Assemblée ; le texte ne la confie pas au président."
  - question: "Qui fixe les impôts : le président, le Gouvernement ou le Parlement ?"
    answer: "L'article 34 réserve à la loi « l'assiette, le taux et les modalités de recouvrement des impositions de toutes natures ». Une promesse fiscale passe donc par le Parlement, mais pas toujours par un vote sur le texte : sur un projet de loi de finances, le Premier ministre peut, après délibération du Conseil des ministres, engager la responsabilité du Gouvernement, et le projet est considéré comme adopté si aucune motion de censure n'est votée (article 49, alinéa 3) ; si le Parlement ne s'est pas prononcé dans le délai que fixe l'article 47, les dispositions du projet peuvent être mises en vigueur par ordonnance. Dans aucun de ces cas la signature du président ne suffit."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"
  bloc: "promesses"
  rang: 10
  nature: "Le texte de la Constitution, citation par citation ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Que peut décider le président seul ?"
  court: "Décider"
  role: "signatures et conditions"
---

{{< reutiliser-ancre >}}

«&nbsp;{{< pv-val "cit8a" >}} {{< pv-val "cit8b" >}}&nbsp;» (article&nbsp;8). La nomination tient à sa seule signature&nbsp;; la fin des fonctions suppose un acte du Premier ministre, la démission qu'il présente.

Pour mesurer l'écart entre l'image d'un président qui décide seul et ce que dit le texte, la page part de la seule liste que la Constitution établit&nbsp;: les actes que le président signe **sans contreseing**, c'est-à-dire sans la signature d'un ministre à côté de la sienne. Elle les lit un par un, et ne note un élément que s'il est écrit, mot pour mot, dans l'article.

*Statut&nbsp;: lecture documentaire de la Constitution, sans certification juridique. Chaque citation est vérifiée mot pour mot&nbsp;; son classement est une lecture, justifiée case par case [plus bas](#methode).*

{{< figure-svg fichier="pouvoirs-article19" alt="Matrice de douze lignes, une par acte que contiennent les huit dispositions dispensées de contreseing par l'article 19, regroupées par article, et quatre colonnes : exigé avant l'acte (proposition, consultation ou acte d'un autre acteur), autre acteur pour la suite, pouvoir partagé avec d'autres autorités, autre cadre écrit. Les cases pleines sont énumérées, citation par citation, dans la section sur la méthode." >}}Le tableau&nbsp;: une ligne par acte, regroupées par disposition de l'article&nbsp;19&nbsp;; une colonne par élément. Case pleine&nbsp;: l'article lui-même contient une citation exacte de l'élément&nbsp;; case vide&nbsp;: cet article ne le contient pas, ce qui ne dit rien des autres articles ni de la pratique. Autre acteur pour la suite&nbsp;: institution, autorité ou corps électoral auquel l'article attribue une intervention distincte, postérieure à l'acte présidentiel, y compris facultative&nbsp;; les simples modalités matérielles d'exécution de l'acte ne sont pas comptées.{{< /figure-svg >}}

{{< fig-actions id="article19" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Sur les {{< pv-val "n_actes" >}} actes que l'article&nbsp;19 dispense de contreseing, {{< pv-val "n_encadres_acte" >}} font intervenir quelqu'un d'autre, avant ou après le président, dans le texte même de leur article.

**Ce compte lit le texte de chaque article, pas la pratique ni le reste de la Constitution.**

Intervenir ne veut pas toujours dire empêcher&nbsp;: avant de dissoudre, le président doit consulter le Premier ministre, pas obtenir son accord. Restent {{< pv-val "n_seuls_acte" >}} actes&nbsp;: {{< pv-val "seuls_acte_liste" >}}. Pour eux, l'article ne prévoit ni proposition, consultation ou acte d'un autre acteur avant, ni intervention d'un autre acteur ensuite.

</div>

## Que signifie «&nbsp;décider seul&nbsp;» pour un président&nbsp;? {#decider-seul}

L'article&nbsp;19 pose la règle&nbsp;: «&nbsp;{{< pv-val "cit19" >}}&nbsp;» Les exceptions sont donc les actes qu'aucun ministre n'a à signer. C'est, dans le texte, ce qui se rapproche le plus de «&nbsp;décider seul&nbsp;», sans se confondre avec lui.

**Sans contreseing ne veut pas dire sans condition.** Le texte peut exiger, avant l'acte, une proposition (pour le référendum), une consultation (pour la dissolution) ou l'acte d'un autre acteur (la démission que présente le Premier ministre). Il peut faire intervenir ensuite les électeurs, le Parlement ou le Conseil constitutionnel, parfois de façon seulement possible&nbsp;: une déclaration devant le Congrès peut être suivie d'un débat, sans vote. D'autres autorités peuvent détenir un pouvoir de même nature. Le texte peut enfin limiter l'acte dans le temps, dans son objet ou dans son effet. Ce sont les quatre colonnes du tableau ci-dessus&nbsp;; un même acte peut en remplir plusieurs.

**Trois niveaux de lecture.** Le tableau et les comptes ne lisent que le texte de l'article visé par l'article&nbsp;19. Les fiches ci-dessous ajoutent ce que disent d'autres articles, des lois organiques et deux décisions de justice. La section sur la politique de la Nation traite enfin de la pratique. Ces deux derniers niveaux changent la portée d'un acte, jamais le contenu d'une case.

Un exemple. Pour nommer le Premier ministre, l'article&nbsp;8 ne fait intervenir personne d'autre. Mais le Gouvernement nommé relève de l'article&nbsp;20&nbsp;: «&nbsp;{{< pv-val "cit20b" >}}&nbsp;». Si l'Assemblée nationale le censure, il doit remettre sa démission (article&nbsp;50).

## Quels actes le président signe-t-il sans contreseing&nbsp;? {#sans-contreseing}

Une fiche par disposition, soit {{< pv-val "n_renvois" >}}&nbsp;: la réponse courte d'abord, puis, en dépliant, le détail citation par citation (ce que le texte exige avant l'acte, qui intervient ensuite, ce que l'acte produit, ce que d'autres textes ajoutent). Elles se lisent avec la fonction que l'article&nbsp;5 assigne au président&nbsp;: veiller au respect de la Constitution et assurer, «&nbsp;{{< pv-val "cit5" >}}&nbsp;».

{{< pouvoirs-president vue="sans_contreseing" >}}

## Quels pouvoirs lui prête-t-on en propre alors qu'ils sont contresignés&nbsp;? {#pouvoirs-contresignes}

Chef des armées, droit de grâce, traités, décrets, nominations&nbsp;: ce sont les attributions les plus visibles de la fonction, et aucune ne figure dans la liste de l'article&nbsp;19. Lorsqu'elles donnent lieu à un acte du président, cet acte est soumis au contreseing que prévoit cet article. Certaines font en outre intervenir le Parlement ou une autre institution&nbsp;: une partie des traités ne peut être ratifiée qu'en vertu d'une loi, et certaines nominations passent par un avis des commissions parlementaires ou par le Conseil supérieur de la magistrature.

{{< pouvoirs-president vue="contresigne" >}}

## Qui fixe les règles que le citoyen ressent&nbsp;? {#qui-fixe-les-regles}

**Signer ne suffit pas à gouverner.** Une baisse d'impôt, une réforme, une règle nouvelle&nbsp;: par quelles autres signatures que la sienne une promesse du président doit-elle passer&nbsp;? Le texte range les règles en deux catégories. **La loi**, qui passe par le Parlement, couvre les matières de l'article&nbsp;34, dont l'impôt. **Le règlement** couvre le reste&nbsp;: «&nbsp;{{< pv-val "cit37" >}}&nbsp;» (article&nbsp;37). Le Premier ministre exerce le pouvoir réglementaire (article&nbsp;21). Exception&nbsp;: les décrets délibérés en Conseil des ministres, que le président signe (article&nbsp;13) et qui sont contresignés (article&nbsp;19). Enfin, avec l'autorisation du Parlement, le Gouvernement peut prendre par ordonnances des mesures qui relèvent de la loi (article&nbsp;38).

{{< pouvoirs-president vue="regles" >}}

Une promesse qui porte sur un impôt passe donc par le Parlement, mais pas toujours par un vote sur le texte. Sur un projet de loi de finances, le Premier ministre peut, après délibération du Conseil des ministres, que le président préside (article&nbsp;9), engager la responsabilité du Gouvernement&nbsp;: «&nbsp;{{< pv-val "cit49" >}}&nbsp;», sauf si une motion de censure est votée (article&nbsp;49, alinéa&nbsp;3). Et si le Parlement ne s'est pas prononcé dans le délai que fixe l'article&nbsp;47, les dispositions du projet peuvent être mises en vigueur par ordonnance. Ces procédures sont détaillées dans la page «&nbsp;[Qui peut faire adopter une loi&nbsp;?](/qui-peut-faire-adopter-une-loi/)&nbsp;». Une promesse qui passe par un décret fait, elle aussi, intervenir d'autres signatures que celle du président&nbsp;: celle du Premier ministre, ou le contreseing si le décret est délibéré en Conseil des ministres.

## Qui détermine la politique de la Nation&nbsp;? {#politique-de-la-nation}

**Pourquoi, alors, l'Élysée semble-t-il tout décider&nbsp;?** La réponse n'est pas dans la liste de l'article&nbsp;19, mais dans l'article&nbsp;20&nbsp;: «&nbsp;{{< pv-val "cit20" >}}&nbsp;» Il dispose de l'administration et de la force armée, et il répond devant le Parlement.

**Le Gouvernement répond devant l'Assemblée.** Une motion de censure ne peut être adoptée qu'à la majorité des membres de l'Assemblée nationale (article&nbsp;49)&nbsp;; si elle l'est, «&nbsp;{{< pv-val "cit50" >}}&nbsp;» (article&nbsp;50). Le Gouvernement ne peut donc se maintenir ni contre une majorité absolue de députés qui vote sa censure, ni lorsque l'Assemblée désapprouve son programme ou une déclaration de politique générale (article&nbsp;50). Le Premier ministre peut aussi présenter sa démission sans avoir été censuré (article&nbsp;8).

**Quand la majorité de l'Assemblée soutient le président**, le Gouvernement qu'il a nommé conduit la politique sur laquelle le président a été élu&nbsp;: c'est de là que vient l'image d'un président qui décide de tout. Ce lien relève de l'exercice politique, que le texte ne décrit pas. Lorsqu'un Premier ministre quitte ses fonctions à la demande du président, ce qui relève de la même pratique, la fin des fonctions passe encore, en droit, par la démission qu'il présente (article&nbsp;8). Le texte ne rend cette démission obligatoire qu'après un vote de l'Assemblée (article&nbsp;50).

**Quand cette majorité lui est opposée**, c'est-à-dire en cohabitation, le même texte donne une autre présidence&nbsp;: le Gouvernement, responsable devant cette majorité, détermine et conduit la politique de la Nation, et le président garde les actes dispensés de contreseing, avec leurs conditions. La dissolution lui permet de redemander une majorité aux électeurs&nbsp;; ce sont eux qui la donnent. Le droit répartit les pouvoirs&nbsp;; la majorité conditionne leur exercice politique.

{{< pouvoirs-president vue="gouvernement" >}}

## Avant d'évaluer une promesse présidentielle, que faut-il vérifier&nbsp;? {#avant-d-evaluer}

Une promesse de campagne ne se juge pas à sa formule, mais au chemin qu'elle devra suivre. Cinq vérifications, chacune appuyée sur une page de ce dossier, s'appliquent à toute promesse, quel que soit le candidat qui la porte&nbsp;:

1. **Qui signe&nbsp;?** L'acte relève-t-il du président sans contreseing, et que son article exige-t-il alors avant et après lui&nbsp;? Ou d'autres signatures sont-elles nécessaires&nbsp;? Voir [les actes sans contreseing](#sans-contreseing), et [qui fixe les règles](#qui-fixe-les-regles).
2. **Faut-il une loi, et qui peut la faire voter&nbsp;?** Voir [qui peut faire adopter une loi](/qui-peut-faire-adopter-une-loi/), et, pour une réforme soumise aux électeurs, [le référendum](/un-president-peut-il-recourir-au-referendum/).
3. **La décision se prend-elle à Paris&nbsp;?** Dans certaines matières, elle se prend dans l'Union européenne, avec d'autres États&nbsp;: voir [ce que la France peut décider dans l'Union européenne](/ce-que-la-france-peut-decider-dans-l-union-europeenne/).
4. **Une fois votée, la mesure s'applique-t-elle, et en combien de temps produit-elle ses effets&nbsp;?** Voir [l'application des lois](/une-loi-votee-s-applique-t-elle-tout-de-suite/) et [le temps d'une formation](/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/).
5. **Selon quel critère observable dira-t-on qu'elle est tenue&nbsp;?** Un indicateur, un acte, un seuil ou une échéance, fixés d'avance. Voir [comment savoir si une promesse est tenue](/comment-savoir-si-une-promesse-est-tenue/).

Ces questions ne disent pas si une promesse est bonne ou mauvaise&nbsp;: elles disent ce dont sa réalisation dépend. Qu'un autre acteur intervienne ne veut pas dire qu'il empêche&nbsp;: cela dit seulement que le résultat ne tient pas à une seule signature. Et elles portent sur les autorisations et les procédures, non sur les moyens&nbsp;: crédits votés en loi de finances, agents et services pour exécuter, collectivités et opérateurs qui appliquent, juge qui peut être saisi. Une promesse peut franchir toutes les étapes de ce dossier et manquer de ces moyens.

## Comment le tableau est-il établi&nbsp;? {#methode}

**Lecture documentaire de la Constitution, sans certification juridique.** Deux choses sont à distinguer. Que chaque citation figure mot pour mot dans le texte en vigueur&nbsp;: un script le vérifie à chaque génération des données, sur la réponse de Légifrance archivée pour chaque texte, et refuse d'écrire sinon. Que chaque citation soit rangée dans la bonne colonne&nbsp;: c'est une lecture, faite case par case par l'équipe de rédaction et soumise à une contre-expertise externe&nbsp;; aucun juriste ne l'a relue à ce jour. Chaque classement porte sa justification, chaque case vide décisive aussi&nbsp;: elles sont dans le repli ci-dessous et dans les données.

**Le critère.** Un acte est retenu quand le texte de son article n'exige avant lui ni proposition, ni consultation, ni acte d'un autre acteur, et ne fait intervenir aucun autre acteur pour la suite, même de façon facultative. Les pouvoirs partagés et les autres encadrements écrits n'entrent pas dans le critère. Compté acte par acte, il retient {{< pv-val "n_seuls_acte" >}} actes sur {{< pv-val "n_actes" >}}.

**Autre acteur pour la suite**&nbsp;: institution, autorité ou corps électoral auquel l'article attribue une intervention distincte, postérieure à l'acte présidentiel, y compris facultative. Les simples modalités matérielles d'exécution de l'acte ne sont pas comptées. Le Conseil constitutionnel saisi d'un traité ou d'une loi statue&nbsp;: c'est une intervention distincte. La lecture du message que le président adresse aux assemblées n'est pas comptée&nbsp;: c'est la manière dont le message leur parvient, non une intervention distincte. Un acte retenu n'est donc pas un acte accompli sans personne&nbsp;; de même, la nomination du Premier ministre produit un Gouvernement responsable devant le Parlement.

<details class="repli"><summary>Compté par disposition&nbsp;: pourquoi une version antérieure trouvait un autre nombre</summary>

Une version antérieure de ces données, publiée le 6&nbsp;octobre 2026, comptait par disposition&nbsp;: chacune y était représentée par le premier acte que son article attribue au président. Le même critère y retient {{< pv-val "n_seuls_renvoi" >}} dispositions sur {{< pv-val "n_renvois" >}}&nbsp;; compté acte par acte, il retient {{< pv-val "n_seuls_acte" >}} actes sur {{< pv-val "n_actes" >}}.

L'acte qui échappait au premier compte est la désignation du président du Conseil constitutionnel, que l'article&nbsp;56 prévoit après la nomination de trois membres. Ces nominations passent par un avis des commissions parlementaires&nbsp;; la désignation du président n'en demande aucun.

</details>

<details class="repli"><summary>Les citations qui remplissent le tableau, acte par acte, et la raison de chaque classement</summary>

{{< pouvoirs-president vue="citations" >}}

</details>

## Ce que cette page ne dit pas {#limites}

Elle s'en tient aux textes en vigueur, relus sur Légifrance, et à deux décisions du Conseil d'État lues dans leur texte intégral. Elle ne décrit pas la pratique des institutions au-delà de ce que la section sur la politique de la Nation en dit, et elle n'est pas un avis juridique. Là où le texte se tait, par exemple sur la possibilité, pour le président, de refuser de signer une ordonnance, la page le dit sans trancher. Les comptes ne mesurent ni l'autonomie du président ni le nombre de ses pouvoirs propres.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Suivre une promesse au-delà de la signature" avis="non" >}}
Cette page dit qui signe. Le livre pose la question suivante&nbsp;: une promesse de campagne, une fois l'élu en place, passe par quelle chaîne&nbsp;? Il propose une grille en quatre zones — ce qu'un président décide dans sa propre chaîne de pouvoir, ce qu'il doit faire voter, ce qu'il doit négocier avec ceux dont la signature manque, et ce qui ne dépendra jamais de lui — et l'éprouve sur neuf promesses écrites, datées et signées. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

Tous les textes cités ici ont été lus dans leur version en vigueur, sur Légifrance, à la date indiquée&nbsp;; l'article&nbsp;17 l'est aussi dans sa version de 1958, pour la comparaison qu'en fait la fiche du droit de grâce. Chaque fiche renvoie aux textes sur lesquels elle repose.

{{< pouvoirs-president vue="sources" >}}

**Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/pouvoirs_president_donnees.csv), en format long, une ligne par citation ou par case vide, avec sa temporalité, son caractère facultatif et la justification de son classement&nbsp;; [JSON](/pouvoirs_president_donnees.json), avec les définitions, les critères de compte et le compte rendu des contrôles. Une version antérieure de ce jeu, une ligne par disposition, est archivée sur Zenodo avec les six autres de la même série et leur note de méthode&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664)&nbsp;; le jeu téléchargeable ici, acte par acte, la remplace.

{{< reutiliser figures="figures_pouvoirs" jeu="pouvoirs_president_donnees" sources="Légifrance (Constitution du 4 octobre 1958)" donnees="L'inventaire des huit dispositions de l'article 19, acte par acte : chaque élément avec sa citation exacte, son article, sa date de lecture, sa temporalité et la justification de son classement, et les articles qui attribuent la loi et le règlement ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Cette page lit dans le texte de la Constitution les {{< pv-val "n_renvois" >}} dispositions que l'article&nbsp;19 dispense de contreseing. Lues acte par acte, elles en contiennent {{< pv-val "n_actes" >}}&nbsp;; {{< pv-val "n_seuls_acte" >}} seulement, {{< pv-val "seuls_acte_liste" >}}, ne prévoient dans leur article ni proposition, consultation ou acte d'un autre acteur avant, ni intervention d'un autre acteur pour la suite. Ce compte décrit le texte de chaque article, non la pratique. La loi, qui passe par le Parlement mais pas toujours par un vote sur le texte (art.&nbsp;47 et 49, al.&nbsp;3), fixe notamment l'impôt (art.&nbsp;34)&nbsp;; le Premier ministre exerce le pouvoir réglementaire (art.&nbsp;21), hors les décrets délibérés en Conseil des ministres, que le président signe et qui sont contresignés.
{{< /reutiliser >}}
