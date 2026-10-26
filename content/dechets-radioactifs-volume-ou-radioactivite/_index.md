---
title: "Déchets radioactifs : le volume dit-il le problème ?"
description: "Fin {dr.an_act}, les déchets de haute activité faisaient {dr.ha_vol_a} % du volume des déchets radioactifs français et {dr.ha_act} % de leur radioactivité déclarée ; leur stockage définitif, prévu à Bure (Cigéo), n'est pas encore autorisé. Volume, radioactivité et filière de stockage, catégorie par catégorie (Andra, données ouvertes)."
chapo: "Les déchets radioactifs se comptent d'abord en mètres cubes : {dr.tot5} million fin {dr.an_vol}. Mais le volume ne dit ni où est la radioactivité, ni ce qui reste sans solution. Fin {dr.an_act}, les déchets de haute activité faisaient {dr.ha_vol_a} % du volume et {dr.ha_act} % de la radioactivité déclarée ; leur stockage définitif est prévu à Bure (Cigéo), mais pas encore autorisé."
date: 2026-10-26
lastmod: 2026-10-26
og_title: "Déchets radioactifs : le volume dit-il le problème ? — S. Lalut"
og_image: "images/og-dechets-radioactifs.jpg"
og_image_alt: "Carte de partage : « Le volume ne dit pas où est la radioactivité » — part du volume et de la radioactivité des déchets de haute activité, et des déchets de faible et très faible activité (Andra, Inventaire national)."
# Page née de l'arbitrage PRO-20261026-033434 (graphe G3 reconçu, page de faits distincte de la notion de communs négatifs).
# Fiche : docs/conception/dechets-radioactifs-volume-ou-radioactivite.md. Aucun chiffre saisi : jetons {dr.*} et shortcode
# dr-val (scripts/update_dechets_radioactifs.py, fichiers ouverts de l'Andra) ; état des filières transcrit et déclaré.
donnees: [dechets_radioactifs]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dechets_radioactifs"
  nom: "Déchets radioactifs en France : volume, radioactivité déclarée et localisation par catégorie (Inventaire national de l'Andra)"
  description: "Volumes en équivalent conditionné et activité déclarée des déchets radioactifs, par catégorie (HA, MA-VL, FA-VL, FMA-VC, TFA, VTC, hors bilans), pour chaque fichier annuel ouvert de l'Inventaire national de l'Andra (fin 2013 à fin {dr.an_vol}), avec les volumes situés dans les centres de stockage de l'Andra ; parts calculées par l'auteur."
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
    answer: "Fin {dr.an_act}, dernière édition de l'inventaire qui déclare la radioactivité, les déchets de haute activité représentaient {dr.ha_vol_a} % du volume des cinq catégories des bilans de l'Andra et {dr.ha_act} % de la radioactivité déclarée. Fin {dr.an_vol}, ils occupent {dr.ha_m3} m³ en équivalent conditionné, {dr.ha_vol} % du volume."
  - question: "Les déchets radioactifs les plus actifs sont-ils stockés ?"
    answer: "Pas encore de façon définitive. Les déchets de haute activité et de moyenne activité à vie longue, qui concentrent {dr.ha_mavl_act} % de la radioactivité déclarée (fin {dr.an_act}), sont entreposés sur leurs sites de production : leur stockage géologique profond, Cigéo, est prévu à Bure ; après l'enquête publique de 2026 et l'avis favorable de la commission d'enquête, l'autorisation de création reste à décider. Les déchets de faible et moyenne activité à vie courte et de très faible activité, plus de neuf dixièmes du volume, ont des stockages en service."
  - question: "D'où viennent ces chiffres ?"
    answer: "Des fichiers ouverts de l'Inventaire national de l'Andra (déchets déclarés à fin {dr.an_vol}, et à fin {dr.an_act} pour l'activité), lus par un script qui refuse de publier si une donnée cesse de soutenir une phrase de la page ; l'état des filières vient des publications de l'Andra. Les données sont téléchargeables en CSV et en JSON, sous licence CC BY 4.0."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/dechets-radioactifs-volume-ou-radioactivite.md"  # fiche de conception (regle 12)
  refonte: "2026-10-26"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 45
  nature: "Données ouvertes recalculées (Andra, Inventaire national)"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données du&nbsp;: {{< dr-val "date_donnees" >}}</span> Andra, Inventaire national des matières et déchets radioactifs, fichiers ouverts (data.gouv.fr)&nbsp;: volume et radioactivité déclarée à fin {{< dr-val "an_act" >}} (dernière édition qui déclare la radioactivité), volumes à fin {{< dr-val "an_vol" >}}. Télécharger&nbsp;: <a href="/dechets_radioactifs.csv">CSV</a> · <a href="/dechets_radioactifs.json">JSON</a></p>

