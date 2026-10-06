---
title: "Une loi votée s'applique-t-elle tout de suite ?"
description: "Une loi promulguée attend souvent des décrets et des arrêtés. Combien de mesures d'application les lois votées depuis 2017 attendent encore, combien de lois n'en appellent aucune, et pourquoi le Sénat et le Gouvernement publient des taux d'application différents. Données ouvertes."
chapo: "Pas du seul fait du vote. Une fois la loi promulguée et publiée, certaines de ses dispositions attendent encore les mesures nécessaires à leur exécution. Au {app.releve}, le baromètre de l'application des lois classe {app.A} des {app.nmes} mesures recensées pour les lois promulguées d'octobre 2017 à septembre 2025 comme encore en attente. Et le « taux d'application » lui-même dépend des conventions de calcul : pour deux sessions documentées ici, le Sénat publie son taux et rapporte un taux différent calculé par le Secrétariat général du Gouvernement."
date: 2026-10-06
lastmod: 2026-10-06
donnees: [promesses_appliquer]
og_title: "Une loi votée s'applique-t-elle tout de suite ? — les mesures d'application en attente — S. Lalut"
og_image: "images/og-appliquer-promesse.jpg"
og_image_alt: "Carte de partage : le nombre de mesures d'application encore attendues pour les lois votées d'octobre 2017 à septembre 2025, et des barres par session de la loi : mesures avec un acte publié, en attente, indiquées sans objet, à la date du relevé du baromètre de l'application des lois."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_appliquer"
  nom: "Mesures d'application des lois promulguées de 2017 à 2025, lois d'application directe et taux publiés par le Sénat"
  description: "État des mesures d'application des lois promulguées du 1er octobre 2017 au 30 septembre 2025, hors conventions, au 5 octobre 2026 (baromètre de l'application des lois, Assemblée nationale et LexImpact, données DILA) ; lois d'application directe par session selon le baromètre et selon le Sénat, rapprochées loi par loi ; taux d'application publiés par le Sénat de 2002-2003 à 2024-2025, par segment de définition."
  couverture_temporelle: "2002/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Mesures d'application par état", unite: "mesures"}
    - {nom: "Lois promulguées et lois d'application directe", unite: "lois"}
    - {nom: "Taux d'application publié par le Sénat", unite: "%"}
  sources:
    - "https://barometre.assemblee-nationale.fr/"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006419280"
  mots: ["application des lois", "décrets d'application", "mesures réglementaires", "Sénat", "Secrétariat général du Gouvernement", "promesses"]
  fichiers: ["promesses_appliquer.csv", "promesses_appliquer.json"]
faq:
  - question: "Une loi s'applique-t-elle dès sa publication au Journal officiel ?"
    answer: "Pas du seul fait du vote : « {app.cit_art10} » (Constitution, art. 10). Une fois publiée, elle entre en vigueur à la date qu'elle fixe ou, à défaut, le lendemain de sa publication. Mais, selon l'article 1er du code civil, « {app.cit_cciv} » Une loi peut donc être en vigueur pour une part et attendre ses décrets et ses arrêtés pour une autre."
  - question: "Combien de mesures d'application attendent encore ?"
    answer: "Au {app.releve}, le baromètre de l'application des lois recense {app.nmes} mesures pour les lois promulguées d'octobre 2017 à septembre 2025, hors conventions : {app.P} ont un acte publié identifié, {app.A} sont en attente, {app.S} sont indiquées sans objet et {app.U} ont un statut incomplet. Pour les lois de 2017-2018, {app.A_1718} mesures sur {app.N_1718} sont encore en attente. Ce n'est ni un taux historique ni une mesure d'efficacité."
  - question: "Quel est le taux d'application des lois ?"
    answer: "Il dépend des conventions de calcul. Pour la session 2018-2019, le Sénat publie {app.senat_1819} et rapporte que le Secrétariat général du Gouvernement parvient à {app.sgg_1819} : selon le Sénat, il compte les arrêtés et les mesures dont l'entrée en vigueur est différée, le Gouvernement non. Les deux niveaux ne sont pas directement comparables sans harmoniser ces conventions."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 30
  nature: "Baromètre de l'application des lois, rapports du Sénat et bilan du SGG, rapprochés loi par loi ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Une loi votée s'applique-t-elle tout de suite ?"
  court: "Appliquer"
  role: "décrets et mesures d'application"
