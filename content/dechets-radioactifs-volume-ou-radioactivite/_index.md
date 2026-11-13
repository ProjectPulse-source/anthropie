---
title: "Déchets radioactifs : le volume dit-il le problème ?"
description: "Fin {dr.an_act}, les déchets de haute activité faisaient {dr.ha_vol_a} % du volume des déchets radioactifs recensés dans les bilans de l'Andra et {dr.ha_act} % de la radioactivité déclarée (pour l'essentiel un maximum, non une mesure exacte) ; leur stockage définitif, prévu à Bure (Cigéo), n'a pas encore reçu son autorisation de création. Volume, radioactivité et filière de stockage, catégorie par catégorie (Andra, données ouvertes et Les Essentiels 2026)."
chapo: "En France, les déchets radioactifs se comptent d'abord en mètres cubes : {dr.tot5} million fin {dr.an_vol} dans les bilans de l'Andra. Mais le volume ne dit ni où est la radioactivité, ni ce qui reste sans solution. Fin {dr.an_act}, les déchets de haute activité faisaient {dr.ha_vol_a} % du volume et {dr.ha_act} % de la radioactivité déclarée (pour l'essentiel un maximum, non une mesure exacte) ; leur stockage définitif est prévu à Bure, dans le centre Cigéo, qui n'a pas encore reçu son autorisation de création."
date: 2026-10-26
lastmod: 2026-11-13
journal:  # révisions qui changent la lecture de la page
  - {date: 2026-11-13, texte: "Correction : une explication de l'absence de filière par des contraintes de gestion, non établie pour ce constat, est retirée ; Cigéo, déclaré d'utilité publique en 2022, « n'a pas encore reçu son autorisation de création » au lieu de « n'est pas encore autorisé »."}
  - {date: 2026-11-12, texte: "Reprise : la radioactivité déclarée, pour l'essentiel un maximum, dite à côté de chaque part et documentée dans le fichier de données et la figure ; le centre de la Manche en phase de fermeture, non en surveillance ; deux classements qui ne mesurent à eux seuls ni les doses, ni la durée de danger, ni le coût ; Malvési rapproché des volumes que publie l'Andra ; volumes hors bilans comptés en tonnes, non additionnés aux mètres cubes ; état de Cigéo vérifié au 12 novembre 2026."}
og_title: "Déchets radioactifs : le volume dit-il le problème ? — S. Lalut"
og_image: "images/og-dechets-radioactifs.jpg"
og_image_alt: "Carte de partage : « Le volume ne dit pas où est la radioactivité » — part du volume et de la radioactivité déclarée (pour l'essentiel un maximum) des déchets de haute activité, et des déchets à vie courte et de très faible activité, fin 2021 (Andra, Inventaire national)."
# Page née de l'arbitrage PRO-20261026-033434 (graphe G3 reconçu, page de faits distincte de la notion de communs négatifs).
# Fiche : docs/conception/dechets-radioactifs-volume-ou-radioactivite.md. Aucun chiffre saisi : jetons {dr.*} et shortcode
# dr-val (scripts/update_dechets_radioactifs.py, fichiers ouverts de l'Andra) ; état des filières transcrit et déclaré.
donnees: [dechets_radioactifs]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dechets_radioactifs"
  apropos: "déchets radioactifs en France : volume et radioactivité"
  nom: "Déchets radioactifs en France : volume et radioactivité déclarée par catégorie, volume situé dans les centres de l'Andra (Inventaire national de l'Andra)"
  description: "Volumes en équivalent conditionné et activité déclarée des déchets radioactifs, par catégorie (HA, MA-VL, FA-VL, FMA-VC, TFA, DSF, VTC, hors bilans), pour chaque fichier annuel ouvert de l'Inventaire national de l'Andra (fin 2013 à fin {dr.an_vol}), avec, pour les FMA-VC et les TFA, les volumes situés dans les centres de l'Andra ; parts calculées par l'auteur."
  couverture_temporelle: "2013/{dr.an_vol}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Volume de déchets radioactifs", unite: "m³ en équivalent conditionné", description: "par catégorie et par année"}
    - {nom: "Activité déclarée", unite: "becquerels", description: "par catégorie, années d'édition de l'inventaire"}
    - {nom: "Volume dans un centre de stockage de l'Andra", unite: "m³", description: "FMA-VC et TFA"}
  sources:
    - "https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs"
    - "https://inventaire.andra.fr/"
  mots: ["déchets radioactifs", "déchets nucléaires", "haute activité", "Cigéo", "Andra", "Inventaire national", "radioactivité", "stockage", "Malvési", "Cires", "Centre de stockage de l'Aube"]
  fichiers: ["dechets_radioactifs.csv", "dechets_radioactifs.json"]
