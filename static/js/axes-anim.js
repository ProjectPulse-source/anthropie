/* axes-anim.js — lance une fois la séquence des trois axes de l'accueil quand la section entre à l'écran (04/11/2026).
   Sans ce script, sans IntersectionObserver, ou si l'appareil demande moins d'animations : rien ne bouge, la feuille
   de style montre l'image finale. Classes : is-attente (état de départ, hors écran), is-jouer (séquence). */
(function () {
  var el = document.querySelector('[data-axes-anim]');
  if (!el || !('IntersectionObserver' in window)) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  function jouer() { el.classList.remove('is-attente'); el.classList.add('is-jouer'); }
  var r = el.getBoundingClientRect();
  if (r.top < window.innerHeight * 0.75 && r.bottom > 0) { jouer(); return; }
  el.classList.add('is-attente');
  var io = new IntersectionObserver(function (entrees) {
    entrees.forEach(function (e) { if (e.isIntersecting) { jouer(); io.disconnect(); } });
  }, { threshold: 0.3 });
  io.observe(el);
})();
