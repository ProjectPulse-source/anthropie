---
date: 2026-04-02  # premier commit de la page (git log --follow)
lastmod: 2026-11-16
journal:  # révisions qui changent la lecture de la page
  - {date: 2026-11-05, texte: "Correction : l'entrée « Boucle anthropique » donne désormais la définition d'AWP-07 (cinq états, du déplacement à la bifurcation) ; le retour vers la cognition en devient un cas, propre au métaprogramme numérique."}
  - {date: 2026-11-05, texte: "Corrections : effet Jevons (cas extrême de l'effet rebond), effet boomerang (crédit à Ulrich Beck, bilan non affirmé), registres de la dette (un déplacement possible, à établir cas par cas)."}
  - {date: 2026-11-16, texte: "Relecture des sources : définitions alignées sur les working papers déposés (dont la saturation, et la boucle anthropique selon la version révisée d'AWP-07) ; « externalisation entropique » présentée comme une recherche que l'hypothèse oriente, sans en préjuger le résultat."}
title: "Glossaire"
og_title: "Glossaire — les notions, définies et sourcées — S. Lalut"
description: "Glossaire des termes clés du cadre anthropique."
og_image: "images/og-glossaire.jpg"
og_image_alt: "Glossaire — Anthropie. On ne crée pas l'ordre, on déplace le désordre."
carte:  # carte du vocabulaire (shortcode glossaire-carte) : ensembles nommés par l'introduction ; chaque ancre doit exister (errorf au build)
  titre: "Carte du vocabulaire"
  coeur: {id: "anthropie", t: "Anthropie", d: "Les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent."}
  groupes:
    - t: "Le mécanisme"
      role: "Le transfert et ses trois dimensions&nbsp;: où va le désordre."
      ton: "ordre"
      termes:
        - {id: "transfert-anthropique", t: "Transfert anthropique"}
        - {id: "externalisation-entropique", t: "Transfert spatial"}
        - {id: "dette-anthropique", t: "Transfert temporel"}
        - {id: "transfert-social", t: "Transfert social"}
        - {id: "ordre-local", t: "Ordre local"}
        - {id: "espace-de-deportation", t: "Espace de déportation"}
    - t: "Les seuils et le retour"
      role: "Quand l'espace de déportation sature et que le désordre revient."
      ton: "cout"
      termes:
        - {id: "saturation", t: "Saturation"}
        - {id: "cout-marginal-croissant", t: "Coût marginal croissant"}
        - {id: "effet-boomerang", t: "Effet boomerang"}
        - {id: "effet-jevons", t: "Effet Jevons"}
        - {id: "boucle-anthropique", t: "Boucle anthropique"}
    - t: "Les configurations"
      role: "Les agencements historiques du transfert, sur 3,3&nbsp;millions d'années."
      termes:
        - {id: "configuration", t: "Configuration"}
        - {id: "metaprogramme", t: "Métaprogramme"}
        - {id: "registre-des-couts-deportes", t: "Registre des coûts déportés"}
    - t: "La posture"
      role: "Devant tout ordre stable, demander où s'écoule le désordre."
      termes:
        - {id: "discipline-du-regard", t: "Discipline du regard"}
    - t: "Les applications"
      large: true
      role: "Le cadre appliqué à un domaine&nbsp;: numérique, héritages, inégalités, savoir."
      termes:
        - {id: "dette-technologique", t: "Dette technologique"}
        - {id: "registres-de-couts-couples", t: "Registres de coûts couplés"}
        - {id: "derisking", t: "Derisking"}
        - {id: "communs-negatifs", t: "Communs négatifs"}
        - {id: "reversibilite-sociale", t: "Réversibilité sociale"}
        - {id: "ordre-epistemique", t: "Ordre épistémique"}
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["notion"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/glossaire.md"  # fiche de conception (regle 12), refonte de presentation du 26/10/2026
  bloc: "notions"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 10
  nature: "Définitions"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Glossaire"
---

Ce glossaire rassemble les termes propres au cadre anthropique. Il ne s'agit pas d'un dictionnaire général&nbsp;: chaque entrée donne le sens qu'un terme, forgé par le cadre ou emprunté à d'autres auteurs, prend dans l'hypothèse anthropique. Les définitions renvoient aux *Anthropie Working Papers* et au livre [*ANTHROPIE — Ordre ici. Dette ailleurs*](/livres/anthropie-ordre-ici-dette-ailleurs/), qui les développent&nbsp;; deux appellations, signalées dans leur entrée, sont propres à ce glossaire.

L'anthropie repose sur une hypothèse unique — les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent — dont les termes ci-dessous constituent le vocabulaire opératoire. Ils s'organisent autour de trois ensembles — le **mécanisme** (transfert anthropique et ses trois dimensions), les **seuils** (saturation, coût marginal croissant, effet boomerang), et les **configurations** (agencements historiques du transfert sur 3,3 millions d'années) — auxquels s'ajoute une posture analytique&nbsp;: la **discipline du regard**.

{{< glossaire-carte >}}

<dl>

<div class="glossaire-entry" id="anthropie">
<dt>Anthropie</dt>
<dd>Hypothèse selon laquelle les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent. Dans cette hypothèse, tout ordre observable suppose un désordre exporté ailleurs&nbsp;; AWP-01 précise qu'elle ne postule pas que tout est transfert, mais que toute stabilité observable mérite d'être interrogée sur ses coûts déportés. Ce déplacement opère selon trois axes — spatial, temporel, social — qui, dans de nombreuses configurations, se combinent et se renforcent mutuellement. Hypothèse proposée par l'économiste Stéphane Lalut (livre <em>ANTHROPIE</em>, 2025&nbsp;; série AWP, 2026). Voir <a href="/quest-ce-que-lanthropie/">Qu'est-ce que l'anthropie&nbsp;?</a></dd>
</div>

<div class="glossaire-entry" id="transfert-anthropique">
<dt>Transfert anthropique</dt>
<dd>Mécanisme par lequel le désordre est déplacé d'un lieu, d'un temps ou d'un groupe vers un autre. Le transfert peut être spatial (vers d'autres territoires), temporel (vers l'avenir) ou social (vers des groupes captifs). Il constitue l'opération centrale du cadre anthropique&nbsp;: ce que d'autres cadres classent séparément comme externalité, dette, inégalité ou risque se lit ici comme les variantes d'un même mécanisme. Voir <a href="/awp/awp-01/">AWP-01</a>.</dd>
</div>

<div class="glossaire-entry" id="externalisation-entropique">
<dt>Transfert spatial (externalisation entropique)</dt>
<dd>Forme spatiale du transfert anthropique (<a href="/awp/awp-01/">AWP-01</a>)&nbsp;; l'appellation «&nbsp;externalisation entropique&nbsp;» est propre à ce glossaire. Le désordre est déplacé vers d'autres territoires — extraction lointaine, pollution délocalisée, relégation géographique. Les métropoles brillent, les périphéries paient&nbsp;: la consommation numérique du Nord repose sur l'extraction de cobalt et de terres rares dans le Sud global. Voir <a href="/awp/awp-04/">AWP-04</a>.</dd>
</div>

<div class="glossaire-entry" id="dette-anthropique">
<dt>Transfert temporel (dette anthropique)</dt>
<dd>Forme temporelle du transfert (<a href="/awp/awp-01/">AWP-01</a>)&nbsp;; l'appellation «&nbsp;dette anthropique&nbsp;» est propre à ce glossaire. Le désordre est reporté vers l'avenir — dette publique, sous-investissement, déficit de maintenance. Le transfert temporel convertit un coût présent en dette future&nbsp;: les générations qui héritent du désordre n'ont pas contracté l'emprunt. Voir <a href="/awp/awp-03/">AWP-03</a>.</dd>
</div>

<div class="glossaire-entry" id="transfert-social">
<dt>Transfert social</dt>
<dd>Forme sociale du transfert anthropique. Le désordre est déplacé vers des groupes moins capables de s'y soustraire — précarisation, exclusion, captation asymétrique des coûts. Le transfert social se mesure à la capacité inégale des groupes à refuser, négocier ou fuir la charge qui leur est imposée. Voir <a href="/awp/awp-01/">AWP-01</a>.</dd>
</div>

<div class="glossaire-entry" id="ordre-local">
<dt>Ordre local</dt>
<dd>Configuration sociale résultant du déplacement du désordre hors du périmètre considéré. L'hypothèse conduit à rechercher, derrière un ordre local, un ailleurs qui en absorberait le coût et dont les destinataires resteraient hors champ. Cette recherche ne préjuge pas de son résultat&nbsp;: l'enquête peut conclure qu'aucun déplacement n'est établi (voir l'entrée <a href="#anthropie">Anthropie</a>). Voir <a href="/awp/awp-01/">AWP-01</a>.</dd>
</div>

<div class="glossaire-entry" id="discipline-du-regard">
<dt>Discipline du regard</dt>
<dd>Posture analytique proposée par l'anthropie&nbsp;: devant tout ordre stable, demander où s'écoule le désordre. Elle conduit à interroger les zones d'ombre de la stabilité apparente. La discipline du regard ne consiste pas à dénoncer abstraitement le désordre du monde, mais à identifier, dans chaque configuration concrète, le mécanisme qui rend le transfert opaque. Voir <a href="/awp/awp-01/">AWP-01</a>.</dd>
</div>

<div class="glossaire-entry" id="saturation">
<dt>Saturation</dt>
<dd>État d'un espace de déportation qui ne peut plus absorber le désordre en silence&nbsp;: sa capacité est atteinte, ou le transfert devient lisible et contesté (<a href="/awp/awp-07/">AWP-07</a>, conditions de saturation). <a href="/awp/awp-02/">AWP-02</a> en avait donné une première esquisse&nbsp;: un espace sature quand externaliser le désordre coûte plus cher que le gérer sur place, ce que signalent deux critères, le coût marginal croissant et l'effet boomerang&nbsp;; AWP-07 range le premier du côté du système qui déplace le désordre et fait du second un retour, postérieur à la saturation. Lorsque plus aucun espace — géographique, social, temporel, cognitif — ne peut absorber la charge, la complexité ne tient plus, selon AWP-02, que par une tension interne vouée à se rompre.</dd>
</div>

<div class="glossaire-entry" id="cout-marginal-croissant">
<dt>Coût marginal croissant</dt>
<dd>Premier critère de saturation selon AWP-02&nbsp;: le transfert devient de plus en plus coûteux à mesure que l'espace de déportation se remplit, chaque unité de désordre exportée coûtant davantage que la précédente. AWP-07 en fait une condition du côté du système qui déplace le désordre, distincte de la saturation de l'espace qui le reçoit. Voir <a href="/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="effet-boomerang">
<dt>Effet boomerang</dt>
<dd>Second critère de saturation selon AWP-02&nbsp;: le désordre déporté revient au système qui l'avait déplacé, parfois sous une forme plus coûteuse que le désordre initial&nbsp;; AWP-07 en fait un retour, postérieur à la saturation. Le changement climatique en est l'illustration planétaire&nbsp;: le désordre exporté dans l'atmosphère pendant deux siècles d'industrialisation revient sous forme de coûts que l'exportation originelle n'avait pas comptés. Au sens d'un retour des risques sur ceux qui les produisent, la notion vient d'Ulrich Beck (<em>Risikogesellschaft</em>, 1986&nbsp;; <em>La Société du risque</em>, 2001 pour la traduction française). Voir <a href="/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="effet-jevons">
<dt>Effet Jevons (paradoxe de Jevons)</dt>
<dd>Cas extrême de l'effet rebond&nbsp;: la hausse de l'usage reprend plus que le gain d'efficacité, et la consommation totale de la ressource augmente au lieu de baisser (Jevons, <em>The Coal Question</em>, 1865). Le cadre anthropique peut le lire comme un effet boomerang&nbsp;: selon AWP-04, les gains d'efficacité de la transition énergétique ouvrent de nouveaux espaces de consommation, donc de nouveaux transferts. Voir la page <a href="/effet-rebond/">Qu'est-ce que l'effet rebond&nbsp;?</a> et <a href="/awp/awp-04/">AWP-04</a>.</dd>
</div>

<div class="glossaire-entry" id="metaprogramme">
<dt>Métaprogramme</dt>
<dd>Configuration contemporaine du transfert anthropique opérant à l'échelle numérique et planétaire. Le métaprogramme déplace le désordre à une vitesse et une échelle sans précédent. Il articule deux dynamiques autrefois distinctes&nbsp;: une dette énergétique et matérielle projetée vers l'avenir, et une captation cognitive opérée dans le présent — attention siphonnée, sens dilué, subjectivités contractées. Voir <a href="/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="boucle-anthropique">
<dt>Boucle anthropique</dt>
<dd>Suite de cinq états conditionnels qui décrit ce que devient le désordre qu'un système social fait supporter ailleurs&nbsp;: déplacement vers un réceptacle (E1), accumulation (E2), saturation (E3), retour possible vers le système émetteur (E4), bifurcation (E5) — nouveau déplacement, reconfiguration ou effondrement partiel. Après le déplacement, aucun passage n'est obligé. Formalisée dans <a href="/awp/awp-07/">AWP-07</a>&nbsp;: cette définition suit sa version révisée, non encore déposée&nbsp;; la version déposée en juillet 2026 tient l'accumulation pour automatique et énonce le cycle sans condition. Présentée sur la page <a href="/boucle-anthropique/">Qu'est-ce que la boucle anthropique&nbsp;?</a>. Dans le métaprogramme numérique, le retour peut viser la capacité même qui avait rendu le déplacement possible, la cognition&nbsp;: attention captée, jugement délégué. C'est alors un retour, non un quatrième axe de transfert. Voir aussi <a href="/quest-ce-que-lanthropie/">Qu'est-ce que l'anthropie&nbsp;?</a> et <a href="/awp/awp-06/">AWP-06</a>.</dd>
</div>

<div class="glossaire-entry" id="ordre-epistemique">
<dt>Ordre épistémique</dt>
<dd>Système de hiérarchies de légitimité, de critères de validité et de circuits de reconnaissance produit par le champ académique. Selon l'hypothèse d'AWP-05, cet ordre suppose un désordre épistémique exporté vers ses marges. L'institution produit à la fois sélection légitime et transfert de coûts&nbsp;: certaines questions, certains formats, certaines postures sont reléguées par un mécanisme analogue au transfert anthropique. Voir <a href="/awp/awp-05/">AWP-05</a>.</dd>
</div>

<div class="glossaire-entry" id="espace-de-deportation">
<dt>Espace de déportation</dt>
<dd>Lieu, temps ou groupe social vers lequel le désordre est transféré. L'espace de déportation peut être géographique, temporel (l'avenir) ou social (un groupe captif). «&nbsp;À chaque saturation d'un espace de déportation, la fuite s'invente ailleurs&nbsp;: plus abstrait, plus lointain, moins politisable.&nbsp;» Voir <a href="/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="configuration">
<dt>Configuration</dt>
<dd>Agencement historique particulier des mécanismes de transfert anthropique. Le cadre distingue sept configurations majeures sur 3,3 millions d'années. Le transfert ne se répète pas à l'identique&nbsp;: ses formes migrent. Des programmes fondateurs au piège néolithique, le transfert reste principalement spatial&nbsp;; des systèmes antiques aux réseaux transcontinentaux, le social prend le dessus&nbsp;; de l'industrialisation au métaprogramme numérique, le temporel et le cognitif l'emportent (AWP-02, version 1.1). Les sept âges du livre suivent une autre périodisation, où le spatial domine jusqu'aux systèmes antiques (p.&nbsp;622). Voir <a href="/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="derisking">
<dt>Derisking</dt>
<dd>Mécanisme par lequel l'État altère le profil de risque d'un investissement privé pour le rendre attractif aux capitaux institutionnels (Daniela Gabor). Le derisking opère le passage du coût présent à la dette future&nbsp;: garanties publiques, contrats d'engagement long terme, dispositifs de stabilisation. Pivot conceptuel pour comprendre comment l'investissabilité des infrastructures numériques se construit au prix d'une dette technologique. Voir <a href="/awp/awp-06/">AWP-06</a>.</dd>
</div>

<div class="glossaire-entry" id="dette-technologique">
<dt>Dette technologique</dt>
<dd>Coût des infrastructures numériques — énergie, matière, territoire, et peut-être attention — devenu dette par trois opérations&nbsp;: l'engagement (contrats de long terme), la garantie publique et l'irréversibilisation des choix d'infrastructure. L'attention y est un registre possible, non une dette déjà constituée. À ne pas confondre avec la «&nbsp;dette technique&nbsp;» du génie logiciel, qui désigne l'accumulation de compromis dans la conception d'un programme&nbsp;: la dette technologique au sens anthropique est un mécanisme économique et politique, pas une propriété du code. Concept formalisé par Stéphane Lalut (AWP-06, 2026). Voir <a href="/dette-technologique/">Qu'est-ce que la dette technologique&nbsp;?</a>, <a href="/awp/awp-06/">AWP-06</a> et le livre <a href="/livres/anthropie-ordre-ici-dette-ailleurs/"><em>ANTHROPIE — Ordre ici. Dette ailleurs</em></a>.</dd>
</div>

<div class="glossaire-entry" id="communs-negatifs">
<dt>Communs négatifs</dt>
<dd>Notion développée par Alexandre Monnin, avec Emmanuel Bonnet et Diego Landivar (<em>Héritage et fermeture</em>, 2021), à partir d'une expression que Monnin fait remonter à Maria Mies et Veronika Bennholdt-Thomsen (2001), pour désigner ce dont nous héritons sans avoir choisi&nbsp;: déchets, ruines, infrastructures obsolètes. Les communs négatifs ne sont pas des biens partagés volontairement, mais des charges transmises&nbsp;— un transfert anthropique cristallisé dans la matérialité du monde. Monnin range les technologies numériques parmi les communs négatifs candidats&nbsp;; AWP-06 analyse certaines infrastructures numériques comme candidates, sous conditions. Voir la page <a href="/communs-negatifs/">Qu'est-ce que les communs négatifs&nbsp;?</a> et <a href="/awp/awp-06/">AWP-06</a>.</dd>
</div>

<div class="glossaire-entry" id="reversibilite-sociale">
<dt>Réversibilité sociale</dt>
<dd>Capacité, évaluée avant une tentative, de supporter son éventuel échec sans fermeture durable de son avenir. Ni un stock ni un flux&nbsp;: une troisième dimension de l'inégalité — ce qu'on peut se permettre de rater. Voir la page <a href="/reversibilite-sociale/">Qu'est-ce que la réversibilité sociale&nbsp;?</a> et les <a href="/premier-coup/">sources et le répertoire</a> de <em>La Société du premier coup</em>.</dd>
</div>

<div class="glossaire-entry" id="registres-de-couts-couples">
<dt>Registres de coûts couplés</dt>
<dd>Apport central d'AWP-06&nbsp;: grille testable des quatre registres&nbsp;— énergie, matière, territoire, attention&nbsp;— qui permet d'examiner comment l'infrastructure numérique peut déplacer simultanément le désordre selon plusieurs axes irréductibles. Ces registres ne s'additionnent pas&nbsp;: ils se couplent. Réduire l'un peut déplacer la charge vers les autres&nbsp;: c'est ce que la grille demande d'établir, cas par cas. Voir <a href="/awp/awp-06/">AWP-06</a>. À ne pas confondre avec le <em>Registre des coûts déportés</em>, qui est une chronologie et non une grille d'analyse.</dd>
</div>

<div class="glossaire-entry" id="registre-des-couts-deportes">
<dt>Registre des coûts déportés</dt>
<dd>Appareil documentaire du livre <em>ANTHROPIE — Ordre ici. Dette ailleurs</em> (2025)&nbsp;: chronologie de 168 jalons, des premiers outils (≈&nbsp;−3,3&nbsp;millions d'années) aux algorithmes contemporains, qui documente pour chaque innovation l'ordre créé et la dette déportée, avec les catégories du transfert. Version en ligne en consultation libre, les 168 jalons&nbsp;: <a href="/registre-des-couts-deportes/">Le Registre des coûts déportés</a>. À ne pas confondre avec les <a href="#registres-de-couts-couples">registres de coûts couplés</a> d'AWP-06, qui sont une grille d'analyse et non une chronologie.</dd>
</div>

</dl>

{{< consultation slug="anthropie-ordre-ici-dette-ailleurs" >}}
