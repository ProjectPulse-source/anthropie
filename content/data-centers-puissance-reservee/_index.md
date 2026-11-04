---
title: "Data centers : les gigawatts réservés annoncent-ils la consommation ?"
description: "En novembre 2025, les data centers avaient réservé {dtc.res_nov2025} GW de raccordement auprès de RTE, dont {dtc.st_2030} GW pour une mise en service à partir de 2030 ; ceux raccordés au réseau de RTE ont consommé près de {dtc.rpt_2025} TWh en 2025. Puissance réservée, calendrier, abandons et consommation, d'après les publications de RTE."
chapo: "Le chiffre qui circule est celui des réservations : près de {dtc.res_mai2026} gigawatts en mai 2026, contre environ {dtc.res_fin2024} fin 2024. Mais une puissance réservée n'est pas une consommation. Plus de la moitié de la puissance réservée en novembre 2025 vise une mise en service à partir de 2030, d'autres réservations ont déjà été abandonnées, et les data centers raccordés au réseau de transport ont consommé près de {dtc.rpt_2025} térawattheure en 2025."
date: 2026-10-27
lastmod: 2026-10-27
og_title: "Data centers : les gigawatts réservés annoncent-ils la consommation ? — S. Lalut"
og_image: "images/og-data-centers.jpg"
og_image_alt: "Carte de partage : « Réservé n'est pas consommé » — puissance réservée par les data centers auprès de RTE et consommation des centres raccordés à son réseau (RTE)."
# Page née de l'arbitrage PRO-20261026-033434 (graphe G4, page de faits distincte de la notion de dette technologique).
# Fiche : docs/conception/data-centers-puissance-reservee.md. Aucun chiffre saisi : jetons {dtc.*} et shortcode dtc-val
# (scripts/update_data_centers.py : valeurs lues dans le texte de trois publications de RTE et du recensement du SDES, répartition mesurée sur une figure).
donnees: [data_centers]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "data_centers"
  nom: "Data centers en France : puissance de raccordement réservée auprès de RTE, répartition par statut et consommation d'électricité (publications de RTE)"
  description: "Puissance de raccordement réservée par les data centers auprès de RTE (fin 2024, novembre 2025, mai 2026), répartition de novembre 2025 par statut (raccordé, en travaux, mise en service 2025-2029 ou à partir de 2030, suspendu, abandonné) mesurée sur la figure 2.3 du Bilan prévisionnel 2025-2035, consommation mesurée et estimée, trajectoires de RTE pour 2030 et 2035 ; chaque valeur porte sa nature (lue dans le texte ou mesurée sur la figure) et sa source."
  couverture_temporelle: "2024/2035"
  couverture_spatiale: "France"
  variables:
    - {nom: "Puissance de raccordement réservée", unite: "GW", description: "centres de données, réseau public de transport"}
    - {nom: "Puissance réservée par statut", unite: "GW", description: "novembre 2025, mesurée sur la figure 2.3"}
    - {nom: "Consommation d'électricité", unite: "TWh par an", description: "mesurée, estimée, ou projetée dans les trajectoires de RTE"}
  sources:
    - "https://assets.rte-france.com/prod/public/2025-12/2025-12-23-bilan-previsionnel-2025-consommation.pdf"
    - "https://assets.rte-france.com/prod/public/2026-02/Bilan-electrique-2025-principaux-resultats.pdf"
    - "https://www.rte-france.com/bases-electricite/consommation-electricite/essor-data-centers-france"
    - "https://www.statistiques.developpement-durable.gouv.fr/la-consommation-delectricite-des-data-centers-en-2024"
  mots: ["data centers", "centres de données", "RTE", "raccordement", "puissance réservée", "consommation d'électricité", "intelligence artificielle", "Bilan prévisionnel", "file d'attente", "réseau électrique"]
  fichiers: ["data_centers.csv", "data_centers.json"]