## Où est la radioactivité&nbsp;? {#volume-radioactivite}

Fin {{< dr-val "an_act" >}}, dernière année où l'inventaire de l'Andra déclare la radioactivité de chaque catégorie, la France comptait {{< dr-val "tot5_a" >}}&nbsp;million de mètres cubes de déchets radioactifs dans les cinq catégories de ses bilans, en équivalent conditionné. Plus de neuf dixièmes de ce volume ({{< dr-val "masse_vol_a" >}}&nbsp;%) étaient des déchets de faible et moyenne activité à vie courte et de très faible activité&nbsp;: ils portaient {{< dr-val "masse_act" >}}&nbsp;% de la radioactivité déclarée. Les déchets de haute activité, eux, faisaient {{< dr-val "ha_vol_a" >}}&nbsp;% du volume, quelques millièmes, et {{< dr-val "ha_act" >}}&nbsp;% de la radioactivité&nbsp;; avec les déchets de moyenne activité à vie longue, {{< dr-val "ha_mavl_act" >}}&nbsp;%.

Les catégories qui concentrent l'essentiel de la radioactivité déclarée ne sont donc pas celles qui occupent le plus de volume, et elles ne relèvent pas des mêmes filières de gestion. Leur radioactivité ne mesure pas, à elle seule, leur dangerosité ni le risque auquel la population est exposée.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dechets-volume-activite-m.svg" width="300" height="890">
    <img src="/img/dechets-volume-activite.svg" alt="Pour chaque catégorie de déchets radioactifs, part du volume et part de la radioactivité déclarée, fin {{< dr-val "an_act" >}}, et filière de stockage. Haute activité : {{< dr-val "vol_ha" >}} % du volume, {{< dr-val "act_ha" >}} % de la radioactivité, stockage géologique profond en projet. Moyenne activité à vie longue : {{< dr-val "vol_mavl" >}} %, {{< dr-val "act_mavl" >}} %, même projet. Faible activité à vie longue : {{< dr-val "vol_favl" >}} %, {{< dr-val "act_favl" >}} %, stockage à l'étude. Faible et moyenne activité à vie courte : {{< dr-val "vol_fmavc" >}} %, {{< dr-val "act_fmavc" >}} %, stockage en service. Très faible activité : {{< dr-val "vol_tfa" >}} %, {{< dr-val "act_tfa" >}} %, stockage en service." width="720" height="397" loading="lazy">
  </picture>
  <figcaption>Volume en équivalent conditionné et radioactivité déclarée, en becquerels, la même année&nbsp;; filières selon l'Andra (Inventaire national, données ouvertes&nbsp;; Les Essentiels 2026).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** En France, fin {{< dr-val "an_act" >}}, les déchets de haute activité faisaient {{< dr-val "ha_vol_a" >}}&nbsp;% du volume des déchets radioactifs et {{< dr-val "ha_act" >}}&nbsp;% de leur radioactivité déclarée&nbsp;; leur stockage définitif, prévu à Bure (Cigéo), n'est pas encore autorisé.

</div>

Depuis, le volume a continué de croître&nbsp;: {{< dr-val "tot5" >}}&nbsp;million de mètres cubes fin {{< dr-val "an_vol" >}}, dont {{< dr-val "ha_m3" >}}&nbsp;m³ de haute activité, toujours {{< dr-val "ha_vol" >}}&nbsp;% du total. La radioactivité, elle, n'est déclarée qu'aux éditions de l'inventaire.

## Ce que le graphe montre, et ce qu'il ne montre pas {#lecture}

Deux façons de mesurer le problème circulent. La première compte des mètres cubes&nbsp;: plus il y a de déchets, plus le problème est grand. La seconde regarde où se trouve la radioactivité et ce qui reste sans solution. Le graphe montre que les deux mesures donnent des hiérarchies très différentes&nbsp;: en volume, les déchets à vie courte et de très faible activité dominent&nbsp;; en radioactivité, la haute activité.

Il montre aussi que les trois catégories à vie longue (haute activité, moyenne et faible activité à vie longue) n'ont pas encore de filière de stockage définitif en exploitation, y compris la faible activité à vie longue, très peu radioactive. Ce constat reflète des contraintes de gestion liées notamment à la période radioactive, au niveau d'activité et aux propriétés des déchets&nbsp;; il ne permet pas d'attribuer la situation à la seule durée de vie.

