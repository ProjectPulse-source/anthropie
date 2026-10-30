/* boucle-exemples.js — boutons d'exemples de la spirale (figure « boucle anthropique », auteur 29/10/2026).

   Chaque bouton remplace les deux sources de la figure (bureau, telephone) et son texte alternatif, puis montre
   le texte de l'exemple sous la legende. Les figures et les textes sont produits au build
   (layouts/partials/figures/boucle-anthropique.html, data/boucle_exemples.yaml) : le script ne compose rien.
   Sans script, les boutons restent caches et les textes s'affichent tous a la suite de la legende. */
(function () {
  "use strict";

  var figures = document.querySelectorAll("[data-boucle-exemples]");
  Array.prototype.forEach.call(figures, function (fig) {
    var barre = fig.querySelector(".boucle-exemples");
    var img = fig.querySelector("picture img");
    var source = fig.querySelector("picture source");
    var lecture = fig.querySelector(".boucle-exemples__lecture");
    var legende = fig.querySelector("figcaption");
    var boutons = barre.querySelectorAll("button");
    var panneaux = fig.querySelectorAll(".boucle-exemples__panneau");

    function choisir(bouton) {
      var id = bouton.getAttribute("data-ex");
      Array.prototype.forEach.call(boutons, function (b) {
        b.setAttribute("aria-pressed", b === bouton ? "true" : "false");
      });
      source.setAttribute("srcset", bouton.getAttribute("data-mobile"));
      img.setAttribute("src", bouton.getAttribute("data-desktop"));
      img.setAttribute("alt", bouton.getAttribute("data-alt"));
      Array.prototype.forEach.call(panneaux, function (p) {
        p.hidden = p.getAttribute("data-ex") !== id;
      });
      if (lecture) { lecture.hidden = !id; }
      // la legende decrit le schema (tours pales) : elle cede la place a la cle de lecture sous un exemple
      if (legende) { legende.hidden = !!id; }
    }

    Array.prototype.forEach.call(boutons, function (b) {
      b.addEventListener("click", function () { choisir(b); });
    });
    barre.hidden = false;
    choisir(boutons[0]);
  });
})();
