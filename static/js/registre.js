// Registre des coûts déportés : recherche, filtre par catégorie, escales de L'Odyssée, filtre par âge depuis la frise
// (maquette C+, arbitrage Audit-18, auteur 07/11/2026). Sans ce script, la page reste la liste complète des jalons et
// chaque barre de la frise reste un lien vers son âge.
(function () {
  var reg = document.querySelector('.registre');
  if (!reg) return;
  var en = (document.documentElement.lang || '').indexOf('en') === 0;
  var box = reg.querySelector('.registre-filtres');
  var q = box.querySelector('.registre-filtres__q');
  var cat = box.querySelector('.registre-filtres__cat');
  var ody = box.querySelector('.registre-filtres__ody input');
  var compte = reg.querySelector('.registre__compte');
  var vide = reg.querySelector('.registre__vide');
  var ages = Array.prototype.slice.call(reg.querySelectorAll('.registre__age'));
  var liens = Array.prototype.slice.call(document.querySelectorAll('.registre-frise__age'));
  var total = parseInt(reg.getAttribute('data-total'), 10);
  var compteInitial = compte.innerHTML;
  var ageSel = null;
  box.hidden = false;
  // Le compte (et « Tout afficher ») entre dans la barre de filtres, collante sur ordinateur : un filtre actif reste
  // visible pendant le défilement (contrôleur de rendu, 07/11/2026).
  box.appendChild(compte);
  // Sans script, la légende dit « mène à ses jalons » (vrai : un lien) ; avec, le clic filtre : la légende le dit.
  var sous = document.querySelector('.registre-frise__sous span[data-js]');
  if (sous) sous.textContent = sous.getAttribute('data-js');

  // Le texte servi porte la typographie du site (apostrophe ’, signe −, espaces insécables) : ramenée à ce que l'on tape.
  function norm(s) {
    return s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[\u2018\u2019]/g, "'")
      .replace(/[\u2011\u2013\u2212]/g, '-').replace(/[\u00a0\u202f]/g, ' ')
      .replace(/(\d) (?=\d)/g, '$1').toLowerCase();
  }

  function filtrer() {
    var qv = q.value.trim(), qn = norm(qv), c = cat.value, o = ody.checked, n = 0;
    ages.forEach(function (s) {
      var k = 0, bonAge = !ageSel || s.getAttribute('data-age') === ageSel;
      s.querySelectorAll('.registre__jalon').forEach(function (j) {
        var ok = bonAge && (!c || j.getAttribute('data-cats').split('|').indexOf(c) >= 0) &&
          (!o || j.hasAttribute('data-ody')) && (!qn || norm(j.textContent).indexOf(qn) >= 0);
        j.hidden = !ok;
        if (ok) k++;
      });
      s.hidden = k === 0;
      n += k;
    });
    vide.hidden = n > 0;
    var f = [];
    if (ageSel) f.push((en ? 'age ' : 'âge ') + ageSel);
    if (c) f.push(c);
    if (o) f.push(en ? 'stop in L’Odyssée' : 'escale de L’Odyssée');
    if (qv) f.push(en ? '“' + qv + '”' : '« ' + qv + ' »');
    if (!f.length) {
      compte.innerHTML = compteInitial;
    } else {
      compte.textContent = (en ? n + ' milestone' + (n !== 1 ? 's' : '') + ' of ' + total
        : n + ' jalon' + (n > 1 ? 's' : '') + ' sur ' + total) + ' · ' + f.join(' · ');
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'registre__raz';
      b.textContent = en ? 'Show all' : 'Tout afficher';
      b.addEventListener('click', function () { q.value = ''; cat.value = ''; ody.checked = false; ageSel = null; filtrer(); q.focus(); });
      compte.appendChild(b);
    }
    liens.forEach(function (l) {
      if (l.getAttribute('data-age') === ageSel) l.setAttribute('aria-current', 'true');
      else l.removeAttribute('aria-current');
    });
  }

  q.addEventListener('input', filtrer);
  cat.addEventListener('change', filtrer);
  ody.addEventListener('change', filtrer);
  liens.forEach(function (l) {
    l.addEventListener('click', function (e) {
      e.preventDefault();
      var a = l.getAttribute('data-age');
      ageSel = ageSel === a ? null : a;
      filtrer();
      var entete = document.querySelector('.site-header');
      var h = entete ? entete.getBoundingClientRect().height : 0;
      var fixe = getComputedStyle(box).position === 'sticky' ? box.getBoundingClientRect().height : 0;
      // Cible : le premier âge affiché, sous l'en-tête et sous la barre de filtres si elle est collante (ordinateur) ;
      // au téléphone, la barre n'est pas collante : on s'arrête sur elle, compte compris.
      var cible = fixe ? ages.filter(function (s) { return !s.hidden; })[0] || compte : box;
      window.scrollTo({ top: cible.getBoundingClientRect().top + window.scrollY - h - fixe - 12, behavior: 'smooth' });
    });
  });
})();