L'inventaire déclare la radioactivité à ses éditions&nbsp;: {{< dr-val "nb_editions" >}} fichiers la recensent ({{< dr-val "editions" >}}). Dans chacun, la haute activité représente entre {{< dr-val "ha_ed_bas" >}} et {{< dr-val "ha_ed_haut" >}}&nbsp;% de la radioactivité recensée, et la haute activité avec la moyenne activité à vie longue au moins {{< dr-val "ha_mavl_ed_bas" >}}&nbsp;%. Les données disponibles ne permettent pas, sans harmonisation supplémentaire, d'expliquer la variation d'une édition à l'autre. Une partie des volumes n'a pas de radioactivité déclarée&nbsp;; si l'on suppose qu'ils ont l'activité moyenne de leur catégorie, hypothèse non vérifiée, la part de la haute activité serait de {{< dr-val "ha_act_aj" >}}&nbsp;%.

**Ce que le graphe ne montre pas.** Le becquerel mesure un nombre de désintégrations par seconde. Il ne mesure directement ni la dose reçue, ni la toxicité d'un radionucléide, ni le risque sanitaire, ni la difficulté ou le coût de gestion. Le graphe montre comment se répartit la radioactivité déclarée entre les catégories&nbsp;; il ne classe ni les risques ni les coûts.

## Où sont ces déchets aujourd'hui&nbsp;? {#stockage}

Fin {{< dr-val "an_vol" >}}, {{< dr-val "stocke_fmavc" >}}&nbsp;% du volume des déchets de faible et moyenne activité à vie courte sont recensés dans les centres de stockage de l'Andra&nbsp;: dans l'Aube, en service, et dans la Manche, fermé aux nouvelles réceptions depuis 1994 et placé sous surveillance. {{< dr-val "stocke_tfa" >}}&nbsp;% des déchets de très faible activité sont au Cires, dans l'Aube.

Les catégories qui concentrent la radioactivité n'ont pas encore de stockage définitif. Selon l'Andra, les déchets de haute activité et de moyenne activité à vie longue sont «&nbsp;produits et entreposés sur leurs sites de production, en attendant la création du centre de stockage destiné à les accueillir&nbsp;: Cigéo&nbsp;»&nbsp;; le stockage des déchets de faible activité à vie longue est à l'étude.

Cigéo est un centre de stockage en couche géologique profonde prévu à Bure (Meuse). L'Andra en a demandé l'autorisation de création en janvier 2023. L'enquête publique s'est close le 16&nbsp;juillet 2026, et la commission d'enquête a rendu en août un avis favorable, assorti de deux réserves et de deux recommandations. Un avis d'enquête ne vaut pas autorisation&nbsp;: à la mi-septembre 2026, la décision d'autorisation de création restait à prendre.

## Ce qui reste hors des bilans {#hors-bilans}

Certains déchets ne figurent pas dans les bilans de l'Andra. Le principal ensemble est celui des résidus historiques de conversion de l'uranium du site d'Orano à Malvési&nbsp;: l'Andra en publie environ {{< dr-val "malvesi" >}}&nbsp;m³ (installation ECRIN, bassins d'évaporation et de décantation), précise que ces volumes «&nbsp;ne sont pas comptabilisés dans les bilans&nbsp;» et que «&nbsp;la recherche d'une filière sûre de gestion à long terme sur le site de Malvési est en cours&nbsp;». S'y ajoutent des stockages historiques, qui relèvent de leurs détenteurs.

## Ce que ces données ne disent pas {#limites}

- **La radioactivité n'est ni le risque ni le coût.** Elle mesure une quantité de désintégrations par seconde&nbsp;; le danger dépend des radionucléides, de leur période et de l'exposition.
- **Un millésime pour la comparaison.** Volume et radioactivité sont comparés fin {{< dr-val "an_act" >}}, dernière édition qui déclare la radioactivité&nbsp;; les volumes de fin {{< dr-val "an_vol" >}} sont donnés à part, sans radioactivité.
- **Des volumes sans radioactivité déclarée.** La variante qui leur attribue l'activité moyenne de leur catégorie repose sur une hypothèse&nbsp;: elle teste la sensibilité du résultat, elle ne le valide pas.
- **Un périmètre hors bilans non réconcilié.** Depuis le fichier de fin {{< dr-val "an_hors" >}}, le fichier ouvert classe hors des catégories des bilans un volume qui atteint {{< dr-val "hors" >}}&nbsp;million de mètres cubes à fin {{< dr-val "an_vol" >}}&nbsp;; sa famille «&nbsp;résidus de conversion&nbsp;» ({{< dr-val "rtcu" >}}&nbsp;million de m³) ne se rapproche pas des volumes publiés par l'Andra pour Malvési. Ce total n'est pas interprété ici.
- **Les déchets, pas les matières.** Les matières radioactives (uranium appauvri, combustibles usés en attente de traitement) ne sont pas des déchets au sens de la loi et ne figurent pas dans ces chiffres.
- **L'état des filières et de Cigéo est repris de sources publiées.** Il n'est pas calculé par le script et se vérifie à chaque étape de la procédure.

<aside class="encadre">

**Une lecture de l'auteur, non testée ici.** La philosophie de l'écologie du démantèlement appelle [communs négatifs](/communs-negatifs/) ce dont une société hérite sans l'avoir choisi&nbsp;: déchets, sols pollués, infrastructures à refermer. L'économiste Stéphane Lalut y lit un désordre déplacé devenu héritage matériel. Les chiffres de cette page décrivent un tel héritage&nbsp;; ils ne démontrent pas cette lecture.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="Pour prolonger la question" avis="non" >}}
*ANTHROPIE — Ordre ici. Dette ailleurs* suit, sur la longue durée, ce que chaque ordre construit laisse derrière lui et à qui il en laisse la charge.
{{< /appel-livre >}}

