/* replis-action.js -- ligne d'action sous le titre de chaque bloc replié (details.repli).
 *
 * Demande de l'auteur (30/09/2026, maquette D + décompte de B) : un lecteur en diagonale ne voyait pas que le bloc
 * se déplie. Sous le titre -- qui porte déjà la conclusion du repli --, une ligne dit l'action et ce qu'on gagne à
 * ouvrir : « Lire le détail · 3 paragraphes ▾ », puis « Replier ▴ » une fois ouvert.
 *
 * Le décompte est CALCULÉ sur le contenu réel du repli, jamais saisi : paragraphes, points de liste, figures et
 * tableaux enfants directs. Rien ne change sans JavaScript : le repli reste un repli, son titre dit l'essentiel.
 * Texte injecté après le passage de french-typography.js : les insécables sont posées ICI, à la source
 * (règle de site du 28/09, troisième organe).
 */
(function () {
  "use strict";
  var en = (document.documentElement.getAttribute("lang") || "").slice(0, 2) === "en";
  var NB = " ";
  var T = en
    ? { lire: "Read the detail", replier: "Hide", unites: [["paragraph", "paragraphs"], ["point", "points"], ["figure", "figures"], ["table", "tables"]] }
    : { lire: "Lire le détail", replier: "Replier", unites: [["paragraphe", "paragraphes"], ["point", "points"], ["figure", "figures"], ["tableau", "tableaux"]] };

  function enfants(d, sel) {
    return Array.prototype.filter.call(d.children, function (c) { return c.matches(sel); });
  }

  function decompte(d) {
    var points = 0;
    enfants(d, "ul, ol").forEach(function (l) { points += enfants(l, "li").length; });
    // Figures et tableaux : les VRAIS éléments du repli, où qu'ils soient enveloppés (conteneur à défilement,
    // bloc de figure), hors replis imbriqués -- compter l'enveloppe ET son contenu donnait « 2 tableaux » pour un.
    function propres(sel) {
      return Array.prototype.filter.call(d.querySelectorAll(sel), function (e) { return e.closest("details") === d; }).length;
    }
    var n = [
      enfants(d, "p").filter(function (p) { return p.textContent.trim().length > 0; }).length,
      points,
      propres("figure"),
      propres("table")
    ];
    var parts = [];
    n.forEach(function (k, i) {
      if (k > 0) parts.push(k + NB + T.unites[i][k > 1 ? 1 : 0]);
    });
    return parts.join(", ");
  }

  function poser(d) {
    var s = d.querySelector(":scope > summary");
    if (!s || s.querySelector(".repli__action")) return;
    var c = decompte(d);
    var ligne = document.createElement("span");
    ligne.className = "repli__action";
    ligne.setAttribute("aria-hidden", "true");
    var ferme = document.createElement("span");
    ferme.className = "repli__ferme";
    ferme.textContent = T.lire + (c ? NB + "·" + NB + c : "") + NB + "▾";
    var ouvert = document.createElement("span");
    ouvert.className = "repli__ouvert";
    ouvert.textContent = T.replier + NB + "▴";
    ligne.appendChild(ferme);
    ligne.appendChild(ouvert);
    s.appendChild(ligne);
  }

  // Ancre visant un repli ou son contenu (contre-expertise de la page « Professeurs », 10/10/2026) : le repli s'ouvre,
  // sinon le lecteur arrivé par le lien croit qu'il n'a rien révélé. Seulement à l'arrivée par une ancre : aucun repli
  // n'est ouvert autrement, et le lecteur garde la main pour le refermer.
  function ouvrirCible() {
    var id = decodeURIComponent((location.hash || "").slice(1));
    var cible = id && document.getElementById(id);
    var d = cible && cible.closest("details.repli");
    if (d && !d.open) {
      d.open = true;
      cible.scrollIntoView();
    }
  }

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll("details.repli"), poser);
    ouvrirCible();
  }
  window.addEventListener("hashchange", ouvrirCible);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
