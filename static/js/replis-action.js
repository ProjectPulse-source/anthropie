/* replis-action.js -- ligne d'action sous le titre de chaque bloc replié (details.repli).
 *
 * Demande de l'auteur (30/09/2026, maquette D + décompte de B) : un lecteur en diagonale ne voyait pas que le bloc
 * se déplie. Sous le titre -- qui porte déjà la conclusion du repli --, une ligne dit l'action et ce qu'on gagne à
 * ouvrir : « Lire le détail · 3 paragraphes ▾ », puis « Replier ▴ » une fois ouvert.
 *
 * Le décompte est CALCULÉ sur le contenu réel du repli, jamais saisi : paragraphes, points de liste, figures et
 * tableaux du repli, hors replis imbriqués. Rien ne change sans JavaScript : le repli reste un repli, son titre dit l'essentiel.
 *
 * Règle constante de l'auteur (23/10/2026) : TOUT bloc qui se déplie, sur toute page, porte cette ligne, qu'il soit
 * écrit dans le Markdown, posé par un shortcode ou construit par un script (fiche de commune : la ligne manquait sous
 * « Évolution 2024-2025 et détail des comptes », replis hors de la classe .repli et construits après le chargement).
 * D'où : tout <details> est visé, la classe .repli ne décide plus que du cadre ; les blocs posés plus tard sont vus par
 * un MutationObserver ; un bloc sans contenu au-delà de son titre n'en reçoit pas (rien à lire). Seule exemption,
 * liste fermée contrôlée par scripts/check-replis.py : la NAVIGATION (data-repli="nav" : sommaire de page, menu du
 * dossier), où le bloc ouvre des liens, pas un détail.
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

  function decompte(d) {
    // Les VRAIS éléments du repli, où qu'ils soient enveloppés (conteneur à défilement, bloc de figure, corps de notion),
    // hors replis imbriqués et hors titre -- compter l'enveloppe ET son contenu donnait « 2 tableaux » pour un.
    // Paragraphes et points vides ne comptent pas ; une figure faite d'une seule image, si.
    function propres(sel, texte) {
      return Array.prototype.filter.call(d.querySelectorAll(sel), function (e) {
        return e.closest("details") === d && !e.closest("summary") && (!texte || e.textContent.trim().length > 0);
      }).length;
    }
    // Un tableau construit en blocs (role="table", fiche de commune) est un tableau pour le lecteur.
    var n = [propres("p", true), propres("li", true), propres("figure"), propres("table, [role='table']")];
    var parts = [];
    n.forEach(function (k, i) {
      if (k > 0) parts.push(k + NB + T.unites[i][k > 1 ? 1 : 0]);
    });
    return parts.join(", ");
  }

  function aDuContenu(d) {
    return Array.prototype.some.call(d.children, function (c) {
      return c.tagName !== "SUMMARY" && (c.textContent.trim().length > 0 || c.querySelector("img, svg, table, canvas"));
    });
  }

  function poser(d) {
    if (d.getAttribute("data-repli") === "nav") return;
    var s = d.querySelector(":scope > summary");
    if (!s || s.querySelector(".repli__action") || !aDuContenu(d)) return;
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
    var d = cible && cible.closest("details");
    if (d && !d.open) {
      d.open = true;
      cible.scrollIntoView();
    }
  }

  function tout(racine) {
    if (racine.matches && racine.matches("details")) poser(racine);
    if (racine.querySelectorAll) Array.prototype.forEach.call(racine.querySelectorAll("details"), poser);
  }

  function init() {
    tout(document);
    ouvrirCible();
    // Blocs construits après le chargement (fiche de commune, tableaux tirés d'un JSON) : même ligne, sans appel à faire.
    if (window.MutationObserver) {
      new MutationObserver(function (ms) {
        ms.forEach(function (m) { Array.prototype.forEach.call(m.addedNodes, function (n) { if (n.nodeType === 1) tout(n); }); });
      }).observe(document.body, { childList: true, subtree: true });
    }
  }
  window.addEventListener("hashchange", ouvrirCible);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
