(function() {
  var triggers = document.querySelectorAll('[data-amazon-trigger]');
  if (!triggers.length) return;

  function closeAll() {
    document.querySelectorAll('[data-amazon-popover]').forEach(function(p) {
      p.setAttribute('hidden', '');
    });
    document.querySelectorAll('[data-amazon-trigger]').forEach(function(t) {
      t.setAttribute('aria-expanded', 'false');
    });
  }

  triggers.forEach(function(trigger) {
    trigger.addEventListener('click', function(e) {
      e.stopPropagation();
      var id = trigger.getAttribute('aria-controls');
      var popover = document.getElementById(id);
      var isOpen = trigger.getAttribute('aria-expanded') === 'true';
      closeAll();
      if (!isOpen) {
        popover.removeAttribute('hidden');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });
  });

  document.addEventListener('click', function(e) {
    if (!e.target.closest('.amazon-wrapper')) closeAll();
  });

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeAll();
  });
})();
