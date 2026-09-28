(function() {
  if (document.documentElement.lang !== 'fr') return;

  var THIN_NBSP = '\u202F';
  var NBSP = '\u00A0';

  var containers = document.querySelectorAll('body');

  // UN NOMBRE NE SE SEPARE JAMAIS DE SON UNITE, ni de ses milliers (regle
  // d'auteur, 28/09 : « les symboles, les chiffres, la ponctuation doivent etre
  // insecables quel que soit le support »). Cette regle vivait dans DEUX organes
  // -- le linter des sources .md et le partial fr-typo.html -- et manquait au
  // troisieme, celui-ci, le seul a traiter ce qu'un script injecte apres coup.
  // Un « € » s'est ainsi retrouve seul en debut de ligne sur Android, sans son
  // montant. La regle couvre aussi les espaces de milliers, que certaines
  // plateformes rendent par une espace ordinaire.
  var UNITES = 'Md€|M€|k€|€|%|km|kg|ha|min|h';

  function fix(text) {
    return text
      .replace(new RegExp('(\\d) (?=(?:' + UNITES + ')(?![A-Za-z]))', 'g'), '$1' + NBSP)
      .replace(/(\d) (?=\d{3}(?!\d))/g, '$1' + NBSP)
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
