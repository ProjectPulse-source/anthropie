/* Accueil (partials/accueil-e.html, maquette E du 23/11/2026) : les trois questions de l'hypothèse — Où ? Quand ? Qui ?
   Sans script, les trois explications s'affichent sous leurs boutons. Avec script, une seule est ouverte à la fois
   (la deuxième au départ, comme dans la maquette) et toucher une question ouvre la sienne. */
(function () {
  var racine = document.querySelector('[data-acc-axes]');
  if (!racine) return;
  var axes = Array.prototype.slice.call(racine.querySelectorAll('[data-axe]'));
  if (!axes.length) return;
  racine.classList.add('is-js');
  function ouvrir(i) {
    axes.forEach(function (a, k) {
      a.classList.toggle('is-open', k === i);
      var b = a.querySelector('button');
      if (b) b.setAttribute('aria-expanded', k === i ? 'true' : 'false');
    });
  }
  axes.forEach(function (a, k) {
    var b = a.querySelector('button');
    if (b) b.addEventListener('click', function () { ouvrir(k); });
  });
  ouvrir(Math.min(1, axes.length - 1));
})();
