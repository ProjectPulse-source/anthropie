---
title: "Une loi votée s'applique-t-elle tout de suite ?"
description: "Du vote à la dernière mesure : les étapes qui séparent une loi votée de son application, combien des lois promulguées depuis 2017 attendent encore un décret ou un arrêté, ce que le Conseil d'État exige du Gouvernement, et pourquoi le Sénat et le Gouvernement publient des taux d'application différents. Données ouvertes."
chapo: "Pas du seul fait du vote. Une fois la loi promulguée et publiée, celles de ses dispositions dont l'exécution nécessite des décrets ou des arrêtés attendent ces mesures. Au {app.releve}, selon le baromètre de l'application des lois, {app.L_att} des {app.nlois} lois promulguées d'octobre 2017 à septembre 2025, hors conventions (lois qui autorisent la ratification ou l'approbation d'un accord international, ou l'adhésion à un tel accord), attendaient encore au moins une mesure ; {app.L_tout} les avaient toutes reçues et {app.L_dir} n'en appelaient aucune. Une mesure en attente n'est pas forcément en retard, mais le Gouvernement n'est pas libre d'attendre indéfiniment : le Conseil d'État exige qu'il agisse « dans un délai raisonnable », et le refus de prendre une mesure due peut être porté devant le juge administratif, qui peut l'annuler et ordonner de la prendre."
date: 2026-10-06
lastmod: 2026-10-12
donnees: [promesses_appliquer]
og_title: "Une loi votée s'applique-t-elle tout de suite ? — les mesures d'application en attente — S. Lalut"
og_image: "images/og-appliquer-promesse.jpg"
og_image_alt: "Carte de partage : le nombre de mesures d'application encore attendues pour les lois votées d'octobre 2017 à septembre 2025, et des barres par session de la loi : mesures avec un acte publié, en attente, indiquées sans objet, à la date du relevé du baromètre de l'application des lois."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_appliquer"
  nom: "Mesures d'application des lois promulguées de 2017 à 2025, statut des lois, lois d'application directe et taux publiés par le Sénat et le Gouvernement"
  description: "Statut, loi par loi, des lois promulguées du 1er octobre 2017 au 30 septembre 2025, hors conventions, et état de leurs mesures d'application au 5 octobre 2026 (baromètre de l'application des lois, Assemblée nationale et LexImpact, données DILA) ; tri des observations « sans objet » par règles écrites ; lois d'application directe par session selon le baromètre et selon le Sénat, rapprochées loi par loi ; taux d'application publiés par le Sénat de 2002-2003 à 2024-2025, par segment de définition, et par le Secrétariat général du Gouvernement au 31 décembre 2025."
  couverture_temporelle: "2002/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Lois par statut d'application", unite: "lois"}
    - {nom: "Mesures d'application par état", unite: "mesures"}
    - {nom: "Lois promulguées et lois d'application directe", unite: "lois"}
    - {nom: "Taux d'application publiés par le Sénat et par le Gouvernement", unite: "%"}
  sources:
    - "https://barometre.assemblee-nationale.fr/"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006419280"
    - "https://www.legifrance.gouv.fr/contenu/menu/autour-de-la-loi/legislatif-et-reglementaire/application-des-lois/bilan-semestriel-au-31-decembre-2025"
  mots: ["application des lois", "décrets d'application", "mesures réglementaires", "délai raisonnable", "Conseil d'État", "Sénat", "Secrétariat général du Gouvernement", "promesses"]
  fichiers: ["promesses_appliquer.csv", "promesses_appliquer.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Une loi s'applique-t-elle dès sa publication au Journal officiel ?"
    answer: "En principe, elle entre en vigueur à la date qu'elle fixe ou, à défaut, le lendemain de sa publication ; en cas d'urgence, dès sa publication si le décret de promulgation le prescrit (code civil, art. 1er). Le même article ajoute : « {app.cit_cciv} » Une loi peut donc être en vigueur pour une part et attendre ses décrets ou ses arrêtés pour une autre."
  - question: "Combien de lois attendent encore une mesure d'application ?"
    answer: "Au {app.releve}, selon le baromètre de l'application des lois, {app.L_att} des {app.nlois} lois promulguées d'octobre 2017 à septembre 2025, hors conventions, comportaient encore au moins une mesure classée « en attente » ; {app.L_tout} avaient reçu toutes leurs mesures, {app.L_dir} n'en appelaient aucune et une n'avait pas d'échéancier. Sur les {app.nmes} mesures recensées pour ces lois, {app.A} étaient en attente. Une mesure en attente n'est pas forcément en retard."
  - question: "Quel est le taux d'application des lois ?"
    answer: "Il dépend des conventions de calcul. Au 31 décembre 2025, le Secrétariat général du Gouvernement publie {app.sgg16_taux} pour les lois de la XVIe législature, décrets seuls, et {app.sgg17_taux} pour celles de la XVIIe, décrets ou arrêtés ; le Sénat publie {app.s2425} pour la session 2024-2025, au 31 mars 2026. Ces taux ne portent ni sur les mêmes lois, ni sur les mêmes mesures, ni à la même date : ils ne se classent pas."
  - question: "Une loi sur deux n'est-elle pas appliquée ?"
    answer: "Au {app.releve}, selon le baromètre, {app.L_att} des {app.nlois} lois promulguées d'octobre 2017 à septembre 2025, hors conventions, comportaient encore au moins une mesure classée « en attente ». Rapportées aux seules {app.L_mes} lois qui appelaient au moins une mesure, elles en forment {app.L_att_pct_mes}, environ une sur deux. Cela ne signifie ni que ces lois étaient entièrement inapplicables, ni que chacune de ces mesures était en retard. Une formule comme « une loi sur deux » peut venir de ce second compte, d'un taux par mesure, d'une seule session ou d'une autre date : avant de la reprendre, il faut savoir ce qu'elle compte, à quelle date et sur quelles lois."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocoles de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-12"
  bloc: "promesses"
  rang: 30
  nature: "Baromètre de l'application des lois, rapports du Sénat, bilan du SGG et décisions du Conseil d'État, rapprochés loi par loi ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Une loi votée s'applique-t-elle tout de suite ?"
  court: "Appliquer"
  role: "décrets et mesures d'application"
---

{{< reutiliser-ancre >}}

Une promesse qui passe par la loi ne s'arrête pas au vote. Entre l'adoption et l'application, la loi franchit plusieurs étapes, et certaines de ses dispositions attendent ensuite des décrets ou des arrêtés. Cette page suit ces étapes, compte les lois et les mesures qui attendent encore pour les lois promulguées depuis 2017, dit ce que le juge exige du Gouvernement, et explique pourquoi les taux d'application publiés ne disent pas tous la même chose. Les comptes de lois et de mesures sont recalculés loi par loi à partir des sources publiques&nbsp;; les taux publiés par le Sénat et par le Gouvernement, transcrits de leurs rapports, sont relus par le script dans les documents archivés.

## Du vote à l'application&nbsp;: par quelles étapes passe une loi&nbsp;? {#du-vote-a-l-application}

Cinq étapes séparent une loi votée de son application, et chacune a son acteur.

1. **Le vote.** Le Parlement adopte définitivement le texte.
2. **La promulgation.** Le Président de la République promulgue la loi dans les quinze jours qui suivent sa transmission au Gouvernement, et peut, dans ce délai, demander au Parlement une nouvelle délibération (Constitution, art.&nbsp;10). Le Conseil constitutionnel s'intercale ici&nbsp;: il examine obligatoirement les lois organiques avant leur promulgation, les autres lois peuvent lui être déférées, et sa saisine suspend le délai de promulgation (art.&nbsp;61).
3. **La publication et l'entrée en vigueur.** Publiée au Journal officiel, la loi entre en vigueur à la date qu'elle fixe ou, à défaut, le lendemain de sa publication (code civil, art.&nbsp;1er, al.&nbsp;1). L'alinéa suivant ajoute&nbsp;: «&nbsp;{{< app-val "cit_cciv" >}}&nbsp;» Un troisième ouvre une voie plus rapide&nbsp;: «&nbsp;{{< app-val "cit_cciv_urg" >}}&nbsp;».
4. **Les mesures d'exécution.** Le Premier ministre assure l'exécution des lois et, sous réserve de l'article&nbsp;13, exerce le pouvoir réglementaire (art.&nbsp;21). Le Président de la République signe les décrets délibérés en Conseil des ministres (art.&nbsp;13), et les actes du Premier ministre sont contresignés, le cas échéant, par les ministres chargés de leur exécution (art.&nbsp;22). La loi peut aussi prévoir des arrêtés, et un décret peut lui-même renvoyer à un arrêté d'un ministre.
5. **La mise en œuvre.** Restent les services, les budgets et les collectivités qui appliquent la règle. Cette étape échappe aux données de cette page&nbsp;: un décret publié n'est pas un résultat obtenu. La page ne dit pas non plus si les crédits nécessaires ont été ouverts, ni ce que font les collectivités chargées d'appliquer certaines lois&nbsp;: aucune source n'a été lue sur ces deux points.

<details class="repli"><summary>Les articles de la Constitution, mot pour mot</summary>

**Article&nbsp;10.** «&nbsp;{{< app-val "cit_art10" >}}&nbsp;» «&nbsp;{{< app-val "cit_art10_al2" >}}&nbsp;»

**Article&nbsp;61.** Les lois organiques sont soumises au Conseil constitutionnel avant leur promulgation (al.&nbsp;1). Pour les autres, l'alinéa&nbsp;2 dispose&nbsp;: «&nbsp;{{< app-val "cit_art61_saisine" >}}&nbsp;» Dans ces cas, «&nbsp;{{< app-val "cit_art61" >}}&nbsp;»

**Article&nbsp;21**, du Premier ministre&nbsp;: «&nbsp;{{< app-val "cit_art21_exec" >}}&nbsp;» Sous réserve de l'article&nbsp;13, «&nbsp;{{< app-val "cit_art21_regl" >}}&nbsp;».

**Article&nbsp;13.** «&nbsp;{{< app-val "cit_art13" >}}&nbsp;»

**Article&nbsp;22.** «&nbsp;{{< app-val "cit_art22" >}}&nbsp;»

</details>

Le code civil ne vise pas toute disposition qui annonce un décret&nbsp;: il vise celles «&nbsp;dont l'exécution nécessite&nbsp;» des mesures. Une loi peut renvoyer à un décret pour une disposition qui s'applique déjà sans lui. En cas de litige, c'est le juge qui en décide, disposition par disposition. En 2021, à propos des bâtiments d'élevage de poules pondeuses en cages, le Conseil d'État a ainsi jugé que «&nbsp;{{< app-val "cit_ce_precision" >}}&nbsp;» (CE, 27&nbsp;mai 2021, n°&nbsp;441660).

## Combien de lois attendent encore une mesure&nbsp;? {#lois-en-attente}

{{< figure-svg fichier="appliquer-statut" alt="Barres horizontales, une par session de 2017-2018 à 2024-2025 : lois qui attendent au moins une mesure, lois qui ont reçu toutes leurs mesures, lois sans mesure à prendre, loi sans échéancier. Chaque session compte des lois qui attendent encore, y compris la plus ancienne. Les valeurs sont dans le tableau sous la figure." >}}Lois promulguées de chaque session, hors conventions, et leur statut au {{< app-val "releve" >}} selon le baromètre de l'application des lois. Une mesure «&nbsp;en attente&nbsp;» n'est pas forcément en retard.{{< /figure-svg >}}

{{< fig-actions id="statut" >}}

{{< app-tableau "statut" "Les valeurs de la figure en tableau" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Au {{< app-val "releve" >}}, selon le baromètre, {{< app-val "L_att" >}} des {{< app-val "nlois" >}} lois promulguées d'octobre 2017 à septembre 2025, hors conventions, comportaient encore au moins une mesure classée «&nbsp;en attente&nbsp;»&nbsp;; {{< app-val "L_tout" >}} avaient reçu toutes leurs mesures, {{< app-val "L_dir" >}} n'en appelaient aucune, et une n'avait pas d'échéancier.

</div>

**Rapporté aux seules lois qui appelaient une mesure.** Sur les {{< app-val "nlois" >}} lois promulguées, {{< app-val "L_dir" >}} n'appelaient aucune mesure selon le baromètre. Les lois qui en appelaient au moins une, qu'elles en attendent encore ou les aient toutes reçues, sont {{< app-val "L_mes" >}}. Parmi elles, les {{< app-val "L_att" >}} lois en attente forment {{< app-val "L_att_pct_mes" >}}, environ une sur deux. La loi sans échéancier n'est comptée ni d'un côté ni de l'autre&nbsp;: le baromètre ne dit pas si elle appelle des mesures. Les deux parts sont exactes&nbsp;: l'une rapporte les lois en attente à toutes les lois promulguées, l'autre aux seules lois qui avaient une mesure à attendre.

**Ce que ces deux parts ne disent pas.** Elles ne disent ni que ces {{< app-val "L_att" >}} lois étaient entièrement inapplicables, ni que chacune de leurs mesures en attente était en retard. Une loi peut s'appliquer pour l'essentiel en attendant un décret sur un point, et la loi elle-même peut différer une mesure. La date prévue manque pour {{< app-val "A_sans_date" >}} des {{< app-val "A" >}} mesures en attente&nbsp;: faute de date, la page ne dit pas si une mesure est en retard. L'ancienneté ne règle pas tout&nbsp;: pour la session 2017-2018, la plus ancienne, {{< app-val "L_att_1718" >}} lois sur {{< app-val "L_N_1718" >}} attendent encore au moins une mesure.

Le compte des lois «&nbsp;sans mesure à prendre&nbsp;» dépend d'une étiquette. Le baromètre classe ainsi une loi dont toutes les mesures sont indiquées «&nbsp;sans objet&nbsp;». La loi n°&nbsp;2025-138 sur la sclérose latérale amyotrophique est dans ce cas, alors que son unique mesure renvoie à un arrêté (voir la section suivante).

**Le témoin du Sénat.** Le Sénat compte, lui, les lois «&nbsp;entièrement applicables&nbsp;»&nbsp;: celles d'application directe et celles qui ont reçu toutes les mesures prévues. Pour la session 2024-2025, il écrit&nbsp;: «&nbsp;{{< app-val "cit_802_36" >}}&nbsp;» Il précise&nbsp;: «&nbsp;{{< app-val "cit_802_detail" >}}&nbsp;» Le baromètre compte lui aussi {{< app-val "s25_N" >}} lois pour cette session. Au {{< app-val "releve" >}}, ces deux mêmes catégories y réunissent {{< app-val "s25_dirtout" >}} lois&nbsp;: {{< app-val "s25_dir" >}} sans mesure à prendre et {{< app-val "s25_tout" >}} dont toutes les mesures sont prises. Ce sont deux constats, à deux dates, par deux producteurs qui ne classent pas les lois de la même façon&nbsp;: ils ne s'additionnent ni ne se confirment, et rien n'établit que les lois comptées de part et d'autre soient les mêmes.

## Combien de mesures d'application attendent encore&nbsp;? {#mesures-en-attente}

Une loi attend des mesures&nbsp;; c'est en mesures que le baromètre suit l'application.

{{< figure-svg fichier="appliquer-mesures" alt="Barres horizontales, une par session de la loi, de 2017-2018 à 2024-2025 : mesures avec un acte publié identifié, en attente, indiquées sans objet, au statut incomplet. Une partie en attente subsiste dans chaque session, y compris la plus ancienne. Les valeurs sont dans le tableau sous la figure." >}}Mesures d'application recensées par le baromètre de l'application des lois pour les lois promulguées de chaque session, hors conventions, et leur état au {{< app-val "releve" >}}. C'est un état à une date&nbsp;: ni un taux historique, ni une mesure d'efficacité.{{< /figure-svg >}}

{{< fig-actions id="mesures" >}}

{{< app-tableau "mesures" "Les valeurs de la figure en tableau" >}}

Au {{< app-val "releve" >}}, sur les {{< app-val "nmes" >}} mesures recensées pour ces lois, {{< app-val "P" >}} ont un acte publié identifié, {{< app-val "A" >}} sont en attente, {{< app-val "S" >}} sont indiquées «&nbsp;sans objet&nbsp;» et {{< app-val "U" >}} ont un statut incomplet («&nbsp;appliqué&nbsp;» sans acte identifié). Pour les lois de 2017-2018, {{< app-val "A_1718" >}} mesures sur {{< app-val "N_1718" >}} restent en attente&nbsp;; pour celles de 2024-2025, {{< app-val "A_2425" >}} sur {{< app-val "N_2425" >}}.

**«&nbsp;En attente&nbsp;» n'est pas «&nbsp;en retard&nbsp;».** {{< app-val "differ_A" >}} des {{< app-val "A" >}} mesures en attente portent, dans leur objet ou leur observation, la mention «&nbsp;différé&nbsp;» ou «&nbsp;différée&nbsp;», dont {{< app-val "differ_1819" >}} pour les lois de 2018-2019 et {{< app-val "differ_1920" >}} pour celles de 2019-2020&nbsp;; la mention ne dit pas si la date différée est passée. La date prévue manque pour {{< app-val "A_sans_date" >}} des {{< app-val "A" >}} mesures en attente&nbsp;: l'ancienneté d'une attente ne se calcule donc pas, et la page ne publie aucun délai.

**«&nbsp;Sans objet&nbsp;» est une étiquette, pas une preuve.** Le producteur range {{< app-val "S" >}} mesures sous cette étiquette et en donne le motif en observation. Triées par règles écrites, ces observations disent le plus souvent que la mesure est déjà appliquée par un texte existant ({{< app-val "tri_deja" >}}), que sa base légale a été abrogée, réécrite ou privée de son renvoi à un décret ({{< app-val "tri_base" >}}), ou qu'aucune mesure n'est nécessaire ({{< app-val "tri_aucune" >}})&nbsp;; {{< app-val "tri_event" >}} portent sur des mesures éventuelles non utilisées, {{< app-val "tri_nonprise" >}} disent qu'un décret n'a pas été pris, et {{< app-val "tri_indet" >}} restent indéterminées, faute de relever d'une seule règle. Ce tri reprend ce qu'écrit le producteur&nbsp;; il ne reclasse aucune mesure.

Restent, parmi les {{< app-val "S" >}} observations «&nbsp;sans objet&nbsp;», les {{< app-val "tri_acte" >}} qui commencent par la référence d'un arrêté ou d'un décret. Pour les lois de 2024-2025, elles sont {{< app-val "obs_acte_2425" >}}. Les {{< app-val "obs_ecartes" >}} observations qui commencent par «&nbsp;Décret non pris&nbsp;», sans référence d'acte, n'y sont pas comptées. Pour la loi n°&nbsp;2025-138, l'observation porte «&nbsp;{{< app-val "cas_2025_138" >}}&nbsp;», et le bilan du Gouvernement au 31&nbsp;décembre 2025 compte sa mesure comme en attente&nbsp;: les deux sources décrivent deux états, à deux dates, et ne se contredisent pas.

<details class="repli"><summary>Ce qui a été vérifié, et comment</summary>

Les mesures sont celles du baromètre de l'application des lois, publié par l'Assemblée nationale et LexImpact à partir des échéanciers de la DILA, dans sa version du {{< app-val "releve" >}}. Une mesure compte comme publiée si son état est «&nbsp;appliqué&nbsp;» et qu'un acte est identifié&nbsp;; «&nbsp;appliqué&nbsp;» sans acte identifié donne un statut incomplet. Le script vérifie que chaque mesure entre dans une et une seule catégorie, session par session, et que le fichier des lois du même producteur donne, loi par loi, le même nombre de mesures appliquées et à appliquer&nbsp;; il vérifie aussi que chaque loi relève d'un et d'un seul des quatre statuts. Un second programme, écrit séparément, a recompté les catégories de mesures à partir du fichier brut&nbsp;: les nombres concordent.

Les règles du tri des observations «&nbsp;sans objet&nbsp;» sont publiées dans le jeu de données&nbsp;; une observation qui relève de zéro ou de plusieurs règles est indéterminée. Une observation compte comme portant la référence d'un acte si elle commence par «&nbsp;Arrêté du&nbsp;», «&nbsp;Décret du&nbsp;» ou «&nbsp;Décret n°&nbsp;»&nbsp;; celles qui commencent par le mot sans référence sont listées dans le jeu de données, avec leur motif.

Le baromètre ne publie que l'état courant. Les données ouvertes de la DILA sur les échéanciers ne remontent qu'en juillet 2025. Aucun taux «&nbsp;six mois après la loi&nbsp;» ne peut donc se recalculer pour les sessions antérieures, et la page n'en publie aucun.

</details>

## Une loi peut-elle s'appliquer sans aucun décret&nbsp;? {#lois-application-directe}

Oui. Le baromètre et le Sénat, dans ses rapports annuels, classent chacun des lois «&nbsp;d'application directe&nbsp;», mais pas toujours les mêmes. Le baromètre classe ainsi une loi dont l'échéancier ne comporte aucune mesure autre que «&nbsp;sans objet&nbsp;»&nbsp;; le Sénat applique ses propres règles. Rapprochées loi par loi sur les {{< app-val "nlois" >}} lois promulguées de 2017-2018 à 2024-2025, hors {{< app-val "conventions" >}} conventions internationales, les deux sources retiennent exactement le même champ, mais classent différemment {{< app-val "ndesacc" >}} lois.

{{< figure-svg fichier="appliquer-lois" alt="Barres horizontales, une par session : lois d'application directe pour les deux sources, lois classées différemment, lois qui appellent des mesures ; un trait marque la moitié des lois de chaque session. En 2018-2019, les lois directes et divergentes dépassent la moitié. Les valeurs sont dans le tableau sous la figure." >}}Lois promulguées de chaque session, hors conventions. En bleu, les lois d'application directe pour les deux sources&nbsp;; en gris foncé, celles qu'elles classent différemment&nbsp;; le trait noir marque la moitié des lois de la session.{{< /figure-svg >}}

{{< fig-actions id="lois" >}}

{{< app-tableau "lois" "Les valeurs de la figure en tableau" >}}

Dans {{< app-val "nautres" >}} sessions sur {{< app-val "nsessions" >}}, les lois d'application directe restent sous la moitié, quelle que soit la source. En {{< app-val "ct_session" >}}, le baromètre en compte {{< app-val "ct_baro" >}} sur {{< app-val "ct_N" >}}, plus de la moitié, quand le Sénat en compte {{< app-val "ct_senat" >}}.

L'écart de 2024-2025 se lit dans un même rapport du Sénat. Sa synthèse écrit&nbsp;: «&nbsp;{{< app-val "cit_802_22" >}}&nbsp;»&nbsp;; une autre page indique que «&nbsp;{{< app-val "cit_802_24" >}}&nbsp;». Le baromètre en compte {{< app-val "s25_baro" >}}. L'écart entre {{< app-val "s25_baro" >}} et {{< app-val "s25_senat" >}} s'explique loi par loi par des règles de classement différentes&nbsp;; celui entre {{< app-val "s25_senat" >}} et {{< app-val "s25_publie" >}} ne s'explique pas, faute de liste nominative.

<details class="repli"><summary>Pourquoi les deux sources divergent sur {{< app-val "ndesacc" >}} lois</summary>

Le Sénat classe les lois dans les annexes de ses rapports. Plusieurs règles expliquent une partie des écarts avec le baromètre&nbsp;: le Sénat écarte, certaines années, les mesures dont la loi laisse la prise facultative&nbsp;; le baromètre classe «&nbsp;directe&nbsp;» une loi dont toutes les mesures sont aujourd'hui indiquées sans objet&nbsp;; il classe «&nbsp;non directe&nbsp;» une loi sans échéancier. Appliquées ensemble, ces règles font disparaître une partie des écarts et en font apparaître d'autres&nbsp;: elles ne sont pas appliquées uniformément d'une année à l'autre. Toutes les lois en écart sont comptées comme incertaines, même quand une règle les explique&nbsp;; d'où les bornes du tableau.

Des défauts des annexes du Sénat, comme un numéro de loi erroné ou un effectif annoncé qui ne correspond pas à la liste qui le suit, ont été corrigés par le titre et la date de la loi&nbsp;; le registre loi par loi les signale.

</details>

## Le Gouvernement a-t-il un délai pour prendre les décrets&nbsp;? {#delai-raisonnable}

Les articles&nbsp;13 et&nbsp;21 de la Constitution ne fixent aucun délai. Le Gouvernement s'en donne un, de six mois, selon le Sénat (voir la série plus bas). Le juge, lui, pose une obligation&nbsp;: «&nbsp;{{< app-val "cit_ce_principe" >}}&nbsp;» (Conseil d'État, 27&nbsp;mai 2021, n°&nbsp;441660&nbsp;; la même formule figure dans ses décisions du 29&nbsp;juin 2011 et du 21&nbsp;janvier 2021). Elle vaut aussi pour les arrêtés&nbsp;: «&nbsp;{{< app-val "cit_ce_arrete" >}}&nbsp;» (CE, 21&nbsp;janvier 2021, n°&nbsp;429956).

Le délai raisonnable ne se chiffre pas une fois pour toutes&nbsp;: il s'apprécie «&nbsp;{{< app-val "cit_ce_nature" >}}&nbsp;» (CE, 27&nbsp;juillet 2005, n°&nbsp;261694). Les durées jugées excessives dans une affaire ne font donc pas une règle.

Le refus de prendre une mesure due peut être porté devant le juge administratif, qui peut l'annuler et ordonner de la prendre. En mai 2021, le Conseil d'État a décidé «&nbsp;{{< app-val "cit_ce_injonction" >}}&nbsp;»&nbsp;; en janvier 2021, «&nbsp;{{< app-val "cit_ce_arrete_injonction" >}}&nbsp;». Le retard peut aussi engager la responsabilité de l'État&nbsp;: «&nbsp;{{< app-val "cit_ce_reparation" >}}&nbsp;» (CE, 27&nbsp;juillet 2005).

Une mesure prévue n'est pas toujours due. En 2011, à propos d'un arrêté prévu par un décret et jamais pris, le Conseil d'État a relevé que «&nbsp;{{< app-val "cit_ce_exhaustif" >}}&nbsp;», et en a conclu que «&nbsp;{{< app-val "cit_ce_pas_tenu" >}}&nbsp;» (CE, 29&nbsp;juin 2011, n°&nbsp;343188).

**Ce que ces décisions ne disent pas.** Elles posent une règle et tranchent des cas&nbsp;; elles ne disent ni combien de refus sont portés devant le juge, ni ce que deviennent les injonctions, et aucune donnée lue ici ne le mesure. Le statut «&nbsp;en attente&nbsp;» du baromètre ne dit pas non plus si une mesure est due, ni si le délai raisonnable est dépassé.

## Pourquoi le Sénat et le Gouvernement publient-ils des taux différents&nbsp;? {#taux-publies}

Parce que leurs conventions de calcul ont différé et diffèrent encore en partie. L'écart a une histoire.

**En 2012-2013, des taux qui coïncident.** Le Sénat écrit que, «&nbsp;{{< app-val "cit_1213" >}}&nbsp;». Cette année-là, le taux changeait selon qu'on comptait des lois ou des mesures, non selon le producteur.

**En 2017-2019, un écart et ses raisons.** Pour 2017-2018, le Sénat écrit&nbsp;: «&nbsp;{{< app-val "cit_senat_1718" >}}&nbsp;». Le Secrétariat général du Gouvernement, entendu par le Sénat, déclare&nbsp;: «&nbsp;{{< app-val "cit_sgg_1718" >}}&nbsp;». Une fois les mesures différées écartées, les deux chiffres se rapprochent, {{< app-val "s1718_hd" >}} pour le Sénat et {{< app-val "sgg1718" >}} pour le Gouvernement&nbsp;; les arrêtés, que seul le Sénat comptait, restent une différence de champ. Pour 2018-2019, le Sénat écrit&nbsp;: «&nbsp;{{< app-val "cit_senat_1819" >}}&nbsp;» et ajoute que «&nbsp;{{< app-val "cit_sgg_1819" >}}&nbsp;». En 2019, il en donnait les raisons&nbsp;: «&nbsp;{{< app-val "cit_diverge" >}}&nbsp;» D'une part, «&nbsp;{{< app-val "cit_arretes" >}}&nbsp;» D'autre part, «&nbsp;{{< app-val "cit_differees" >}}&nbsp;» Il mentionne aussi un troisième motif, qu'il qualifie lui-même de raisons politiques&nbsp;: «&nbsp;{{< app-val "cit_politique" >}}&nbsp;» Un taux peut ainsi intégrer une appréciation, et non seulement un comptage.

**Depuis 2024, des méthodes rapprochées.** Le rapport du Sénat de 2026 l'écrit&nbsp;: «&nbsp;{{< app-val "cit_802_arretes" >}}&nbsp;» Pour le Sénat lui-même, «&nbsp;{{< app-val "cit_802_differees" >}}&nbsp;». Il ajoute&nbsp;: «&nbsp;{{< app-val "cit_802_appreciation" >}}&nbsp;»

**Les taux publiés aujourd'hui.** Au 31&nbsp;décembre 2025, le bilan semestriel du Gouvernement sur la XVI<sup>e</sup>&nbsp;législature «&nbsp;{{< app-val "cit_sgg16_def" >}}&nbsp;» Il donne un taux de {{< app-val "sgg16_taux" >}}, sur {{< app-val "sgg16_n" >}} mesures. Celui de la XVII<sup>e</sup>&nbsp;législature «&nbsp;{{< app-val "cit_sgg17_def" >}}&nbsp;» Il donne {{< app-val "sgg17_taux" >}}, sur {{< app-val "sgg17_n" >}} mesures. Le Sénat publie {{< app-val "s2425" >}} pour la session 2024-2025. Ces trois taux ne portent ni sur les mêmes lois, ni sur les mêmes mesures, ni à la même date&nbsp;: le tableau ci-dessous les range par définition, il ne les classe pas. Un taux d'application n'est interprétable qu'avec son périmètre, sa date d'arrêté et ses règles de comptage.

{{< app-tableau "taux" "La définition de chaque taux" >}}

## Le taux d'application des lois a-t-il progressé depuis 2002&nbsp;? {#serie-senat}

La série du Sénat ne permet pas de le dire d'un bout à l'autre. Le corpus fait apparaître {{< app-val "nsegments" >}} définitions successives depuis 2002-2003, qui diffèrent par la date d'arrêté, le champ des lois et le traitement des mesures différées et éventuelles&nbsp;: les segments ne se lisent pas comme une seule série. Le Sénat lit pourtant une tendance à travers ses propres ruptures&nbsp;: «&nbsp;{{< app-val "cit_802_baisse" >}}&nbsp;». Sa série ne permet de confronter cette lecture que segment par segment&nbsp;: 2024-2025 relève d'une autre définition que les sessions précédentes.

{{< figure-svg fichier="appliquer-serie" alt="Points par session de 2002-2003 à 2024-2025, regroupés en segments séparés par des ruptures de définition. Le premier segment, de 2002-2003 à 2008-2009, se situe nettement plus bas que les suivants. Les valeurs, leur document et leur définition sont dans le tableau sous la figure." >}}Taux d'application des lois publiés par le Sénat, tels que publiés. Les segments correspondent à des définitions différentes&nbsp;: ne pas les relier. Le cercle vide marque la valeur de 2019-2020 donnée par le rapport suivant.{{< /figure-svg >}}

{{< fig-actions id="serie" >}}

{{< app-tableau "serie" "Les valeurs, leur document et leur définition" >}}

Le dernier point du premier segment et le premier point retenu du suivant sont séparés par une rupture de définition, que le Sénat décrit ainsi&nbsp;: «&nbsp;{{< app-val "cit_six_mois" >}}&nbsp;» En 2024-2025, il publie un seul taux («&nbsp;{{< app-val "cit_802_66" >}}&nbsp;»), et précise en note&nbsp;: «&nbsp;{{< app-val "cit_802_note" >}}&nbsp;» Les mesures éventuelles sont celles que la loi permet de prendre sans l'imposer.

Les «&nbsp;+&nbsp;{{< app-val "plus4" >}}&nbsp;points&nbsp;» ne se lisent pas dans le tableau, qui donne {{< app-val "s2324" >}} pour 2023-2024&nbsp;: le Sénat compare à son taux de 2023-2024 hors mesures différées. Le rapport précédent l'indiquait&nbsp;: «&nbsp;{{< app-val "cit_2324_62" >}}&nbsp;».

Pour 2019-2020, les rapports donnent deux valeurs. Celui de 2020 écrit&nbsp;: «&nbsp;{{< app-val "cit_2020_62" >}}&nbsp;». Le suivant, consacré à 2020-2021, écrit «&nbsp;{{< app-val "cit_2021_60" >}}&nbsp;», puis&nbsp;: «&nbsp;{{< app-val "cit_2021_62" >}}&nbsp;». Révision du chiffre ou autre variante du taux&nbsp;: les documents ne permettent pas de le trancher, et la série garde les deux valeurs. La session 2009-2010 n'est pas retenue sur la figure, faute de date d'arrêté établie dans la phrase qui donne son taux. Deux valeurs pour une même session et une rupture de définition sont deux faits distincts&nbsp;: la série les garde l'un et l'autre.

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas si une loi produit l'effet que visait la promesse. Elle ne mesure pas la qualité des décrets, ni leur conformité à la volonté du législateur, que le Sénat apprécie lui-même. Elle ne donne aucun délai de publication, faute d'historique daté des échéanciers. Elle met côte à côte les taux du Sénat et du Gouvernement avec leurs définitions, sans les classer, et ne relie pas deux segments de la série du Sénat.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Après le vote" avis="non" >}}
Cette page compte ce qu'une loi attend encore après son vote. Le livre suit neuf promesses écrites, datées et signées, le long de la chaîne qui va de la décision à son résultat&nbsp;: ce qu'un président décide dans sa propre chaîne de pouvoir, ce qu'il doit faire voter, ce qu'il doit négocier, et ce qui ne dépendra jamais de lui. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Baromètre de l'application des lois**, Assemblée nationale et LexImpact, à partir des échéanciers de la DILA&nbsp;: fichiers des lois et des mesures, version du {{< app-val "releve" >}}.

**Sénat**, rapports annuels sur l'application des lois de 2011 à 2026, synthèses et communiqués de 2003 à 2011&nbsp;; le document et la page de chaque valeur et de chaque citation sont donnés dans le jeu de données.

**Secrétariat général du Gouvernement**, bilan semestriel de l'application des lois au 31&nbsp;décembre 2025, lu sur Légifrance par navigateur.

**Conseil d'État**, décisions du 27&nbsp;juillet 2005 (n°&nbsp;261694), du 29&nbsp;juin 2011 (n°&nbsp;343188), du 21&nbsp;janvier 2021 (n°&nbsp;429956) et du 27&nbsp;mai 2021 (n°&nbsp;441660), lues sur ArianeWeb.

**Constitution**, art.&nbsp;10, 13, 21, 22 et 61, et **code civil**, art.&nbsp;1er, lus sur Légifrance (API).

Les chiffres, les citations, les contrôles et les figures sont produits par un script unique, qui s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases. Chaque citation est vérifiée mot pour mot dans le document archivé dont elle est tirée&nbsp;: pages des rapports du Sénat, articles de la Constitution et du code civil, décisions du Conseil d'État&nbsp;; pour le bilan du Secrétariat général du Gouvernement, que Légifrance refuse aux scripts, dans un relevé de la page lue par navigateur, dont l'empreinte est celle que le navigateur a calculée. Les comptes de lois et de mesures sont recalculés à partir des fichiers du baromètre&nbsp;; les taux du Sénat, transcrits dans le script, sont relus dans les pages archivées de ses rapports&nbsp;; le tri des observations «&nbsp;sans objet&nbsp;» suit des règles écrites dans le script. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_appliquer.csv), en format long&nbsp;; [JSON](/promesses_appliquer.json), avec les définitions, les règles du tri et le compte rendu des contrôles. Ce jeu est aussi archivé sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent à citer&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_appliquer" jeu="promesses_appliquer" sources="Assemblée nationale et LexImpact (données DILA), Sénat, SGG, Conseil d'État, Légifrance" donnees="Le statut des lois et l'état de leurs mesures d'application par session, le tri des observations « sans objet », les lois d'application directe selon les deux sources et les taux publiés par le Sénat depuis 2002-2003 et par le Gouvernement au 31 décembre 2025 ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Au {{< app-val "releve" >}}, selon le baromètre de l'application des lois, {{< app-val "L_att" >}} des {{< app-val "nlois" >}} lois promulguées d'octobre 2017 à septembre 2025, hors conventions, attendaient encore au moins une mesure&nbsp;; {{< app-val "L_tout" >}} les avaient toutes reçues et {{< app-val "L_dir" >}} n'en appelaient aucune. Le Conseil d'État exige que les mesures qu'implique nécessairement l'application de la loi soient prises dans un délai raisonnable. Les taux d'application du Sénat et du Gouvernement reposent sur des conventions de calcul différentes, et la série du Sénat sur {{< app-val "nsegments" >}} définitions successives depuis 2002-2003.
{{< /reutiliser >}}
