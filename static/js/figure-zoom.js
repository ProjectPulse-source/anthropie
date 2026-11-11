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
  // Ecran tactile sans souris ni clavier (telephone, tablette) : on ne parle ni de clic ni de touche Echap (11/11/2026).
  var TACTILE = !!(window.matchMedia && window.matchMedia("(hover: none) and (pointer: coarse)").matches);
  var T = EN
    ? { ouvrir: "Enlarge this figure", fermer: "Close",
        aide: TACTILE ? "Tap to close" : "Click or press Escape to close" }
    : { ouvrir: "Agrandir cette figure", fermer: "Fermer",
        aide: TACTILE ? "Toucher pour fermer" : "Cliquer ou appuyer sur Échap pour fermer" };

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
    // preventScroll : sans lui, rendre le focus a une figure qui depasse l'ecran faisait sauter la page de plusieurs
    // centaines de pixels a la fermeture (second controle du rendu, 11/11/2026).
    if (origine) {
      try { origine.focus({ preventScroll: true }); } catch (e) { origine.focus(); }
      origine = null;
    }
  }

  // Largeur de dessin de la version AFFICHEE : attribut width de la <source> retenue par le navigateur, sinon de
  // l'<img>. naturalWidth ne convient pas : ces SVG n'ont qu'un viewBox, et le navigateur leur prete 150 px de haut.
  function largeurDeDessin(img) {
    var src = img.currentSrc || img.src || "", p = img.parentNode, w = 0;
    if (p && p.tagName === "PICTURE") {
      Array.prototype.forEach.call(p.querySelectorAll("source"), function (s) {
        var fichier = ((s.getAttribute("srcset") || "").split(/[\s,]/)[0] || "").replace(/^.*\//, "");
        if (fichier && src.indexOf("/" + fichier) !== -1) w = parseInt(s.getAttribute("width"), 10) || w;
      });
    }
    return w || parseInt(img.getAttribute("width"), 10) || 0;
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
    // La couche donne la largeur de l'ecran (feuille de style), sans depasser le double de la taille de dessin :
    // une figure telephone (300 px) ouverte sur tablette ne devient pas trois fois plus haute que l'ecran.
    var dessin = largeurDeDessin(img);
    if (dessin) grande.style.maxWidth = Math.min(1440, dessin * 2) + "px";

    var bouton = document.createElement("button");
    bouton.type = "button";
    bouton.className = "figure-zoom__fermer";
    bouton.textContent = T.fermer;

    var aide = document.createElement("p");
    aide.className = "figure-zoom__aide";
    aide.textContent = T.aide;

    // L'aide avant l'image : sous une figure plus haute que l'ecran, elle n'etait pas visible a l'ouverture.
    couche.appendChild(bouton);
    couche.appendChild(aide);
    couche.appendChild(grande);
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
    // La couche est une boite modale (aria-modal) : la tabulation reste sur son seul element activable, le bouton
    // « Fermer », au lieu de partir vers les liens de la page masques derriere elle (second controle, 11/11/2026).
    if (couche && e.key === "Tab") {
      e.preventDefault();
      var b = couche.querySelector("button");
      if (b) b.focus();
    }
  });
})();