faq:
  - question: "Quelle part du volume des déchets radioactifs représentent les déchets de haute activité ?"
    answer: "Fin {dr.an_act}, dernière édition de l'inventaire qui déclare la radioactivité, les déchets de haute activité représentaient {dr.ha_vol_a} % du volume des cinq catégories des bilans de l'Andra et {dr.ha_act} % de la radioactivité déclarée (pour l'essentiel un maximum, non une mesure exacte). Fin {dr.an_vol}, ils occupent {dr.ha_m3} m³ en équivalent conditionné, {dr.ha_vol} % du volume."
  - question: "Les déchets radioactifs les plus actifs sont-ils stockés ?"
    answer: "Non : ils sont entreposés, c'est-à-dire placés à titre temporaire avec l'intention de les retirer, et non stockés, mot que la loi réserve à une conservation potentiellement définitive (code de l'environnement, art. L. 542-1-1). Les déchets de haute activité et de moyenne activité à vie longue, qui concentrent {dr.ha_mavl_act} % de la radioactivité déclarée (fin {dr.an_act}), sont entreposés sur les sites qui les produisent ou les détiennent : leur stockage géologique profond, Cigéo, est prévu à Bure ; après l'enquête publique de 2026 et l'avis favorable de la commission d'enquête, assorti de deux réserves, aucun décret d'autorisation de création n'avait été publié au 12 novembre 2026. Les déchets de faible et moyenne activité à vie courte et de très faible activité, plus de neuf dixièmes du volume, ont des stockages en service."
  - question: "D'où viennent ces chiffres ?"
    answer: "Des fichiers ouverts de l'Inventaire national de l'Andra (déchets déclarés à fin {dr.an_vol}, et à fin {dr.an_act} pour l'activité), lus par un script qui s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases de la page. L'état des filières et les volumes de Malvési sont transcrits des publications de l'Andra (Les Essentiels 2026, lus le 26 octobre 2026). Les données sont téléchargeables en CSV et en JSON, sous licence CC BY 4.0."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/dechets-radioactifs-volume-ou-radioactivite.md"  # fiche de conception (regle 12)
  refonte: "2026-11-12"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 45
  nature: "Données ouvertes recalculées (Andra, Inventaire national)"
reperes:  # trois repères sous le chapô, à partir de 600 px de large (partials/reperes-page.html ; règle 17 du site,
  # reprise du style du 13/11/2026, test du premier écran). Chacun reprend un résultat écrit dans sa section, avec sa
  # période et sa réserve, à son contact. Aucun nombre saisi : jetons {dr.*} (scripts/update_dechets_radioactifs.py).
  - ancre: "volume-radioactivite"
    fort: "{dr.ha_act} %"
    texte: "de la radioactivité déclarée (pour l'essentiel un maximum, non une mesure exacte) dans {dr.ha_vol_a} % du volume : les déchets de haute activité des bilans de l'Andra, fin {dr.an_act}"
  - ancre: "volume-radioactivite"
    fort: "{dr.masse_act} %"
    texte: "de la radioactivité déclarée dans plus de neuf dixièmes du volume, fin {dr.an_act} : les déchets de faible et moyenne activité à vie courte et de très faible activité"
  - ancre: "stockage"
    fort: "Cigéo"
    texte: "n'a pas encore reçu son autorisation de création : le centre de stockage prévu à Bure pour les déchets de haute activité et de moyenne activité à vie longue"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données mises à jour le {{< dr-val "date_donnees" >}}</span> Andra, Inventaire national des matières et déchets radioactifs, fichiers ouverts (data.gouv.fr)&nbsp;: volume et radioactivité déclarée à fin {{< dr-val "an_act" >}} (dernière édition qui déclare la radioactivité), volumes à fin {{< dr-val "an_vol" >}}. Télécharger&nbsp;: <a href="/dechets_radioactifs.csv">CSV</a> · <a href="/dechets_radioactifs.json">JSON</a></p>

## Où est la radioactivité&nbsp;? {#volume-radioactivite}