faq:
  - question: "Combien de puissance les data centers ont-ils réservée sur le réseau électrique français ?"
    answer: "Selon RTE, près de {dtc.res_mai2026} gigawatts en mai 2026, pour environ {dtc.projets_2026} projets, contre environ {dtc.res_fin2024} fin 2024. En novembre 2025, sur {dtc.res_nov2025} GW réservés, {dtc.st_2030} GW visaient une mise en service à partir de 2030 et des réservations totalisant environ {dtc.st_abandon} GW avaient été abandonnées depuis 2023."
  - question: "Combien d'électricité consomment les data centers en France ?"
    answer: "Les data centers sur sites dédiés raccordés au réseau de transport de RTE ont consommé près de {dtc.rpt_2025} TWh en 2025, contre {dtc.rpt_2024} TWh en 2024 ; ceux du réseau de distribution d'Enedis, {dtc.enedis_2024} TWh en 2024. RTE estime l'ensemble des sites dédiés à {dtc.sd_bas} à {dtc.sd_haut} TWh en 2024, et ses deux trajectoires donnent {dtc.l2030} à {dtc.r2030} TWh en 2030."
  - question: "D'où viennent ces chiffres ?"
    answer: "De trois publications de RTE (Bilan prévisionnel 2025-2035, Bilan électrique 2025, page « Les data centers en chiffres clés ») et, comme contrôle indépendant, du recensement du SDES (juillet 2026), téléchargés par un script qui lit chaque valeur dans la phrase qui la porte, mesure la répartition par statut sur une figure du Bilan prévisionnel et s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases de la page. Les données sont téléchargeables en CSV et en JSON, sous licence CC BY 4.0."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/data-centers-puissance-reservee.md"  # fiche de conception (regle 12)
  refonte: "2026-10-27"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 47
  nature: "Publications de RTE relues et mesurées"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données du&nbsp;: {{< dtc-val "date_donnees" >}}</span> RTE, Bilan prévisionnel 2025-2035 (décembre 2025), Bilan électrique 2025 (février 2026) et page «&nbsp;Les data centers en chiffres clés&nbsp;» (mise à jour du {{< dtc-val "date_web" >}})&nbsp;: valeurs lues dans le texte, répartition par statut mesurée sur une figure. Télécharger&nbsp;: <a href="/data_centers.csv">CSV</a> · <a href="/data_centers.json">JSON</a></p>

## Ce qui est réservé, ce qui est consommé {#reserve-consomme}

En mai 2026, selon RTE, les data centers avaient réservé près de {{< dtc-val "res_mai2026" >}}&nbsp;gigawatts (GW) de capacité de raccordement à son réseau, pour environ {{< dtc-val "projets_2026" >}}&nbsp;projets. Fin 2024, une quarantaine de projets totalisaient environ {{< dtc-val "res_fin2024" >}}&nbsp;GW&nbsp;: en moins d'un an et demi, la puissance réservée a plus que triplé. Fin novembre 2025, les data centers détenaient {{< dtc-val "res_nov2025" >}}&nbsp;GW des quelque {{< dtc-val "tot_nov2025" >}}&nbsp;GW de droits d'accès attribués par RTE aux grands projets, devant l'hydrogène ({{< dtc-val "tot_h2" >}}&nbsp;GW) et l'industrie ({{< dtc-val "tot_ind" >}}&nbsp;GW).

La consommation, elle, se compte en térawattheures (TWh). Les data centers sur sites dédiés raccordés au réseau de transport de RTE ont consommé {{< dtc-val "rpt_2024" >}}&nbsp;TWh en 2024 et près de {{< dtc-val "rpt_2025" >}}&nbsp;TWh en 2025&nbsp;; ceux du réseau de distribution d'Enedis, {{< dtc-val "enedis_2024" >}}&nbsp;TWh en 2024. RTE estime l'ensemble des sites dédiés à {{< dtc-val "sd_bas" >}} à {{< dtc-val "sd_haut" >}}&nbsp;TWh en 2024, et {{< dtc-val "int_bas" >}} à {{< dtc-val "int_haut" >}}&nbsp;TWh avec les salles informatiques internes des entreprises et des administrations. Le service statistique du ministère de la Transition écologique (SDES), qui recense les centres eux-mêmes, aboutit au même ordre de grandeur&nbsp;: {{< dtc-val "sdes_n" >}} centres consommant plus de 1&nbsp;GWh par an ont consommé près de {{< dtc-val "sdes_twh" >}}&nbsp;TWh en 2024, et l'ensemble est estimé entre {{< dtc-val "sdes_bas" >}} et {{< dtc-val "sdes_haut" >}}&nbsp;TWh. Les deux estimations ne portent pas exactement sur le même périmètre&nbsp;: elles se recoupent, sans se remplacer.

