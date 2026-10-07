---
title: "Que peut décider le président de la République seul ?"
description: "Ce que la Constitution permet au président de faire sans contreseing, à quelles conditions, et qui d'autre intervient : les huit dispositions de l'article 19 lues dans le texte, chaque élément appuyé sur une citation exacte. Données ouvertes."
chapo: "Sans contreseing, le président peut notamment nommer le Premier ministre et dissoudre l'Assemblée nationale, dans les conditions que fixe la Constitution. L'article 19 énumère huit dispositions dispensées de contreseing ; les autres actes du président sont, en principe, soumis au contreseing que prévoit cet article."
date: 2026-09-30
lastmod: 2026-10-05
donnees: [pouvoirs_president_donnees]
og_title: "Que peut décider le président de la République seul ? — le texte, citation par citation — S. Lalut"
og_image: "images/og-pouvoirs-president.jpg"
og_image_alt: "Carte de partage : « Décider seul : ce que dit le texte » — une matrice de huit lignes, une par acte que l'article 19 de la Constitution dispense de contreseing, et quatre colonnes : condition préalable, autre acteur, pouvoir de même nature, autre encadrement écrit ; case pleine quand l'article contient une citation exacte de l'élément."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "pouvoirs_president_donnees"
  nom: "Les actes du président de la République dispensés de contreseing : inventaire de l'article 19 en citations"
  description: "Pour chacune des huit dispositions que l'article 19 de la Constitution dispense de contreseing (art. 8 al. 1, 11, 12, 16, 18, 54, 56, 61) : l'acte, la proposition ou la consultation exigée, l'autre acteur appelé à intervenir, les autres autorités disposant d'un pouvoir de même nature et l'autre encadrement écrit, chacun appuyé sur une citation exacte de l'article, vérifiée contre le texte en vigueur lu sur Légifrance ; et les articles qui attribuent la loi et le règlement (art. 13, 19, 21, 34, 37)."
  couverture_temporelle: "2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Attribut de l'acte (acte, condition, autre autorité, partage, limite)", unite: "présent ou absent dans le texte de l'article"}
    - {nom: "Citation exacte de l'article", unite: "texte"}
  sources:
    - "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/"
  mots: ["président de la République", "contreseing", "article 19", "Constitution de 1958", "pouvoirs du président", "domaine de la loi"]
  fichiers: ["pouvoirs_president_donnees.csv", "pouvoirs_president_donnees.json"]
faq:
  - question: "Que peut décider le président de la République seul ?"
    answer: "La Constitution ne parle pas de décider seul. Elle énumère, à l'article 19, huit dispositions dont les actes échappent au contreseing du Premier ministre : nommer le Premier ministre, soumettre un projet de loi au référendum, dissoudre l'Assemblée nationale, exercer les pouvoirs exceptionnels, adresser des messages au Parlement, saisir le Conseil constitutionnel d'un traité, nommer au Conseil constitutionnel, lui déférer une loi. Plusieurs ont leurs conditions écrites : le référendum exige une proposition du Gouvernement ou des deux assemblées, la dissolution la consultation du Premier ministre et des présidents des assemblées, les pouvoirs exceptionnels une crise définie et un contrôle du Conseil constitutionnel. Ses autres actes sont soumis au contreseing prévu par l'article 19 : celui du Premier ministre et, le cas échéant, des ministres responsables."
  - question: "Le président peut-il renvoyer le Premier ministre ?"
    answer: "L'article 8 décrit une seule voie : le président met fin aux fonctions du Premier ministre « sur la présentation par celui-ci de la démission du Gouvernement ». Le texte ne prévoit pas de révocation par le président ; il prévoit la responsabilité du Gouvernement devant l'Assemblée nationale (article 20, qui renvoie aux articles 49 et 50)."
  - question: "Le président peut-il refuser de promulguer une loi ?"
    answer: "L'article 10 fixe un délai, non un veto. Le président promulgue la loi dans les quinze jours qui suivent sa transmission ; dans ce délai, il peut demander au Parlement une nouvelle délibération de la loi ou de certains de ses articles, qui ne peut être refusée, et c'est le Parlement qui vote à nouveau. Il peut aussi déférer la loi au Conseil constitutionnel avant sa promulgation (article 61), ce qui suspend le délai : il obtient alors un contrôle de constitutionnalité, pas un jugement d'opportunité."
  - question: "Qui fixe les impôts : le président, le Gouvernement ou le Parlement ?"
    answer: "L'article 34 de la Constitution réserve à la loi « l'assiette, le taux et les modalités de recouvrement des impositions de toutes natures » : la loi est votée par le Parlement. Les matières qui ne relèvent pas de la loi ont un caractère réglementaire (article 37), et le pouvoir réglementaire est exercé par le Premier ministre (article 21), sous réserve des décrets délibérés en Conseil des ministres que signe le président (article 13), soumis au contreseing (article 19). Après habilitation du Parlement, le Gouvernement peut aussi agir par ordonnances (article 38), délibérées en Conseil des ministres et signées par le président (article 13)."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 10
  nature: "Le texte de la Constitution, citation par citation ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Que peut décider le président seul ?"
  court: "Décider"
  role: "signatures et conditions"