Fin {{< dr-val "an_act" >}}, dernière année où l'inventaire de l'Andra déclare la radioactivité de chaque catégorie, la France comptait {{< dr-val "tot5_a" >}}&nbsp;million de mètres cubes de déchets radioactifs dans les cinq catégories des bilans de l'Andra, en équivalent conditionné. Plus de neuf dixièmes de ce volume ({{< dr-val "masse_vol_a" >}}&nbsp;%) étaient des déchets de faible et moyenne activité à vie courte et de très faible activité&nbsp;: ils portaient {{< dr-val "masse_act" >}}&nbsp;% de la radioactivité déclarée. Les déchets de haute activité, eux, faisaient {{< dr-val "ha_vol_a" >}}&nbsp;% du volume, quelques millièmes, et {{< dr-val "ha_act" >}}&nbsp;% de la radioactivité déclarée (pour l'essentiel un maximum, non une mesure exacte)&nbsp;; avec les déchets de moyenne activité à vie longue, {{< dr-val "ha_mavl_act" >}}&nbsp;%.

Les catégories qui concentrent l'essentiel de la radioactivité déclarée ne sont donc pas celles qui occupent le plus de volume, et elles ne relèvent pas des mêmes filières de gestion. Leur radioactivité ne mesure pas, à elle seule, leur dangerosité ni le risque auquel la population est exposée.

<div class="figure-lecture">
<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/dechets-volume-activite-m.svg" width="300" height="1045">
    <img src="/img/dechets-volume-activite.svg" alt="Pour chacune des cinq catégories de déchets radioactifs des bilans de l'Andra, part du volume et part de la radioactivité déclarée (pour l'essentiel un maximum), fin {{< dr-val "an_act" >}}, et filière de stockage. Haute activité : {{< dr-val "vol_ha" >}} % du volume, {{< dr-val "act_ha" >}} % de la radioactivité, stockage géologique profond en projet. Moyenne activité à vie longue : {{< dr-val "vol_mavl" >}} %, {{< dr-val "act_mavl" >}} %, même projet. Faible activité à vie longue : {{< dr-val "vol_favl" >}} %, {{< dr-val "act_favl" >}} %, stockage à l'étude. Faible et moyenne activité à vie courte : {{< dr-val "vol_fmavc" >}} %, {{< dr-val "act_fmavc" >}} %, stockage en service. Très faible activité : {{< dr-val "vol_tfa" >}} %, {{< dr-val "act_tfa" >}} %, stockage en service." width="720" height="425" loading="lazy">
  </picture>
  <figcaption>Volume en équivalent conditionné et radioactivité déclarée, en becquerels, la même année&nbsp;; filières selon l'Andra (Inventaire national, données ouvertes&nbsp;; Les Essentiels 2026).</figcaption>
</figure>
<div class="figure-lecture__texte">
<div class="resultat-phrase">

**Le résultat en une phrase.** En France, fin {{< dr-val "an_act" >}}, les déchets de haute activité faisaient {{< dr-val "ha_vol_a" >}}&nbsp;% du volume des déchets radioactifs recensés dans les bilans de l'Andra et {{< dr-val "ha_act" >}}&nbsp;% de la radioactivité déclarée (pour l'essentiel un maximum, non une mesure exacte)&nbsp;; leur stockage définitif, prévu à Bure (Cigéo), n'a pas encore reçu son autorisation de création.

</div>
</div>
</div>

Depuis, le volume a continué de croître&nbsp;: {{< dr-val "tot5" >}}&nbsp;million de mètres cubes fin {{< dr-val "an_vol" >}}, dont {{< dr-val "ha_m3" >}}&nbsp;m³ de haute activité, toujours {{< dr-val "ha_vol" >}}&nbsp;% du total. La radioactivité, elle, n'est déclarée, pour l'essentiel du volume, que dans les fichiers des éditions de l'inventaire, la dernière à fin {{< dr-val "an_act" >}}.

## Ce que le graphe montre, et ce qu'il ne montre pas {#lecture}

Deux classements donnent des hiérarchies très différentes, et le graphe les place côte à côte&nbsp;: en volume, les déchets à vie courte et de très faible activité dominent&nbsp;; en radioactivité déclarée, la haute activité. Mais ni l'un ni l'autre ne mesure, à lui seul, les doses auxquelles une population peut être exposée, la durée pendant laquelle les déchets restent dangereux ou le coût des solutions de gestion.

