/* fiche-commune.js — fiche de votre commune, /budget-2027-votre-commune/#fiche (option A de l'auteur, 22/10/2026 ;
   architecture v3, pièces 0124_Communes-11 et 0133_Communes-12, 23/10/2026).
   Recherche dans static/budget2027-communes/index.json, puis lecture de la fiche dans <dep>.json. Tous les nombres
   affichés viennent de ces fichiers (scripts/update_budget_communes.py) ou des attributs data-* posés par le shortcode
   fiche-commune (statuts du registre des votes, médianes des strates, documents et compte du témoin des annexes) :
   aucun chiffre de données écrit ici.
   Ordre de la fiche : 01 la réponse (le fait le plus informatif démontré, critères ci-dessous) ; 02 les principales
   mesures examinées ; 03 la conséquence DILICO (contributrices seulement) ; 04 la situation financière ; preuves repliées.
   Réponse, critères explicites, dans cet ordre (pièce 12) : (1) écart DILICO 2027, conditionnel à l'adoption de
   l'article 84 en l'état ; (2) part de la DGF dans les recettes de fonctionnement au moins 1,5 fois la médiane de la
   strate et supérieure d'au moins 5 points, dite comme une part observée, jamais comme une variation prévue ;
   (3) exonération établie (outre-mer, rang DSU) ; (4) limites explicites. L'exonération reste dans le corps de la réponse
   quand le titre porte un autre fait. Qualification graduée de l'exonération (contre-expertise PRO-20261022-215525).
   Règles : valeur absente = « non disponible », jamais zéro ; commune et intercommunalité séparées ; le seul montant
   2027 est l'écart DILICO, présenté comme un scénario conditionnel.
   Typographie : ce script écrit après french-typography.js, il pose donc lui-même les insécables (nombre + unité,
   séparateur de milliers). */
