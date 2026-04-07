(function() {
  var MAX_BLUESKY = 300;

  function init() {
    document.querySelectorAll('.transmettre').forEach(setupTransmettre);
    document.addEventListener('click', closeAllPanels);
  }

  function setupTransmettre(container) {
    var button = container.querySelector('.transmettre__button');
    var panel = container.querySelector('.transmettre__panel');

    button.addEventListener('click', function(e) {
      e.stopPropagation();
      var isOpen = button.getAttribute('aria-expanded') === 'true';
      closeAllPanels();
      if (!isOpen) {
        button.setAttribute('aria-expanded', 'true');
        panel.hidden = false;
      }
    });

    panel.addEventListener('click', function(e) {
      e.stopPropagation();
    });

    panel.querySelectorAll('.transmettre__option').forEach(function(option) {
      option.addEventListener('click', function(e) {
        e.preventDefault();
        handleShare(option);
      });
    });
  }

  function closeAllPanels() {
    document.querySelectorAll('.transmettre__button[aria-expanded="true"]').forEach(function(btn) {
      btn.setAttribute('aria-expanded', 'false');
    });
    document.querySelectorAll('.transmettre__panel').forEach(function(p) {
      p.hidden = true;
    });
  }

  function handleShare(option) {
    var channel = option.dataset.channel;
    var url = option.dataset.url;
    var title = option.dataset.title || '';

    switch(channel) {
      case 'bluesky':
        var maxTitleLength = MAX_BLUESKY - url.length - 4;
        var truncatedTitle = title.length > maxTitleLength
          ? title.substring(0, maxTitleLength - 1) + '\u2026'
          : title;
        var text = truncatedTitle + '\n\n' + url;
        window.open('https://bsky.app/intent/compose?text=' + encodeURIComponent(text), '_blank', 'noopener');
        break;

      case 'linkedin':
        window.open('https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(url), '_blank', 'noopener');
        break;

      case 'email':
        var intro = option.dataset.emailIntro || '';
        var subject = encodeURIComponent(title);
        var body = encodeURIComponent(intro + '\n\n' + title + '\n\n' + url);
        window.location.href = 'mailto:?subject=' + subject + '&body=' + body;
        break;

      case 'copy':
        var label = option.querySelector('.transmettre__copy-label');
        var original = label.textContent;
        var copiedText = option.dataset.copiedLabel || 'Lien copié \u2713';
        navigator.clipboard.writeText(url).then(function() {
          label.textContent = copiedText;
          setTimeout(function() {
            label.textContent = original;
            closeAllPanels();
          }, 1500);
        }).catch(function() {
          prompt('URL :', url);
        });
        return;
    }

    closeAllPanels();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