**Une puissance réservée n'est pas une consommation.** Une réservation garantit un accès au réseau&nbsp;; elle ne dit ni si le site sera construit, ni quand, ni à quelle puissance il fonctionnera. La figure place les deux grandeurs l'une sous l'autre, chacune sur son échelle, sans les rapporter l'une à l'autre.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/data-centers-reserve-consomme-m.svg" width="300" height="1125">
    <img src="/img/data-centers-reserve-consomme.svg" alt="Deux panneaux. En haut, la puissance de raccordement réservée par les data centers auprès de RTE : environ {{< dtc-val "res_fin2024" >}} GW fin 2024, {{< dtc-val "res_nov2025" >}} GW en novembre 2025, dont {{< dtc-val "st_avant2030" >}} GW pour une mise en service avant 2030 et {{< dtc-val "st_2030" >}} GW à partir de 2030, près de {{< dtc-val "res_mai2026" >}} GW en mai 2026 ; {{< dtc-val "rac_gw" >}} GW déjà raccordés au réseau de RTE. En bas, la consommation : {{< dtc-val "rpt_2024" >}} TWh en 2024 et près de {{< dtc-val "rpt_2025" >}} TWh en 2025 sur le réseau de RTE, {{< dtc-val "sd_bas" >}} à {{< dtc-val "sd_haut" >}} TWh estimés pour l'ensemble des sites dédiés en 2024, {{< dtc-val "l2030" >}} à {{< dtc-val "r2030" >}} TWh en 2030 et {{< dtc-val "l2035" >}} à {{< dtc-val "r2035" >}} TWh en 2035 dans les deux trajectoires de RTE." width="720" height="539" loading="lazy">
  </picture>
  <figcaption>Puissance de raccordement réservée (GW) et consommation d'électricité (TWh par an) des data centers, d'après RTE&nbsp;; répartition de novembre 2025 mesurée sur la figure 2.3 du Bilan prévisionnel 2025-2035.</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** En novembre 2025, les data centers avaient réservé {{< dtc-val "res_nov2025" >}}&nbsp;GW de raccordement auprès de RTE, dont {{< dtc-val "st_2030" >}}&nbsp;GW pour une mise en service à partir de 2030&nbsp;; ceux raccordés au réseau de RTE ont consommé près de {{< dtc-val "rpt_2025" >}}&nbsp;TWh en 2025.

</div>

## Une réservation annonce-t-elle une consommation&nbsp;? {#calendrier}

Entre une réservation et une consommation, chaque étape a son incertitude&nbsp;: le projet doit être construit et raccordé&nbsp;; une fois raccordé, il n'appelle qu'une partie de la puissance réservée, et seulement après une montée en charge&nbsp;; c'est enfin la durée pendant laquelle cette puissance est appelée qui fait les térawattheures consommés.

Deux lectures du chiffre des réservations circulent. La première y voit une consommation annoncée, et prochaine&nbsp;: c'est elle que suppose toute conversion de gigawatts réservés en réacteurs nucléaires ou en foyers. La seconde y voit une option sur le réseau, dont une part se réalisera lentement et une autre jamais&nbsp;: c'est celle de RTE, qui attribue ces réservations et prépare la réforme de leur file d'attente. Elle n'est pas neutre pour autant&nbsp;: elle sert aussi l'argument de cette réforme.

Les réservations elles-mêmes permettent de les départager sur un point&nbsp;: le calendrier. Au {{< dtc-val "date_fig23" >}}, les gigawatts réservés par les data centers se répartissaient ainsi (mesure sur une figure de RTE, au dixième de gigawatt près)&nbsp;: en travaux, {{< dtc-val "st_travaux" >}}&nbsp;GW&nbsp;; signés pour une mise en service entre 2025 et 2029, {{< dtc-val "st_2529" >}}&nbsp;GW&nbsp;; pour une mise en service à partir de 2030, {{< dtc-val "st_2030" >}}&nbsp;GW&nbsp;; suspendus, {{< dtc-val "st_suspendu" >}}&nbsp;GW. Plus de la moitié de la puissance réservée vise donc 2030 ou après. Et depuis 2023, des réservations totalisant environ {{< dtc-val "st_abandon" >}}&nbsp;GW ont été abandonnées, pour {{< dtc-val "st_raccorde" >}}&nbsp;GW de projets effectivement raccordés. Les {{< dtc-val "sites_rte" >}}&nbsp;data centers directement raccordés au réseau de RTE totalisent {{< dtc-val "rac_mw" >}}&nbsp;mégawatts.

RTE donne trois raisons à cet écart entre réservation et consommation. Certains développeurs ont sécurisé un accès au réseau en plusieurs points pour des projets en réalité similaires. Les sites montent en charge lentement&nbsp;: selon les principaux opérateurs, cités par RTE, il faut {{< dtc-val "montee" >}} pour atteindre environ {{< dtc-val "montee_pct" >}}&nbsp;% de la puissance demandée, car les serveurs, très coûteux, ne sont installés qu'au rythme des usages. Enfin, la puissance appelée reste inférieure à la puissance de raccordement&nbsp;: RTE constate que les data centers raccordés à son réseau depuis deux à trois ans ne consomment pour l'instant, en moyenne, que {{< dtc-val "util_obs" >}}&nbsp;% de la puissance qu'ils ont demandée.

