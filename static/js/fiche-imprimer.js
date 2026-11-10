// Imprime UNE fiche élève de /enseignants/, sans son corrigé ni le reste de la page.
// Le bouton porte data-imprimer-fiche="<id de la section .fiche>". Les classes posées ici
// sont lues par assets/scss/_enseignants.scss (@media print) et retirées après l'impression.
// data-imprimer-corrige="<id>" (10/11/2026, page Littérature) : imprime le corrigé de la fiche, déplié, avec le bloc
// .fiche__prof (programme, déroulé) et sans la partie élève ; l'état replié du corrigé est rétabli après.
(function () {
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-imprimer-fiche], [data-imprimer-corrige]");
    if (!b) return;
    var corrige = b.hasAttribute("data-imprimer-corrige");
    var cible = document.getElementById(b.getAttribute(corrige ? "data-imprimer-corrige" : "data-imprimer-fiche"));
    if (!cible) return;
    var replis = corrige ? Array.prototype.filter.call(cible.querySelectorAll("details.fiche__corrige"), function (d) { return !d.open; }) : [];
    replis.forEach(function (d) { d.open = true; });
    document.body.classList.add("imprime-une-fiche");
    if (corrige) document.body.classList.add("imprime-corrige-seul");
    cible.classList.add("imprime-cible");
    var fin = function () {
      document.body.classList.remove("imprime-une-fiche", "imprime-corrige-seul");
      cible.classList.remove("imprime-cible");
      replis.forEach(function (d) { d.open = false; });
      window.removeEventListener("afterprint", fin);
    };
    window.addEventListener("afterprint", fin);
    window.print();
  });
})();