Le graphe montre aussi que la haute activité et les deux catégories à vie longue (moyenne et faible activité) n'ont pas encore de filière de stockage définitif en exploitation, y compris la faible activité à vie longue, qui ne porte que {{< dr-val "act_favl" >}}&nbsp;% de la radioactivité déclarée. Ce constat ne permet pas d'attribuer cette absence de filière à la seule durée de vie.

La radioactivité de chaque catégorie figure dans {{< dr-val "nb_editions" >}} fichiers ({{< dr-val "editions" >}})&nbsp;: déclarée chaque année jusqu'aux données de fin 2016, elle ne l'est plus, depuis, pour l'essentiel du volume, qu'aux éditions de l'inventaire&nbsp;; les fichiers des autres années n'en donnent que pour moins d'un millième du volume. Dans chacun de ces cinq fichiers, la haute activité représente entre {{< dr-val "ha_ed_bas" >}} et {{< dr-val "ha_ed_haut" >}}&nbsp;% de la radioactivité recensée dans les cinq catégories des bilans, et la haute activité avec la moyenne activité à vie longue, au moins {{< dr-val "ha_mavl_ed_bas" >}}&nbsp;%. Les données disponibles ne permettent pas, sans harmonisation supplémentaire, de lire ces parts comme une évolution, ni d'expliquer la variation d'une édition à l'autre.

Une partie des volumes n'a pas de radioactivité déclarée&nbsp;; si l'on suppose que ces volumes ont l'activité moyenne de leur catégorie, hypothèse non vérifiée, la part de la haute activité serait de {{< dr-val "ha_act_aj" >}}&nbsp;%.

**Ce que le graphe ne montre pas.** Le becquerel mesure un nombre de désintégrations par seconde. Il ne mesure directement ni la dose reçue, ni la toxicité d'un radionucléide, ni le risque sanitaire, ni la difficulté ou le coût de gestion. Le graphe montre comment se répartit la radioactivité déclarée entre les catégories&nbsp;; il ne classe ni les risques ni les coûts.

## Où sont ces déchets aujourd'hui&nbsp;? {#stockage}

Fin {{< dr-val "an_vol" >}}, {{< dr-val "stocke_fmavc" >}}&nbsp;% du volume des déchets de faible et moyenne activité à vie courte est recensé dans les centres de stockage de l'Andra&nbsp;: dans celui de l'Aube, en service, et dans celui de la Manche, qui ne reçoit plus de déchets depuis 1994 et est en phase de fermeture. Au Cires, dans l'Aube, se trouvent {{< dr-val "stocke_tfa" >}}&nbsp;% des déchets de très faible activité.

Les catégories qui concentrent la radioactivité n'ont pas encore de stockage définitif. Selon l'Andra, des déchets de haute activité et de moyenne activité à vie longue sont «&nbsp;produits et entreposés sur leurs sites de production, en attendant la création du centre de stockage destiné à les accueillir&nbsp;: Cigéo&nbsp;»&nbsp;; le stockage des déchets de faible activité à vie longue est à l'étude.

Cigéo est un centre de stockage en couche géologique profonde prévu à Bure (Meuse). Il a été déclaré d'utilité publique par un décret du 7&nbsp;juillet 2022 (n°&nbsp;2022-993)&nbsp;; son autorisation de création relève d'une autre procédure.

<div class="fiche-etapes">
<p class="surtitre-bloc">La procédure d'autorisation de création de Cigéo</p>
<ol>
<li><span class="fiche-etapes__n">Étape&nbsp;1</span> <span>Janvier 2023&nbsp;: l'Andra demande l'autorisation de création</span></li>
<li><span class="fiche-etapes__n">Étape&nbsp;2</span> <span>16&nbsp;juillet 2026&nbsp;: l'enquête publique se clôt</span></li>
<li><span class="fiche-etapes__n">Étape&nbsp;3</span> <span>Août 2026&nbsp;: la commission d'enquête rend un avis favorable, assorti de deux réserves et de deux recommandations&nbsp;; cet avis ne vaut pas autorisation</span></li>
<li><span class="fiche-etapes__n">Ensuite</span> <span>La procédure prévoit un avant-projet de décret transmis à l'Andra pour observations, un avis de l'Autorité de sûreté nucléaire et de radioprotection, puis un décret pris après avis du Conseil d'État</span></li>
</ol>
</div>

