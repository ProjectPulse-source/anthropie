"""dette_cout_figures.py -- figures du volet 2 du dossier dette (« Combien coûte la dette publique ? ») ajoutées à la
phase B de la refonte (11/10/2026) : la décomposition comptable de la hausse de la charge (encours / taux implicite),
et les versions TÉLÉPHONE (300 de large, police jamais sous 13,5) des figures de la page.

Appelé par update_dette_insee.py, qui calcule tout et passe ici des séries déjà gardées : aucun calcul de donnée dans
ce module, seulement du dessin. Le contexte graphique (palette, police, formateurs de nombres) arrive par `C`, un
dictionnaire construit par le générateur : une seule définition de la palette, dans le générateur.

Contrôles appliqués par l'appelant : parité de chaque version téléphone avec sa version détaillée
(pied_figure.parite : tout nombre dessiné en téléphone figure dans la description de la détaillée ; aucune police
sous 13,5), estimation des textes hors cadre (pied_figure.hors_cadre), hauteurs lues par le shortcode figure-svg.
"""
from __future__ import annotations

import html

import pied_figure as PF

WM = PF.LARGEUR_M
FS = PF.POLICE_M


def esc(s: str) -> str:
    return html.escape(str(s), quote=False)


def _pied_m(e, y0, source, note, licence, C):
    return PF.pied_mobile(e, y0, [(source, C["INK2"], "pied-source"), (note, C["INK2"], "pied-note"),
                                  (licence, C["MUTED"], "pied-licence")], C["GRID"])


def _courbe_m(e, y0, h, series, a0, a1, vmin, vmax, ticks, C, ml=34, mr=8, fmt_tick=str, ans_axe=None):
    """Panneau de courbes pour le téléphone : axe Y à gauche (ticks), années sous l'axe. Rend (X, Y)."""
    def X(a):
        return ml + (a - a0) / (a1 - a0) * (WM - ml - mr)

    def Y(v):
        return y0 + h - (v - vmin) / (vmax - vmin) * h
    for t in ticks:
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (ml, Y(t), WM - mr, Y(t),
                                                                              C["AXIS"] if t == vmin else C["GRID"]))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%s</text>'
                 % (ml - 5, Y(t) + 5, FS, C["MUTED"], esc(fmt_tick(t))))
    for a in (ans_axe or (a0, a1)):
        e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s">%d</text>'
                 % (X(a), y0 + h + 19, FS, C["MUTED"], "start" if a == a0 else ("end" if a == a1 else "middle"), a))
    for pts, couleur, ep in series:
        d = "M" + " L".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in pts)
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
                 'stroke-linejoin="round"/>' % (d, couleur, ep))
    return X, Y


# ------------------------------------------------------------ décomposition
TXT_DEC = {
    "fr": {
        "titre": "D'où vient la hausse de la charge d'intérêts : encours ou taux implicite ?",
        "titre_m": "Hausse de la charge d'intérêts : encours ou taux implicite ?",
        "unite": "Variation annuelle de la charge, en milliards d'euros, et ce qui la compose",
        "unite_m": "en milliards d'euros, année par année",
        "leg": ("hausse de l'encours", "hausse du taux implicite", "variation de la charge"),
        "cumul": "De %d à %d : %s Md€, dont %s par l'encours et %s par le taux implicite",
        "cumul_m": ("De %d à %d :", "%s Md€", "encours %s · taux implicite %s"),
        "desc": ("Barres empilées par année, de %d à %d, en milliards d'euros : en bleu la contribution de la hausse de "
                 "l'encours de dette, en orange celle du taux implicite ; le point noir est la variation de la charge "
                 "d'intérêts. %s Sur l'ensemble, de %d à %d, la charge augmente de %s milliards : %s au titre de l'encours, "
                 "%s au titre du taux implicite. Décomposition comptable, non causale."),
        "annee": "En %d : %s (encours %s, taux implicite %s).",
        "src": "Calcul sur séries Eurostat (gov_10a_main, D41PAY) et INSEE (dette de Maastricht au 31 décembre), %d-%d",
        "note": ("Décomposition comptable encours / taux implicite (contributions à mi-chemin, calculées chaque année puis "
                 "additionnées). La part du taux implicite mêle "
                 "refinancement, composition de la dette et indexation des titres indexés sur l'inflation : elle ne "
                 "mesure pas à elle seule l'effet des taux de marché."),
        "md": "Md€",
    },
    "en": {
        "titre": "Where does the rise in interest come from: the debt stock or the implicit rate?",
        "titre_m": "Rise in interest: the debt stock or the implicit rate?",
        "unite": "Annual change in interest, billion euros, and what it is made of",
        "unite_m": "billion euros, year by year",
        "leg": ("rise in the debt stock", "rise in the implicit rate", "change in interest"),
        "cumul": "From %d to %d: %s bn, of which %s from the stock and %s from the implicit rate",
        "cumul_m": ("From %d to %d:", "%s bn", "stock %s · implicit rate %s"),
        "desc": ("Stacked bars by year, from %d to %d, in billion euros: in blue the contribution of the rise in the debt "
                 "stock, in orange that of the implicit rate; the black dot is the change in interest. %s Overall, from "
                 "%d to %d, interest rises by %s billion: %s from the stock, %s from the implicit rate. An accounting "
                 "decomposition, not a causal one."),
        "annee": "In %d: %s (stock %s, implicit rate %s).",
        "src": "Computed on Eurostat (gov_10a_main, D41PAY) and INSEE (Maastricht debt at 31 December) series, %d-%d",
        "note": ("Accounting decomposition, debt stock / implicit rate (midpoint contributions, computed each year and then "
                 "added up). The implicit-rate part mixes "
                 "refinancing, the composition of the debt and the indexation of inflation-linked bonds: on its own, it "
                 "does not measure the effect of market rates."),
        "md": "bn",
    },
}


