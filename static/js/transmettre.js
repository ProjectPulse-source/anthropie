(function() {
  var MAX_BLUESKY = 300;

  function init() {
    document.querySelectorAll('.transmettre').forEach(setupTransmettre);
    document.addEventListener('click', closeAllPanels);
  }

  function setupTransmettre(container) {
    var button = container.querySelector('.transmettre__button');
    var panel = container.querySelector('.transmettre__panel');
    // Là où l'appareil a un menu de partage (téléphones, tablettes, Safari,
    // Edge…), le bouton l'ouvre directement : il contient déjà WhatsApp,
    // l'e-mail, LinkedIn, X… La liste ci-dessous ne sert qu'ailleurs.
    var ref = panel.querySelector('[data-channel="x"]');

    button.addEventListener('click', function(e) {
      e.stopPropagation();
      if (navigator.share && ref) {
        // Annulation par l'utilisateur = rejet de la promesse : rien à signaler.
        navigator.share({ title: ref.dataset.title, url: ref.dataset.url }).catch(function() {});
        return;
      }
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
      case 'whatsapp':
        window.open('https://wa.me/?text=' + encodeURIComponent(title + '\n' + url), '_blank', 'noopener');
        break;

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

      case 'x':
        window.open('https://x.com/intent/tweet?url=' + encodeURIComponent(url) + '&text=' + encodeURIComponent(title), '_blank', 'noopener');
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
        var done = function() {
          label.textContent = copiedText;
          setTimeout(function() {
            label.textContent = original;
            closeAllPanels();
          }, 1500);
        };
        // Sans presse-papiers (navigateurs intégrés aux applis), l'appel
        // plantait avant d'atteindre le repli : copie de secours, puis prompt.
        var fallback = function() {
          var ta = document.createElement('textarea');
          ta.value = url;
          ta.setAttribute('readonly', '');
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          ta.setSelectionRange(0, url.length);
          var ok = false;
          try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
          ta.remove();
          if (ok) { done(); } else { prompt('URL :', url); }
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(done, fallback);
        } else {
          fallback();
        }
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
