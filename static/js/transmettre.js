(function() {
  var MAX_BLUESKY = 300;

  function init() {
    document.querySelectorAll('.transmettre').forEach(setupTransmettre);
    document.addEventListener('click', closeAllPanels);
  }

  function setupTransmettre(container) {
    var button = container.querySelector('.transmettre__button');
    var panel = container.querySelector('.transmettre__panel');
    var coarse = !!window.matchMedia && window.matchMedia('(pointer: coarse)').matches;
    // Sur écran tactile (téléphones, tablettes), le bouton ouvre directement le
    // menu de partage de l'appareil : il contient déjà WhatsApp, l'e-mail,
    // LinkedIn, X… Sur ordinateur, on garde la liste du site, même quand le
    // navigateur propose un partage natif : la fenêtre de Windows ou de macOS
    // ne se stylise pas et jure avec le site (remarque auteur, 24/09).
    // data-native="off" (pages ressources offertes) : jamais de menu natif, qui
    // ouvrirait LinkedIn, X… — ces pages se transmettent de personne à personne.
    var ref = panel.querySelector('[data-channel="x"]');
    var nativeOk = container.dataset.native !== 'off' && !!navigator.share && coarse;
    // SMS : seulement sur écran tactile (aucun client SMS sur un ordinateur).
    panel.querySelectorAll('[data-channel="sms"]').forEach(function(o) { o.hidden = !coarse; });

    button.addEventListener('click', function(e) {
      e.stopPropagation();
      if (nativeOk && ref) {
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

  // Un texte prérempli propre à la page (data-text, data-subject, data-body,
  // data-copy-text : invitations des pages ressources) l'emporte sur le
  // message générique « titre + lien ».
  function handleShare(option) {
    var channel = option.dataset.channel;
    var url = option.dataset.url;
    var title = option.dataset.title || '';
    var text = option.dataset.text || (title + '\n' + url);

    switch(channel) {
      case 'whatsapp':
        window.open('https://wa.me/?text=' + encodeURIComponent(text), '_blank', 'noopener');
        break;

      case 'telegram':
        // Telegram ajoute lui-même le lien : on ne lui passe que le texte d'accroche.
        window.open('https://t.me/share/url?url=' + encodeURIComponent(url) +
          '&text=' + encodeURIComponent(option.dataset.text || title), '_blank', 'noopener');
        break;

      case 'sms':
        var sep = /iPhone|iPad|iPod/i.test(navigator.userAgent) ? '&' : '?';
        window.location.href = 'sms:' + sep + 'body=' + encodeURIComponent(text);
        break;

      case 'bluesky':
        var maxTitleLength = MAX_BLUESKY - url.length - 4;
        var truncatedTitle = title.length > maxTitleLength
          ? title.substring(0, maxTitleLength - 1) + '…'
          : title;
        window.open('https://bsky.app/intent/compose?text=' +
          encodeURIComponent(truncatedTitle + '\n\n' + url), '_blank', 'noopener');
        break;

      case 'linkedin':
        window.open('https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(url), '_blank', 'noopener');
        break;

      case 'x':
        window.open('https://x.com/intent/tweet?url=' + encodeURIComponent(url) + '&text=' + encodeURIComponent(title), '_blank', 'noopener');
        break;

      case 'email':
        var subject = option.dataset.subject || title;
        var body = option.dataset.body ||
          ((option.dataset.emailIntro || '') + '\n\n' + title + '\n\n' + url);
        window.location.href = 'mailto:?subject=' + encodeURIComponent(subject) +
          '&body=' + encodeURIComponent(body.replace(/\r?\n/g, '\r\n'));
        break;

      case 'copy':
        var copyText = option.dataset.copyText || url;
        var label = option.querySelector('.transmettre__copy-label');
        var original = label.textContent;
        var copiedText = option.dataset.copiedLabel || 'Lien copié ✓';
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
          ta.value = copyText;
          ta.setAttribute('readonly', '');
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          ta.setSelectionRange(0, copyText.length);
          var ok = false;
          try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
          ta.remove();
          if (ok) { done(); } else { prompt('', copyText); }
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(copyText).then(done, fallback);
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