Au 12&nbsp;novembre 2026, aucun décret d'autorisation de création n'avait été publié au Journal officiel.

## Ce qui reste hors des bilans {#hors-bilans}

Certains déchets ne figurent pas dans les bilans de l'Andra. Parmi eux se trouvent les résidus historiques de conversion de l'uranium du site d'Orano à Malvési&nbsp;: l'Andra en publie environ {{< dr-val "malvesi" >}}&nbsp;m³ (installation ECRIN, bassins d'évaporation et de décantation), précise que ces volumes «&nbsp;ne sont pas comptabilisés dans les bilans&nbsp;» et que «&nbsp;la recherche d'une filière sûre de gestion à long terme sur le site de Malvési est en cours&nbsp;».

Restent aussi hors des bilans, notamment, les résidus du traitement des minerais d'uranium des anciens sites miniers et des déchets à radioactivité naturelle élevée&nbsp;: l'Andra les compte en tonnes (des dizaines de millions), et ils ne s'additionnent donc pas à ces mètres cubes. Des stockages historiques, qui relèvent de leurs détenteurs, en sont également absents.

## Ce que ces données ne disent pas {#limites}

- **La radioactivité n'est ni le risque ni le coût.** Elle mesure un nombre de désintégrations par seconde&nbsp;; le danger dépend des radionucléides, de leur période et de l'exposition.
- **Une radioactivité déclarée, pour l'essentiel un maximum.** Dans le fichier de fin {{< dr-val "an_act" >}}, {{< dr-val "maj_5" >}}&nbsp;% de la radioactivité déclarée des cinq catégories ({{< dr-val "maj_ha" >}}&nbsp;% pour la haute activité) porte le signe «&nbsp;&lt;&nbsp;», qui signale, selon le dictionnaire de données de l'inventaire, une activité majorante&nbsp;: une valeur maximale, non une mesure exacte. Les parts de la page sont des parts de ces valeurs déclarées&nbsp;; le fichier de données donne, par catégorie et par année, l'activité déclarée et sa part majorante.
- **Un millésime pour la comparaison.** Volume et radioactivité sont comparés à fin {{< dr-val "an_act" >}}, dernière édition qui déclare la radioactivité&nbsp;; les volumes de fin {{< dr-val "an_vol" >}} sont donnés à part, sans radioactivité.
- **Des volumes sans radioactivité déclarée.** La variante qui leur attribue l'activité moyenne de leur catégorie repose sur une hypothèse&nbsp;: elle teste la sensibilité du résultat, elle ne le valide pas.
- **Un périmètre hors bilans non réconcilié.** Depuis le fichier de fin {{< dr-val "an_hors" >}}, le fichier ouvert classe hors des catégories des bilans un volume qui atteint {{< dr-val "hors" >}}&nbsp;million de mètres cubes à fin {{< dr-val "an_vol" >}}&nbsp;; sa famille des résidus de conversion de l'uranium ({{< dr-val "rtcu" >}}&nbsp;million de m³) comprend, en plus des volumes que l'Andra publie pour Malvési, une ligne de stériles d'une ancienne mine de soufre, que l'Andra ne compte pas dans ces volumes. Ce total n'est pas interprété ici.
- **Les déchets, pas les matières.** Les matières radioactives (uranium appauvri, combustibles usés en attente de traitement) ne sont pas des déchets au sens de la loi, sauf si l'autorité administrative les requalifie en déchets (code de l'environnement, art.&nbsp;L.&nbsp;542-1-1 et L.&nbsp;542-13-2), et ne figurent pas dans ces chiffres.
- **L'état des filières et de Cigéo est repris de sources publiées.** Il n'est pas calculé par le script de lecture des données&nbsp;: celui des filières est lu dans *Les Essentiels 2026* de l'Andra, celui de Cigéo a été vérifié le 12&nbsp;novembre 2026 sur Légifrance (Journal officiel) et sur la page de la préfecture de la Meuse.

<aside class="encadre">

**Une lecture de l'auteur, non testée ici.** La philosophie de l'écologie du démantèlement appelle [communs négatifs](/communs-negatifs/) ce dont une société hérite sans l'avoir choisi&nbsp;: déchets, sols pollués, infrastructures à refermer. L'économiste Stéphane Lalut y lit un désordre déplacé devenu héritage matériel. Les chiffres de cette page décrivent un tel héritage&nbsp;; ils ne démontrent pas cette lecture.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="Pour prolonger la question" avis="non" >}}
*ANTHROPIE — Ordre ici. Dette ailleurs* suit, sur la longue durée, ce que laisse derrière lui chaque ordre construit, et à qui il en laisse la charge.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

