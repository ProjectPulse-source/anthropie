/* Relais du bouton d'exemplaire offert (ressources-offertes/single.html, arbitrage A+ du 23/11/2026).
   Le rappel de fin de page et la barre du téléphone ne portent AUCUNE logique d'attribution : un clic sur l'un d'eux
   clique le bouton du guichet (ressources-guichet-script.html), dans le même geste, ce qui garde l'ouverture d'onglet
   autorisée. Ils ne s'affichent que si ce bouton est actionnable (stock lu, pas encore attribué) ; la barre, en plus,
   seulement quand ni le bouton ni le rappel ne sont à l'écran. Sans script, ils restent cachés (attribut hidden). */
(function () {
  var hero = document.querySelector('.ro-hero');
  if (!hero) return;
  var cta = hero.querySelector('.ressources-book__cta');
  var obtain = hero.querySelector('.ressources-book__obtain');
  var reprise = document.querySelector('[data-ro-reprise]');
  var barre = document.querySelector('[data-ro-barre]');
  if (!cta || !obtain) return;

  var vus = new Map();
  function actionnable() { return !cta.disabled && !obtain.hidden; }
  function maj() {
    var ok = actionnable();
    if (reprise) reprise.hidden = !ok;
    if (barre) {
      var montrer = ok && !vus.get(obtain) && !(reprise && vus.get(reprise));
      barre.hidden = !montrer;
      document.body.classList.toggle('avec-ro-barre', montrer);
    }
  }

  document.querySelectorAll('[data-ro-relais]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (!actionnable()) return;
      cta.click();
      // Le résultat (attribution, message, lien) s'affiche dans le premier écran : on y ramène le lecteur.
      var doux = !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
      hero.scrollIntoView({ block: 'start', behavior: doux ? 'smooth' : 'auto' });
    });
  });

  new MutationObserver(maj).observe(hero, { attributes: true, subtree: true, attributeFilter: ['disabled', 'hidden'] });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (e) { vus.set(e.target, e.isIntersecting); });
      maj();
    });
    io.observe(obtain);
    if (reprise) io.observe(reprise);
  } else {
    vus.set(obtain, true);   // sans observateur : pas de barre, le rappel suffit
  }
  maj();
})();