## Sources {#sources}

- Andra, Inventaire national des matières et déchets radioactifs, [fichiers ouverts des déchets déclarés](https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs) (fin 2013 à fin {{< dr-val "an_vol" >}}), lus par script&nbsp;; calculs de l'auteur&nbsp;: parts par catégorie, variante d'activité, volumes situés dans les centres de stockage de l'Andra (repérés par le nom du site).
- Andra, [Inventaire national](https://inventaire.andra.fr/), *Les Essentiels 2026* et page «&nbsp;Classification des déchets radioactifs et filières de gestion&nbsp;»&nbsp;: état des filières, volumes de Malvési et citations, lus le 26&nbsp;octobre 2026. Témoin du calcul&nbsp;: les volumes par catégorie et les volumes stockés publiés par l'Andra pour fin 2024 sont retrouvés à l'arrondi près.
- Autorité de sûreté nucléaire et de radioprotection, [lettre du 30&nbsp;mars 2026](https://reglementation-controle.asnr.fr/Media/Files/demande-d-autorisation-de-creation-de-l-installation-nucleaire-de-base-cigeo) (CODEP-DRC-2026-012666)&nbsp;: demande d'autorisation de Cigéo. Préfecture de la Haute-Marne, [page de l'enquête publique](https://www.haute-marne.gouv.fr/index.php/Actions-de-l-Etat/CIGEO/Demande-d-autorisation-de-creation-de-Cigeo), lue le 26&nbsp;octobre 2026&nbsp;: dates de l'enquête (18&nbsp;mai au 16&nbsp;juillet 2026, après prolongation), avis favorable de la commission assorti de deux réserves et de deux recommandations, rapport en ligne depuis le 14&nbsp;septembre 2026, décision par décret en Conseil d'État à venir. Dépêche AFP du 14&nbsp;septembre 2026, [reprise par Connaissance des énergies](https://www.connaissancedesenergies.org/afp/dechets-nucleaires-avis-favorable-de-la-commission-denquete-pour-cigeo-260914)&nbsp;: clôture de l'enquête publique et avis de la commission.

{{< reutiliser figures="figures_dechets" jeu="dechets_radioactifs" sources="Andra (Inventaire national)" donnees="Pour chaque fichier annuel de l'Inventaire national depuis fin 2013 : volume en équivalent conditionné et activité déclarée par catégorie, volume avec activité déclarée, volume situé dans un centre de stockage de l'Andra ; le même contenu existe en CSV, au format long." >}}
En France, fin {{< dr-val "an_act" >}}, les déchets de haute activité faisaient {{< dr-val "ha_vol_a" >}} % du volume des déchets radioactifs et {{< dr-val "ha_act" >}} % de leur radioactivité déclarée. Les déchets à vie longue n'ont pas encore de filière de stockage définitif en exploitation&nbsp;: celui de la haute activité et de la moyenne activité à vie longue est prévu à Bure (Cigéo), pas encore autorisé. Le volume, lui, est porté pour l'essentiel par des catégories qui ont un stockage en service.
{{< /reutiliser >}}
