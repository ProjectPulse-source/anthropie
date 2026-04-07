(function() {
  if (document.documentElement.lang !== 'fr') return;

  var THIN_NBSP = '\u202F';
  var NBSP = '\u00A0';

  var containers = document.querySelectorAll('body');

  function fix(text) {
    return text
      .replace(/ ([?!;:])/g, THIN_NBSP + '$1')
      .replace(/« /g, '\u00AB' + NBSP)
      .replace(/ »/g, NBSP + '\u00BB')
      .replace(/ (\u2014|\u2013) /g, NBSP + '$1 ');
  }

  function walk(node) {
    if (node.nodeType === 3) {
      if (node.nodeValue && node.nodeValue.trim().length > 0) {
        node.nodeValue = fix(node.nodeValue);
      }
    } else if (node.nodeType === 1) {
      var tag = node.tagName.toLowerCase();
      if (['code', 'pre', 'input', 'textarea', 'script', 'style', 'meta', 'title', 'head'].indexOf(tag) !== -1) return;
      for (var i = 0; i < node.childNodes.length; i++) {
        walk(node.childNodes[i]);
      }
    }
  }

  if (containers.length === 0) {
    walk(document.body);
  } else {
    containers.forEach(walk);
  }
})();
