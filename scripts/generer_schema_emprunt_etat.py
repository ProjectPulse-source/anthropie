# -*- coding: utf-8 -*-
"""generer_schema_emprunt_etat.py -- schéma « Comment l'État emprunte » (FR, EN ; bureau 720, téléphone 300).

Demande de l'auteur (09/11/2026) : « une explication extrêmement claire du mécanisme d'emprunt de l'État, avec
graphisme ». Pièce pédagogique de la section « Annuler la dette détenue par la Banque de France » de
/qui-paie-la-dette-publique/ (fiche docs/conception/annuler-dette-banque-de-france.md). Schéma, non figure de données :
aucun chiffre, sauf les années des achats nets de la Banque de France (2015-2022), déjà publiées par le site
(/inflation-et-dette-publique/#achats-banque-centrale).

Deux volets : (1) le chemin d'un titre, de l'Agence France Trésor à la Banque de France, qui n'achète que sur le
marché et paie en réserves ; (2) ce que l'État paie chaque année, et à qui : coupons aux détenteurs, Banque de France
comprise ; intérêts des réserves payés par la Banque de France aux banques ; bénéfices de la Banque de France reversés
à l'État. Couleurs du site : bleu = le titre (le stock), orange = les intérêts (le coût), gris = ce qui revient.

Usage : python scripts/generer_schema_emprunt_etat.py [--png]
Sorties : static/img/schema-emprunt-etat{,-en}{,-m}.svg (+ .png avec --png).
"""
from __future__ import annotations

import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pied_figure as PF  # noqa: E402

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLEU, ORANGE = "#184f95", "#eb6834"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FOND = "#f6f5f1"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
W, WM = 720, PF.LARGEUR_M