---

{{< reutiliser-ancre >}}

**«&nbsp;Décider seul&nbsp;» n'est pas une catégorie de la Constitution.** Elle distingue les actes que le président signe **sans contreseing**, ceux des {{< pv-val "n_renvois" >}} dispositions qu'énumère l'article&nbsp;19, de tous les autres, soumis au contreseing du Premier ministre et, le cas échéant, des ministres responsables. La question est pourtant la bonne, parce que c'est celle que pose l'électeur&nbsp;: de ce qu'un président promet, qu'est-ce qui dépend de sa signature, et qui d'autre le texte fait-il intervenir&nbsp;?

**Sans contreseing ne veut pas dire sans condition, ni sans intervention d'autres acteurs.** Cette page décrit les compétences et les interventions que le texte fait apparaître&nbsp;; elle ne mesure pas l'influence politique du président dans la pratique. Pour le montrer, cette page lit les {{< pv-val "n_renvois" >}} articles visés par l'article&nbsp;19 et ne remplit une case que par une **citation exacte** de l'article, retrouvée mot pour mot dans le texte en vigueur par un script&nbsp;: aucune case n'est remplie à la main.

{{< figure-svg fichier="pouvoirs-article19" alt="Matrice de huit lignes, une par acte que l'article 19 dispense de contreseing, et quatre colonnes : condition préalable, autre acteur qui intervient pour la suite, pouvoir de même nature attribué à d'autres autorités, autre encadrement écrit. Les cases pleines sont énumérées, citation par citation, dans le tableau qui suit la figure." >}}Une ligne par disposition visée par l'article&nbsp;19, une colonne par élément. Case pleine&nbsp;: l'article lui-même contient une citation exacte de l'élément (liste complète plus bas)&nbsp;; case vide&nbsp;: cet article ne le contient pas, ce qui ne dit rien des autres articles ni de la pratique.{{< /figure-svg >}}