def _desc_dec(rows, cumul, lang, C):
    T, nb, sg = TXT_DEC[lang], C["nb"][lang], C["sg"][lang]
    ans = " ".join(T["annee"] % (r["annee"], sg(r["delta"]), sg(r["volume"]), sg(r["taux"])) for r in rows)
    return T["desc"] % (rows[0]["annee"], rows[-1]["annee"], ans, cumul["a0"], cumul["a1"], sg(cumul["delta"]),
                        sg(cumul["volume"]), sg(cumul["taux"]))


def fig_decomp(rows, cumul, lang, C, licence):
    """Barres empilées des contributions (encours en bleu = stock, taux implicite en orange = coût), point noir = variation."""
    T, sg = TXT_DEC[lang], C["sg"][lang]
    W, H = 720, 330
    ml, mr, mt, mb = 56, 24, 92, 40
    vals = [r["volume"] for r in rows] + [r["taux"] for r in rows] + [r["delta"] for r in rows]
    pos = [max(0, r["volume"]) + max(0, r["taux"]) for r in rows]
    neg = [min(0, r["volume"]) + min(0, r["taux"]) for r in rows]
    vmax = max(pos + [max(vals)]) * 1.15
    vmin = min(neg + [min(vals), 0]) * 1.15

    def Y(v):
        return mt + (vmax - v) / (vmax - vmin) * (H - mt - mb)
    n = len(rows)
    pas = (W - ml - mr) / n
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="dc-t dc-d" font-family="%s">' % (W, H, C["FONT"]),
         '<title id="dc-t">%s</title>' % esc(T["titre"]),
         '<desc id="dc-d">%s</desc>' % esc(_desc_dec(rows, cumul, lang, C)),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H),
         '<text x="0" y="22" font-size="15" font-weight="600" fill="%s">%s</text>' % (C["INK"], esc(T["titre"])),
         '<text x="0" y="42" font-size="12" fill="%s">%s</text>' % (C["INK2"], esc(T["unite"])),
         '<text x="0" y="64" font-size="13" font-weight="600" fill="%s">%s</text>'
         % (C["INK"], esc(T["cumul"] % (cumul["a0"], cumul["a1"], sg(cumul["delta"]), sg(cumul["volume"]),
                                        sg(cumul["taux"]))))]
    # légende
    x = 0
    for lib, coul, forme in ((T["leg"][0], C["BLEU"], "rect"), (T["leg"][1], C["ORANGE"], "rect"),
                             (T["leg"][2], C["INK"], "rond")):
        if forme == "rect":
            e.append('<rect x="%d" y="72" width="12" height="12" fill="%s"/>' % (x, coul))
        else:
            e.append('<circle cx="%d" cy="78" r="5" fill="%s"/>' % (x + 6, coul))
        e.append('<text x="%d" y="83" font-size="12" fill="%s">%s</text>' % (x + 17, C["INK2"], esc(lib)))
        x += 17 + int(6.2 * len(lib)) + 22
    g = 0
    pas_g = 5 if vmax - vmin < 30 else 10
    t = pas_g * int(vmin // pas_g)
    while t <= vmax:
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>'
                 % (ml, Y(t), W - mr, Y(t), C["AXIS"] if t == 0 else C["GRID"]))
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s" text-anchor="end">%s</text>'
                 % (ml - 6, Y(t) + 4, C["MUTED"], esc(sg(t, 0) if t else "0")))
        t += pas_g
    for i, r in enumerate(rows):
        cx = ml + pas * (i + 0.5)
        bw = min(56, pas * 0.5)
        haut, bas = 0.0, 0.0
        for v, coul in ((r["volume"], C["BLEU"]), (r["taux"], C["ORANGE"])):
            if v >= 0:
                e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'
                         % (cx - bw / 2, Y(haut + v), bw, Y(haut) - Y(haut + v), coul))
                haut += v
            else:
                e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'
                         % (cx - bw / 2, Y(bas), bw, Y(bas + v) - Y(bas), coul))
                bas += v
        e.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s" stroke="#ffffff" stroke-width="1.5"/>'
                 % (cx, Y(r["delta"]), C["INK"]))
        e.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="600" fill="%s" text-anchor="middle">%s</text>'
                 % (cx, min(Y(haut), Y(r["delta"])) - 9, C["INK"], esc(sg(r["delta"]))))
        e.append('<text x="%.1f" y="%.1f" font-size="11" fill="%s" text-anchor="middle">%d</text>'
                 % (cx, H - mb + 18, C["MUTED"], r["annee"]))
    return PF.pied(e, H + 4, W, [(T["src"] % (cumul["a0"], cumul["a1"]), C["INK2"], "pied-source"),
                                 (T["note"], C["INK2"], "pied-note"), (licence, C["MUTED"], "pied-licence")],
                   C["GRID"]) + "\n"


