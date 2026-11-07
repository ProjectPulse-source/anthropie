/* Barre d'achat compacte de la fiche livre (partials/book-barre.html), téléphone seulement.
   Montrée quand ni la marge d'achat (#book-actions) ni le second appel (#book-appel) ne sont visibles :
   jamais deux appels à l'achat à l'écran en même temps. Sur ordinateur, la feuille de style la masque. */
(function () {
  var barre = document.querySelector('[data-book-barre]');
  if (!barre || !('IntersectionObserver' in window)) return;
  var lien = barre.querySelector('a');
  var cibles = ['book-actions', 'book-appel']
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);
  var vus = new Map();
  var io = new IntersectionObserver(function (entrees) {
    entrees.forEach(function (e) { vus.set(e.target, e.isIntersecting); });
    var montrer = cibles.every(function (c) { return !vus.get(c); });
    barre.classList.toggle('is-on', montrer);
    barre.setAttribute('aria-hidden', montrer ? 'false' : 'true');
    if (lien) lien.tabIndex = montrer ? 0 : -1;
  });
  cibles.forEach(function (c) { io.observe(c); });
})();