T = {
    "fr": dict(
        titre="Comment l'État emprunte, et qui reçoit les intérêts",
        desc=("Schéma en deux volets. Premier volet, le chemin d'un titre : l'Agence France Trésor vend les titres de "
              "l'État aux enchères à des banques agréées, les spécialistes en valeurs du Trésor ; elles les revendent aux "
              "investisseurs, en France et à l'étranger ; de 2015 à 2022 (achats nets), la Banque de France en a acheté sur ce marché, "
              "jamais directement à l'État, en payant avec des réserves créditées aux banques. Second volet, ce que l'État "
              "paie chaque année : les coupons, à chaque détenteur, Banque de France comprise ; la Banque de France paie "
              "de son côté les réserves placées par les banques, au taux de dépôt de la BCE, et reverse ses bénéfices à "
              "l'État selon ses résultats. À l'échéance, l'État rembourse chaque titre avec sa trésorerie ou un nouvel emprunt."),
        v1="1. Le chemin d'un titre", v2="2. Les intérêts payés chaque année, et à qui",
        v2_m="2. Les intérêts payés, et à qui",
        etat=("L'État", "Agence France Trésor"),
        svt=("Spécialistes en valeurs du Trésor", "banques agréées"),
        inv=("Investisseurs", "assureurs, banques, fonds, en France et à l'étranger"),
        bdf=("Banque de France", "pour l'Eurosystème"),
        banques=("Banques", "qui détiennent les réserves"),
        l1=[("1", "L'Agence France Trésor vend les titres de l'État, pour l'essentiel aux enchères (adjudication). Seuls les spécialistes en "
                  "valeurs du Trésor y achètent : l'État reçoit leur argent, c'est l'emprunt."),
            ("2", "Ils les gardent ou les revendent aux investisseurs, sur le marché « secondaire »."),
            ("3", "De 2015 à 2022 (achats nets), la Banque de France en a acheté sur ce marché pour l'Eurosystème (les "
                  "banques centrales de la zone euro), puis a remplacé les titres échus jusqu'en juillet 2023 ou fin 2024 "
                  "selon le programme ; jamais à l'État lui-même : le traité européen l'interdit (article 123)."),
            ("4", "Elle les a payés en monnaie de banque centrale, créée pour l'achat : des réserves créditées à la banque "
                  "du vendeur.")],
        l2=[("5", "Chaque année, l'État paie les intérêts de ses titres à chaque détenteur, Banque de France comprise. "
                  "À l'échéance, il rembourse le titre avec sa trésorerie ou un nouvel emprunt : retour en 1."),
            ("6", "La Banque de France rémunère au taux de dépôt de la BCE les réserves placées à sa facilité de dépôt "
                  "(les réserves obligatoires ne sont plus rémunérées depuis septembre 2023)."),
            ("7", "Selon ses résultats, elle reverse à l'État un impôt et un dividende. Quand les réserves lui coûtent plus "
                  "que ses titres ne rapportent, ses résultats baissent : elle n'a versé aucun dividende au titre des "
                  "exercices 2022 à 2025.")],
        source="Schéma de l'auteur ; Agence France Trésor, Banque de France (comptes annuels), BCE, traité sur le fonctionnement de l'UE (art. 123).",
        note="Schéma simplifié : l'État n'est qu'une partie des administrations publiques, et la Banque de France n'en fait pas partie.",
        licence="Stéphane Lalut, CC BY 4.0 · stephane-lalut.com/qui-paie-la-dette-publique/",
        licence_m="Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
    ),
    "en": dict(
        titre="How the French State borrows, and who receives the interest",
        desc=("Two-part diagram. Part one, the path of a bond: the French Treasury agency (Agence France Trésor) sells "
              "government bonds at auction to licensed banks, the primary dealers; they resell them to investors in "
              "France and abroad; from 2015 to 2022 (net purchases), the Banque de France bought some of them on that market, never "
              "directly from the State, paying with reserves credited to banks. Part two, what the State pays each year: "
              "coupons to every holder, the Banque de France included; the Banque de France in turn pays interest on "
              "the reserves banks place with it, at the ECB deposit rate, and passes its profits on to the State. At maturity, the State "
              "repays each bond from its cash or new borrowing."),
        v1="1. The path of a bond", v2="2. Interest paid each year, and to whom",
        v2_m="2. Interest paid, and to whom",
        etat=("The State", "Agence France Trésor"),
        svt=("Primary dealers", "licensed banks"),
        inv=("Investors", "insurers, banks, funds, in France and abroad"),
        bdf=("Banque de France", "for the Eurosystem"),
        banques=("Banks", "holding the reserves"),
        l1=[("1", "The Agence France Trésor sells government bonds, mostly at auction. Only primary dealers can buy there: the "
                  "State receives their money; that is the borrowing."),
            ("2", "They keep them or resell them to investors on the secondary market."),
            ("3", "From 2015 to 2022 (net purchases), the Banque de France bought some on that market for the Eurosystem "
                  "(the euro area central banks), then replaced maturing bonds until July 2023 or end-2024 depending on "
                  "the programme; never from the State itself: the EU Treaty forbids it (Article 123)."),
            ("4", "It paid in central bank money created for the purchase: reserves credited to the seller's bank.")],
        l2=[("5", "Each year, the State pays interest on its bonds to every holder, the Banque de France included. At "
                  "maturity, it repays the bond from its cash or new borrowing: back to 1."),
            ("6", "The Banque de France pays the ECB deposit rate on reserves placed in its deposit facility (minimum "
                  "reserves have not been remunerated since September 2023)."),
            ("7", "Depending on its results, it pays the State tax and a dividend. When reserves cost it more than its "
                  "bonds earn, its results fall: it paid no dividend for the 2022 to 2025 financial years.")],
        source="Author's diagram; Agence France Trésor, Banque de France (annual accounts), ECB, Treaty on the Functioning of the EU (Art. 123).",
        note="Simplified: the State is only part of general government, and the Banque de France is not part of it.",
        licence="Stéphane Lalut, CC BY 4.0 · stephane-lalut.com/en/who-pays-public-debt/",
        licence_m="Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
    ),
}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def defs() -> str:
    m = ""
    for nom, col in (("b", BLEU), ("o", ORANGE), ("g", MUTED)):
        m += ('<marker id="f%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
              '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>' % (nom, col))
    return "<defs>%s</defs>" % m


def boite(e, x, y, w, h, nom, sous, car, fs=12, accent=INK):
    e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="6" fill="%s" stroke="%s"/>' % (x, y, w, h, FOND, GRID))
    lignes = [(l, True) for l in PF.coupe(nom, car)] + [(l, False) for l in PF.coupe(sous, car + 2)]
    y0 = y + h / 2 - (len(lignes) - 1) * (fs + 3) / 2 + fs * 0.35
    for k, (l, gras) in enumerate(lignes):
        e.append('<text x="%.1f" y="%.1f" font-size="%s" text-anchor="middle" fill="%s"%s>%s</text>'
                 % (x + w / 2, y0 + k * (fs + 3), fs if gras else fs - 1, accent if gras else INK2,
                    ' font-weight="600"' if gras else "", esc(l)))