def fig_decomp_m(rows, cumul, lang, C, licence_m, svg_d):
    """Téléphone : une ligne par année (année, variation en gras), une barre empilée dessous, à une échelle commune."""
    T, sg = TXT_DEC[lang], C["sg"][lang]
    e, y = PF.tete_mobile("dcm2", T["titre_m"], PF_desc(svg_d), C["INK"], C["FONT"])
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y + 4, FS, C["INK2"], esc(T["unite_m"])))
    y += 30
    c0, c1, c2 = T["cumul_m"]
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS, C["INK2"], esc(c0 % (cumul["a0"], cumul["a1"]))))
    e.append('<text x="%d" y="%d" font-size="17" font-weight="600" fill="%s" text-anchor="end">%s</text>'
             % (WM, y, C["INK"], esc(c1 % sg(cumul["delta"]))))
    y += 20
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>'
             % (y, FS, C["INK2"], esc(c2 % (sg(cumul["volume"]), sg(cumul["taux"])))))
    y += 22
    for lib, coul in ((T["leg"][0], C["BLEU"]), (T["leg"][1], C["ORANGE"])):
        e.append('<rect x="0" y="%d" width="12" height="12" fill="%s"/>' % (y - 11, coul))
        e.append('<text x="18" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS, C["INK2"], esc(lib)))
        y += 20
    y += 6
    m = max(max(0, r["volume"]) + max(0, r["taux"]) for r in rows)
    mneg = -min(min(0, r["volume"]) + min(0, r["taux"]) for r in rows)
    zero = 4 + (WM - 8) * mneg / (m + mneg) if mneg else 4
    k = (WM - 8 - zero + 4) / m
    for r in rows:
        y += 18
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%d</text>' % (y, FS, C["INK2"], r["annee"]))
        e.append('<text x="%d" y="%d" font-size="15" font-weight="600" fill="%s" text-anchor="end">%s</text>'
                 % (WM, y, C["INK"], esc(sg(r["delta"]))))
        y += 8
        xp, xn = zero, zero
        for v, coul in ((r["volume"], C["BLEU"]), (r["taux"], C["ORANGE"])):
            if v >= 0:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="14" fill="%s"/>' % (xp, y, max(1.5, v * k), coul))
                xp += v * k
            else:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="14" fill="%s"/>' % (xn + v * k, y, max(1.5, -v * k), coul))
                xn += v * k
        y += 22
    return _pied_m(e, y + 8, T["src"] % (cumul["a0"], cumul["a1"]), T["note"], licence_m, C)


def PF_desc(svg):
    import re
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S).group(1))


