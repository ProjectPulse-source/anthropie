(function () {
  document.querySelectorAll('[data-copy-target]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var target = document.querySelector(btn.dataset.copyTarget);
      if (!target) return;
      var text = target.innerText.trim();
      navigator.clipboard.writeText(text).then(function () {
        var original = btn.textContent;
        btn.textContent = btn.dataset.copyFeedback || 'Copied';
        setTimeout(function () { btn.textContent = original; }, 2000);
      }).catch(function () {
        var range = document.createRange();
        range.selectNode(target);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        document.execCommand('copy');
        window.getSelection().removeAllRanges();
        var original = btn.textContent;
        btn.textContent = btn.dataset.copyFeedback || 'Copied';
        setTimeout(function () { btn.textContent = original; }, 2000);
      });
    });
  });
})();