(function () {
  var root = document.getElementById('fiche-commune');
  if (!root) return;
  var L = root.dataset.lang === 'en' ? 'en' : 'fr';
  var base = root.dataset.base;
  var statuts = JSON.parse(root.dataset.statuts || '{}');
  var strates = JSON.parse(root.dataset.strates || '{}');
  var exercices = JSON.parse(root.dataset.exercices || '[]');
  var etat = root.dataset.etat;
  var SEUILS = JSON.parse(root.dataset.seuils || '{}');
  var DOCS = JSON.parse(root.dataset.documents || '{}');
  var TEMOIN = JSON.parse(root.dataset.temoin || '{}');
  var PROC = JSON.parse(root.dataset.procedure || '[]');
  var NB = ' ', FIN = ' ';
  var T = {
    fr: {
      nd: 'non disponible', pop: 'habitants', aucune: 'sans intercommunalité à fiscalité propre publiée', insee: 'code Insee',
      sous: function (a) { return 'Statuts au ' + etat + ', provisoires' + NB + ': la procédure parlementaire continue · comptes de la commune ' + a; },
      et: ' et ',
      n1: '01 — La réponse', n2: '02 — Principales mesures examinées et leur statut', n3: '03 — Comprendre la conséquence',
      n4: function (n, a) { return n + ' — Situation financière (comptes ' + a + ')'; },
      col: ['Mesure', 'Statut au ' + etat, 'Pour la commune', 'Pour préparer 2027'],
      qDil: function (n, x) { return n + NB + ': ' + x + ' de reversement DILICO différés en 2027' + NB + '?'; },
      rDil: 'C’est l’écart entre le calendrier actuel de restitution du DILICO et celui du projet de loi déposé (article 84). Le montant total restitué ne change pas' + NB + '; seule sa répartition dans le temps serait modifiée si l’article était adopté en l’état.',
      qDgf: function (n, x, m, a) { return n + NB + ': en ' + a + ', la DGF représente ' + x + ' des recettes de fonctionnement, contre ' + m + ' pour la médiane des communes de même taille'; },
      pDgf: function () { return 'Une part observée, non une prévision' + NB + ': le montant de la DGF 2027 de la commune ne sera connu qu’à la notification.'; },
      qExo: function (n) { return n + NB + ': exonérée si la contribution sur les recettes était rétablie'; },
      qRien: function (n) { return n + NB + ': aucun effet individuel chiffrable des mesures examinées à ce stade'; },
      nonContrib: 'La commune n’a pas contribué au DILICO en 2025.',
      sansDot: 'Les données de dotations de la commune ne sont pas disponibles' + NB + ': sa contribution au DILICO 2025 et une éventuelle exonération ne peuvent pas être établies ici.',
      si: function (supp) { return supp ? ' Si l’article 37, ' + statuts.cpeb + ', était rétabli dans sa rédaction initiale,' : ' Selon la rédaction initiale de l’article 37,'; },
      exoDoc: function (m) { return ' la commune serait exonérée de la contribution sur les recettes' + NB + ': ' + m + '.'; },
      dom: 'commune d’un département ou d’une région d’outre-mer',
      exoDsrcR: function (r) { return ' une exonération de la contribution sur les recettes serait possible, à confirmer' + NB + ': ' + r + NB + '; le texte ne précise pas l’année du classement retenu.'; },
      exoSeuilR: ' une exonération de la contribution sur les recettes serait possible, à confirmer' + NB + ': calculée au taux maximal de 3' + NB + '% sur ses recettes de fonctionnement 2024 publiées, la contribution resterait sous le seuil de 5' + FIN + '000' + NB + '€.',
      horsChamp: ' La commune est hors du champ de la contribution sur les recettes (article 37) du texte déposé.',
      aucunCritere: ' Aucun critère d’exonération de la contribution sur les recettes (article 37) n’est établi dans les données examinées.',
      dgfReste: ' Sa dotation globale de fonctionnement pour 2027 reste à déterminer' + NB + ': le montant individuel ne sera connu qu’à la notification.',
      aucuneAutre: ' Aucune autre mesure examinée n’a, à ce stade, d’effet individuel chiffrable pour elle.',
      autres: ' Les autres dispositions du projet de loi ne sont pas examinées ici.',
      article: 'article ', retab: NB + '; rétablissement possible',
      mDil: 'Restitution du DILICO', mCp: 'Contribution sur les recettes', mFc: 'FCTVA (TVA sur l’investissement)', mDgf: 'Dotation globale de fonctionnement',
      art: function (n) { return 'art.' + NB + n; },
      dilDiff: function (x) { return '<strong class="fiche-commune__cout">' + x + ' différés</strong> en 2027 (scénario chiffrable)'; },
      dilNon: 'non concernée' + NB + ': pas de prélèvement en 2025', dilPrep: 'comparer deux scénarios de trésorerie',
      cpSupExo: 'aucune à ce stade' + NB + '; exonérée si elle était rétablie',
      cpSupPos: 'aucune à ce stade' + NB + '; exonération possible, à confirmer, si elle était rétablie',
      cpSup: 'aucune à ce stade de la procédure', cpExo: 'exonérée selon le texte déposé', cpPos: 'exonération possible, à confirmer',
      cpMt: 'montant non déterminé', cpPrep: 'ne pas l’inscrire comme une charge certaine',
      fcSup: function (x, a) { return 'taux de 16,404' + NB + '% maintenu à ce stade' + NB + '; perçu en ' + a + NB + ': ' + x; },
      fcAct: function (x, a) { return 'baisse du taux envisagée' + NB + '; perçu en ' + a + NB + ': ' + x; },
      fcPrep: 'suivre la suite de l’examen',
      dgfCom: function (x) { return 'montant individuel 2027 encore inconnu' + NB + '; notifiée pour 2026' + NB + ': ' + x; },
      dgfPrep: 'distinguer l’hypothèse de DGF 2027 du montant qui sera notifié',
      hDil: 'Ce que la commune récupère chaque année au titre du DILICO 2025',
      actuel: 'Droit actuel', projet: 'Projet déposé', annee: 'Année', aucunV: 'aucun versement', parAn: ' par an', a2029: '2029 à 2031',
      noteDil: function (t, p) { return 'Un reversement plus faible à court terme, compensé par des versements étalés jusqu’en 2031' + NB + ': total restitué identique (' + t + ' sur ' + p + ' prélevés)' + NB + '; ce décalage peut avoir un coût de trésorerie, non chiffré ici.'; },
      aFaire: 'Pour préparer le budget 2027 →', aFaireDil: 'comparer deux scénarios de trésorerie' + NB + ': le calendrier actuel et celui qui résulterait de l’adoption de l’article 84 sans modification.',
      kEb: 'Épargne brute (marge d’autofinancement)', kEbS: 'en % des recettes de fonctionnement',
      kDh: 'Dette par habitant', kDhS: 'encours du budget principal',
      kAd: 'Capacité de désendettement théorique', kAdS: 'budget principal' + NB + '; un ratio, pas un échéancier',
      kPd: 'Part de la DGF', kPdS: 'dans les recettes de fonctionnement', med: 'médiane', ans: 'ans',
      strate: function (s) { return 'Médianes des ' + ent(s.n) + ' communes de ' + ent(s.pop_min) + ' à ' + ent(s.pop_max) + NB + 'habitants (strate de l’OFGL), exercice ' + exercices[exercices.length - 1] + NB + ': un repère descriptif, pas un groupe parfaitement comparable ni une norme de gestion.'; },
      evo: function (a0, a1) { return 'Évolution ' + a0 + '-' + a1 + ' et détail des comptes'; }, evo1: function (a) { return 'Détail des comptes ' + a; },
      t1s: 'Comptes du budget principal publiés par l’Observatoire des finances et de la gestion publique locales (OFGL). Budgets annexes et intercommunalité non compris.',
      colG: ['', '', '', 'Médiane de la strate'],
      rf: 'Recettes de fonctionnement', eb: 'Épargne brute', teb: 'Taux d’épargne brute', dette: 'Encours de dette', dh: 'Dette par habitant', ad: 'Capacité de désendettement théorique (années, budget principal)', dgf: 'Dotation globale de fonctionnement (comptabilisée)', pdgf: 'Part de la DGF dans les recettes de fonctionnement', fctva: 'FCTVA perçu', eq: 'Dépenses d’équipement', eqh: 'Dépenses d’équipement par habitant',
      sans24: function (a) { return 'Pas de compte ' + a + ' publié par l’OFGL pour ce code Insee (commune créée ou modifiée récemment, ou compte non transmis)' + NB + ': l’évolution ne peut pas être affichée.'; },
      cn: function (a0, a1) { return 'Commune nouvelle (elle perçoit la dotation en faveur des communes nouvelles)' + NB + ': si son périmètre a changé entre ' + a0 + ' et ' + a1 + ', les deux exercices ne sont pas directement comparables.'; },
      calc: 'Comprendre le calcul et vérifier les sources',
      cDil: function (p, r, b, e, l) { return '<strong>DILICO</strong>' + NB + ': prélèvement 2025 de ' + p + ' (' + l.arrete_dilico + ', annexe' + NB + ': ' + l.dil + ')' + NB + '; restitution de 90' + NB + '% par tiers, soit ' + r + ' par an en 2026, 2027 et 2028 selon le droit actuel (' + l.lf2025_186 + NB + '; versement 2026' + NB + ': ' + l.rev + ')' + NB + '; selon l’article 84 du ' + l.plf + ', 12' + NB + '% de la contribution, soit ' + b + ' par an de 2027 à 2031. Écart 2027' + NB + ': ' + r + ' − ' + b + ' = ' + e + '.'; },
      cDilNon: function (l) { return '<strong>DILICO</strong>' + NB + ': la commune ne figure pas dans l’annexe du prélèvement 2025 (' + l.dil + NB + '; ' + l.arrete_dilico + ').'; },
      cDgf: function (x, comp, dcn, l) { return '<strong>DGF notifiée pour 2026</strong>' + NB + ': ' + x + (comp ? ' (' + comp + ')' : '') + NB + '; annexe de l’arrêté, ' + l.dgf + '.' + (dcn ? ' Dotation en faveur des communes nouvelles, distincte de la DGF' + NB + ': ' + dcn + '.' : '') + ' La DGF des comptes est la DGF comptabilisée' + NB + ': exercice et nature différents.'; },
      cCtl: function (n, l) { return '<strong>Contrôles</strong>' + NB + ': montants DILICO et DGF relus, commune par commune, dans les annexes des arrêtés publiées au Journal officiel (' + n + ' montants, aucun écart au-delà de l’arrondi à l’euro)' + NB + '; comptes' + NB + ': ' + l.ofgl + ', budget principal' + NB + '; dotations' + NB + ': ' + l.ofgl_dot + '.'; },
      cRat: '<strong>Ratios</strong>' + NB + ': épargne brute (marge d’autofinancement) = recettes réelles moins dépenses réelles de fonctionnement, rapportée aux recettes de fonctionnement' + NB + '; capacité de désendettement = encours de dette / épargne brute' + NB + '; part de la DGF = DGF comptabilisée / recettes de fonctionnement' + NB + '; budget principal seul.',
      detail: 'Le détail de chaque mesure pour la commune',
      cpeb: 'Contribution progressive (art.' + NB + '37)', fctvaM: 'FCTVA (art.' + NB + '35)', dgfM: 'DGF (art.' + NB + '34)', dilicoM: 'DILICO (art.' + NB + '84)', tvaM: 'TVA affectée (art.' + NB + '36)',
      cpebTxt: function () { return 'Exonération non déterminable' + NB + ': commune absente du jeu des dotations. Montant non déterminé' + NB + ': il dépend du rang de la commune parmi toutes les autres, sur un indice de potentiel financier et de revenu' + NB + '; assiette' + NB + ': recettes réelles de fonctionnement de 2024, retraitées.'; },
      epciC: function (n) { return 'L’intercommunalité (' + n + ') était visée par une contribution distincte, qui n’est pas imputée à la commune.'; },
      fctvaTxt: function (x, a) { return 'FCTVA perçu en ' + a + NB + ': ' + x + ' (montant passé). Le texte déposé abaissait le taux de 16,404' + NB + '% à 11,404' + NB + '% pour les attributions versées à partir de 2027, sauf pour les dépenses de transition écologique et de voirie' + NB + '; l’effet pour la commune dépend de ses investissements à venir et de leur nature, non connus ici.'; },
      dgfTxt: function (x, a) { return 'DGF ' + a + NB + ': ' + x + '. Montant 2027 non déterminable' + NB + ': il dépend de la loi votée et de la répartition du Comité des finances locales.'; },
      dilicoTxt: function (n) { return 'DILICO 2025' + NB + ': contribution de la commune non disponible. DILICO 2026' + NB + ': les communes n’y contribuent pas' + (n ? NB + '; l’intercommunalité (' + n + ') peut y avoir contribué.' : '.'); },
      dilicoNon: 'DILICO 2025' + NB + ': la commune n’était pas contributrice' + NB + '; aucun reversement ne la concerne.',
      dilicoOui: function (p, r, b) { return 'DILICO 2025' + NB + ': ' + p + ' mis en réserve' + NB + '; la commune en récupère 90' + NB + '%. Reçu en 2026' + NB + ': ' + r + '. Selon le droit actuel, la même somme en 2027 et en 2028' + NB + '; selon le projet déposé, ' + b + ' par an de 2027 à 2031.'; },
      dilico26: function (n) { return ' DILICO 2026' + NB + ': les communes n’y contribuent pas' + (n ? NB + '; l’intercommunalité (' + n + ') peut y avoir contribué.' : '.'); },
      dgfNot: function (x, comp, dcn) { return 'DGF 2026 notifiée (base de la DGCL, via l’OFGL)' + NB + ': ' + x + (comp ? ' (' + comp + ')' : '') + '.' + (dcn ? ' Dotation en faveur des communes nouvelles, distincte de la DGF' + NB + ': ' + dcn + '.' : '') + ' Le tableau des comptes donne la DGF comptabilisée' + NB + ': exercice et nature différents. Montant 2027 non déterminable' + NB + ': il dépend de la loi votée et de la répartition du Comité des finances locales.'; },
      comp: {forf: 'dotation forfaitaire', dsu: 'dotation de solidarité urbaine', dsr: 'dotation de solidarité rurale', dnp: 'dotation nationale de péréquation', dacom: 'dotation d’aménagement des communes d’outre-mer'},
      classe: {r_dsu10: '2026 de la dotation de solidarité urbaine (communes de 10' + FIN + '000 habitants et plus)', r_dsu5: '2026 de la dotation de solidarité urbaine (communes de 5' + FIN + '000 à 9' + FIN + '999 habitants)', r_dsrc: '2026 selon l’indice de la fraction cible de la dotation de solidarité rurale'},
      rang: function (k, r, n) { return 'rang ' + ent(r) + ' au classement ' + T.classe[k] + ', ' + (r <= n ? 'parmi les ' : 'hors des ') + ent(n) + ' premières'; },
      exoDom: function (n) { return 'Exonérée par le texte déposé, qui exonérait les communes des départements et régions d’outre-mer' + (n ? ', comme leurs intercommunalités (' + n + ').' : '.'); },
      exoRang: function (r) { return 'Exonérée selon le classement publié par la DGCL (via l’OFGL)' + NB + ': ' + r + ', que le texte déposé exonérait.'; },
      exoSeuil: function (x) { return 'Exonération possible, à confirmer' + NB + ': calculée au taux maximal de 3' + NB + '% sur les recettes de fonctionnement 2024 publiées (' + x + '), la contribution resterait sous le seuil de 5' + FIN + '000' + NB + '€ en dessous duquel le texte déposé exonérait' + NB + '; mais l’assiette légale, non publiée, peut différer de ces recettes.'; },
      exoCom: 'Hors du champ du texte déposé, qui ne classait que les communes de métropole et des départements et régions d’outre-mer.',
      nonExo: function (r) { return 'Aucun critère d’exonération établi dans les données examinées' + (r ? NB + ': ' + r : '') + '. Le seuil de 5' + FIN + '000' + NB + '€ dépend du taux et de l’assiette légale, non déterminables ici.'; },
      cpebMt: ' Montant non déterminé' + NB + ': il dépend du rang de la commune parmi toutes les autres, sur un indice de potentiel financier et de revenu' + NB + '; assiette' + NB + ': recettes réelles de fonctionnement de 2024, retraitées.',
      tvaTxt: 'À vérifier' + NB + ': fraction de TVA perçue par la commune, ou par son intercommunalité.',
      exoDsrc: function (r) { return 'Exonération possible, à confirmer' + NB + ': ' + r + ', que le texte déposé exonérait' + NB + '; mais il ne précise pas l’année du classement retenu pour 2027.'; },
      paris: ' Ville de Paris' + NB + ': le texte déposé ne retenait que 70,87' + NB + '% de ses recettes pour cette contribution, et la soumettait en outre, sur 29,13' + NB + '% de ses recettes, à la contribution des départements (taux de 0 à 2' + NB + '% selon un indice de fragilité sociale).',
      nc: 'non calculable (épargne brute nulle ou négative)',
      texte: 'Où en est le texte', echeance: 'Prochaine échéance' + NB + ': ', texteL: 'Le projet déposé et ce qu’il en reste, mesure par mesure',
      lien: 'Copier le lien', copie: 'Lien copié', imprimer: 'Imprimer', transmettre: 'Transmettre', aucun: 'Aucune commune trouvée.',
      objetT: function (n) { return 'Budget 2027 : la fiche de ' + n; },
      source: function (r) { return 'Sources' + NB + ': OFGL, comptes des communes (DGFiP) et dotations des communes (DGCL), données relevées le ' + r + NB + '; annexes des arrêtés publiées au Journal officiel' + NB + '; CSV complet et méthode en bas de page.'; }
    },
    en: {
      nd: 'not available', pop: 'inhabitants', aucune: 'no inter-municipal body with own tax published', insee: 'INSEE code',
      sous: function (a) { return 'Statuses as of ' + etat + ', provisional: the parliamentary procedure continues · municipal accounts ' + a; },
      et: ' and ',
      n1: '01 — The answer', n2: '02 — Main measures examined and their status', n3: '03 — Understanding the consequence',
      n4: function (n, a) { return n + ' — Financial position (' + a + ' accounts)'; },
      col: ['Measure', 'Status as of ' + etat, 'For the municipality', 'To prepare 2027'],
      qDil: function (n, x) { return n + ': ' + x + ' of DILICO repayment deferred in 2027?'; },
      rDil: 'This is the gap between the current DILICO repayment schedule and that of the bill as tabled (article 84). The total repaid does not change; only its spread over time would change if the article were adopted as it stands.',
      qDgf: function (n, x, m, a) { return n + ': in ' + a + ', the DGF makes up ' + x + ' of operating revenue, against ' + m + ' for the median municipality of the same size'; },
      pDgf: function () { return 'An observed share, not a forecast: the municipality’s 2027 DGF will be known only on notification.'; },
      qExo: function (n) { return n + ': exempt if the revenue contribution were reinstated'; },
      qRien: function (n) { return n + ': no individual effect of the measures examined can be quantified at this stage'; },
      nonContrib: 'The municipality did not contribute to the 2025 DILICO.',
      sansDot: 'The municipality’s grant data are not available: its 2025 DILICO contribution and any exemption cannot be established here.',
      si: function (supp) { return supp ? ' If article 37, ' + statuts.cpeb + ', were reinstated as originally drafted,' : ' Under the original drafting of article 37,'; },
      exoDoc: function (m) { return ' the municipality would be exempt from the revenue contribution: ' + m + '.'; },
      dom: 'a municipality in an overseas department or region',
      exoDsrcR: function (r) { return ' an exemption from the revenue contribution would be possible, to be confirmed: ' + r + '; the text does not specify the year of the ranking used.'; },
      exoSeuilR: ' an exemption from the revenue contribution would be possible, to be confirmed: computed at the maximum 3% rate on its published 2024 operating revenue, the contribution would stay under the €5,000 threshold.',
      horsChamp: ' The municipality is outside the scope of the revenue contribution (article 37) of the bill as tabled.',
      aucunCritere: ' No exemption criterion for the revenue contribution (article 37) is established in the data examined.',
      dgfReste: ' Its general operating grant for 2027 remains to be determined: the individual amount will be known only on notification.',
      aucuneAutre: ' No other measure examined has, at this stage, an individual effect that can be quantified for it.',
      autres: ' Other provisions of the bill are not examined here.',
      article: 'article ', retab: '; may be reinstated',
      mDil: 'DILICO repayment', mCp: 'Revenue contribution', mFc: 'FCTVA (VAT on investment)', mDgf: 'General operating grant',
      art: function (n) { return 'art. ' + n; },
      dilDiff: function (x) { return '<strong class="fiche-commune__cout">' + x + ' deferred</strong> in 2027 (quantifiable scenario)'; },
      dilNon: 'not concerned: no levy in 2025', dilPrep: 'compare two cash-flow scenarios',
      cpSupExo: 'none at this stage; exempt if it were reinstated',
      cpSupPos: 'none at this stage; exemption possible, to be confirmed, if it were reinstated',
      cpSup: 'none at this stage of the procedure', cpExo: 'exempt under the bill as tabled', cpPos: 'exemption possible, to be confirmed',
      cpMt: 'amount not determined', cpPrep: 'do not enter it as a certain charge',
      fcSup: function (x, a) { return '16.404% rate maintained at this stage; received in ' + a + ': ' + x; },
      fcAct: function (x, a) { return 'rate cut envisaged; received in ' + a + ': ' + x; },
      fcPrep: 'follow the rest of the examination',
      dgfCom: function (x) { return 'individual 2027 amount still unknown; notified for 2026: ' + x; },
      dgfPrep: 'distinguish the 2027 DGF assumption from the amount that will be notified',
      hDil: 'What the municipality recovers each year from the 2025 DILICO',
      actuel: 'Current law', projet: 'Bill as tabled', annee: 'Year', aucunV: 'no payment', parAn: ' a year', a2029: '2029 to 2031',
      noteDil: function (t, p) { return 'A smaller repayment in the short term, offset by payments spread until 2031: the same total repaid (' + t + ' of ' + p + ' levied); this shift may carry a cash-flow cost, not quantified here.'; },
      aFaire: 'To prepare the 2027 budget →', aFaireDil: 'compare two cash-flow scenarios: the current schedule and the one that would result from adopting article 84 unchanged.',
      kEb: 'Gross savings (self-financing margin)', kEbS: 'as % of operating revenue',
      kDh: 'Debt per inhabitant', kDhS: 'main-budget debt outstanding',
      kAd: 'Theoretical debt-repayment capacity', kAdS: 'main budget; a ratio, not a schedule',
      kPd: 'Share of the DGF', kPdS: 'in operating revenue', med: 'median', ans: 'years',
      strate: function (s) { return 'Medians of the ' + ent(s.n) + ' municipalities of ' + ent(s.pop_min) + ' to ' + ent(s.pop_max) + ' inhabitants (OFGL size band), ' + exercices[exercices.length - 1] + ': a descriptive marker, not a perfectly comparable group nor a management norm.'; },
      evo: function (a0, a1) { return 'Change ' + a0 + '-' + a1 + ' and detailed accounts'; }, evo1: function (a) { return 'Detailed accounts ' + a; },
      t1s: 'Main-budget accounts published by the Observatory of Local Public Finance and Management (OFGL). Ancillary budgets and the inter-municipal body excluded.',
      colG: ['', '', '', 'Median of the size band'],
      rf: 'Operating revenue', eb: 'Gross savings', teb: 'Gross savings rate', dette: 'Debt outstanding', dh: 'Debt per inhabitant', ad: 'Theoretical debt-repayment capacity (years, main budget)', dgf: 'General operating grant (DGF, recorded)', pdgf: 'Share of the DGF in operating revenue', fctva: 'FCTVA received', eq: 'Capital spending', eqh: 'Capital spending per inhabitant',
      sans24: function (a) { return 'No ' + a + ' account published by the OFGL for this INSEE code (municipality recently created or changed, or account not filed): the change cannot be shown.'; },
      cn: function (a0, a1) { return 'New municipality (it receives the grant for new municipalities): if its boundaries changed between ' + a0 + ' and ' + a1 + ', the two years are not directly comparable.'; },
      calc: 'Understanding the calculation and checking the sources',
      cDil: function (p, r, b, e, l) { return '<strong>DILICO</strong>: 2025 levy of ' + p + ' (' + l.arrete_dilico + ', annex: ' + l.dil + '); 90% repaid in thirds, i.e. ' + r + ' a year in 2026, 2027 and 2028 under current law (' + l.lf2025_186 + '; 2026 payment: ' + l.rev + '); under article 84 of the ' + l.plf + ', 12% of the contribution, i.e. ' + b + ' a year from 2027 to 2031. 2027 gap: ' + r + ' − ' + b + ' = ' + e + '.'; },
      cDilNon: function (l) { return '<strong>DILICO</strong>: the municipality is not in the annex of the 2025 levy (' + l.dil + '; ' + l.arrete_dilico + ').'; },
      cDgf: function (x, comp, dcn, l) { return '<strong>DGF notified for 2026</strong>: ' + x + (comp ? ' (' + comp + ')' : '') + '; annex to the order, ' + l.dgf + '.' + (dcn ? ' Grant for new municipalities, separate from the DGF: ' + dcn + '.' : '') + ' The DGF in the accounts is the DGF recorded: a different year and nature.'; },
      cCtl: function (n, l) { return '<strong>Checks</strong>: DILICO and DGF amounts read again, municipality by municipality, in the annexes to the orders published in the Official Journal (' + n + ' amounts, no gap beyond rounding to the euro); accounts: ' + l.ofgl + ', main budget; grants: ' + l.ofgl_dot + '.'; },
      cRat: '<strong>Ratios</strong>: gross savings (self-financing margin) = real operating revenue minus real operating expenditure, divided by operating revenue; debt-repayment capacity = debt outstanding / gross savings; share of the DGF = DGF recorded / operating revenue; main budget only.',
      detail: 'Each measure in detail for the municipality',
      cpeb: 'Progressive contribution (art. 37)', fctvaM: 'FCTVA (art. 35)', dgfM: 'DGF (art. 34)', dilicoM: 'DILICO (art. 84)', tvaM: 'Assigned VAT (art. 36)',
      cpebTxt: function () { return 'Exemption not determinable: the municipality is missing from the grants dataset. Amount not determined: it depends on the municipality’s rank among all others, on an index of financial potential and income; base: 2024 real operating revenue, adjusted.'; },
      epciC: function (n) { return 'The inter-municipal body (' + n + ') was targeted by a separate contribution, which is not attributed to the municipality.'; },
      fctvaTxt: function (x, a) { return 'FCTVA received in ' + a + ': ' + x + ' (past amount). The bill as tabled lowered the rate from 16.404% to 11.404% for payments made from 2027, except for ecological transition and road spending; the effect for the municipality depends on its future investment and its nature, not known here.'; },
      dgfTxt: function (x, a) { return 'DGF ' + a + ': ' + x + '. Amount for 2027 not determinable: it depends on the act as passed and on the Local Finance Committee’s distribution.'; },
      dilicoTxt: function (n) { return '2025 DILICO: the municipality’s contribution is not available. 2026 DILICO: municipalities do not contribute' + (n ? '; the inter-municipal body (' + n + ') may have.' : '.'); },
      dilicoNon: '2025 DILICO: the municipality was not a contributor; no repayment concerns it.',
      dilicoOui: function (p, r, b) { return '2025 DILICO: ' + p + ' placed in reserve; the municipality recovers 90% of it. Received in 2026: ' + r + '. Under current law, the same sum in 2027 and 2028; under the bill as tabled, ' + b + ' a year from 2027 to 2031.'; },
      dilico26: function (n) { return ' 2026 DILICO: municipalities do not contribute' + (n ? '; the inter-municipal body (' + n + ') may have.' : '.'); },
      dgfNot: function (x, comp, dcn) { return '2026 DGF notified (DGCL database, via the OFGL): ' + x + (comp ? ' (' + comp + ')' : '') + '.' + (dcn ? ' Grant for new municipalities, separate from the DGF: ' + dcn + '.' : '') + ' The accounts table gives the DGF recorded: a different year and nature. Amount for 2027 not determinable: it depends on the act as passed and on the Local Finance Committee’s distribution.'; },
      comp: {forf: 'flat-rate grant', dsu: 'urban solidarity grant', dsr: 'rural solidarity grant', dnp: 'national equalisation grant', dacom: 'overseas municipalities grant'},
      classe: {r_dsu10: '2026 ranking for the urban solidarity grant (municipalities of 10,000 inhabitants or more)', r_dsu5: '2026 ranking for the urban solidarity grant (municipalities of 5,000 to 9,999 inhabitants)', r_dsrc: '2026 ranking by the index of the targeted share of the rural solidarity grant'},
      rang: function (k, r, n) { return 'ranked ' + ent(r) + ' in the ' + T.classe[k] + ', ' + (r <= n ? 'within' : 'outside') + ' the first ' + ent(n); },
      exoDom: function (n) { return 'Exempt under the bill as tabled, which exempted municipalities in overseas departments and regions' + (n ? ', like their inter-municipal bodies (' + n + ').' : '.'); },
      exoRang: function (r) { return 'Exempt according to the ranking published by the DGCL (via the OFGL): ' + r + ', which the bill as tabled exempted.'; },
      exoSeuil: function (x) { return 'Exemption possible, to be confirmed: computed at the maximum 3% rate on published 2024 operating revenue (' + x + '), the contribution would stay under the €5,000 threshold below which the bill as tabled exempted; but the legal base, not published, may differ from this revenue.'; },
      exoCom: 'Outside the scope of the bill as tabled, which ranked only municipalities in metropolitan France and in overseas departments and regions.',
      nonExo: function (r) { return 'No exemption criterion established in the data examined' + (r ? ': ' + r : '') + '. The €5,000 threshold depends on the rate and the legal base, not determinable here.'; },
      cpebMt: ' Amount not determined: it depends on the municipality’s rank among all others, on an index of financial potential and income; base: 2024 real operating revenue, adjusted.',
      tvaTxt: 'To check: a share of VAT received by the municipality, or by its inter-municipal body.',
      exoDsrc: function (r) { return 'Exemption possible, to be confirmed: ' + r + ', which the bill as tabled exempted; but it does not specify the year of the ranking used for 2027.'; },
      paris: ' City of Paris: the bill as tabled took only 70.87% of its revenue into account for this contribution, and also subjected it, on 29.13% of its revenue, to the departments’ contribution (rate from 0 to 2% according to a social fragility index).',
      nc: 'not calculable (gross savings zero or negative)',
      texte: 'Where the text stands', echeance: 'Next step: ', texteL: 'The bill as tabled and what remains of it, measure by measure',
      lien: 'Copy the link', copie: 'Link copied', imprimer: 'Print', transmettre: 'Pass on', aucun: 'No municipality found.',
      objetT: function (n) { return '2027 budget: the sheet for ' + n; },
      source: function (r) { return 'Sources: OFGL, municipal accounts (DGFiP) and municipal grants (DGCL), data retrieved on ' + r + '; annexes to the orders published in the Official Journal; full CSV and method at the foot of the page.'; }
    }
  }[L];

  function ent(x) { // entier, separateur de milliers insecable fin
    if (x === null || x === undefined) return T.nd;
    return Math.round(x).toString().replace(/\B(?=(\d{3})+(?!\d))/g, L === 'fr' ? FIN : ',');
  }
  function dec(x, n) { // decimal, partie entiere groupee comme ent() ; nombre rond a la precision affichee : sans
    // decimale (auteur, 23/10/2026 : « 1 an, 2 ans », jamais « 1,0 an »)
    var s = x.toFixed(n).split('.'), e = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, L === 'fr' ? FIN : ',');
    return s.length > 1 && /[1-9]/.test(s[1]) ? e + (L === 'fr' ? ',' : '.') + s[1] : e;
  }
  function meur(x, ref) { // millions d'euros ; sous le million, euros a la centaine (« 0,02 M€ » effacait l'ordre de grandeur).
    // ref : plus grande valeur de la ligne, pour qu'une ligne du tableau garde une seule unite.
    if (x === null || x === undefined) return T.nd;
    if (Math.abs(ref === undefined ? x : ref) < 1e6) return eur(Math.round(x / 100) * 100);
    var m = x / 1e6, n = Math.abs(m) < 9.995 ? 2 : 1;  // 9 995 000 € arrondi a deux decimales donnerait « 10,00 »
    return L === 'fr' ? dec(m, n) + NB + 'M€' : '€' + dec(m, n) + 'm';
  }
  function eur(x) { // sous 10 €, deux decimales : un « 0 € » se lirait comme un zero publie
    if (x === null || x === undefined) return T.nd;
    var v = (x !== 0 && Math.abs(x) < 10) ? dec(x, 2) : ent(x);
    return L === 'fr' ? v + NB + '€' : '€' + v;
  }
  function court(x) { return Math.abs(x) < 1e6 ? eur(x) : meur(x); } // etiquette de barre : euros sous le million
  function pct(x) { if (x === null || x === undefined) return T.nd; return L === 'fr' ? dec(100 * x, 1) + NB + '%' : dec(100 * x, 1) + '%'; }
  function ans(x) { if (x === null || x === undefined) return T.nd; if (x === 'nc') return T.nc; return dec(x, 1); }
  function ansU(x) { // français : « an » au singulier sous 2 (« 1,9 an »), comme l'accord de « point » du module de langue
    var a = ans(x);
    if (x === null || x === undefined || x === 'nc') return a;
    return a + NB + (L === 'fr' && Math.abs(x) < 2 ? 'an' : T.ans);
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]; }); }
  function norm(s) { return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[-'’ ]+/g, ' ').trim(); }
  function lien(k) { var d = DOCS[k]; return d ? '<a href="' + esc(d.url) + '">' + esc(L === 'en' ? d.titre_en : d.titre) + '</a>' : ''; }
  // Article supprime ou non adopte : la phrase devient conditionnelle (« si … était rétabli ») ; sinon, texte en discussion.
  function supprime(k) { return /supprim|non adopt|deleted|not adopted/i.test(statuts[k] || ''); }

  var index = null, champ = document.getElementById('fiche-commune-champ'), liste = document.getElementById('fiche-commune-liste'),
      sortie = document.getElementById('fiche-commune-resultat'), cacheDep = {};
  function chargerIndex() {
    if (index) return Promise.resolve(index);
    return fetch(base + 'index.json').then(function (r) { return r.json(); }).then(function (d) {
      index = d.map(function (c) { return {insee: c[0], nom: c[1], dep: c[2], cle: norm(c[1])}; });
      return index;
    });
  }
  function chercher(q) {
    var n = norm(q);
    if (n.length < 2) return [];
    var exact = [], debut = [], autres = [];
    index.forEach(function (c) {
      if (c.insee === q.trim().toUpperCase()) exact.push(c);
      else if (c.cle === n) exact.push(c);
      else if (c.cle.indexOf(n) === 0) debut.push(c);
      else if (c.cle.indexOf(n) > 0 || c.dep === n.toUpperCase()) autres.push(c);
    });
    return exact.concat(debut, autres).slice(0, 12);
  }
  function proposer() {
    chargerIndex().then(function () {
      var r = chercher(champ.value);
      liste.innerHTML = r.length ? r.map(function (c, k) {
        return '<li role="option" tabindex="-1" data-insee="' + esc(c.insee) + '" data-dep="' + esc(c.dep) + '">' + esc(c.nom) + ' <span>(' + esc(c.dep) + ', ' + esc(c.insee) + ')</span></li>';
      }).join('') : (champ.value.trim().length > 1 ? '<li class="fiche-commune__vide">' + T.aucun + '</li>' : '');
      liste.hidden = !liste.innerHTML;
    });
  }
  function depDe(insee) { // a partir de l'index (homonymes : le code Insee tranche)
    var c = index.filter(function (x) { return x.insee === insee; })[0];
    return c ? c.dep : null;
  }
  function afficher(insee) {
    chargerIndex().then(function () {
      var dep = depDe(insee);
      if (!dep) { sortie.innerHTML = '<p>' + T.aucun + '</p>'; return; }
      (cacheDep[dep] ? Promise.resolve(cacheDep[dep]) : fetch(base + dep + '.json').then(function (r) { return r.json(); }).then(function (d) { cacheDep[dep] = d; return d; }))
        .then(function (d) { rendre(insee, d[insee]); });
    });
  }
  // data-col : libellé de la colonne, repris devant chaque valeur quand le tableau devient une carte sur téléphone.
  var SEP = L === 'fr' ? NB + ': ' : ': ';
  function ligne(lib, a, b, med) {
    var a0 = String(exercices[0]), a1 = String(exercices[exercices.length - 1]), md = L === 'fr' ? 'médiane de la strate' : 'size-band median';
    var td = function (lab, x) { return '<span role="cell" class="fiche-commune__val"' + (x ? ' data-col="' + lab + SEP + '">' + x : '>') + '</span>'; };
    return '<div role="row" class="fiche-commune__ligne"><span role="rowheader" class="fiche-commune__lib">' + lib + '</span>' + td(a0, a) + td(a1, b) + td(md, med) + '</div>';
  }
  function bloc(num, corps, cls) { return '<section class="fiche-commune__bloc' + (cls ? ' ' + cls : '') + '"><p class="fiche-commune__num">' + num + '</p>' + corps + '</section>'; }

  function rendre(insee, c) {
    if (!c) { sortie.innerHTML = '<p>' + T.aucun + '</p>'; return; }
    var a0 = String(exercices[0]), a1 = String(exercices[exercices.length - 1]);
    var has0 = !!c.v[a0], v0 = c.v[a0] || {}, v1 = c.v[a1] || {}, s = strates[c.strate] || {}, p = c.pop;
    var div = function (x, y) { return (x === null || x === undefined || !y) ? null : x / y; };
    var taux = function (v) { return (v.rf && v.eb !== null && v.eb !== undefined) ? v.eb / v.rf : null; };
    var annees = function (v) { // dette / epargne brute ; epargne nulle ou negative : ratio sans sens, dit comme tel
      if (v.dette === null || v.dette === undefined || v.eb === null || v.eb === undefined) return null;
      return v.eb > 0 ? v.dette / v.eb : 'nc'; };
    var d = c.d, nom = esc(c.nom), nomE = c.epci_nom ? esc(c.epci_nom) : null;
    var dil = d && d.dil, rev = d ? d.rev : null, b = d ? 0.12 * d.dil : null;
    var ecart = dil ? Math.round(rev) - Math.round(b) : 0;
    var partDgf = div(v1.dgf, v1.rf), medDgf = s.part_dgf;
    var rangTxt = d && d.rang ? T.rang(d.rang[0], d.rang[1], SEUILS[d.rang[0]]) : '';
    var exoDoc = d && (d.exo === 'dom' || d.exo === 'r_dsu10' || d.exo === 'r_dsu5');
    var exoPos = d && (d.exo === 'r_dsrc' || d.exo === 'seuil');
    var sup = supprime('cpeb');
    var L_ = {}; Object.keys(DOCS).forEach(function (k) { L_[k] = lien(k); });

    // 01 — la réponse
    var phraseExo;
    if (!d) phraseExo = '';
    else if (exoDoc) phraseExo = T.si(sup) + T.exoDoc(d.exo === 'dom' ? T.dom : rangTxt);
    else if (d.exo === 'r_dsrc') phraseExo = T.si(sup) + T.exoDsrcR(rangTxt);
    else if (d.exo === 'seuil') phraseExo = T.si(sup) + T.exoSeuilR;
    else if (d.om === '03') phraseExo = T.horsChamp;
    else phraseExo = T.aucunCritere;
    var q, rep, prec = '';
    var faitDgf = partDgf !== null && medDgf !== null && medDgf !== undefined && partDgf >= 1.5 * medDgf && partDgf - medDgf >= 0.05;
    if (dil) { q = T.qDil(nom, eur(ecart)); rep = T.rDil; }
    else if (!d) { q = T.qRien(nom); rep = T.sansDot + T.dgfReste + T.autres; }
    else if (faitDgf) { q = T.qDgf(nom, pct(partDgf), pct(medDgf), a1); rep = T.nonContrib + phraseExo; prec = T.pDgf(); }
    else if (exoDoc) { q = T.qExo(nom); rep = T.nonContrib + phraseExo + T.aucuneAutre + T.dgfReste; }
    else { q = T.qRien(nom); rep = T.nonContrib + phraseExo + T.dgfReste + T.autres; }

    var h = '';
    h += '<header class="fiche-commune__tete"><div><h3>' + nom + '</h3><p class="fiche-commune__id">' + ent(p) + NB + T.pop + ' · ' + (nomE || T.aucune) + ' · ' + T.insee + ' ' + esc(insee) + '</p></div>';
    var urlFiche = location.origin + location.pathname + '?insee=' + encodeURIComponent(insee) + '#fiche';
    h += '<p class="fiche-commune__actions"><button type="button" data-action="imprimer">' + T.imprimer + '</button><button type="button" data-action="copier">' + T.lien + '</button>' +
      '<a href="mailto:?subject=' + encodeURIComponent(T.objetT(c.nom)) + '&amp;body=' + encodeURIComponent(urlFiche) + '">' + T.transmettre + '</a></p></header>';
    h += '<p class="fiche-commune__sous">' + T.sous(has0 ? a0 + T.et + a1 : a1) + '</p>';
    h += bloc(T.n1, '<div class="fiche-commune__reponse"><p class="fiche-commune__q">' + q + '</p><p>' + rep + '</p></div>' + (prec ? '<p class="fiche-commune__note">' + prec + '</p>' : ''));

    // 02 — principales mesures examinées
    var st = function (k) { return T.article + esc(statuts[k]) + (supprime(k) ? T.retab : ''); };
    var lignesM = [
      [T.mDil, T.art(84), st('dilico'), !d ? T.nd : (dil ? T.dilDiff(eur(ecart)) : T.dilNon), dil ? T.dilPrep : '—'],
      [T.mCp, T.art(37), st('cpeb'), !d ? T.nd : (sup ? (exoDoc ? T.cpSupExo : exoPos ? T.cpSupPos : T.cpSup) : (exoDoc ? T.cpExo : exoPos ? T.cpPos : T.cpMt)), T.cpPrep],
      [T.mFc, T.art(35), st('fctva'), (supprime('fctva') ? T.fcSup : T.fcAct)(meur(v1.fctva), a1), T.fcPrep],
      [T.mDgf, T.art(34), st('dgf'), d && d.dgf !== null ? T.dgfCom(meur(d.dgf)) : T.nd, T.dgfPrep]
    ];
    var tab = '<div class="fiche-commune__mesures" role="table"><div role="row" class="fiche-commune__mrow fiche-commune__mtete">' +
      T.col.map(function (x) { return '<span role="columnheader">' + x + '</span>'; }).join('') + '</div>';
    tab += lignesM.map(function (m) {
      return '<div role="row" class="fiche-commune__mrow"><span role="rowheader" class="fiche-commune__mnom">' + m[0] + '<span>' + m[1] + '</span></span>' +
        '<span role="cell" class="fiche-commune__statut" data-col="' + T.col[1] + '">' + m[2] + '</span>' +
        '<span role="cell" data-col="' + T.col[2] + '">' + m[3] + '</span>' +
        '<span role="cell" data-col="' + T.col[3] + '">' + m[4] + '</span></div>';
    }).join('') + '</div>';
    h += bloc(T.n2, tab);

    // 03 — la conséquence DILICO (contributrices)
    var n4 = '03';
    if (dil) {
      n4 = '04';
      var annesX = [2026, 2027, 2028, 2029, 2030, 2031];
      var act = {2026: rev, 2027: rev, 2028: rev}, pro = {2026: rev, 2027: b, 2028: b, 2029: b, 2030: b, 2031: b};
      var vmax = Math.max(rev, b);
      var barres = function (serie, cls) {
        return annesX.map(function (a) {
          var x = serie[a];
          return '<div class="fiche-commune__col"><span class="fiche-commune__v">' + (x ? court(x) : '—') + '</span><div class="fiche-commune__barre ' + cls + '" style="height:' + (x ? Math.round(100 * x / vmax) : 0) + '%"></div><span class="fiche-commune__an">' + a + '</span></div>';
        }).join('');
      };
      var corps = '<h4>' + T.hDil + '</h4>' +
        '<div class="fiche-commune__rangee" aria-hidden="true"><p>' + T.actuel + '</p><div class="fiche-commune__cols">' + barres(act, 'actuel') + '</div></div>' +
        '<div class="fiche-commune__rangee" aria-hidden="true"><p>' + T.projet + '</p><div class="fiche-commune__cols">' + barres(pro, 'projet') + '</div></div>' +
        '<div class="fiche-commune__cal" role="table" aria-label="' + T.hDil + '">' +
        '<div role="row" class="fiche-commune__crow fiche-commune__ctete"><span role="columnheader">' + T.annee + '</span><span role="columnheader">' + T.actuel + '</span><span role="columnheader">' + T.projet + '</span></div>' +
        [['2026', eur(rev), eur(rev)], ['2027', eur(rev), '<span class="fiche-commune__cout">' + eur(b) + '</span>'], ['2028', eur(rev), '<span class="fiche-commune__cout">' + eur(b) + '</span>'], [T.a2029, T.aucunV, eur(b) + T.parAn]]
          .map(function (r) { return '<div role="row" class="fiche-commune__crow"><span role="rowheader">' + r[0] + '</span><span role="cell">' + r[1] + '</span><span role="cell">' + r[2] + '</span></div>'; }).join('') +
        '</div>' +
        '<p class="fiche-commune__note">' + T.noteDil(eur(3 * Math.round(rev)), eur(d.dil)) + '</p>' +
        '<p class="fiche-commune__afaire"><span>' + T.aFaire + '</span> ' + T.aFaireDil + '</p>';
      h += bloc(T.n3, corps);
    }

    // 04 — situation financière
    var kpis = [[T.kEb, T.kEbS, pct(taux(v1)), pct(s.taux_eb)], [T.kDh, T.kDhS, eur(div(v1.dette, p)), eur(s.dette_hab)],
                [T.kAd, T.kAdS, ansU(annees(v1)), ansU(s.annees_dette)], [T.kPd, T.kPdS, pct(partDgf), pct(medDgf)]];
    var corps4 = '<div class="fiche-commune__kpis">' + kpis.map(function (k) {
      return '<div class="fiche-commune__kpi"><p class="fiche-commune__klib">' + k[0] + '</p><p class="fiche-commune__kv">' + k[2] + '</p><p class="fiche-commune__km">' + k[1] + '<br>' + T.med + ' ' + k[3] + '</p></div>';
    }).join('') + '</div>';
    if (s.n) corps4 += '<p class="fiche-commune__note">' + T.strate(s) + '</p>';
    // Évolution et détail des comptes, repliés (pièce 12) ; grille et non <table> : la règle globale du site (main table
    // en cartes sous 768 px, !important) cachait les valeurs.
    var g = '<p class="fiche-commune__note">' + T.t1s + '</p>';
    g += '<div role="table" class="fiche-commune__grille"><div role="row" class="fiche-commune__ligne fiche-commune__entete"><span role="columnheader"></span><span role="columnheader">' + a0 + '</span><span role="columnheader">' + a1 + '</span><span role="columnheader">' + T.colG[3] + '</span></div>';
    var m2 = function (x, y) { var r = Math.max(Math.abs(x || 0), Math.abs(y || 0)); return [meur(x, r), meur(y, r)]; };
    var mm;
    mm = m2(v0.rf, v1.rf); g += ligne(T.rf, mm[0], mm[1], '');
    mm = m2(v0.eb, v1.eb); g += ligne(T.eb, mm[0], mm[1], '');
    g += ligne(T.teb, pct(taux(v0)), pct(taux(v1)), pct(s.taux_eb));
    mm = m2(v0.dette, v1.dette); g += ligne(T.dette, mm[0], mm[1], '');
    g += ligne(T.dh, '', eur(div(v1.dette, p)), eur(s.dette_hab));
    g += ligne(T.ad, ans(annees(v0)), ans(annees(v1)), ans(s.annees_dette));
    mm = m2(v0.dgf, v1.dgf); g += ligne(T.dgf, mm[0], mm[1], '');
    g += ligne(T.pdgf, pct(div(v0.dgf, v0.rf)), pct(partDgf), pct(medDgf));
    mm = m2(v0.fctva, v1.fctva); g += ligne(T.fctva, mm[0], mm[1], '');
    mm = m2(v0.equip, v1.equip); g += ligne(T.eq, mm[0], mm[1], '');
    g += ligne(T.eqh, '', eur(div(v1.equip, p)), eur(s.equip_hab));
    g += '</div>';
    if (!has0) g += '<p class="fiche-commune__note">' + T.sans24(a0) + '</p>';
    else if (d && d.dcn) g += '<p class="fiche-commune__note">' + T.cn(a0, a1) + '</p>';
    corps4 += '<details class="fiche-commune__repli"><summary>' + (has0 ? T.evo(a0, a1) : T.evo1(a1)) + '</summary>' + g + '</details>';

    // Preuves repliées : calcul, liens directs vers les sources, détail de chaque mesure (textes de la fiche du 22/10).
    var comp = d ? Object.keys(T.comp).filter(function (k) { return d.comp[k]; }).map(function (k) { return T.comp[k] + SEP + meur(d.comp[k]); }).join(L === 'fr' ? ' ; ' : '; ') : '';
    var calc = '<ul class="fiche-commune__calc">';
    if (d) {
      calc += '<li>' + (dil ? T.cDil(eur(d.dil), eur(rev), eur(b), eur(ecart), L_) : T.cDilNon(L_)) + '</li>';
      if (d.dgf !== null) calc += '<li>' + T.cDgf(meur(d.dgf), Object.keys(d.comp).length > 1 ? comp : '', d.dcn ? meur(d.dcn) : '', L_) + '</li>';
    }
    calc += '<li>' + T.cCtl(ent(TEMOIN.montants_relus), L_) + '</li><li>' + T.cRat + '</li></ul>';
    var mesure = function (titre, statut, txt) { return '<div class="fiche-commune__mesure"><p class="fiche-commune__mesure-titre"><strong>' + titre + '</strong> · <span>' + esc(statut) + '</span></p><p>' + txt + '</p></div>'; };
    var epci = nomE ? ' ' + T.epciC(nomE) : '', cp;
    if (!d) cp = T.cpebTxt();
    else if (d.exo === 'dom') { cp = T.exoDom(nomE); epci = ''; }
    else if (d.exo === 'r_dsrc') cp = T.exoDsrc(rangTxt);
    else if (d.exo === 'seuil') cp = T.exoSeuil(meur((c.v['2024'] || {}).rf));
    else if (d.exo) cp = T.exoRang(rangTxt);
    else if (d.om === '03') { cp = T.exoCom; epci = ''; }
    else cp = T.nonExo(rangTxt) + T.cpebMt;
    if (insee === '75056') cp += T.paris;
    var det = '<p class="fiche-commune__dtitre">' + T.detail + '</p>';
    det += mesure(T.cpeb, statuts.cpeb, cp + epci);
    det += mesure(T.fctvaM, statuts.fctva, T.fctvaTxt(meur(v1.fctva), a1));
    if (d && d.dgf !== null) det += mesure(T.dgfM, statuts.dgf, T.dgfNot(meur(d.dgf), Object.keys(d.comp).length > 1 ? comp : '', d.dcn ? meur(d.dcn) : ''));
    else det += mesure(T.dgfM, statuts.dgf, T.dgfTxt(meur(v1.dgf), a1));
    if (!d) det += mesure(T.dilicoM, statuts.dilico, T.dilicoTxt(nomE));
    else if (!d.dil) det += mesure(T.dilicoM, statuts.dilico, T.dilicoNon + T.dilico26(nomE));
    else det += mesure(T.dilicoM, statuts.dilico, T.dilicoOui(eur(d.dil), eur(d.rev), eur(b)) + T.dilico26(nomE));
    det += mesure(T.tvaM, statuts.tva, T.tvaTxt);
    corps4 += '<details class="fiche-commune__repli fiche-commune__preuves"><summary>' + T.calc + '</summary>' + calc + det + '</details>';
    h += bloc(T.n4(n4, a1), corps4);
    if (PROC.length) {
      h += '<section class="fiche-commune__bloc"><p class="fiche-commune__num">' + T.texte + '</p><ol class="fiche-commune__frise">' +
        PROC.map(function (e) { return '<li class="' + esc(e.etat) + '"><span>' + esc(e.lib) + '</span><span>' + esc(e.detail) + '</span></li>'; }).join('') +
        '</ol>' + (root.dataset.echeance ? '<p class="fiche-commune__note">' + T.echeance + esc(root.dataset.echeance) + '.</p>' : '') +
        '<p class="fiche-commune__texte"><a href="#etat-du-texte">' + T.texteL + '</a></p></section>';
    }
    h += '<p class="fiche-commune__note fiche-commune__sources">' + T.source(root.dataset.releve) + '</p>';
    sortie.innerHTML = '<article class="fiche-commune__fiche">' + h + '</article>';
    var u = new URL(location.href); u.searchParams.set('insee', insee); u.hash = 'fiche';
    history.replaceState(null, '', u.toString());
    sortie.querySelector('[data-action="copier"]').addEventListener('click', function (e) {
      navigator.clipboard && navigator.clipboard.writeText(location.href).then(function () { e.target.textContent = T.copie; });
    });
    // Impression de la fiche seule : copie en fin de <body>, le reste de la page masqué à l'impression, retiré ensuite.
    sortie.querySelector('[data-action="imprimer"]').addEventListener('click', function () {
      var copie = sortie.querySelector('.fiche-commune__fiche').cloneNode(true);
      copie.classList.add('fiche-commune__imprime');
      copie.querySelectorAll('details').forEach(function (x) { x.open = true; });
      document.body.appendChild(copie);
      document.documentElement.classList.add('fiche-commune-impression');
      var fin = function () { copie.remove(); document.documentElement.classList.remove('fiche-commune-impression'); window.removeEventListener('afterprint', fin); };
      window.addEventListener('afterprint', fin);
      window.print();
    });
  }
  var voir = document.getElementById('fiche-commune-voir');
  if (voir) voir.addEventListener('click', function () {
    chargerIndex().then(function () {
      var r = chercher(champ.value);
      if (r.length) { champ.value = r[0].nom; liste.hidden = true; afficher(r[0].insee); }
      else { proposer(); }
    });
  });
  champ.addEventListener('focus', chargerIndex);
  champ.addEventListener('input', proposer);
  liste.addEventListener('click', function (e) {
    var li = e.target.closest('li[data-insee]');
    if (!li) return;
    champ.value = li.firstChild.textContent.trim();
    liste.hidden = true;
    afficher(li.dataset.insee);
  });
  champ.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { var li = liste.querySelector('li[data-insee]'); if (li) li.click(); }
    if (e.key === 'Escape') liste.hidden = true;
  });
  var q = new URL(location.href).searchParams.get('insee');
  if (q && /^[0-9AB]{5}$/i.test(q)) afficher(q.toUpperCase());
})();