# ------------------------------------------------------------------- ciseau
def fig_ciseau_m(dette_annuel, d41_pib, lang, C, licence_m, svg_d, titre, source, note):
    """Deux panneaux empilés sur le même axe des années : la dette (bleu), la charge (orange), en % du PIB."""
    nb = C["nb"][lang]
    pc = " %" if lang == "fr" else "%"
    e, y = PF.tete_mobile("czm", titre, PF_desc(svg_d), C["INK"], C["FONT"])
    a0, a1 = min(min(dette_annuel), min(d41_pib)), max(max(dette_annuel), max(d41_pib))
    lib = ({"fr": ("Dette publique, en % du PIB", "Intérêts, en % du PIB"),
            "en": ("Public debt, % of GDP", "Interest, % of GDP")})[lang]
    for k, (serie, coul, vmax, ticks) in enumerate(((dette_annuel, C["BLEU"], 125, (0, 40, 80, 120)),
                                                     (d41_pib, C["ORANGE"], 4, (0, 1, 2, 3, 4)))):
        y += 14
        e.append('<text x="0" y="%d" font-size="%s" font-weight="600" fill="%s">%s</text>' % (y, FS, C["INK"], esc(lib[k])))
        y += 14
        pts = sorted(serie.items())
        X, Y = _courbe_m(e, y, 130, [(pts, coul, 2.6)], a0, a1, 0, vmax, ticks, C)
        premier, dernier = pts[0], pts[-1]
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (X(dernier[0]), Y(dernier[1]), coul))
        e.append('<text x="%.1f" y="%.1f" font-size="15" font-weight="600" fill="%s" text-anchor="end">%s</text>'
                 % (X(dernier[0]) - 6, Y(dernier[1]) - 9 if k == 0 else Y(dernier[1]) - 10, C["INK"],
                    esc(nb(dernier[1]) + pc)))
        e.append('<text x="%.1f" y="%.1f" font-size="%s" font-weight="600" fill="%s">%s</text>'
                 % (X(premier[0]) + 2, Y(premier[1]) - 9, FS, coul, esc(nb(premier[1]) + pc)))
        if k == 1:
            creux = min(pts, key=lambda p: p[1])
            e.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (X(creux[0]), Y(creux[1]), coul))
            e.append('<text x="%.1f" y="%.1f" font-size="%s" font-weight="600" fill="%s" text-anchor="middle">%s</text>'
                     % (X(creux[0]), Y(creux[1]) + 20, FS, coul, esc(nb(creux[1]) + pc)))
        y += 130 + 26
    return _pied_m(e, y + 4, source, note, licence_m, C)


# ------------------------------------------------------------------- charge
def fig_charge_m(interets_md, prev, lang, C, licence_m, svg_d, titre, source, note):
    """Observé en trait plein ; prévision en cercles évidés, sans trait qui la relie à l'observé (base non réconciliée)."""
    nb = C["nb"][lang]
    md = " Md€" if lang == "fr" else " bn"
    e, y = PF.tete_mobile("chm", titre, PF_desc(svg_d), C["INK"], C["FONT"])
    obs = sorted(interets_md.items())
    pv = sorted((a, v) for a, v in (prev or {}).items() if a > obs[-1][0])
    a0, a1 = obs[0][0], (pv[-1][0] if pv else obs[-1][0])
    vmax = max([v for _, v in obs] + [v for _, v in pv]) * 1.15
    y += 16
    X, Y = _courbe_m(e, y, 190, [(obs, C["ORANGE"], 2.6)], a0, a1, 0, vmax, [t for t in (0, 20, 40, 60, 80, 100) if t < vmax],
                     C, mr=14, ans_axe=(a0, obs[-1][0]) if not pv else (a0, a1))
    creux = min(obs, key=lambda p: p[1])
    e.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (X(creux[0]), Y(creux[1]), C["ORANGE"]))
    e.append('<text x="%.1f" y="%.1f" font-size="%s" font-weight="600" fill="%s" text-anchor="middle">%s</text>'
             % (X(creux[0]), Y(creux[1]) + 20, FS, C["ORANGE"], esc(nb(creux[1]))))
    lx, ly = X(obs[-1][0]), Y(obs[-1][1])
    e.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s"/>' % (lx, ly, C["ORANGE"]))
    e.append('<text x="%.1f" y="%.1f" font-size="15" font-weight="600" fill="%s" text-anchor="end">%s</text>'
             % (lx - 8, ly - 4, C["INK"], esc(nb(obs[-1][1]) + md)))
    for a, v in pv:
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#ffffff" stroke="%s" stroke-width="2"/>' % (X(a), Y(v), C["ORANGE"]))
    y += 190 + 34
    if pv:
        lib = ({"fr": "Prévision du Gouvernement :", "en": "Government forecast:"})[lang]
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS, C["INK2"], esc(lib)))
        for a, v in pv:
            y += 19
            d = 0 if v == round(v) else 1
            e.append('<text x="0" y="%d" font-size="%s" font-weight="600" fill="%s">%d : %s</text>'
                     % (y, FS, C["ORANGE"], a, esc(nb(v, d) + md)) if lang == "fr" else
                     '<text x="0" y="%d" font-size="%s" font-weight="600" fill="%s">%d: %s</text>'
                     % (y, FS, C["ORANGE"], a, esc(nb(v, d) + md)))
        y += 10
    return _pied_m(e, y + 4, source, note, licence_m, C)


