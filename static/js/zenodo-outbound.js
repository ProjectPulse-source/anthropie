// Comptage des clics sortants vers Zenodo via GoatCounter (déjà chargé en prod).
// Événement par nature du lien et par page d'origine : pdf = fichier direct
// (téléchargement Zenodo sans vue du record), record = page du dépôt (vue),
// doi = résolveur (vue). Sert à rapprocher les compteurs Zenodo des parcours
// réels des lecteurs (écart explicable, 06/09/2026). Aucune donnée
// personnelle, aucun cookie.
(function () {
  'use strict';
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest &&
      e.target.closest('a[href*="zenodo.org"], a[href*="doi.org/10.5281/zenodo"]');
    if (!a) return;
    if (!window.goatcounter || typeof window.goatcounter.count !== 'function') return;
    var kind = /\/files\//.test(a.href) ? 'pdf'
      : (/doi\.org\//.test(a.href) ? 'doi' : 'record');
    window.goatcounter.count({
      path: 'ext-zenodo-' + kind + '-' + location.pathname,
      title: a.href,
      event: true
    });
  });
})();