{{< fig-actions id="article19" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Sur les {{< pv-val "n_renvois" >}} dispositions que l'article&nbsp;19 dispense de contreseing, {{< pv-val "n_seuls" >}} seulement ne contiennent, dans leur texte, ni condition préalable, ni intervention ultérieure d'un autre acteur, ni pouvoir de même nature attribué à d'autres autorités&nbsp;: {{< pv-val "seuls_liste" >}}. Cette observation ne signifie pas que le président ne disposerait que de {{< pv-val "n_seuls" >}} pouvoirs propres.

</div>

<details class="repli"><summary>Les citations qui remplissent la matrice, case par case</summary>

{{< pouvoirs-president vue="citations" >}}

Chaque citation est contrôlée à chaque génération des données&nbsp;: le script relit la réponse de Légifrance archivée pour l'article (identifiant, version en vigueur, empreinte) et refuse d'écrire si une citation n'y figure pas mot pour mot. Il relit aussi la liste des renvois dans le texte de l'article&nbsp;19 lui-même&nbsp;: un acte oublié ou ajouté arrêterait la publication.

</details>

## Que signifie «&nbsp;décider seul&nbsp;» pour un président&nbsp;? {#decider-seul}

L'article&nbsp;19 pose la règle générale&nbsp;: «&nbsp;{{< pv-val "cit19" >}}&nbsp;» Le contreseing est la signature d'un membre du Gouvernement à côté de celle du président. La liste des exceptions est donc la liste des actes qu'aucun ministre n'a à signer.

Ce critère ne dit pas tout. Un acte dispensé de contreseing peut exiger une proposition (le référendum), une consultation (la dissolution, les pouvoirs exceptionnels), faire intervenir les électeurs ou le Conseil constitutionnel pour la suite, ou appartenir aussi à d'autres autorités&nbsp;: le Premier ministre, les présidents des assemblées et soixante députés ou sénateurs peuvent, eux aussi, saisir le Conseil constitutionnel. Les quatre colonnes de la matrice sont ces quatre éléments, et ils se cumulent.

## Quels actes le président signe-t-il sans contreseing&nbsp;? {#sans-contreseing}

Les fiches qui suivent reprennent, pour chacune des {{< pv-val "n_renvois" >}} dispositions, qui décide, la condition, le tiers qui intervient et ce que l'acte produit. Ils se lisent avec la fonction que l'article&nbsp;5 assigne au président&nbsp;: veiller au respect de la Constitution et assurer, «&nbsp;{{< pv-val "cit5" >}}&nbsp;».

{{< pouvoirs-president vue="sans_contreseing" >}}

## Qui fixe les règles que le citoyen ressent&nbsp;? {#qui-fixe-les-regles}

**Signer ne suffit pas à gouverner.** Lorsqu'un président promet une baisse d'impôt, une réforme ou une règle nouvelle, par quelles autres signatures doit-il passer&nbsp;? Les impôts, les prestations, les obligations&nbsp;: le texte les répartit entre deux instruments, la loi et le règlement. **La loi**, votée par le Parlement, fixe les règles dans les matières de l'article&nbsp;34, dont l'impôt. **Le règlement** couvre le reste&nbsp;: «&nbsp;{{< pv-val "cit37" >}}&nbsp;» (article&nbsp;37). Le pouvoir réglementaire est exercé par le Premier ministre (article&nbsp;21), sous réserve des décrets délibérés en Conseil des ministres, que le président signe (article&nbsp;13) et qui sont soumis au contreseing (article&nbsp;19). Après habilitation du Parlement, le Gouvernement peut aussi prendre par ordonnances des mesures du domaine de la loi (article&nbsp;38).

{{< pouvoirs-president vue="regles" >}}

C'est pourquoi une promesse de campagne qui porte sur un impôt passe par un vote. Lorsqu'une promesse doit être mise en œuvre au niveau national par décret, celui-ci relève du Premier ministre ou, s'il est délibéré en Conseil des ministres, est signé par le président et soumis au contreseing&nbsp;: dans les deux cas, d'autres signatures que celle du président seul interviennent.

## Quels pouvoirs lui prête-t-on en propre alors qu'ils sont contresignés&nbsp;? {#pouvoirs-contresignes}

Chef des armées, droit de grâce, traités, décrets, nominations&nbsp;: ce sont les attributions les plus visibles de la fonction, et aucune ne figure dans la liste de l'article&nbsp;19. Lorsqu'elles donnent lieu à un acte du président ne relevant pas des exceptions de l'article&nbsp;19, ces attributions sont soumises au contreseing que prévoit cet article.

{{< pouvoirs-president vue="contresigne" >}}

## Qui détermine la politique de la Nation&nbsp;? {#politique-de-la-nation}

L'article&nbsp;20 répond sans détour&nbsp;: «&nbsp;{{< pv-val "cit20" >}}&nbsp;» Il dispose de l'administration et de la force armée, et il est responsable devant le Parlement. C'est la phrase qui sépare le mieux ce qu'un président promet de ce qu'il signe.

{{< pouvoirs-president vue="gouvernement" >}}

## Avant d'évaluer une promesse présidentielle, que faut-il vérifier&nbsp;? {#avant-d-evaluer}

Une promesse de campagne ne se juge pas à sa formule, mais au chemin qu'elle devra suivre. Cinq vérifications, chacune
appuyée sur une page de ce dossier, s'appliquent à toute promesse, quel que soit le candidat qui la porte&nbsp;:

1. **Qui signe&nbsp;?** L'acte relève-t-il du président seul, ou d'autres signatures sont-elles nécessaires&nbsp;? Voir ci-dessus, et [qui fixe les règles](#qui-fixe-les-regles).
2. **Faut-il une loi, et qui peut la faire voter&nbsp;?** Voir [qui peut faire adopter une loi](/qui-peut-faire-adopter-une-loi/), et, pour une réforme soumise aux électeurs, [le référendum](/un-president-peut-il-recourir-au-referendum/).
3. **La décision se prend-elle à Paris&nbsp;?** Dans certaines matières, elle se prend dans l'Union européenne, avec d'autres États&nbsp;: voir [ce que la France peut décider dans l'Union européenne](/ce-que-la-france-peut-decider-dans-l-union-europeenne/).
4. **Une fois votée, la mesure s'applique-t-elle, et en combien de temps produit-elle ses effets&nbsp;?** Voir [l'application des lois](/une-loi-votee-s-applique-t-elle-tout-de-suite/) et [le temps d'une formation](/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/).
5. **Avec quel indicateur dira-t-on qu'elle est tenue&nbsp;?** Voir [comment savoir si une promesse est tenue](/comment-savoir-si-une-promesse-est-tenue/).

Ces questions ne disent pas si une promesse est bonne ou mauvaise&nbsp;: elles disent ce dont sa réalisation dépend.

## Ce que cette page ne dit pas {#limites}

Elle s'en tient au texte en vigueur, relu sur Légifrance. Elle ne décrit ni la pratique des institutions ni la jurisprudence, et elle n'est pas un avis juridique&nbsp;: une case vide de la matrice signifie que l'article concerné ne contient pas l'élément, pas qu'aucun autre article ni aucune pratique ne le contient. Là où le texte se tait, par exemple sur la possibilité, pour le président, de refuser de signer une ordonnance, la page le dit sans trancher.

Le texte fixe les signatures&nbsp;; il ne dit pas qui inspire les décisions. Le poids réel d'un président dépend aussi de la majorité à l'Assemblée nationale, devant laquelle le Gouvernement est responsable (art.&nbsp;20)&nbsp;: c'est pourquoi le même texte peut donner des présidences très différentes selon que cette majorité le soutient ou non.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Suivre une promesse au-delà de la signature" avis="non" >}}
Cette page dit qui signe. Le livre pose la question suivante&nbsp;: une promesse de campagne, une fois l'élu en place, passe par quelle chaîne&nbsp;? Il propose une grille en quatre zones — ce qu'un président décide dans sa propre chaîne de pouvoir, ce qu'il doit faire voter, ce qu'il doit négocier avec ceux dont la signature manque, et ce qui ne dépendra jamais de lui — et l'éprouve sur neuf promesses écrites, datées et signées. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

Tous les articles cités ici ont été lus dans leur version en vigueur, sur Légifrance, à la date indiquée. Chaque fiche renvoie aux articles sur lesquels elle repose.

{{< pouvoirs-president vue="sources" >}}

L'inventaire, les citations et la matrice sont produits par un script unique, qui relit les textes archivés et refuse d'écrire si une citation cesse de figurer dans son article&nbsp;; aucune case n'est remplie à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/pouvoirs_president_donnees.csv), en format long, une ligne par élément et par article&nbsp;; [JSON](/pouvoirs_president_donnees.json), avec les définitions et le compte rendu des contrôles.

{{< reutiliser figures="figures_pouvoirs" jeu="pouvoirs_president_donnees" sources="Légifrance (Constitution du 4 octobre 1958)" donnees="L'inventaire des huit dispositions de l'article 19, chaque élément avec sa citation exacte, son article et sa date de lecture, et les articles qui attribuent la loi et le règlement ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Cette page lit dans le texte de la Constitution les {{< pv-val "n_renvois" >}} dispositions que l'article&nbsp;19 dispense de contreseing. {{< pv-val "n_seuls_maj" >}} seulement, {{< pv-val "seuls_liste" >}}, ne contiennent dans leur article ni condition préalable, ni intervention ultérieure d'un autre acteur, ni pouvoir de même nature attribué à d'autres autorités&nbsp;; ce qui ne signifie pas que le président ne disposerait que de ces pouvoirs propres. La loi, votée par le Parlement, fixe notamment l'impôt (art.&nbsp;34)&nbsp;; le règlement appartient au Premier ministre (art.&nbsp;21), hors les décrets délibérés en Conseil des ministres, soumis au contreseing.
{{< /reutiliser >}}