# ------------------------------------------------------------------- marché
def fig_marche_m(apparent, marche, lang, C, licence_m, svg_d, titre, source, note):
    nb = C["nb"][lang]
    pc = " %" if lang == "fr" else "%"
    e, y = PF.tete_mobile("tmm", titre, PF_desc(svg_d), C["INK"], C["FONT"])
    ans = sorted(int(a) for a in apparent if a in marche)
    pa = [(a, apparent[str(a)]) for a in ans]
    pm = [(a, marche[str(a)]) for a in ans]
    y += 14
    X, Y = _courbe_m(e, y, 200, [(pm, C["INK2"], 1.6), (pa, C["ORANGE"], 2.6)], ans[0], ans[-1], -1, 7, (0, 2, 4, 6), C)
    for pts, coul in ((pm, C["INK2"]), (pa, C["ORANGE"])):
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (X(pts[-1][0]), Y(pts[-1][1]), coul))
    y += 200 + 36
    lib = ({"fr": ("Taux à 10 ans", "Taux implicite"), "en": ("10-year rate", "Implicit rate")})[lang]
    for (nom, pts, coul) in ((lib[0], pm, C["INK2"]), (lib[1], pa, C["ORANGE"])):
        e.append('<line x1="0" y1="%d" x2="18" y2="%d" stroke="%s" stroke-width="%s"/>'
                 % (y - 5, y - 5, coul, 1.6 if coul == C["INK2"] else 2.6))
        e.append('<text x="24" y="%d" font-size="%s" fill="%s">%s %d</text>' % (y, FS, C["INK2"], esc(nom), pts[-1][0]))
        e.append('<text x="%d" y="%d" font-size="15" font-weight="600" fill="%s" text-anchor="end">%s</text>'
                 % (WM, y, coul, esc(nb(pts[-1][1]) + pc)))
        y += 22
    return _pied_m(e, y + 4, source, note, licence_m, C)