def fleche(e, pts, col, nom):
    d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % p for k, p in enumerate(pts))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2" marker-end="url(#f%s)"/>' % (d, col, nom))


def pastille(e, x, y, n, col, r=9):
    e.append('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (x, y, r, col))
    e.append('<text x="%.1f" y="%.1f" font-size="%d" font-weight="600" text-anchor="middle" fill="#fff">%s</text>'
             % (x, y + 4, r + 2, n))


def legende(e, y, items, cols, car, x0=0, fs=12, pas=16, r=8):
    for n, texte in items:
        pastille(e, x0 + r, y + 6, n, cols[n], r)
        for k, l in enumerate(PF.coupe(texte, car)):
            e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s">%s</text>' % (x0 + 2 * r + 8, y + 10 + k * pas, fs, INK, esc(l)))
        y += pas * len(PF.coupe(texte, car)) + 6
    return y


COULEURS = {"1": BLEU, "2": BLEU, "3": BLEU, "4": MUTED, "5": ORANGE, "6": ORANGE, "7": MUTED}


def bureau(lang: str) -> str:
    L = T[lang]
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" aria-labelledby="se-t se-d" '
         'font-family="%s">' % (W, FONT),
         '<title id="se-t">%s</title><desc id="se-d">%s</desc>' % (esc(L["titre"]), esc(L["desc"])),
         '<rect width="%d" height="0" fill="#ffffff"/>' % W, defs(),
         '<text x="0" y="18" font-size="13" font-weight="600" fill="%s">%s</text>' % (INK, esc(L["titre"]))]
    # Volet 1 : quatre boîtes en ligne.
    e.append('<text x="0" y="50" font-size="12" font-weight="600" fill="%s">%s</text>' % (BLEU, esc(L["v1"])))
    bw, bh, by, gap = 150, 84, 64, 40
    xs = [0, bw + gap, 2 * (bw + gap), 3 * (bw + gap)]
    for x, (nom, sous) in zip(xs, (L["etat"], L["svt"], L["inv"], L["bdf"])):
        boite(e, x, by, bw, bh, nom, sous, 22)
    for k in range(3):
        x1, x2 = xs[k] + bw + 3, xs[k + 1] - 3
        fleche(e, [(x1, by + 30), (x2, by + 30)], BLEU, "b")
        pastille(e, (x1 + x2) / 2, by + 13, str(k + 1), BLEU)
    x1, x2 = xs[3] - 3, xs[2] + bw + 3
    fleche(e, [(x1, by + 62), (x2, by + 62)], MUTED, "g")
    pastille(e, (x1 + x2) / 2, by + 79, "4", MUTED)
    y = legende(e, by + bh + 22, L["l1"], COULEURS, 100)
    # Volet 2 : l'État à gauche ; investisseurs et Banque de France au centre ; banques à droite.
    y += 18
    e.append('<text x="0" y="%.1f" font-size="12" font-weight="600" fill="%s">%s</text>' % (y, ORANGE, esc(L["v2"])))
    y0 = y + 16
    bw2, bh2 = 170, 62
    xe, xc, xd = 0, 275, 550
    ye, yi, yb = y0 + 52, y0, y0 + 104
    boite(e, xe, ye, bw2, bh2, *L["etat"], car=24)
    boite(e, xc, yi, bw2, bh2, *L["inv"], car=24)
    boite(e, xc, yb, bw2, bh2, *L["bdf"], car=24)
    boite(e, xd, yb, bw2, bh2, *L["banques"], car=24)
    # 5 : coupons de l'État vers les deux détenteurs.
    fleche(e, [(xe + bw2 + 3, ye + 18), (xc - 3, yi + bh2 / 2)], ORANGE, "o")
    fleche(e, [(xe + bw2 + 3, ye + bh2 - 18), (xc - 3, yb + 20)], ORANGE, "o")
    pastille(e, (xe + bw2 + xc) / 2, ye + bh2 / 2, "5", ORANGE)
    # 6 : intérêts des réserves, de la Banque de France aux banques.
    fleche(e, [(xc + bw2 + 3, yb + 20), (xd - 3, yb + 20)], ORANGE, "o")
    pastille(e, (xc + bw2 + xd) / 2, yb + 8, "6", ORANGE)
    # 7 : bénéfices reversés à l'État, sous les boîtes.
    fleche(e, [(xc + 30, yb + bh2 + 3), (xc + 30, yb + bh2 + 22), (xe + bw2 / 2, yb + bh2 + 22), (xe + bw2 / 2, ye + bh2 + 3)],
           MUTED, "g")
    pastille(e, (xc + 30 + xe + bw2 / 2) / 2, yb + bh2 + 22, "7", MUTED)
    y = legende(e, yb + bh2 + 50, L["l2"], COULEURS, 100)
    blocs = [(L["source"], INK2, "pied-source"), (L["note"], INK2, "pied-note"), (L["licence"], MUTED, "pied-licence")]
    return PF.pied(e, y + 10, W, blocs, GRID)


def telephone(lang: str) -> str:
    L = T[lang]
    e, y = PF.tete_mobile("sem", L["titre"], L["desc"], INK, FONT, car=28)
    e.insert(3, defs())
    fs = PF.POLICE_M

    def colonne(y, boites, fleches, couleur_titre, titre):
        e.append('<text x="0" y="%.1f" font-size="%s" font-weight="600" fill="%s">%s</text>' % (y + 18, fs, couleur_titre, esc(titre)))
        y += 30
        bw, bh, gap = 230, 58, 34
        x = (WM - bw) / 2
        ys = []
        for k, (nom, sous) in enumerate(boites):
            boite(e, x, y, bw, bh, nom, sous, 26, fs=13)
            ys.append(y)
            y += bh + gap
        for (a, b, n, col, nm) in fleches:
            if b == a + 1:
                fleche(e, [(x + bw / 2, ys[a] + bh + 3), (x + bw / 2, ys[b] - 3)], col, nm)
                pastille(e, x + bw / 2 + 22, (ys[a] + bh + ys[b]) / 2, n, col)
            elif b > a:
                # Flèche qui saute une boîte (coupons de l'État à la Banque de France) : par la gauche.
                fleche(e, [(x - 3, ys[a] + bh / 2), (x - 22, ys[a] + bh / 2), (x - 22, ys[b] + bh / 2),
                           (x - 3, ys[b] + bh / 2)], col, nm)
                pastille(e, x - 22, (ys[a] + ys[b]) / 2 + bh / 2, n, col)
            else:
                fleche(e, [(x + bw + 3, ys[a] + bh / 2), (x + bw + 22, ys[a] + bh / 2), (x + bw + 22, ys[b] + bh / 2),
                           (x + bw + 3, ys[b] + bh / 2)], col, nm)
                pastille(e, x + bw + 22, (ys[a] + ys[b]) / 2 + bh / 2, n, col)
        return y - gap + 18

    y = colonne(y, [L["etat"], L["svt"], L["inv"], L["bdf"]],
                [(0, 1, "1", BLEU, "b"), (1, 2, "2", BLEU, "b"), (2, 3, "3", BLEU, "b"), (3, 2, "4", MUTED, "g")],
                BLEU, L["v1"])
    y = legende(e, y, L["l1"], COULEURS, 30, fs=fs, pas=17, r=9) + 10
    y = colonne(y, [L["etat"], L["inv"], L["bdf"], L["banques"]],
                [(0, 1, "5", ORANGE, "o"), (0, 2, "5", ORANGE, "o"), (2, 3, "6", ORANGE, "o"), (2, 0, "7", MUTED, "g")],
                ORANGE, L["v2_m"])
    y = legende(e, y, L["l2"], COULEURS, 30, fs=fs, pas=17, r=9)
    blocs = [(L["source"], INK2, "pied-source"), (L["note"], INK2, "pied-note"), (L["licence_m"], MUTED, "pied-licence")]
    return PF.pied_mobile(e, y + 10, blocs, GRID)


def main() -> int:
    png = "--png" in sys.argv
    sorties = {}
    for lang in ("fr", "en"):
        suf = "" if lang == "fr" else "-en"
        sorties["schema-emprunt-etat%s.svg" % suf] = bureau(lang)
        sorties["schema-emprunt-etat%s-m.svg" % suf] = telephone(lang)
    for nom, svg in sorties.items():
        chemin = os.path.join(RACINE, "static", "img", nom)
        with open(chemin, "w", encoding="utf-8", newline="\n") as f:
            f.write(svg)
        if png:
            import cairosvg
            largeur = 900 if nom.endswith("-m.svg") else 1440
            cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=chemin[:-4] + ".png", output_width=largeur,
                             background_color="#ffffff")
    print("Ecrit : %d schemas SVG%s" % (len(sorties), " + PNG" if png else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
