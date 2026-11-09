# -*- coding: utf-8 -*-
"""figures_dette_futurs.py -- figures du volet « Quels futurs ? » (A2 éventail, B2 leviers), bureau et téléphone, FR et EN.

Maquettes arbitrées : PRO-20261109-092834 (réponse Dette-06) et ENTRANTE Dette-07 (09/11/2026) ; maquettes de référence :
D:\\PRO\\06_PROMOTION\\MAQUETTES_FIGURE_QUELS_FUTURS_2026-11-09\\maquettes_v2.py. Charte : bleu #184f95 dette (Commission),
orange #eb6834 trajectoire du Gouvernement (point contemporain), orange atténué #b8703f repère ancien (plan de 2024),
gris ce qui fait baisser. Pied commun : pied_figure (source, note, licence ; classes relues par « Réutiliser »).
Toutes les valeurs viennent du calcul R d'update_dette_futurs.py ; aucune n'est saisie ici.
"""
from __future__ import annotations

import html

import pied_figure as pf

BLEU, ORANGE, ORANGE_A, GRIS, ENCRE, SEC, GRILLE, FILET = "#184f95", "#eb6834", "#b8703f", "#8a8984", "#1a1a1a", "#52514e", "#e6e5e1", "#d8d6d0"
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
W = 720


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def nb(v: float, lang: str, d: int = 1) -> str:
    s = ("%." + str(d) + "f") % v
    s = s.replace("-", "−")
    return s.replace(".", ",") if lang == "fr" else s


def pct(v: float, lang: str) -> str:
    return nb(v, lang) + ("\u00a0%" if lang == "fr" else "%")


def txt(x, y, s, size=12, anchor="start", weight=400, fill=ENCRE):
    return '<text x="%.1f" y="%.1f" font-size="%s" font-weight="%d" text-anchor="%s" fill="%s">%s</text>' % (
        x, y, size, weight, anchor, fill, esc(s))


