// Comptage des clics sortants vers Amazon via GoatCounter (déjà chargé en prod).
// Événement par format (kindle/broché) et par page d'origine — baseline avant
// Amazon Attribution (sept. 2026). Aucune donnée personnelle, aucun cookie.
(function () {
  'use strict';
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href*="amazon."]');
    if (!a) return;
    if (!window.goatcounter || typeof window.goatcounter.count !== 'function') return;
    // ASIN Kindle = B0…, broché = ISBN-10 numérique
    var format = /\/dp\/B0/.test(a.href) ? 'kindle' : 'broche';
    window.goatcounter.count({
      path: 'ext-amazon-' + format + '-' + location.pathname,
      title: a.href,
      event: true
    });
  });
})();