**Ce graphe tranche une question de calendrier, pas de volume.** Il montre que la puissance réservée ne se traduit ni immédiatement ni intégralement en consommation&nbsp;; il ne dit pas quelle part se réalisera d'ici 2035.

## Ce que RTE projette {#trajectoires}

Dans son Bilan prévisionnel 2025-2035, RTE retient deux trajectoires pour la consommation des data centers sur sites dédiés&nbsp;: {{< dtc-val "l2030" >}} à {{< dtc-val "r2030" >}}&nbsp;TWh en 2030, {{< dtc-val "l2035" >}} à {{< dtc-val "r2035" >}}&nbsp;TWh en 2035. La plus haute suppose qu'environ {{< dtc-val "concret_r" >}}&nbsp;% des projets ayant demandé un raccordement au réseau de transport pour une mise en service avant 2030 se concrétisent ({{< dtc-val "concret_r_gw" >}}&nbsp;GW), et que ces sites utilisent en moyenne {{< dtc-val "util_2030" >}}&nbsp;% de leur puissance de raccordement à cet horizon&nbsp;; la plus basse, une concrétisation d'environ {{< dtc-val "concret_l" >}}&nbsp;%. Ce sont des hypothèses, non des mesures.

RTE donne lui-même l'ordre de grandeur de ce que ces hypothèses écartent&nbsp;: si l'ensemble des quelque {{< dtc-val "tot_nov2025" >}}&nbsp;GW réservés par les grands projets, data centers, hydrogène et industrie confondus, fonctionnait à pleine puissance toute l'année, la consommation atteindrait théoriquement environ {{< dtc-val "theo_twh" >}}&nbsp;TWh, «&nbsp;un niveau sans commune mesure&nbsp;» avec ses hypothèses.

Les publications de RTE ne donnent pas toutes les mêmes chiffres. Sa page «&nbsp;Les data centers en chiffres clés&nbsp;», mise à jour le {{< dtc-val "date_web" >}}, attribue au même Bilan prévisionnel une consommation de {{< dtc-val "w30_bas" >}} à {{< dtc-val "w30_haut" >}}&nbsp;TWh en 2030 et de {{< dtc-val "w35_bas" >}} à {{< dtc-val "w35_haut" >}}&nbsp;TWh en 2035 «&nbsp;dans une trajectoire de décarbonation rapide&nbsp;», et une consommation actuelle d'environ {{< dtc-val "web_conso" >}}&nbsp;TWh. Le document publié donne {{< dtc-val "r2030" >}} et {{< dtc-val "r2035" >}}&nbsp;TWh pour cette trajectoire, et {{< dtc-val "sd_bas" >}} à {{< dtc-val "sd_haut" >}}&nbsp;TWh en 2024 pour les sites dédiés. Cette page suit le document publié&nbsp;; la page web n'explique pas l'écart.

## Une réservation engage-t-elle déjà la collectivité&nbsp;? {#engagement}

Pas encore de façon irréversible. À la demande de son titulaire, une réservation peut être suspendue un an, reconductible une fois&nbsp;: la puissance reste garantie, mais les conditions financières et de délai peuvent être revues. Elle peut aussi être abandonnée&nbsp;: c'est arrivé à environ {{< dtc-val "st_abandon" >}}&nbsp;GW de réservations de data centers depuis 2023.

Ce qui pourrait engager durablement la collectivité se trouve ailleurs&nbsp;: dans les ouvrages de réseau construits pour accueillir ces sites, et dans la façon dont ils sont financés. Cette page ne les mesure pas. RTE juge d'ailleurs «&nbsp;peu engageant&nbsp;» le système actuel de réservation, fondé sur le principe du «&nbsp;premier arrivé, premier servi&nbsp;», qui peut retarder ou bloquer le raccordement d'autres projets&nbsp;; il a annoncé une réforme fondée plutôt sur celui du «&nbsp;premier prêt, premier servi&nbsp;».

## Ce que ces données ne disent pas {#limites}