T = {
    "fr": dict(
        a_titre="La dette publique en 2030 : plusieurs futurs, sous quelles hypothèses ?",
        a_sous="Dette publique française, en % du PIB",
        p90="90e centile", p10="10e centile", ref="Commission, politique inchangée", ref2="sans nouvelles mesures après 2026",
        plf="Prévision du PLF 2027", psmt="Engagement d'octobre 2024", en_="en",
        ref35="Commission, politique inchangée (2035, hors graphique)",
        au_dela="Au-delà de 2030, hors de l'éventail : projection à politique inchangée de la Commission en 2035, {v} du PIB, "
                "sans nouvelles mesures après 2026.",
        bandes="Bandes, de la plus claire à la plus foncée : du 10e au 90e, du 20e au 80e et du 40e au 60e centile des "
               "trajectoires simulées par la Commission (8, 6 et 2 sur 10).",
        a_note="Les bandes sont des projections conditionnelles fondées sur des chocs économiques historiques ; elles "
               "ne prédisent ni les décisions futures ni leurs conséquences. {bandes} Les trois trajectoires reposent sur "
               "des hypothèses et des points de départ différents. Départs en 2025 : Commission {a} (février 2026), "
               "PLF 2027 {b} (octobre 2026), engagement de 2024 {c} (octobre 2024) ; l'engagement ne donne pas de "
               "valeur pour 2026.",
        a_note_m="Les bandes sont des projections conditionnelles fondées sur des chocs historiques, non des prévisions. "
                 "{bandes} Départs en 2025 : Commission {a}, PLF 2027 {b}, engagement de 2024 {c} ; l'engagement ne "
                 "donne pas de valeur pour 2026.",
        a_source_m="Sources : Commission européenne (DSM 2025) ; Gouvernement (plan d'octobre 2024, PLF 2027).",
        a_source="Sources : Commission européenne, Debt Sustainability Monitor 2025 (fiche France) ; Gouvernement, plan "
                 "budgétaire et structurel à moyen terme (octobre 2024) et rapport sur la dette annexé au PLF 2027.",
        licence="Graphique : Stéphane Lalut, CC BY 4.0 · stephane-lalut.com/dette-publique-quels-futurs/",
        licence_m="Graphique : Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
        b_titre="Dette publique en 2035 : ce que changent le solde, les taux et la croissance",
        b_sous="Effet en 2035 sur le ratio dette/PIB, en points de PIB, par rapport à la référence de la Commission",
        cle_b="Orange : la dette augmente ; gris : elle baisse ; contour pointillé : calcul comptable.",
        fam=("Solde primaire", "Conditions de financement", "Activité économique"),
        l_solde="Solde primaire supérieur d'un point de PIB chaque année, de 2028 à 2035",
        l_solde_n="Calcul comptable, hors effets sur la croissance et les taux",
        l_eub="Taux de marché plus bas de 0,2 point",
        l_t100="Taux de marché plus hauts de 1 point",
        l_gp="Croissance nominale plus forte de 0,5 point par an",
        l_gm="Croissance nominale plus faible de 0,5 point par an",
        b_note="Sensibilités : un seul paramètre modifié à la fois, les autres inchangés ; ni prévisions, ni "
               "évaluations complètes de politiques, ni classement coût-bénéfice.",
        b_source="Calculs de l'auteur à partir de la référence de la Commission européenne (Debt Sustainability Monitor "
                 "2025, fiche France), moteur testé contre la Commission et contre la sensibilité publiée par l'AFT.",
        points="points"),
    "en": dict(
        a_titre="Public debt in 2030: several futures, under which assumptions?",
        a_sous="French public debt, % of GDP",
        p90="90th percentile", p10="10th percentile", ref="Commission, unchanged policy", ref2="no new measures after 2026",
        plf="2027 draft budget forecast", psmt="October 2024 commitment", en_="in",
        ref35="Commission, unchanged policy (2035, off the chart)",
        au_dela="Beyond 2030, outside the fan: the Commission's unchanged-policy projection for 2035 is {v} of GDP, with "
                "no new measures after 2026.",
        bandes="Bands, from lightest to darkest: 10th to 90th, 20th to 80th and 40th to 60th percentiles of the paths "
               "simulated by the Commission (8, 6 and 2 in 10).",
        a_note="The bands are conditional projections based on historical economic shocks; they do not predict future "
               "decisions or their consequences. {bandes} The three paths rest on different assumptions and starting "
               "points. Starting points in 2025: Commission {a} (February 2026 release), 2027 draft budget {b} (October "
               "2026), 2024 commitment {c} (October 2024); the commitment gives no figure for 2026.",
        a_note_m="The bands are conditional projections based on historical shocks, not forecasts. {bandes} Starting "
                 "points in 2025: Commission {a}, 2027 draft budget {b}, 2024 commitment {c}; the commitment gives no "
                 "figure for 2026.",
        a_source_m="Sources: European Commission (DSM 2025); French government (October 2024 plan, 2027 draft budget).",
        a_source="Sources: European Commission, Debt Sustainability Monitor 2025 (France country fiche); French "
                 "government, medium-term fiscal-structural plan (October 2024) and debt report annexed to the 2027 "
                 "draft budget.",
        licence="Chart: Stéphane Lalut, CC BY 4.0 · stephane-lalut.com/en/public-debt-what-futures/",
        licence_m="Chart: Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
        b_titre="Public debt in 2035: how far the primary balance, interest rates and growth move it",
        b_sous="Effect on the debt-to-GDP ratio in 2035, in percentage points of GDP, relative to the Commission's baseline",
        cle_b="Orange: debt rises; grey: debt falls; dotted outline: accounting calculation.",
        fam=("Primary balance", "Financing conditions", "Economic activity"),
        l_solde="Primary balance 1 percentage point of GDP higher every year, from 2028 to 2035",
        l_solde_n="Accounting calculation, ignoring any effect on growth or interest rates",
        l_eub="Market rates 0.2 percentage point lower",
        l_t100="Market rates 1 percentage point higher",
        l_gp="Nominal growth 0.5 percentage point higher each year",
        l_gm="Nominal growth 0.5 percentage point lower each year",
        b_note="Sensitivities: one parameter changed at a time, the others unchanged. These are not forecasts, full policy assessments or a "
               "cost-benefit ranking.",
        b_source="Author's calculations based on the European Commission's baseline (Debt Sustainability Monitor 2025, "
                 "France country fiche), engine tested against the Commission and against the sensitivity published "
                 "by the French Treasury (AFT).",
        points="points"),
}


