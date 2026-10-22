/* fiche-commune.js — fiche de votre commune, /budget-2027-votre-commune/#fiche (option A de l'auteur, 22/10/2026).
   Recherche dans static/budget2027-communes/index.json, puis lecture de la fiche dans <dep>.json. Tous les nombres
   affichés viennent de ces fichiers (scripts/update_budget_communes.py) ou des attributs data-* posés par le shortcode
   fiche-commune (statuts du registre des votes, médianes des strates) : aucun chiffre écrit ici.
   Règles : valeur absente = « non disponible », jamais zéro ; commune et intercommunalité séparées ; aucun montant 2027.
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
  var NB = ' ', FIN = ' ';
  var T = {
    fr: {
      nd: 'non disponible', pop: 'habitants', epci: 'Intercommunalité', aucune: 'aucune intercommunalité à fiscalité propre publiée',
      t1: 'Les chiffres officiels connus', t1s: 'Comptes du budget principal publiés par l’Observatoire des finances et de la gestion publique locales (OFGL). Budgets annexes et intercommunalité non compris.',
      col: ['', '', '', 'Médiane de la strate'], strate: function (s) { return 'Strate de population de l’OFGL : ' + ent(s.n) + ' communes, de ' + ent(s.pop_min) + ' à ' + ent(s.pop_max) + NB + 'habitants ; médianes de l’exercice ' + exercices[exercices.length - 1] + ', repère descriptif et non norme de gestion.'; },
      rf: 'Recettes de fonctionnement', eb: 'Épargne brute', teb: 'Taux d’épargne brute', dette: 'Encours de dette', dh: 'Dette par habitant', ad: 'Capacité de désendettement théorique (années, budget principal)', dgf: 'Dotation globale de fonctionnement', dgfh: 'DGF par habitant', fctva: 'FCTVA perçu', eq: 'Dépenses d’équipement', eqh: 'Dépenses d’équipement par habitant',
      t2: 'Les mesures du projet de loi de finances, pour cette commune', t2s: function () { return 'État du texte au ' + etat + '. Aucun montant pour 2027 n’est déterminable : les montants viendront de la loi votée, puis des arrêtés et notifications.'; },
      cpeb: 'Contribution progressive (art.' + NB + '37)', fctvaM: 'FCTVA (art.' + NB + '35)', dgfM: 'DGF (art.' + NB + '34)', dilicoM: 'DILICO (art.' + NB + '84)', tvaM: 'TVA affectée (art.' + NB + '36)',
      cpebTxt: function () { return 'Exonération non déterminable : commune absente du jeu des dotations. Montant non déterminé : il dépend du rang de la commune parmi toutes les autres, sur un indice de potentiel financier et de revenu ; assiette : recettes réelles de fonctionnement de 2024, retraitées.'; },
      epciC: function (n) { return 'L’intercommunalité (' + n + ') était visée par une contribution distincte, qui n’est pas imputée à la commune.'; },
      fctvaTxt: function (x, a) { return 'FCTVA perçu en ' + a + ' : ' + x + ' (montant passé). Le texte déposé abaissait le taux de 16,404' + NB + '% à 11,404' + NB + '% pour les attributions versées à partir de 2027, sauf pour les dépenses de transition écologique et de voirie ; l’effet pour la commune dépend de ses investissements à venir et de leur nature, non connus ici.'; },
      dgfTxt: function (x, a) { return 'DGF ' + a + ' : ' + x + '. Montant 2027 non déterminable : il dépend de la loi votée et de la répartition du Comité des finances locales.'; },
      dilicoTxt: function (n) { return 'DILICO 2025 : contribution de la commune non disponible. DILICO 2026 : les communes n’y contribuent pas' + (n ? ' ; l’intercommunalité (' + n + ') peut y avoir contribué.' : '.'); },
      dilicoNon: 'DILICO 2025 : la commune n’était pas contributrice ; aucun reversement ne la concerne.',
      dilicoOui: function (p, r, b) { return 'DILICO 2025 : ' + p + ' mis en réserve ; la commune en récupère 90' + NB + '%. Reçu en 2026 : ' + r + '. Selon le droit actuel, la même somme en 2027 et en 2028 ; selon le projet déposé, ' + b + ' par an de 2027 à 2031.'; },
      dilico26: function (n) { return ' DILICO 2026 : les communes n’y contribuent pas' + (n ? ' ; l’intercommunalité (' + n + ') peut y avoir contribué.' : '.'); },
      dgfNot: function (x, comp, dcn) { return 'DGF 2026 notifiée (base de la DGCL, via l’OFGL) : ' + x + (comp ? ' (' + comp + ')' : '') + '.' + (dcn ? ' Dotation en faveur des communes nouvelles, distincte de la DGF : ' + dcn + '.' : '') + ' Le tableau donne la DGF comptabilisée en 2024 et 2025 : exercice et nature différents. Montant 2027 non déterminable : il dépend de la loi votée et de la répartition du Comité des finances locales.'; },
      comp: {forf: 'dotation forfaitaire', dsu: 'dotation de solidarité urbaine', dsr: 'dotation de solidarité rurale', dnp: 'dotation nationale de péréquation', dacom: 'dotation d’aménagement des communes d’outre-mer'},
      classe: {r_dsu10: '2026 de la dotation de solidarité urbaine (communes de 10' + FIN + '000 habitants et plus)', r_dsu5: '2026 de la dotation de solidarité urbaine (communes de 5' + FIN + '000 à 9' + FIN + '999 habitants)', r_dsrc: '2026 selon l’indice de la fraction cible de la dotation de solidarité rurale'},
      rang: function (k, r, n) { return 'rang ' + ent(r) + ' au classement ' + T.classe[k] + ', ' + (r <= n ? 'parmi les ' : 'hors des ') + ent(n) + ' premières'; },
      exoDom: function (n) { return 'Exonérée par le texte déposé, qui exonérait les communes des départements et régions d’outre-mer' + (n ? ', comme leurs intercommunalités (' + n + ').' : '.'); },
      exoRang: function (r) { return 'Exonérée selon le classement publié par la DGCL (via l’OFGL) : ' + r + ', que le texte déposé exonérait.'; },
      exoSeuil: function (x) { return 'Exonération possible, à confirmer : calculée au taux maximal de 3' + NB + '% sur les recettes de fonctionnement 2024 publiées (' + x + '), la contribution resterait sous le seuil de 5' + FIN + '000' + NB + '€ en dessous duquel le texte déposé exonérait ; mais l’assiette légale, non publiée, peut différer de ces recettes.'; },
      exoCom: 'Hors du champ du texte déposé, qui ne classait que les communes de métropole et des départements et régions d’outre-mer.',
      nonExo: function (r) { return 'Aucun critère d’exonération établi dans les données examinées' + (r ? ' : ' + r : '') + '. Le seuil de 5' + FIN + '000' + NB + '€ dépend du taux et de l’assiette légale, non déterminables ici.'; },
      cpebMt: ' Montant non déterminé : il dépend du rang de la commune parmi toutes les autres, sur un indice de potentiel financier et de revenu ; assiette : recettes réelles de fonctionnement de 2024, retraitées.',
      tvaTxt: 'À vérifier : fraction de TVA perçue par la commune, ou par son intercommunalité.',
      lien: 'Copier le lien de cette fiche', copie: 'Lien copié', imprimer: 'Imprimer', aucun: 'Aucune commune trouvée.',
      exoDsrc: function (r) { return 'Exonération possible, à confirmer : ' + r + ', que le texte déposé exonérait ; mais il ne précise pas l’année du classement retenu pour 2027.'; },
      paris: ' Ville de Paris : le texte déposé ne retenait que 70,87' + NB + '% de ses recettes pour cette contribution, et la soumettait en outre, sur 29,13' + NB + '% de ses recettes, à la contribution des départements (taux de 0 à 2' + NB + '% selon un indice de fragilité sociale).',
      nc: 'non calculable (épargne brute nulle ou négative)',
      source: function (r) { return 'Sources : OFGL, comptes des communes (DGFiP) et dotations des communes (DGCL), données relevées le ' + r + ' ; CSV complet et méthode en bas de page.'; }
    },
    en: {
      nd: 'not available', pop: 'inhabitants', epci: 'Inter-municipal body', aucune: 'no inter-municipal body with own tax published',
      t1: 'The official figures known', t1s: 'Main-budget accounts published by the Observatory of Local Public Finance and Management (OFGL). Ancillary budgets and the inter-municipal body excluded.',
      col: ['', '', '', 'Median of the size band'], strate: function (s) { return 'OFGL population band: ' + ent(s.n) + ' municipalities, ' + ent(s.pop_min) + ' to ' + ent(s.pop_max) + ' inhabitants; medians for ' + exercices[exercices.length - 1] + ', a descriptive marker, not a management norm.'; },
      rf: 'Operating revenue', eb: 'Gross savings', teb: 'Gross savings rate', dette: 'Debt outstanding', dh: 'Debt per inhabitant', ad: 'Theoretical debt-repayment capacity (years, main budget)', dgf: 'General operating grant (DGF)', dgfh: 'DGF per inhabitant', fctva: 'FCTVA received', eq: 'Capital spending', eqh: 'Capital spending per inhabitant',
      t2: 'The measures of the draft budget bill, for this municipality', t2s: function () { return 'State of the text on ' + etat + '. No amount for 2027 can be determined: amounts will come from the act as passed, then from orders and notifications.'; },
      cpeb: 'Progressive contribution (art. 37)', fctvaM: 'FCTVA (art. 35)', dgfM: 'DGF (art. 34)', dilicoM: 'DILICO (art. 84)', tvaM: 'Assigned VAT (art. 36)',
      cpebTxt: function () { return 'Exemption not determinable: the municipality is missing from the grants dataset. Amount not determined: it depends on the municipality’s rank among all others, on an index of financial potential and income; base: 2024 real operating revenue, adjusted.'; },
      epciC: function (n) { return 'The inter-municipal body (' + n + ') was targeted by a separate contribution, which is not attributed to the municipality.'; },
      fctvaTxt: function (x, a) { return 'FCTVA received in ' + a + ': ' + x + ' (past amount). The bill as tabled lowered the rate from 16.404% to 11.404% for payments made from 2027, except for ecological transition and road spending; the effect for the municipality depends on its future investment and its nature, not known here.'; },
      dgfTxt: function (x, a) { return 'DGF ' + a + ': ' + x + '. Amount for 2027 not determinable: it depends on the act as passed and on the Local Finance Committee’s distribution.'; },
      dilicoTxt: function (n) { return '2025 DILICO: the municipality’s contribution is not available. 2026 DILICO: municipalities do not contribute' + (n ? '; the inter-municipal body (' + n + ') may have.' : '.'); },
      dilicoNon: '2025 DILICO: the municipality was not a contributor; no repayment concerns it.',
      dilicoOui: function (p, r, b) { return '2025 DILICO: ' + p + ' placed in reserve; the municipality recovers 90% of it. Received in 2026: ' + r + '. Under current law, the same sum in 2027 and 2028; under the bill as tabled, ' + b + ' a year from 2027 to 2031.'; },
      dilico26: function (n) { return ' 2026 DILICO: municipalities do not contribute' + (n ? '; the inter-municipal body (' + n + ') may have.' : '.'); },
      dgfNot: function (x, comp, dcn) { return '2026 DGF notified (DGCL database, via the OFGL): ' + x + (comp ? ' (' + comp + ')' : '') + '.' + (dcn ? ' Grant for new municipalities, separate from the DGF: ' + dcn + '.' : '') + ' The table gives the DGF recorded in the accounts for 2024 and 2025: a different year and nature. Amount for 2027 not determinable: it depends on the act as passed and on the Local Finance Committee’s distribution.'; },
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
      lien: 'Copy the link to this sheet', copie: 'Link copied', imprimer: 'Print', aucun: 'No municipality found.',
      exoDsrc: function (r) { return 'Exemption possible, to be confirmed: ' + r + ', which the bill as tabled exempted; but it does not specify the year of the ranking used for 2027.'; },
      paris: ' City of Paris: the bill as tabled took only 70.87% of its revenue into account for this contribution, and also subjected it, on 29.13% of its revenue, to the departments’ contribution (rate from 0 to 2% according to a social fragility index).',
      nc: 'not calculable (gross savings zero or negative)',
      source: function (r) { return 'Sources: OFGL, municipal accounts (DGFiP) and municipal grants (DGCL), data retrieved on ' + r + '; full CSV and method at the foot of the page.'; }
    }
  }[L];

  function ent(x) { // entier, separateur de milliers insecable fin
    if (x === null || x === undefined) return T.nd;
    return Math.round(x).toString().replace(/\B(?=(\d{3})+(?!\d))/g, L === 'fr' ? FIN : ',');
  }
  function dec(x, n) { // decimal, partie entiere groupee comme ent()
    var s = x.toFixed(n).split('.'), e = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, L === 'fr' ? FIN : ',');
    return s.length > 1 ? e + (L === 'fr' ? ',' : '.') + s[1] : e;
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
  function pct(x) { if (x === null || x === undefined) return T.nd; return L === 'fr' ? dec(100 * x, 1) + NB + '%' : dec(100 * x, 1) + '%'; }
  function ans(x) { if (x === null || x === undefined) return T.nd; if (x === 'nc') return T.nc; return dec(x, 1); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]; }); }
  function norm(s) { return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[-'’ ]+/g, ' ').trim(); }

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
  function rendre(insee, c) {
    if (!c) { sortie.innerHTML = '<p>' + T.aucun + '</p>'; return; }
    var a0 = String(exercices[0]), a1 = String(exercices[exercices.length - 1]);
    var v0 = c.v[a0] || {}, v1 = c.v[a1] || {}, s = strates[c.strate] || {}, p = c.pop;
    var div = function (x, y) { return (x === null || x === undefined || !y) ? null : x / y; };
    var taux = function (v) { return (v.rf && v.eb !== null && v.eb !== undefined) ? v.eb / v.rf : null; };
    var annees = function (v) { // dette / epargne brute ; epargne nulle ou negative : ratio sans sens, dit comme tel
      if (v.dette === null || v.dette === undefined || v.eb === null || v.eb === undefined) return null;
      return v.eb > 0 ? v.dette / v.eb : 'nc'; };
    var h = '';
    h += '<header class="fiche-commune__tete"><h3>' + esc(c.nom) + ' <span>(' + esc(c.dep) + ', ' + esc(insee) + ')</span></h3>';
    h += '<p>' + ent(p) + NB + T.pop + ' · ' + T.epci + (L === 'fr' ? NB + ': ' : ': ') + (c.epci_nom ? esc(c.epci_nom) : T.aucune) + '</p></header>';
    h += '<h4>' + T.t1 + '</h4><p class="fiche-commune__note">' + T.t1s + '</p>';
    // Grille, pas <table> : la règle globale du site (main table en cartes sous 768 px, !important) cachait les valeurs.
    h += '<div role="table" class="fiche-commune__grille"><div role="row" class="fiche-commune__ligne fiche-commune__entete"><span role="columnheader"></span><span role="columnheader">' + a0 + '</span><span role="columnheader">' + a1 + '</span><span role="columnheader">' + T.col[3] + '</span></div>';
    var m2 = function (x, y) { var r = Math.max(Math.abs(x || 0), Math.abs(y || 0)); return [meur(x, r), meur(y, r)]; };
    var mm;
    mm = m2(v0.rf, v1.rf); h += ligne(T.rf, mm[0], mm[1], '');
    mm = m2(v0.eb, v1.eb); h += ligne(T.eb, mm[0], mm[1], '');
    h += ligne(T.teb, pct(taux(v0)), pct(taux(v1)), pct(s.taux_eb));
    mm = m2(v0.dette, v1.dette); h += ligne(T.dette, mm[0], mm[1], '');
    h += ligne(T.dh, '', eur(div(v1.dette, p)), eur(s.dette_hab));
    h += ligne(T.ad, ans(annees(v0)), ans(annees(v1)), ans(s.annees_dette));
    mm = m2(v0.dgf, v1.dgf); h += ligne(T.dgf, mm[0], mm[1], '');
    h += ligne(T.dgfh, '', eur(div(v1.dgf, p)), eur(s.dgf_hab));
    mm = m2(v0.fctva, v1.fctva); h += ligne(T.fctva, mm[0], mm[1], '');
    mm = m2(v0.equip, v1.equip); h += ligne(T.eq, mm[0], mm[1], '');
    h += ligne(T.eqh, '', eur(div(v1.equip, p)), eur(s.equip_hab));
    h += '</div>';
    if (s.n) h += '<p class="fiche-commune__note">' + T.strate(s) + '</p>';
    h += '<h4>' + T.t2 + '</h4><p class="fiche-commune__note">' + T.t2s() + '</p>';
    var rf24 = (c.v['2024'] || {}).rf;
    // Contre-expertise PRO-20261022-215525 : qualification graduee, aucun plafond individualise.
    var mesure = function (titre, statut, txt) { return '<div class="fiche-commune__mesure"><p class="fiche-commune__mesure-titre"><strong>' + titre + '</strong> · <span>' + esc(statut) + '</span></p><p>' + txt + '</p></div>'; };
    var d = c.d, nomE = c.epci_nom ? esc(c.epci_nom) : null, cp;
    var epci = nomE ? ' ' + T.epciC(nomE) : '';
    var rangTxt = d && d.rang ? T.rang(d.rang[0], d.rang[1], SEUILS[d.rang[0]]) : '';
    if (!d) cp = T.cpebTxt();
    else if (d.exo === 'dom') { cp = T.exoDom(nomE); epci = ''; }
    else if (d.exo === 'r_dsrc') cp = T.exoDsrc(rangTxt);
    else if (d.exo === 'seuil') cp = T.exoSeuil(meur(rf24));
    else if (d.exo) cp = T.exoRang(rangTxt);
    else if (d.om === '03') { cp = T.exoCom; epci = ''; }
    else cp = T.nonExo(rangTxt) + T.cpebMt;
    if (insee === '75056') cp += T.paris;
    h += mesure(T.cpeb, statuts.cpeb, cp + epci);
    h += mesure(T.fctvaM, statuts.fctva, T.fctvaTxt(meur(v1.fctva), a1));
    if (d && d.dgf !== null) {
      cp = Object.keys(T.comp).filter(function (k) { return d.comp[k]; }).map(function (k) { return T.comp[k] + (L === 'fr' ? NB + ': ' : ': ') + meur(d.comp[k]); }).join(L === 'fr' ? ' ; ' : '; ');
      h += mesure(T.dgfM, statuts.dgf, T.dgfNot(meur(d.dgf), Object.keys(d.comp).length > 1 ? cp : '', d.dcn ? meur(d.dcn) : ''));
    } else h += mesure(T.dgfM, statuts.dgf, T.dgfTxt(meur(v1.dgf), a1));
    if (!d) h += mesure(T.dilicoM, statuts.dilico, T.dilicoTxt(nomE));
    else if (!d.dil) h += mesure(T.dilicoM, statuts.dilico, T.dilicoNon + T.dilico26(nomE));
    else h += mesure(T.dilicoM, statuts.dilico, T.dilicoOui(eur(d.dil), eur(d.rev), eur(0.12 * d.dil)) + T.dilico26(nomE));
    h += mesure(T.tvaM, statuts.tva, T.tvaTxt);
    h += '<p class="fiche-commune__actions"><button type="button" data-action="copier">' + T.lien + '</button> <button type="button" data-action="imprimer">' + T.imprimer + '</button></p>';
    h += '<p class="fiche-commune__note">' + T.source(root.dataset.releve) + '</p>';
    sortie.innerHTML = h;
    var u = new URL(location.href); u.searchParams.set('insee', insee); u.hash = 'fiche';
    history.replaceState(null, '', u.toString());
    sortie.querySelector('[data-action="copier"]').addEventListener('click', function (e) {
      navigator.clipboard && navigator.clipboard.writeText(location.href).then(function () { e.target.textContent = T.copie; });
    });
    sortie.querySelector('[data-action="imprimer"]').addEventListener('click', function () { window.print(); });
  }
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