- **Un producteur principal, partie prenante.** Toutes les valeurs viennent de RTE, sauf le recensement du SDES, cité comme contrôle&nbsp;; RTE attribue les réservations et en réforme la file d'attente&nbsp;; la consommation du réseau de distribution est reprise de RTE, non lue chez Enedis.
- **Deux grandeurs qui ne se comparent pas.** Une puissance réservée (GW) n'est ni une puissance appelée ni une consommation (TWh)&nbsp;; aucun rapport n'est calculé entre elles. Le taux de {{< dtc-val "util_obs" >}}&nbsp;% cité plus haut est une observation de RTE sur les sites raccordés depuis deux à trois ans.
- **Une répartition mesurée sur une figure.** La répartition par statut est lue sur la figure 2.3 du Bilan prévisionnel, à 0,1&nbsp;GW près, au {{< dtc-val "date_fig23" >}}&nbsp;; le total de {{< dtc-val "res_nov2025" >}}&nbsp;GW est daté de fin novembre. La somme mesurée, {{< dtc-val "actif_dc" >}}&nbsp;GW, le retrouve à 0,1&nbsp;GW près.
- **Des trajectoires, pas des prévisions.** Elles reposent sur des taux de concrétisation et d'utilisation supposés.
- **Ni l'eau, ni le foncier, ni les coûts de réseau** ne sont mesurés ici.

<aside class="encadre">

**Une lecture de l'auteur, non testée ici.** L'économiste Stéphane Lalut appelle [dette technologique](/dette-technologique/) le coût des infrastructures numériques converti en engagements que d'autres porteront (working paper [AWP-06](/awp/awp-06/)). Les chiffres de cette page montrent qu'une réservation de raccordement n'est pas encore un tel engagement&nbsp;; ils ne mesurent pas ceux qui le seraient.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="Pour prolonger la question" avis="non" >}}
*ANTHROPIE — Ordre ici. Dette ailleurs* suit, sur la longue durée, ce que chaque ordre construit engage, et qui en porte la charge.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

- RTE, [*Bilan prévisionnel 2025-2035, La consommation d'électricité*](https://assets.rte-france.com/prod/public/2025-12/2025-12-23-bilan-previsionnel-2025-consommation.pdf) (décembre 2025)&nbsp;: chapitre 2.1.3 (réservations, abattements, consommation théorique, suspension des réservations, réforme du raccordement) et 2.5 (consommation des centres de données, trajectoires, hypothèses)&nbsp;; figure 2.3 (répartition des réservations par statut, mesurée par script) et figure 2.10 (trajectoires).
- RTE, [*Bilan électrique 2025, principaux résultats*](https://assets.rte-france.com/prod/public/2026-02/Bilan-electrique-2025-principaux-resultats.pdf) (février 2026)&nbsp;: droits d'accès par secteur fin novembre 2025, consommation des centres de données raccordés au réseau de transport et au réseau de distribution.
- RTE, [«&nbsp;Les data centers en chiffres clés&nbsp;»](https://www.rte-france.com/bases-electricite/consommation-electricite/essor-data-centers-france), page mise à jour le {{< dtc-val "date_web" >}}&nbsp;: réservations de fin 2024 et de mai 2026, sites raccordés, taux d'utilisation observé, durée de montée en charge, projections citées.
- SDES, [«&nbsp;La consommation d'électricité des data centers en 2024&nbsp;»](https://www.statistiques.developpement-durable.gouv.fr/la-consommation-delectricite-des-data-centers-en-2024) ({{< dtc-val "date_sdes" >}})&nbsp;: recensement des centres de plus de 1&nbsp;GWh et estimation de l'ensemble, contrôle indépendant de RTE.

{{< reutiliser figures="figures_data_centers" jeu="data_centers" sources="RTE" donnees="Puissance réservée par les data centers (fin 2024, novembre 2025, mai 2026), répartition de novembre 2025 par statut, consommation mesurée, estimée et projetée ; pour chaque valeur, sa nature (lue dans le texte ou mesurée sur la figure) et sa source, en CSV au format long." >}}
En novembre 2025, les data centers avaient réservé {{< dtc-val "res_nov2025" >}} GW de raccordement auprès de RTE, dont {{< dtc-val "st_2030" >}} GW pour une mise en service à partir de 2030, et des réservations totalisant environ {{< dtc-val "st_abandon" >}} GW avaient été abandonnées depuis 2023. Ceux raccordés au réseau de RTE ont consommé près de {{< dtc-val "rpt_2025" >}} TWh en 2025&nbsp;; RTE retient {{< dtc-val "l2030" >}} à {{< dtc-val "r2030" >}} TWh en 2030 pour l'ensemble des sites dédiés.
{{< /reutiliser >}}