def ouvrir(ident: str, titre: str, desc: str, w: int = W) -> list[str]:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (w, ident, ident, esc(FONT)),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="0" fill="#ffffff"/>' % w]


def fermer_bureau(e: list[str], y0: float, blocs) -> str:
    s = pf.pied(e, y0, W, blocs, FILET)
    return s.replace('viewBox="0 0 %d 0"' % W, 'viewBox="0 0 %d 0"' % W)


def donnees(R: dict) -> dict:
    ref = R["ref"]
    base = {int(a): v for a, v in ref["base"].items()}
    dist = {c: {int(a): v for a, v in s.items()} for c, s in ref["stoch"].items()}
    plf = {int(a): v for a, v in R["gv"]["plf2027"]["dette"].items()}
    psmt = {int(a): v for a, v in R["gv"]["psmt"].items()}
    return dict(base=base, dist=dist, plf=plf, psmt=psmt, sens=R["sens"])


# ------------------------------------------------------------------ A2 : l'éventail
def desc_a(D: dict, lang: str) -> str:
    t, b, d, p, s = T[lang], D["base"], D["dist"], D["plf"], D["psmt"]
    if lang == "fr":
        return ("Éventail des trajectoires de dette simulées par la Commission européenne de 2025 à 2030 : en 2030, 10e "
                "centile %s, 90e centile %s ; référence de la Commission %s en 2030 et %s en 2035 ; prévision du PLF "
                "2027 : %s en 2030 ; engagement d'octobre 2024 : %s en 2029. %s Départs en 2025 : Commission %s, PLF "
                "2027 %s, engagement de 2024 %s." % (pct(d["p10"][2030], lang), pct(d["p90"][2030], lang),
                                                       pct(b[2030], lang), pct(b[2035], lang), pct(p[2030], lang),
                                                       pct(s[2029], lang), t["bandes"], pct(b[2025], lang),
                                                       pct(p[2025], lang), pct(s[2025], lang)))
    return ("Fan of debt paths simulated by the European Commission, 2025 to 2030: in 2030, 10th percentile %s, 90th "
            "percentile %s; Commission baseline %s in 2030 and %s in 2035; 2027 draft budget forecast: %s in 2030; "
            "October 2024 commitment: %s in 2029. %s Starting points in 2025: Commission %s, 2027 draft budget %s, 2024 "
            "commitment %s." % (pct(d["p10"][2030], lang), pct(d["p90"][2030], lang), pct(b[2030], lang),
                                pct(b[2035], lang), pct(p[2030], lang), pct(s[2029], lang), t["bandes"],
                                pct(b[2025], lang), pct(p[2025], lang), pct(s[2025], lang)))


def blocs_a(D, lang):
    t = T[lang]
    note = t["a_note"].format(a=pct(D["base"][2025], lang), b=pct(D["plf"][2025], lang), c=pct(D["psmt"][2025], lang),
                              bandes=t["bandes"])
    return [(t["a_source"], SEC, "pied-source"), (t["au_dela"].format(v=pct(D["base"][2035], lang)) + " " + note, SEC, "pied-note"),
            (t["licence"], SEC, "pied-licence")]


