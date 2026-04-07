(function() {
  var burger = document.querySelector('.site-header__burger');
  var menu = document.getElementById('mobile-menu');
  var close = document.querySelector('.mobile-menu__close');
  if (!burger || !menu) return;

  function openMenu() {
    menu.classList.add('is-open');
    menu.setAttribute('aria-hidden', 'false');
    burger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('menu-open');
  }
  function closeMenu() {
    menu.classList.remove('is-open');
    menu.setAttribute('aria-hidden', 'true');
    burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
  }

  burger.addEventListener('click', openMenu);
  if (close) close.addEventListener('click', closeMenu);
  menu.querySelectorAll('a').forEach(function(a) { a.addEventListener('click', closeMenu); });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && menu.classList.contains('is-open')) closeMenu();
  });
})();
