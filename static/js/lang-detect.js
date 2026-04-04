(function() {
  if (localStorage.getItem('lang-choice')) return;
  if (!navigator.language.startsWith('fr') && !window.location.pathname.startsWith('/en/')) {
    localStorage.setItem('lang-choice', 'en');
    window.location.replace('/en/');
  }
})();