def eventail(D: dict, lang: str) -> str:
    t, b, d, p, s = T[lang], D["base"], D["dist"], D["plf"], D["psmt"]
    e = ouvrir("futurs-eventail", t["a_titre"], desc_a(D, lang))
    e.append(txt(0, 22, t["a_titre"], 17, weight=600))
    e.append(txt(0, 44, t["a_sous"], 13, fill=SEC))
    # x0 d\u00e9coll\u00e9 de l'axe (09/11/2026) : \u00e0 46, \u00ab 115 % \u00bb touchait les points de d\u00e9part 2025 et se lisait comme leur \u00e9tiquette.
    x0, x1, y0, y1, v0, v1 = 58, 450, 380, 76, 113, 138
    X = lambda a: x0 + (a - 2025) / 5 * (x1 - x0)
    Y = lambda v: y0 - (v - v0) / (v1 - v0) * (y0 - y1)
    for v in range(115, 139, 5):
        e.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="%s"/>' % (x0 - 4, x1, Y(v), Y(v), GRILLE))
        e.append(txt(x0 - 12, Y(v) + 4, "%d" % v + ("\u00a0%" if lang == "fr" else "%"), 12, "end", fill=SEC))
    for a in range(2025, 2031):
        e.append(txt(X(a), y0 + 20, str(a), 12, "middle", fill=SEC))
    ans = list(range(2025, 2031))
    for bas, haut, op in (("p10", "p90", 0.13), ("p20", "p80", 0.18), ("p40", "p60", 0.28)):
        pts = ["%.1f,%.1f" % (X(a), Y(d[haut][a])) for a in ans] + ["%.1f,%.1f" % (X(a), Y(d[bas][a])) for a in reversed(ans)]
        e.append('<polygon points="%s" fill="%s" fill-opacity="%.2f" stroke="none"/>' % (" ".join(pts), BLEU, op))
    e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="6 4"/>' % (
        " ".join("%.1f,%.1f" % (X(a), Y(b[a])) for a in ans), BLEU))
    # Prévision du Gouvernement en tirets (charte : une prévision se dessine en pointillés ; contrôleur, 09/11/2026).
    e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="10 4"/>' % (
        " ".join("%.1f,%.1f" % (X(a), Y(p[a])) for a in ans), ORANGE))
    for a in ans:
        e.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (X(a), Y(p[a]), ORANGE))
    ps = [a for a in sorted(s) if a >= 2025]
    e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="2 4"/>' % (
        " ".join("%.1f,%.1f" % (X(a), Y(s[a])) for a in ps), ORANGE_A))
    for a in ps:
        e.append('<circle cx="%.1f" cy="%.1f" r="3" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % (X(a), Y(s[a]), ORANGE_A))
    # Engagement de 2024 : nom puis valeur, centrés sous le point de 2029 qu'ils désignent.
    e.append(txt(X(2029), Y(s[2029]) + 20, t["psmt"], 12, "middle", fill=ORANGE_A))
    e.append(txt(X(2029), Y(s[2029]) + 34, "%s %s 2029" % (pct(s[2029], lang), t["en_"]), 12, "middle", fill=ORANGE_A))
    xr = X(2030) + 10
    e.append(txt(xr, Y(d["p90"][2030]) + 4, "%s — %s" % (t["p90"], pct(d["p90"][2030], lang)), 12, fill=SEC))
    e.append(txt(xr, Y(b[2030]) + 4, t["ref"], 12, weight=600, fill=BLEU))
    e.append(txt(xr, Y(b[2030]) + 20, "%s %s 2030" % (pct(b[2030], lang), t["en_"]), 12, weight=600, fill=BLEU))
    e.append(txt(xr, Y(b[2030]) + 36, t["ref2"], 12, fill=BLEU))
    e.append(txt(xr, Y(p[2030]) - 6, t["plf"], 12, weight=600, fill=ORANGE))
    e.append(txt(xr, Y(p[2030]) + 10, "%s %s 2030" % (pct(p[2030], lang), t["en_"]), 12, weight=600, fill=ORANGE))
    e.append(txt(xr, Y(d["p10"][2030]) + 4, "%s — %s" % (t["p10"], pct(d["p10"][2030], lang)), 12, fill=SEC))
    return pf.pied(e, y0 + 40, W, blocs_a(D, lang), FILET)


def eventail_m(D: dict, lang: str) -> str:
    t, b, d, p, s = T[lang], D["base"], D["dist"], D["plf"], D["psmt"]
    e, y = pf.tete_mobile("futurs-eventail-m", t["a_titre"], desc_a(D, lang), ENCRE, FONT)
    e.append(txt(0, y + 4, t["a_sous"], 13.5, fill=SEC))
    y += 14
    x0, x1, v0, v1 = 48, 292, 113, 138   # 42 et libellés à x0 - 10 : « 115 » décollé des points de départ
    y1 = y + 16
    y0 = y1 + 230
    X = lambda a: x0 + (a - 2025) / 5 * (x1 - x0)
    Y = lambda v: y0 - (v - v0) / (v1 - v0) * (y0 - y1)
    for v in range(115, 139, 5):
        e.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="%s"/>' % (x0, x1, Y(v), Y(v), GRILLE))
        e.append(txt(x0 - 15, Y(v) + 5, "%d" % v, 13.5, "end", fill=SEC))
    # Toutes les années graduées (09/11/2026) : la page parle d'une prévision qui monte jusqu'en 2028 et d'un
    # engagement qui s'arrête en 2029 ; sans graduation ni marque, rien de cela ne se repérait sur téléphone.
    for a in range(2025, 2031):
        e.append('<line x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f" stroke="%s"/>' % (X(a), X(a), y0, y0 + 5, SEC))
    for a in (2025, 2028, 2030):
        e.append(txt(X(a), y0 + 20, str(a), 13.5, {2025: "start", 2028: "middle", 2030: "end"}[a], fill=SEC))
    ans = list(range(2025, 2031))
    for bas, haut, op in (("p10", "p90", 0.13), ("p20", "p80", 0.18), ("p40", "p60", 0.28)):
        pts = ["%.1f,%.1f" % (X(a), Y(d[haut][a])) for a in ans] + ["%.1f,%.1f" % (X(a), Y(d[bas][a])) for a in reversed(ans)]
        e.append('<polygon points="%s" fill="%s" fill-opacity="%.2f" stroke="none"/>' % (" ".join(pts), BLEU, op))
    e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="6 4"/>' % (
        " ".join("%.1f,%.1f" % (X(a), Y(b[a])) for a in ans), BLEU))
    e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="10 4"/>' % (
        " ".join("%.1f,%.1f" % (X(a), Y(p[a])) for a in ans), ORANGE))
    for a in ans:
        e.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (X(a), Y(p[a]), ORANGE))
    ps = [a for a in sorted(s) if a >= 2025]
    e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="2 4"/>' % (
        " ".join("%.1f,%.1f" % (X(a), Y(s[a])) for a in ps), ORANGE_A))
    for a in ps:
        e.append('<circle cx="%.1f" cy="%.1f" r="2.5" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % (X(a), Y(s[a]), ORANGE_A))
    y = y0 + 48
    # Échantillon du trait devant chaque libellé (contrôleur, 09/11/2026) : la couleur du texte seule reliait mal le
    # pointillé de l'engagement et les tirets de la prévision, deux orangés voisins sur un petit écran.
    traits = {"ref": (BLEU, "6 4", 2.5), "plf": (ORANGE, "10 4", 2.5), "psmt": (ORANGE_A, "2 4", 1.5)}
    for lib, val, coul, gras, tr in ((t["p90"] + " (2030)", pct(d["p90"][2030], lang), SEC, 400, None),
                                     (t["ref"] + " (2030), " + t["ref2"], pct(b[2030], lang), BLEU, 600, "ref"),
                                     (t["plf"] + " (2030)", pct(p[2030], lang), ORANGE, 600, "plf"),
                                     (t["p10"] + " (2030)", pct(d["p10"][2030], lang), SEC, 400, None),
                                     (t["psmt"] + " (2029)", pct(s[2029], lang), ORANGE_A, 400, "psmt"),
                                     (t["ref35"], pct(b[2035], lang), BLEU, 400, "aucun")):
        xt = 30 if tr else 0
        if tr and tr in traits:
            c, da, w_ = traits[tr]
            e.append('<line x1="0" x2="22" y1="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-dasharray="%s"/>'
                     % (y - 5, y - 5, c, w_, da))
        lignes = pf.coupe(lib, 26 if tr else 28)
        for k, l in enumerate(lignes):
            e.append(txt(xt, y + 18 * k, l, 13.5, fill=coul, weight=gras))
        e.append(txt(300, y, val, 13.5, "end", 600, coul))
        y += 18 * len(lignes) + 8
    blocs = [(T[lang]["a_source_m"], SEC, "pied-source"),
             (T[lang]["a_note_m"].format(a=pct(b[2025], lang), b=pct(p[2025], lang), c=pct(s[2025], lang),
                                         bandes=T[lang]["bandes"]), SEC, "pied-note"),
             (T[lang]["licence_m"], SEC, "pied-licence")]
    return pf.pied_mobile(e, y + 4, blocs, FILET)


# ------------------------------------------------------------------ B2 : les leviers
def leviers_donnees(D: dict, lang: str):
    t, s = T[lang], D["sens"]
    return [(t["fam"][0], [(t["l_solde"], s["solde_plus_1_comptable"]["dette_2035"], True)]),
            (t["fam"][1], [(t["l_eub"], s["taux_moins_20pb"]["dette_2035"], False), (t["l_t100"], s["taux_plus_100pb"]["dette_2035"], False)]),
            (t["fam"][2], [(t["l_gp"], s["croissance_plus_05"]["dette_2035"], False), (t["l_gm"], s["croissance_moins_05"]["dette_2035"], False)])]


def desc_b(D: dict, lang: str) -> str:
    parts = []
    for fam, items in leviers_donnees(D, lang):
        for lib, v, _ in items:
            lib = lib if not parts else lib[0].lower() + lib[1:]
            parts.append("%s : %s" % (lib, nbs(v, lang)) if lang == "fr" else "%s: %s" % (lib, nbs(v, lang)))
    t = T[lang]
    return "%s. %s %s." % (t["b_sous"], t["cle_b"], (" ; " if lang == "fr" else "; ").join(parts))


def nbs(v: float, lang: str) -> str:
    """Valeur signée (« +5,5 », « −8,2 ») : l'axe est gradué en « +5 » et « −5 »."""
    return ("+" if v > 0 else "") + nb(v, lang)


def blocs_b(lang, mobile=False):
    t = T[lang]
    return [(t["b_source"], SEC, "pied-source"), (t["b_note"], SEC, "pied-note"),
            (t["licence_m" if mobile else "licence"], SEC, "pied-licence")]


def leviers(D: dict, lang: str) -> str:
    t = T[lang]
    e = ouvrir("futurs-leviers", t["b_titre"], desc_b(D, lang))
    e.append(txt(0, 22, t["b_titre"], 17, weight=600))
    y = 44
    for l in pf.coupe(t["b_sous"], 108) + pf.coupe(t["cle_b"], 108):
        e.append(txt(0, y, l, 13, fill=SEC))
        y += 18
    ytop = y - 4
    xm, xa = 400, 700
    X = lambda v: xm + (v + 10) / 20 * (xa - xm)
    y += 2
    i_grille = len(e)
    for fam, items in leviers_donnees(D, lang):
        e.append(txt(0, y + 12, fam, 13, weight=600))
        y += 22
        for lib, v, comptable in items:
            lignes = pf.coupe(lib, 62)
            for k, l in enumerate(lignes):
                e.append(txt(0, y + 12 + 15 * k, l, 12))
            xa_, xb = sorted((X(0), X(v)))
            if comptable:
                e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="18" fill="#ffffff" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"/>' % (xa_, y + 2, xb - xa_, GRIS))
                for k, l in enumerate(pf.coupe(t["l_solde_n"], 62)):
                    e.append(txt(0, y + 12 + 15 * (len(lignes) + k), l, 12, fill=SEC))
                lignes = lignes + pf.coupe(t["l_solde_n"], 62)
            else:
                e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="18" fill="%s"/>' % (xa_, y + 2, xb - xa_, GRIS if v < 0 else ORANGE))
            if v > 0:
                e.append(txt(X(v) + 6, y + 16, nbs(v, lang), 13, "start", 600, ORANGE))
            elif comptable:
                e.append(txt(X(v) + 6, y + 16, nbs(v, lang), 13, "start", 600, ENCRE))
            else:
                e.append(txt(X(v) - 6, y + 16, nbs(v, lang), 13, "end", 600, ENCRE))
            y += max(34, 15 * len(lignes) + 12)
        y += 8
    grille = ['<line x1="%.1f" x2="%.1f" y1="%d" y2="%d" stroke="%s"/>' % (X(v), X(v), ytop, y, "#9a9994" if v == 0 else GRILLE)
              for v in (-10, -5, 0, 5, 10)]
    e[i_grille:i_grille] = grille
    for v in (-10, -5, 0, 5, 10):
        e.append(txt(X(v), y + 18, ("%+d" % v).replace("-", "−") if v else "0", 12, "middle", fill=SEC))
    return pf.pied(e, y + 34, W, blocs_b(lang), FILET)


def leviers_m(D: dict, lang: str) -> str:
    t = T[lang]
    e, y = pf.tete_mobile("futurs-leviers-m", t["b_titre"], desc_b(D, lang), ENCRE, FONT)
    for l in pf.coupe(t["b_sous"], 38):
        e.append(txt(0, y + 4, l, 13.5, fill=SEC))
        y += 18
    y += 6
    for l in pf.coupe(t["cle_b"], 38):
        e.append(txt(0, y + 4, l, 13.5, fill=SEC))
        y += 18
    # Échelle élargie et valeur au bout de sa barre (09/11/2026) : collées au bord droit, les valeurs négatives
    # tombaient de l'autre côté du zéro, loin de leur marque.
    X = lambda v: 44 + (v + 10) / 20 * 232
    y += 8
    for fam, items in leviers_donnees(D, lang):
        e.append(txt(0, y + 14, fam, 15, weight=600))
        y += 26
        for lib, v, comptable in items:
            for l in pf.coupe(lib, 36):
                e.append(txt(0, y + 13, l, 13.5))
                y += 18
            if comptable:
                for l in pf.coupe(t["l_solde_n"], 36):
                    e.append(txt(0, y + 13, l, 13.5, fill=SEC))
                    y += 18
            xa_, xb = sorted((X(0), X(v)))
            e.append('<line x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f" stroke="#9a9994"/>' % (X(0), X(0), y + 2, y + 24))
            if comptable:
                e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="16" fill="#ffffff" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"/>' % (xa_, y + 5, xb - xa_, GRIS))
            else:
                e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="16" fill="%s"/>' % (xa_, y + 5, xb - xa_, GRIS if v < 0 else ORANGE))
            if v > 0:
                e.append(txt(X(v) + 5, y + 18, nbs(v, lang), 13.5, "start", 600, ORANGE))
            else:
                e.append(txt(X(v) - 5, y + 18, nbs(v, lang), 13.5, "end", 600, ENCRE))
            y += 34
        y += 6
    e.append(txt(X(0), y + 8, "0", 13.5, "middle", fill=SEC))
    y += 14
    return pf.pied_mobile(e, y + 4, blocs_b(lang, mobile=True), FILET)


def produire(R: dict) -> dict:
    """Rend {nom de fichier: SVG} : 2 figures x (bureau, téléphone) x (fr, en)."""
    D = donnees(R)
    out = {}
    for lang, suf in (("fr", ""), ("en", "-en")):
        out["dette-futurs-eventail%s.svg" % suf] = eventail(D, lang)
        out["dette-futurs-eventail%s-m.svg" % suf] = eventail_m(D, lang)
        out["dette-futurs-leviers%s.svg" % suf] = leviers(D, lang)
        out["dette-futurs-leviers%s-m.svg" % suf] = leviers_m(D, lang)
    return out
