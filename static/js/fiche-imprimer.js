// Imprime UNE fiche élève de /enseignants/, sans son corrigé ni le reste de la page.
// Le bouton porte data-imprimer-fiche="<id de la section .fiche>". Les classes posées ici
// sont lues par assets/scss/_enseignants.scss (@media print) et retirées après l'impression.
(function () {
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-imprimer-fiche]");
    if (!b) return;
    var cible = document.getElementById(b.getAttribute("data-imprimer-fiche"));
    if (!cible) return;
    document.body.classList.add("imprime-une-fiche");
    cible.classList.add("imprime-cible");
    var fin = function () {
      document.body.classList.remove("imprime-une-fiche");
      cible.classList.remove("imprime-cible");
      window.removeEventListener("afterprint", fin);
    };
    window.addEventListener("afterprint", fin);
    window.print();
  });
})();
