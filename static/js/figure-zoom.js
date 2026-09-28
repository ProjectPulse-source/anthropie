/* figure-zoom.js — agrandir une figure du corps, au clic, sur mobile comme sur bureau.

   DEFAUT TRAITE (auteur, 28/09) : « sur telephone et sur ordi de bureau il n'est
   pas possible de cliquer sur le graphique pour l'agrandir ». Les figures sont
   servies a 720 px de large et reduites par le CSS ; un lecteur qui veut lire une
   etiquette ou un cartouche n'avait aucun moyen de le faire, et un journaliste
   encore moins. Le service au lecteur prime sur l'elegance du composant.

   PARTI PRIS. Zero dependance, comme le reste du depot. Le SVG est reaffiche en
   plein ecran dans une couche, sans rien telecharger de plus : c'est le MEME
   fichier, deja en cache. La couche ne bloque pas le zoom natif du navigateur,
   donc le pincement fonctionne par-dessus sur telephone.

   ACCESSIBILITE. La figure devient un bouton reel (role, tabindex, libelle), pas
   une image avec un gestionnaire de clic : elle s'atteint au clavier, s'active a
   Entree ou Espace, et la couche se ferme a Echap ou au clic. Le focus revient
   sur la figure d'origine a la fermeture, sinon le lecteur au clavier repart du
   haut de la page.

   NE S'APPLIQUE PAS aux figures deja cliquables ni aux images decoratives : on
   ne traite que `figure.figure-ciseau img` et `.dette-chiffres__figure img`,
   c'est-a-dire les figures de donnees du dossier. */
(function () {
  "use strict";

  var EN = document.documentElement.lang === "en";
  var T = EN
    ? { ouvrir: "Enlarge this figure", fermer: "Close", aide: "Click or press Escape to close" }
    : { ouvrir: "Agrandir cette figure", fermer: "Fermer",
        aide: "Cliquer ou appuyer sur Échap pour fermer" };

  var figures = document.querySelectorAll(
    "figure.figure-ciseau img, .dette-chiffres__figure img");
  if (!figures.length) return;

  var couche = null;
  var origine = null;

  function fermer() {
    if (!couche) return;
    couche.remove();
    couche = null;
    document.body.style.overflow = "";
    if (origine) { origine.focus(); origine = null; }
  }

  function ouvrir(img) {
    fermer();
    origine = img;
    couche = document.createElement("div");
    couche.className = "figure-zoom";
    couche.setAttribute("role", "dialog");
    couche.setAttribute("aria-modal", "true");
    couche.setAttribute("aria-label", img.getAttribute("alt") || T.ouvrir);

    var grande = document.createElement("img");
    grande.src = img.currentSrc || img.src;
    grande.alt = img.getAttribute("alt") || "";
    grande.className = "figure-zoom__image";

    var bouton = document.createElement("button");
    bouton.type = "button";
    bouton.className = "figure-zoom__fermer";
    bouton.textContent = T.fermer;

    var aide = document.createElement("p");
    aide.className = "figure-zoom__aide";
    aide.textContent = T.aide;

    couche.appendChild(bouton);
    couche.appendChild(grande);
    couche.appendChild(aide);
    couche.addEventListener("click", fermer);
    document.body.appendChild(couche);
    // Le fond de page ne defile plus sous la couche : sur telephone, un scroll
    // derriere une couche plein ecran donne l'impression que le geste ne fait rien.
    document.body.style.overflow = "hidden";
    bouton.focus();
  }

  Array.prototype.forEach.call(figures, function (img) {
    if (img.closest("a")) return;          // deja cliquable : on ne double pas
    img.classList.add("est-agrandissable");
    img.setAttribute("role", "button");
    img.setAttribute("tabindex", "0");
    img.setAttribute("title", T.ouvrir);
    img.setAttribute("aria-label", (img.getAttribute("alt") || "") + " — " + T.ouvrir);
    img.addEventListener("click", function () { ouvrir(img); });
    img.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " " || e.key === "Spacebar") {
        e.preventDefault();
        ouvrir(img);
      }
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" || e.key === "Esc") fermer();
  });
})();