- Andra, Inventaire national des matières et déchets radioactifs, [fichiers ouverts des déchets déclarés](https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs) (fin 2013 à fin {{< dr-val "an_vol" >}}), lus par script&nbsp;; calculs de l'auteur&nbsp;: parts par catégorie, variante d'activité, volumes situés dans les centres de stockage de l'Andra (repérés par le nom du site).
- Andra, [Inventaire national](https://inventaire.andra.fr/), *Les Essentiels 2026* et page «&nbsp;Classification des déchets radioactifs et filières de gestion&nbsp;»&nbsp;: état des filières, volumes de Malvési et citations, lus le 26&nbsp;octobre 2026. Témoin du calcul&nbsp;: les volumes par catégorie publiés par l'Andra pour fin 2024 sont retrouvés à l'arrondi près&nbsp;; les volumes stockés, à quelques centaines de mètres cubes près, le script comptant ce qui est situé dans un centre de l'Andra.
- Autorité de sûreté nucléaire et de radioprotection, [lettre du 30&nbsp;mars 2026](https://reglementation-controle.asnr.fr/Media/Files/demande-d-autorisation-de-creation-de-l-installation-nucleaire-de-base-cigeo) (CODEP-DRC-2026-012666)&nbsp;: demande d'autorisation de Cigéo. Préfecture de la Haute-Marne, [page de l'enquête publique](https://www.haute-marne.gouv.fr/index.php/Actions-de-l-Etat/CIGEO/Demande-d-autorisation-de-creation-de-Cigeo), lue le 26&nbsp;octobre 2026&nbsp;: dates de l'enquête (18&nbsp;mai au 16&nbsp;juillet 2026, après prolongation), avis favorable de la commission assorti de deux réserves et de deux recommandations, rapport en ligne depuis le 14&nbsp;septembre 2026, décision par décret en Conseil d'État à venir. Légifrance, recherche «&nbsp;Cigéo&nbsp;» au Journal officiel, et préfecture de la Meuse, [page de la demande d'autorisation de création](https://www.meuse.gouv.fr/Actions-de-l-Etat/CIGEO/Demande-d-autorisation-de-creation-de-Cigeo), consultées le 12&nbsp;novembre 2026&nbsp;: aucun décret d'autorisation publié, aucune étape de la procédure après le 14&nbsp;septembre 2026. Dépêche AFP du 14&nbsp;septembre 2026, [reprise par Connaissance des énergies](https://www.connaissancedesenergies.org/afp/dechets-nucleaires-avis-favorable-de-la-commission-denquete-pour-cigeo-260914)&nbsp;: clôture de l'enquête publique et avis de la commission.

{{< reutiliser figures="figures_dechets" jeu="dechets_radioactifs" sources="Andra, Inventaire national" donnees="Dans le CSV, au format long, pour chaque fichier annuel de l'Inventaire national depuis fin 2013 : volume en équivalent conditionné et activité déclarée par catégorie, volume avec activité déclarée, activité déclarée majorante et, pour les déchets de faible et moyenne activité à vie courte (FMA-VC) et de très faible activité (TFA), volume situé dans un centre de l'Andra (non repéré pour 2013, 2014 et 2023) ; le JSON donne les parts calculées, dont celles que trace la figure (volume et radioactivité déclarée, la même année)." >}}
En France, fin {{< dr-val "an_act" >}}, les déchets de haute activité faisaient {{< dr-val "ha_vol_a" >}} % du volume des déchets radioactifs recensés dans les bilans de l'Andra et {{< dr-val "ha_act" >}} % de la radioactivité déclarée (pour l'essentiel un maximum, non une mesure exacte). La haute activité et les deux catégories à vie longue (moyenne et faible activité) n'ont pas encore de filière de stockage définitif en exploitation&nbsp;: le stockage de la haute activité et de la moyenne activité à vie longue est prévu à Bure, dans le centre Cigéo, qui n'a pas encore reçu son autorisation de création. Le volume, lui, est porté pour l'essentiel par des catégories qui ont un stockage en service.
{{< /reutiliser >}}