---

{{< reutiliser-ancre >}}

Une promesse qui passe par la loi ne s'arrête pas au vote. Certaines dispositions attendent les mesures nécessaires à leur exécution, notamment des décrets ou des arrêtés. Cette page compte ces mesures pour les lois promulguées depuis 2017, montre combien de lois n'en appellent aucune, et explique pourquoi les taux d'application publiés ne disent pas tous la même chose. Tous les nombres viennent des sources publiques, rapprochées loi par loi, et aucun n'est saisi à la main.

**Réponse courte.** Pas du seul fait du vote. Une fois la loi promulguée et publiée, elle entre en vigueur à la date qu'elle fixe ou le lendemain de sa publication&nbsp;; mais celles de ses dispositions qui appellent des mesures d'application attendent ces mesures. Au {{< app-val "releve" >}}, {{< app-val "A" >}} des {{< app-val "nmes" >}} mesures recensées pour les lois de 2017 à 2025 sont encore en attente.

Entre le vote et l'entrée en vigueur, la Constitution place la promulgation&nbsp;: «&nbsp;{{< app-val "cit_art10" >}}&nbsp;» (art.&nbsp;10). Si le Conseil constitutionnel est saisi, «&nbsp;{{< app-val "cit_art61" >}}&nbsp;» (art.&nbsp;61). Une fois la loi publiée au Journal officiel, le code civil fixe la règle&nbsp;: «&nbsp;{{< app-val "cit_cciv" >}}&nbsp;» (art.&nbsp;1er).

## Combien de mesures d'application attendent encore&nbsp;? {#mesures-en-attente}

{{< figure-svg fichier="appliquer-mesures" alt="Barres horizontales, une par session de la loi, de 2017-2018 à 2024-2025 : mesures avec un acte publié identifié, en attente, indiquées sans objet. Une partie en attente subsiste dans chaque session, y compris la plus ancienne. Les valeurs sont dans le tableau sous la figure." >}}Mesures d'application recensées par le baromètre de l'application des lois pour les lois promulguées de chaque session, hors conventions, et leur état au {{< app-val "releve" >}}. C'est un état à une date&nbsp;: ni un taux historique, ni une mesure d'efficacité.{{< /figure-svg >}}

{{< fig-actions id="mesures" >}}

