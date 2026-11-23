/* Étagère des livres offerts (ressources-offertes/list.html, maquette C+ validée par l'auteur le 23/11/2026).
   Sans script : les six fiches s'affichent l'une sous l'autre et chaque couverture de l'étagère y mène par ancre.
   Avec script : une seule fiche visible, celle de la couverture touchée ; la couverture choisie sort du rang.
   Ce script ne touche à RIEN du guichet (ressources-guichet-script.html) : il ne fait que montrer ou cacher des fiches
   que le guichet a déjà toutes traitées (stock, attribution, « déjà reçu »).
   Fiche ouverte au chargement, dans l'ordre : celle que désigne l'adresse (#offre-<livre>), celle du livre déjà reçu
   par ce visiteur (le guichet y affiche son message), sinon la première. */
(function () {
  var racine = document.querySelector('[data-ro-etagere]');
  if (!racine) return;
  var slots = Array.prototype.slice.call(racine.querySelectorAll('[data-ro-slot]'));
  var fiches = Array.prototype.slice.call(racine.querySelectorAll('[data-ro-fiche]'));
  if (!slots.length || slots.length !== fiches.length) return;

  function choisir(i, defiler) {
    fiches.forEach(function (f, k) { f.hidden = k !== i; });
    slots.forEach(function (s, k) {
      if (k === i) s.setAttribute('aria-current', 'true'); else s.removeAttribute('aria-current');
    });
    if (defiler) {
      var r = fiches[i].getBoundingClientRect();
      if (r.top > window.innerHeight * 0.7 || r.top < 0) {
        var doux = !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
        // Défilement calculé plutôt que scrollIntoView, resté sans effet dans un cadre de 390 px (recette du 23/11/2026) ;
        // 80 px de marge pour le bandeau collant.
        window.scrollTo({ top: Math.max(0, r.top + window.pageYOffset - 80), behavior: doux ? 'smooth' : 'auto' });
      }
    }
  }

  function depart() {
    var h = (location.hash || '').slice(1);
    for (var k = 0; k < fiches.length; k++) { if (h && fiches[k].id === h) return k; }
    try {
      var c = JSON.parse(localStorage.getItem('ro-claim') || 'null');
      if (c && c.book) {
        for (var j = 0; j < fiches.length; j++) { if (fiches[j].getAttribute('data-book') === c.book) return j; }
      }
    } catch (e) {}
    return 0;
  }

  racine.classList.add('is-js');
  slots.forEach(function (s, k) {
    s.setAttribute('aria-controls', fiches[k].id);
    s.addEventListener('click', function (ev) {
      ev.preventDefault();
      choisir(k, true);
      try { history.replaceState(null, '', '#' + fiches[k].id); } catch (e) {}
    });
  });
  choisir(depart(), false);
})();
