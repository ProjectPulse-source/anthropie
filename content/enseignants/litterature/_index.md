---
title: "Enseigner la vérification des citations en français : une activité de Première"
description: "Une activité de français pour la Première, à l'heure de l'IA : une réponse juste est-elle une réponse vérifiée ? Cinq citations prêtées à Voltaire, Hugo, La Fontaine et Molière, deux réponses à comparer, une enquête dans les œuvres. Fiche élève imprimable, sans écran, et corrigé."
og_title: "Authentique, retouchée ou introuvable ? — une activité de français, Première"
og_image: "images/og-texte-litterature.jpg"   # carte propre (scripts/og_ressources_texte.py) ; vignette vig-texte-litterature.jpg lue par /ressources/
og_image_alt: "Carte de partage : « Authentique, retouchée ou introuvable ? », activité de Première"
date: 2026-11-04
lastmod: 2026-11-10
# Première page de la discipline Littérature (bloc `enseigner`, `disciplines` dans content/ressources/_index.md), demandée par
# l'auteur le 04/11/2026 : l'atelier de /citations-celebres-verifiees/ en fiche élève imprimable, avec corrigé. Français
# seulement (exclusion déclarée, comme la page mère). AUCUN STATUT NI FAIT NOUVEAU : chaque réponse du corrigé reprend la
# fiche de la page mère, qui donne la source. Programme : objets d'étude de Première (Éduscol, juin 2021, reprenant le
# BO n° 5 du 4 février 2021) ; les œuvres au programme changent chaque année et ne sont pas citées.
# Refonte du 10/11/2026 (IA) : arbitrage D:\CONTRE_EXPERTISE\2026-11-10_LITTERATURE_IA\ARBITRAGE.md ; les deux réponses
# de la question 2 sont RÉDIGÉES pour l'exercice et dites telles, jamais attribuées à un modèle nommé.
# Seconde passe (10/11) : ARBITRAGE-01.md du même dossier -- dossier documentaire, deux boutons d'impression
# (fiche élève et dossier ; corrigé), blocs .fiche__prof / .fiche__eleve / .fiche__dossier lus par _enseignants.scss.
ressource:
  type: ["usage"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "enseigner"
  discipline: "litterature"
  theme: "Vérifier une citation"
  rang: 10
  nature: "Activité de français — Première, vérifier une citation"
  intitule: "Une réponse juste est-elle une réponse vérifiée ? Vérifier une citation célèbre"
  encart: true
  bouton: "Voir l'activité"
  conception: "docs/conception/litterature.md"  # fiche de conception (règle 12)
onglet:  # barre de la discipline (partials/barre-discipline.html)
  court: "Citations"
  role: "Première"
activite:  # JSON-LD LearningResource (partials/schema-activite.html)
  nom: "Une réponse juste est-elle une réponse vérifiée ? Vérifier une citation célèbre"
  niveau: "Première"
  discipline: "Français"
  type: "Activité pédagogique"
  duree: "PT45M"
  enseigne: ["citation", "édition de référence", "variante", "attribution", "contexte d'une phrase", "littérature d'idées", "théâtre", "preuve", "intelligence artificielle"]
  sources:
    - "https://eduscol.education.fr/document/8138/download"
    - "https://www.education.gouv.fr/bo/21/Hebdo5/MENE2036974N.htm"
    - "https://eduscol.education.fr/document/67356/download"
lang_repli: "/en/resources/"  # pas de version anglaise (exclusion déclarée) : cible de l'onglet EN, partials/lang-cible.html
---

**Première, français.** Une citation célèbre porte un grand nom. Un assistant d'IA confirme l'attribution, ou la corrige.
Personne n'a encore ouvert le livre&nbsp;: que sait-on vraiment&nbsp;? L'activité fait chercher, sur cinq phrases prêtées à
Voltaire, Hugo, La Fontaine et Molière, ce qui est réellement écrit, où, et ce qu'en dit le passage qui l'entoure. Les
réponses sont celles de la page
[Citations célèbres&nbsp;: qu'ont vraiment écrit Hugo, Voltaire, Molière, La Fontaine et Wilde&nbsp;?](/citations-celebres-verifiees/),
qui donne pour chacune l'édition et le passage consultés.

<section class="fiche" id="fiche-citations">

### Première — Une réponse juste est-elle une réponse vérifiée&nbsp;? {#premiere-citations}

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-citations">Imprimer la fiche élève et le dossier</button> <button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-corrige="fiche-citations">Imprimer le corrigé</button></p>

<p class="fiche__bref"><strong>Ce que les élèves découvrent</strong>&nbsp;: une citation célèbre peut être mal attribuée, retouchée, ou exacte mais trompeuse hors de son œuvre&nbsp;; et une réponse juste n'est pas encore une réponse prouvée. <strong>Première · 45&nbsp;minutes · en binômes · sans écran.</strong> Fiche élève et dossier documentaire à imprimer&nbsp;; déroulé et corrigé pour l'enseignant.</p>

<div class="fiche__eleve">

#### Fiche élève

Voici cinq phrases célèbres, telles qu'elles circulent&nbsp;:

- A. «&nbsp;Je ne suis pas d'accord avec ce que vous dites, mais je me battrai jusqu'à la mort pour que vous ayez le droit de le dire&nbsp;», prêtée à Voltaire.
- B. «&nbsp;Ouvrez une école, vous fermerez une prison&nbsp;», prêtée à Victor Hugo.
- C. «&nbsp;La raison du plus fort est toujours la meilleure&nbsp;», prêtée à La Fontaine.
- D. «&nbsp;Les femmes sont comme les girouettes&nbsp;: elles se fixent quand elles se rouillent&nbsp;», prêtée à Voltaire.
- E. «&nbsp;Que diable allait-il faire dans cette galère&nbsp;?&nbsp;», prêtée à Molière.

1. **Seul, sans écran, sur la citation de votre binôme.** Dites en une ligne ce qu'elle signifie. Puis faites une hypothèse&nbsp;: authentique, retouchée ou introuvable chez l'auteur&nbsp;? Notez l'indice qui vous guide (la langue, l'époque, le ton, l'œuvre que vous connaissez).
2. **Deux réponses.** On a demandé qui a écrit la phrase A. Voici deux réponses, rédigées pour l'exercice sur le modèle de celles d'un assistant d'IA&nbsp;:
   - Réponse 1&nbsp;: «&nbsp;Cette phrase n'est pas de Voltaire. Elle a été écrite par une biographe anglaise au début du XXe&nbsp;siècle pour résumer sa pensée.&nbsp;»
   - Réponse 2&nbsp;: «&nbsp;Cette phrase n'est pas de Voltaire. Elle paraît en anglais en 1906, dans *The Friends of Voltaire* d'Evelyn Beatrice Hall, qui signe S.&nbsp;G.&nbsp;Tallentyre (chapitre&nbsp;VII, p.&nbsp;199)&nbsp;; Hall a écrit en 1939 que la formule était la sienne.&nbsp;»

   Les deux disent la même chose. Laquelle pouvez-vous vérifier directement, et comment&nbsp;? Une réponse que l'on peut vérifier est-elle pour autant vérifiée&nbsp;? Enfin, la phrase A circule en français, et Hall l'a écrite en anglais&nbsp;: de qui sont les mots français&nbsp;?
3. **Examen des pièces, en binôme, dans le document de votre citation.** Le dossier rassemble les pièces d'une enquête déjà menée&nbsp;: à vous de juger ce qu'elles prouvent. Si la phrase s'y trouve&nbsp;: notez l'œuvre, l'édition, le passage, la forme exacte, qui parle (un personnage n'est pas l'auteur), et ce qui vient avant et après. Si elle ne s'y trouve pas&nbsp;: notez ce qui a été cherché, dans quels textes, et la source où la phrase apparaît, s'il y en a une.
4. **Ce que la source permet d'affirmer.** Votre hypothèse est-elle confirmée, nuancée ou laissée indécidable&nbsp;? Qu'est-ce qui permet de dire qu'une phrase est dans une œuvre, et qu'est-ce qui permet de dire qu'elle n'y est pas&nbsp;?
5. **Mise en commun.** Chez La Fontaine, le vers C est suivi de celui-ci&nbsp;: «&nbsp;Nous l'allons montrer tout à l'heure.&nbsp;» Lisez la fin de la fable dans le document C&nbsp;: que montre-t-elle, et que change-t-elle au sens du premier vers&nbsp;? Et pourquoi, selon vous, attribue-t-on plus volontiers une phrase à un auteur connu&nbsp;?
6. **Synthèse.** Quelles sont les trois vérifications à faire avant de citer ou de partager une phrase célèbre&nbsp;?

</div>

<div class="fiche__dossier">

#### Dossier documentaire

Les textes sont donnés dans l'orthographe des éditions citées.

- **Document A.** «&nbsp;*“I disapprove of what you say, but I will defend to the death your right to say it,” was his attitude now.*&nbsp;» — S.&nbsp;G.&nbsp;Tallentyre (Evelyn Beatrice Hall), *The Friends of Voltaire*, Londres, John Murray, 1906, chapitre&nbsp;VII, p.&nbsp;199. Hall commente ici la réaction de Voltaire à la condamnation d'un livre d'Helvétius. En 1939, interrogée par Burdette Kinne, elle écrit que la phrase «&nbsp;*is my own expression and should not have been put in inverted commas*&nbsp;» (lettre du 9&nbsp;mai 1939, publiée dans *Modern Language Notes* en 1943).
- **Document B.** «&nbsp;Chaque enfant qu'on enseigne est un homme qu'on gagne. / Quatrevingt-dix voleurs sur cent qui sont au bagne / Ne sont jamais allés à l'école une fois, / Et ne savent pas lire, et signent d'une croix.&nbsp;» — Victor Hugo, *Les Quatre Vents de l'esprit* (1881), «&nbsp;Écrit après la visite d'un bagne&nbsp;». Ce qui a été cherché&nbsp;: «&nbsp;ouvrez une école&nbsp;», «&nbsp;ouvrir une école&nbsp;» et «&nbsp;fermer une prison&nbsp;», dans le texte intégral des œuvres de Hugo sur Wikisource&nbsp;: aucune occurrence. Le *Grand dictionnaire universel du XIXe&nbsp;siècle* de Pierre Larousse cite, aux articles «&nbsp;École&nbsp;» et «&nbsp;Prison&nbsp;»&nbsp;: «&nbsp;Ouvrir une école aujourd'hui, c'est fermer une prison dans vingt ans&nbsp;», signé L.&nbsp;Jourdan.
- **Document C.** «&nbsp;La raison du plus fort est toujours la meilleure&nbsp;: / Nous l'allons montrer tout à l'heure.&nbsp;» […] «&nbsp;Tu la troubles&nbsp;! reprit cette bête cruelle&nbsp;; / Et je sais que de moi tu médis l'an passé. / Comment l'aurais-je fait, si je n'étais pas né&nbsp;? / Reprit l'agneau&nbsp;: je tette encor ma mère.&nbsp;» […] «&nbsp;On me l'a dit&nbsp;: il faut que je me venge. / Là-dessus, au fond des forêts / Le loup l'emporte, et puis le mange, / Sans autre forme de procès.&nbsp;» — La Fontaine, *Fables* (1668), livre&nbsp;I, «&nbsp;Le Loup et l'Agneau&nbsp;»&nbsp;; édition Bernardin-Béchet, 1874, p.&nbsp;41-43.
- **Document D.** «&nbsp;Les femmes ressemblent aux girouettes&nbsp;: elles se fixent quand elles se rouillent.&nbsp;» — Voltaire, *Le Sottisier*, carnet de notes publié pour la première fois en 1880, Librairie des bibliophiles, p.&nbsp;99.
- **Document E.** «&nbsp;Que diable alloit-il faire dans cette galère&nbsp;?&nbsp;» — Molière, *Les Fourberies de Scapin* (1671), acte&nbsp;II, réplique de Géronte. Dix-sept ans plus tôt&nbsp;: «&nbsp;Que Diable aller faire aussi dans la Galère d'un Turc&nbsp;?&nbsp;» — Cyrano de Bergerac, *Le Pédant joué* (1654), acte&nbsp;II, scène&nbsp;4.

</div>

<div class="fiche__prof">

#### Pour l'enseignant

**Programme.** Le programme de français fixe quatre objets d'étude pour la classe de première, dont «&nbsp;la poésie du
XIXe&nbsp;siècle au XXIe&nbsp;siècle&nbsp;», «&nbsp;la littérature d'idées du XVIe&nbsp;siècle au XVIIIe&nbsp;siècle&nbsp;» et
«&nbsp;le théâtre du XVIIe&nbsp;siècle au XXIe&nbsp;siècle&nbsp;» (Éduscol, juin 2021). Les cinq citations relèvent de ces trois
objets&nbsp;: Hugo pour le premier, Voltaire et La Fontaine pour le deuxième, Molière pour le troisième.

**L'IA en classe.** Le [cadre d'usage de l'IA en éducation](https://eduscol.education.fr/document/67356/download) du ministère
de l'Éducation nationale (2025) permet aux lycéens d'utiliser les IA génératives «&nbsp;de manière autonome dans un cadre
d'apprentissage et de formation explicitement défini par l'enseignant&nbsp;», exclut de leur demander «&nbsp;de se créer un
compte personnel auprès de services d'IA accessibles au grand public&nbsp;», et demande de vérifier «&nbsp;l'exactitude des
réponses en comparant avec d'autres sources&nbsp;». La fiche se fait donc sans écran&nbsp;: les deux réponses à comparer et les
documents de l'enquête y sont fournis. Là où l'établissement le permet, une réponse obtenue d'une IA en classe peut s'y
ajouter et se traite de la même façon.

**Organisation**&nbsp;: 45&nbsp;minutes, en binômes&nbsp;; chaque binôme reçoit une des cinq citations (A à E) et le document qui
lui correspond. Le dossier rassemble les pièces d'une enquête déjà menée&nbsp;: les élèves jugent ce qu'elles prouvent, ils
ne refont pas la recherche. Pour la refaire, les textes sont en ligne aux adresses que donne la page mère. **Usage**&nbsp;: en classe, ou hors du cadre scolaire avec des adolescents et des adultes, en français.

**Déroulé**&nbsp;:

- **Hypothèse, 5&nbsp;min.** Seuls, sans écran&nbsp;: le sens de leur citation et une première attribution (question&nbsp;1).
- **Deux réponses, 5&nbsp;min.** Comparer deux réponses justes, inégalement documentées (question&nbsp;2).
- **Examen des pièces, 15&nbsp;min.** En binôme, dans le document fourni (question&nbsp;3).
- **Conclusion, 10&nbsp;min.** Ce que la source confirme, nuance ou laisse indécidable (question&nbsp;4).
- **Mise en commun, 10&nbsp;min.** Chaque binôme présente son cas&nbsp;; lecture de la fable de La Fontaine (question&nbsp;5)&nbsp;; synthèse en trois vérifications (question&nbsp;6).

Ces durées sont indicatives.

</div>

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

**Questions 1 et 3.** Les statuts sont ceux de la page mère, qui donne l'édition et le passage consultés. Pour chaque citation, ce qui prouve, et ce qui reste indécidable&nbsp;:

- A. **Non établie chez Voltaire** dans les sources consultées. La preuve porte sur une autre origine&nbsp;: Hall, *The Friends of Voltaire*, 1906, chapitre&nbsp;VII, p.&nbsp;199, où la phrase résume l'attitude de Voltaire, et sa lettre de 1939 qui la reconnaît pour sienne ([la fiche](/citations-celebres-verifiees/#voltaire-je-me-battrai)).
- B. **Non établie** chez Hugo dans les sources consultées. La recherche de la formule et de deux variantes dans le texte intégral de Hugo sur Wikisource n'a donné aucun résultat&nbsp;; l'idée est dans son poème, la formule courante est plus nette que son vers. Qui l'a dite le premier reste indécidable&nbsp;: Larousse cite L.&nbsp;Jourdan, et des formes voisines plus anciennes sont signalées ([la fiche](/citations-celebres-verifiees/#hugo-ouvrez-une-ecole)).
- C. **Établie**&nbsp;: *Fables*, livre&nbsp;I, «&nbsp;Le Loup et l'Agneau&nbsp;», premier vers&nbsp;; la preuve est le passage lui-même ([la fiche](/citations-celebres-verifiees/#la-fontaine-la-raison-du-plus-fort)).
- D. **Variante documentée**&nbsp;: Voltaire écrit «&nbsp;ressemblent aux girouettes&nbsp;», non «&nbsp;sont comme les girouettes&nbsp;». Le carnet prouve qu'il l'a écrite ou recopiée, pas qu'il l'a inventée&nbsp;; la phrase a aussi été prêtée à d'autres auteurs ([la fiche](/citations-celebres-verifiees/#voltaire-les-femmes-et-les-girouettes)).
- E. **Établie chez Molière**, à l'orthographe près («&nbsp;alloit&nbsp;»). Mais Molière reprend le mot de Cyrano de Bergerac&nbsp;: être dans une œuvre n'est pas en être l'origine ([la fiche](/citations-celebres-verifiees/#moliere-cette-galere)).

**Question 2.** Les deux réponses sont justes. La seconde est directement vérifiable&nbsp;: elle donne un livre, une date, un chapitre et une page, que l'on peut ouvrir (le livre est en ligne sur Project Gutenberg). La première oblige à retrouver les sources par soi-même. Aucune n'est vérifiée tant qu'on ne les a pas ouvertes&nbsp;: une référence précise peut être fausse. Les mots français ne sont pas de Hall&nbsp;: ils traduisent sa phrase anglaise. La phrase A ne peut donc pas être attestée mot pour mot dans l'édition de 1906&nbsp;; on y atteste la formule anglaise dont elle est la traduction. Le dossier ne permet d'identifier ni le traducteur ni la première attestation de la phrase en français&nbsp;: la bonne réponse est une connaissance délimitée.

**Question 4.** Une présence se prouve&nbsp;: on produit le passage. Une absence se constate dans un ensemble de textes délimité, pour les formes cherchées&nbsp;: la recherche de la formule B et de deux variantes dans le texte intégral de Hugo sur Wikisource n'a donné aucun résultat. La conclusion vaut pour ce corpus et ces formes&nbsp;; une autre tournure ou un texte absent du corpus pourraient y échapper. Ce qui ne s'établit pas, c'est qu'un auteur ne l'a jamais dite ni écrite nulle part. C'est le sens de «&nbsp;non établie dans les sources consultées&nbsp;», qui ne veut pas dire «&nbsp;fausse&nbsp;».

**Question 5.** Les «&nbsp;raisons&nbsp;» du loup tombent l'une après l'autre&nbsp;: l'agneau boit en aval, il n'était pas né l'an passé. Le loup le mange quand même, «&nbsp;sans autre forme de procès&nbsp;». La «&nbsp;raison&nbsp;» du premier vers est l'argument&nbsp;: celle du plus fort l'emporte parce qu'il est le plus fort, non parce qu'elle est juste. L'édition de 1874 le note sous le vers&nbsp;: «&nbsp;Cette phrase est prise dans un sens ironique.&nbsp;» Citée seule, la phrase peut se lire comme une approbation&nbsp;: une citation authentique peut tromper quand elle circule sans sa fable. Sur l'attribution&nbsp;: un nom connu rend la phrase plus vraisemblable et plus facile à retenir, et la source réelle se perd quand la phrase circule seule.

**Question 6.** Trois vérifications&nbsp;: **les mots** (la phrase est-elle exacte, dans sa forme d'origine&nbsp;?)&nbsp;; **la source** (quelle œuvre, quelle édition, quel passage, et qui parle&nbsp;?)&nbsp;; **le sens** (que dit le passage entier, et la phrase y veut-elle dire ce qu'on lui fait dire&nbsp;?). Les cinq citations en donnent chacune un exemple&nbsp;: les mots changent en D, la source en A, B et E, le sens en C.

</details>

</section>

Les réponses et leurs sources sont dans la page [Citations célèbres vérifiées](/citations-celebres-verifiees/), qui
examine vingt citations prêtées à cinq auteurs. Elle prolonge la vérification des citations de
[*Livresque des mots*](/livres/livresque-des-mots/). La fiche, le dossier et le corrigé sont sous licence CC&nbsp;BY&nbsp;4.0, à reprendre
en citant la source&nbsp;; les extraits d'œuvres cités dans le dossier n'en relèvent pas.

<script src="/js/fiche-imprimer.js" defer></script>