{{< app-tableau "mesures" "Les valeurs de la figure en tableau" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Au {{< app-val "releve" >}}, sur les {{< app-val "nmes" >}} mesures d'application recensées pour les lois promulguées d'octobre 2017 à septembre 2025, {{< app-val "P" >}} ont un acte publié identifié, {{< app-val "A" >}} sont en attente et {{< app-val "S" >}} sont indiquées sans objet.

</div>

Au {{< app-val "releve" >}}, {{< app-val "A_1718" >}} des {{< app-val "N_1718" >}} mesures recensées pour les lois de la session 2017-2018 restent classées «&nbsp;en attente&nbsp;» par le baromètre&nbsp;; pour celles de 2024-2025, {{< app-val "A_2425" >}} sur {{< app-val "N_2425" >}}. Ce statut ne suffit pas, à lui seul, à qualifier un retard&nbsp;: {{< app-val "differ_A" >}} des {{< app-val "A" >}} mesures en attente portent, dans leur objet ou leur observation, la mention «&nbsp;différé&nbsp;» ou «&nbsp;différée&nbsp;», et la loi peut fixer elle-même une date ultérieure.

**Un classement à lire avec sa réserve.** {{< app-val "obs_acte" >}} des mesures indiquées «&nbsp;sans objet&nbsp;» comportent dans leur observation la référence d'un arrêté ou d'un décret, dont {{< app-val "obs_acte_2425" >}} pour les lois de 2024-2025. Ce constat ne permet pas de les reclasser&nbsp;: «&nbsp;sans objet&nbsp;» est repris ici comme l'étiquette du producteur. Pour l'une d'elles, la loi n°&nbsp;2025-138 sur la prise en charge de la sclérose latérale amyotrophique, l'observation porte «&nbsp;{{< app-val "cas_2025_138" >}}&nbsp;», et le bilan du Gouvernement au 31&nbsp;décembre 2025 compte sa mesure comme en attente. L'étiquette ne prouve donc pas qu'une mesure a été abandonnée.

<details class="repli"><summary>Ce qui a été vérifié, et comment</summary>

Les mesures sont celles du baromètre de l'application des lois, publié par l'Assemblée nationale et LexImpact à partir des échéanciers de la DILA, dans sa version du {{< app-val "releve" >}}. Une mesure compte comme publiée si son état est «&nbsp;appliqué&nbsp;» et qu'un acte est identifié&nbsp;; «&nbsp;appliqué&nbsp;» sans acte identifié donne un statut incomplet. Le script vérifie que chaque mesure entre dans une et une seule catégorie, session par session, et que le fichier des lois du même producteur donne, loi par loi, le même nombre de mesures appliquées et à appliquer. Un second programme, écrit séparément, a recompté les mêmes catégories à partir du fichier brut&nbsp;: les nombres concordent.

Le baromètre ne publie que l'état courant. Les données ouvertes de la DILA sur les échéanciers ne remontent qu'en juillet 2025. Aucun taux «&nbsp;six mois après la loi&nbsp;» ne peut donc se recalculer pour les sessions antérieures, et la page n'en publie aucun.

</details>

## Une loi peut-elle s'appliquer sans aucun décret&nbsp;? {#lois-application-directe}

Oui. Les deux sources qui classent les lois de chaque session, le baromètre et le Sénat dans ses rapports annuels, distinguent des lois d'application directe, mais elles ne donnent pas toujours ce statut aux mêmes textes. Dans le baromètre, une loi est classée directe lorsque son échéancier ne comporte aucune mesure autre que «&nbsp;sans objet&nbsp;»&nbsp;; le Sénat applique ses propres règles de classement. Rapprochées loi par loi sur les {{< app-val "nlois" >}} lois promulguées de 2017-2018 à 2024-2025, hors {{< app-val "conventions" >}} conventions internationales, elles retiennent exactement le même champ, mais classent différemment {{< app-val "ndesacc" >}} lois.

{{< figure-svg fichier="appliquer-lois" alt="Barres horizontales, une par session : lois d'application directe pour les deux sources, lois classées différemment, lois qui appellent des mesures ; un trait marque la moitié des lois de chaque session. En 2018-2019, les lois directes et divergentes dépassent la moitié. Les valeurs sont dans le tableau sous la figure." >}}Lois promulguées de chaque session, hors conventions. En bleu, les lois d'application directe pour les deux sources&nbsp;; en gris foncé, celles qu'elles classent différemment&nbsp;; le trait noir marque la moitié des lois de la session.{{< /figure-svg >}}

{{< fig-actions id="lois" >}}

{{< app-tableau "lois" "Les valeurs de la figure en tableau" >}}

La proposition «&nbsp;moins de la moitié des lois dans chaque session&nbsp;» ne tient pas sur les {{< app-val "nsessions" >}} sessions&nbsp;: en {{< app-val "ct_session" >}}, le baromètre compte {{< app-val "ct_baro" >}} lois d'application directe sur {{< app-val "ct_N" >}}, plus de la moitié, quand le Sénat en compte {{< app-val "ct_senat" >}}. Dans les {{< app-val "nautres" >}} autres sessions, même la borne haute reste inférieure à la moitié.

L'écart de 2024-2025 se lit dans un même rapport du Sénat. Sa synthèse écrit&nbsp;: «&nbsp;{{< app-val "cit_802_22" >}}&nbsp;»&nbsp;; une autre page indique que «&nbsp;{{< app-val "cit_802_24" >}}&nbsp;». Le baromètre en compte {{< app-val "s25_baro" >}}. L'écart entre {{< app-val "s25_baro" >}} et {{< app-val "s25_senat" >}} s'explique loi par loi par des règles de classement différentes&nbsp;; celui entre {{< app-val "s25_senat" >}} et {{< app-val "s25_publie" >}} ne s'explique pas, faute de liste nominative.

<details class="repli"><summary>Pourquoi les deux sources divergent sur {{< app-val "ndesacc" >}} lois</summary>

Le baromètre classe une loi «&nbsp;d'application directe&nbsp;» quand son échéancier ne comporte aucune mesure autre que «&nbsp;sans objet&nbsp;». Le Sénat la classe dans ses annexes. Plusieurs règles expliquent une partie des écarts&nbsp;: le Sénat écarte, certaines années, les mesures dont la loi laisse la prise facultative&nbsp;; le baromètre classe «&nbsp;directe&nbsp;» une loi dont toutes les mesures sont aujourd'hui indiquées sans objet&nbsp;; il classe «&nbsp;non directe&nbsp;» une loi sans échéancier. Appliquées ensemble, ces règles font disparaître une partie des écarts et en font apparaître d'autres&nbsp;: elles ne sont pas appliquées uniformément d'une année à l'autre. Toutes les lois en écart sont comptées comme incertaines, même quand une règle les explique&nbsp;; d'où les bornes du tableau.

Des défauts des annexes du Sénat, comme un numéro de loi erroné ou un effectif annoncé qui ne correspond pas à la liste qui le suit, ont été corrigés par le titre et la date de la loi&nbsp;; le registre loi par loi les signale.

</details>

## Pourquoi le Sénat et le Gouvernement publient-ils des taux différents&nbsp;? {#taux-publies}

Parce que leurs conventions de calcul diffèrent. Pour les sessions 2017-2018 et 2018-2019, les rapports du Sénat publient son taux et rapportent un taux différent calculé par le Secrétariat général du Gouvernement. Pour 2017-2018, le Sénat écrit&nbsp;: «&nbsp;{{< app-val "cit_senat_1718" >}}&nbsp;». Le Secrétariat général du Gouvernement, entendu par le Sénat, rapporte pour sa part que «&nbsp;{{< app-val "cit_sgg_1718" >}}&nbsp;». Pour la session 2018-2019, le Sénat écrit&nbsp;: «&nbsp;{{< app-val "cit_senat_1819" >}}&nbsp;», et ajoute que «&nbsp;{{< app-val "cit_sgg_1819" >}}&nbsp;».

Le Sénat donne lui-même les raisons de l'écart&nbsp;: «&nbsp;{{< app-val "cit_diverge" >}}&nbsp;» D'une part, «&nbsp;{{< app-val "cit_arretes" >}}&nbsp;» D'autre part, «&nbsp;{{< app-val "cit_differees" >}}&nbsp;» Le Sénat mentionne aussi un troisième motif, qu'il qualifie lui-même de raisons politiques&nbsp;: «&nbsp;{{< app-val "cit_politique" >}}&nbsp;» Un taux peut ainsi intégrer une appréciation, et non seulement un comptage.

Un taux d'application n'est donc interprétable qu'avec son périmètre, sa date d'arrêté et ses règles de comptage. Le bilan semestriel du Gouvernement suit les lois par législature et non par session&nbsp;: au 31&nbsp;décembre 2025, il suit, pour la XVI<sup>e</sup>&nbsp;législature, les lois qui «&nbsp;{{< app-val "cit_sgg16_def" >}}&nbsp;», et pour la XVII<sup>e</sup>, celles qui «&nbsp;{{< app-val "cit_sgg17_def" >}}&nbsp;» Dans les cas documentés ici, le Sénat et le Secrétariat général du Gouvernement ne mesurent pas exactement le même objet&nbsp;; leurs niveaux ne sont donc pas directement comparables sans harmoniser ces conventions.

## Le taux d'application des lois a-t-il progressé depuis 2002&nbsp;? {#serie-senat}

La série du Sénat ne permet pas de le dire d'un bout à l'autre. Le corpus fait apparaître {{< app-val "nsegments" >}} définitions successives depuis 2002-2003, qui diffèrent par la date d'arrêté, le champ des lois et le traitement des mesures différées et éventuelles&nbsp;: les segments ne se lisent pas comme une seule série.

{{< figure-svg fichier="appliquer-serie" alt="Points par session de 2002-2003 à 2024-2025, regroupés en segments séparés par des ruptures de définition. Le premier segment, de 2002-2003 à 2008-2009, se situe nettement plus bas que les suivants. Les valeurs, leur document et leur définition sont dans le tableau sous la figure." >}}Taux d'application des lois publiés par le Sénat, tels que publiés. Les segments correspondent à des définitions différentes&nbsp;: ne pas les relier. Le cercle vide marque la valeur de 2019-2020 reprise à la baisse dans le rapport suivant.{{< /figure-svg >}}

{{< fig-actions id="serie" >}}

{{< app-tableau "serie" "Les valeurs, leur document et leur définition" >}}

Le dernier point du premier segment et le premier point retenu du suivant sont séparés par une rupture de définition, que le Sénat décrit ainsi&nbsp;: «&nbsp;{{< app-val "cit_six_mois" >}}&nbsp;» En 2024-2025, il publie un seul taux («&nbsp;{{< app-val "cit_802_66" >}}&nbsp;»), et précise en note&nbsp;: «&nbsp;{{< app-val "cit_802_note" >}}&nbsp;» Les mesures éventuelles sont celles que la loi permet de prendre sans l'imposer. La session 2009-2010 n'est pas retenue sur la figure, faute de date d'arrêté établie dans la phrase qui donne son taux. Une révision de chiffre, comme celle de 2019-2020, et une rupture de définition sont deux faits distincts&nbsp;: la série les garde tous les deux.

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas si une loi produit l'effet que visait la promesse&nbsp;: un décret publié n'est pas un résultat obtenu. Elle ne mesure pas la qualité des décrets, ni leur conformité à la volonté du législateur, que le Sénat apprécie lui-même. Elle ne donne aucun délai moyen de publication, faute d'historique daté des échéanciers. Elle ne compare pas les taux du Sénat et du Gouvernement entre eux, ni deux segments de la série du Sénat.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Après le vote" avis="non" >}}
Cette page compte ce qu'une loi attend encore après son vote. Le livre suit neuf promesses écrites, datées et signées, le long de la chaîne qui va de la décision à son résultat&nbsp;: ce qu'un président décide dans sa propre chaîne de pouvoir, ce qu'il doit faire voter, ce qu'il doit négocier, et ce qui ne dépendra jamais de lui. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Baromètre de l'application des lois**, Assemblée nationale et LexImpact, à partir des échéanciers de la DILA&nbsp;: fichiers des lois et des mesures, version du {{< app-val "releve" >}}.

**Sénat**, rapports annuels sur l'application des lois de 2011 à 2026, synthèses et communiqués de 2003 à 2011&nbsp;; le document et la page de chaque valeur et de chaque citation sont donnés dans le jeu de données.

**Secrétariat général du Gouvernement**, bilan semestriel de l'application des lois au 31&nbsp;décembre 2025, lu sur Légifrance.

**Constitution**, art.&nbsp;10 et 61, et **code civil**, art.&nbsp;1er, lus sur Légifrance (API).

Les chiffres, les citations, les contrôles et les figures sont produits par un script unique&nbsp;; chaque citation est vérifiée mot pour mot dans la page du document dont elle est tirée, et aucun chiffre de cette page n'est saisi à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_appliquer.csv), en format long&nbsp;; [JSON](/promesses_appliquer.json), avec les définitions et le compte rendu des contrôles.

{{< reutiliser figures="figures_appliquer" jeu="promesses_appliquer" sources="Assemblée nationale et LexImpact (données DILA), Sénat, SGG, Légifrance" donnees="L'état des mesures d'application par session de la loi, les lois d'application directe selon les deux sources et les taux publiés par le Sénat depuis 2002-2003 ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Au {{< app-val "releve" >}}, sur les {{< app-val "nmes" >}} mesures d'application recensées pour les lois promulguées d'octobre 2017 à septembre 2025, {{< app-val "A" >}} sont en attente. Pour deux sessions, les rapports du Sénat publient son taux d'application et rapportent un taux différent calculé par le Secrétariat général du Gouvernement, selon d'autres conventions de calcul&nbsp;; la série du Sénat repose sur {{< app-val "nsegments" >}} définitions successives depuis 2002-2003.
{{< /reutiliser >}}