# ------------------------------------------------------------------- masses
def fig_masses_m(interets, cofog, noms, lang, C, licence_m, svg_d, titre, source, note):
    """Courbes sans étiquette dans le tracé ; valeurs finales et croissance depuis le creux en liste dessous."""
    nb = C["nb"][lang]
    e, y = PF.tete_mobile("mam", titre, PF_desc(svg_d), C["INK"], C["FONT"])
    fonctions = ("GF07", "GF09", "GF03")
    ans = sorted(set(interets) & set.intersection(*[set(cofog[c]) for c in fonctions]))
    a0, a1 = ans[0], ans[-1]
    gris = {"GF07": C["INK2"], "GF09": C["MUTED"], "GF03": C["CTX3"]}
    vmax = max(max(cofog[c][a] for a in ans) for c in fonctions) * 1.08
    y += 14
    series = [([(a, cofog[c][a]) for a in ans], gris[c], 1.6) for c in fonctions]
    series.append(([(a, interets[a]) for a in ans], C["ORANGE"], 2.6))
    X, Y = _courbe_m(e, y, 200, series, a0, a1, 0, vmax, [t for t in (0, 100, 200, 300) if t < vmax], C)
    ref = min(ans, key=lambda a: interets[a])
    y += 200 + 38
    md = " Md€" if lang == "fr" else " bn"
    lignes = [(noms["interets"], interets[a1], interets[a1] / interets[ref] - 1, C["ORANGE"], 2.6)]
    lignes += [(noms[c], cofog[c][a1], cofog[c][a1] / cofog[c][ref] - 1, gris[c], 1.6) for c in fonctions]
    lignes.sort(key=lambda l: -l[1])
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>'
             % (y, FS, C["INK2"], esc(("En %d, et évolution depuis %d :" if lang == "fr" else "In %d, and change since %d:")
                                       % (a1, ref))))
    for nom, v, cr, coul, ep in lignes:
        y += 21
        e.append('<line x1="0" y1="%d" x2="14" y2="%d" stroke="%s" stroke-width="%s"/>' % (y - 5, y - 5, coul, ep))
        e.append('<text x="20" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS, C["INK2"], esc(nom)))
        e.append('<text x="%d" y="%d" font-size="%s" font-weight="600" fill="%s" text-anchor="end">%s</text>'
                 % (WM - 62, y, FS, C["INK"], esc(nb(v, 0) + md)))
        e.append('<text x="%d" y="%d" font-size="%s" fill="%s" text-anchor="end">%+d%s</text>'
                 % (WM, y, FS, C["MUTED"], round(cr * 100), " %" if lang == "fr" else "%"))
    y += 14
    return _pied_m(e, y + 4, source, note, licence_m, C)


# ------------------------------------------------------------------- longue
def fig_longue_m(annuel, pct_courant, label_courant, seuils, lang, C, licence_m, svg_d, titre, source, note):
    nb = C["nb"][lang]
    pc = " %" if lang == "fr" else "%"
    e, y = PF.tete_mobile("dlm", titre, PF_desc(svg_d), C["INK"], C["FONT"])
    # meme trace que la version detaillee : la serie annuelle, prolongee par le dernier trimestre publie
    pts = sorted(annuel.items()) + [(max(annuel) + 0.25, pct_courant)]
    y += 14
    X, Y = _courbe_m(e, y, 190, [(pts, C["BLEU"], 2.6)], pts[0][0], pts[-1][0], 0, 130, (0, 30, 60, 90, 120), C,
                     mr=14, ans_axe=(pts[0][0], max(annuel)))
    e.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s"/>' % (X(pts[-1][0]), Y(pts[-1][1]), C["ORANGE"]))
    y += 190 + 36
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>'
             % (y, FS, C["INK2"], esc("Seuils franchis (fin d'année) :" if lang == "fr" else "Thresholds crossed (year-end):")))
    lig = [("%d" % pts[0][0], nb(pts[0][1]) + pc)]
    lig += [(str(seuils[s]), "> %d%s" % (s, pc)) for s in (30, 60, 80, 100)]
    lig.append((label_courant, nb(pct_courant) + pc))
    for k in range(0, len(lig), 2):
        y += 21
        for j, (an, v) in enumerate(lig[k:k + 2]):
            x = 0 if j == 0 else 154
            e.append('<text x="%d" y="%d" font-size="%s" fill="%s">%s</text>' % (x, y, FS, C["INK2"], esc(an)))
            e.append('<text x="%d" y="%d" font-size="%s" font-weight="600" fill="%s" text-anchor="end">%s</text>'
                     % (x + 140, y, FS, C["BLEU"], esc(v)))
    y += 14
    return _pied_m(e, y + 4, source, note, licence_m, C)


# ------------------------------------------------------------------- taux implicite seul
def fig_taux_m(taux, lang, C, licence_m, svg_d, titre, source, note):
    """Le taux implicite seul (figure de la page, en repli) : depart, point bas et derniere valeur etiquetes."""
    nb = C["nb"][lang]
    pc = " %" if lang == "fr" else "%"
    e, y = PF.tete_mobile("tam", titre, PF_desc(svg_d), C["INK"], C["FONT"])
    pts = sorted((int(a), v) for a, v in taux.items())
    y += 30
    X, Y = _courbe_m(e, y, 200, [(pts, C["ORANGE"], 2.6)], pts[0][0], pts[-1][0], 0, 7, (0, 2, 4, 6), C, mr=14)
    creux = min(pts, key=lambda p: p[1])
    for (a, v), ancre, dy in ((pts[0], "start", -10), (creux, "middle", 22), (pts[-1], "end", -12)):
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (X(a), Y(v), C["ORANGE"]))
        e.append('<text x="%.1f" y="%.1f" font-size="15" font-weight="600" fill="%s" text-anchor="%s">%s</text>'
                 % (X(a) + (6 if ancre == "start" else 0), Y(v) + dy, C["INK"], ancre, esc(nb(v) + pc)))
    y += 200 + 30
    return _pied_m(e, y + 4, source, note, licence_m, C)
