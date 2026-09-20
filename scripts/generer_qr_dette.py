#!/usr/bin/env python3
"""Genere le QR code du livre « Dette Publique : Qui paie vraiment ? ».

DESTINATION : la page du compteur, qui se met a jour toute seule. C'est ce qui
fait l'interet du renvoi -- le livre est imprime une fois, la page vit.

⛔ CE QR N'A PAS SA PLACE DANS LE CONTENU A+ D'AMAZON. Les guidelines KDP sont
explicites : « Do not include any shipping details, QR barcodes, or personal
information [...] on the A+ page », et « Web links or language attempting to
redirect to other sites inside or outside of Amazon [...] are prohibited ». Il
est destine au LIVRE lui-meme -- 4e de couverture, page de fin, interieur --
ou il fait partie du produit, pas du materiel promotionnel de la fiche.

PARAMETRE DE MESURE. L'URL nue et l'URL suivie mènent a la meme page ; seule la
seconde permet de savoir d'ou viennent les lecteurs. Le QR de l'EPUB porte deja
`?src=compteur-qr` : un parametre DISTINCT par support est ce qui rend la
mesure lisible, sinon les deux sources se confondent et le chiffre ne dit plus
rien.

CORRECTION D'ERREUR : niveau Q (~25 % de redondance). Un QR imprime vit sur du
papier qui se plie, se tache et vieillit ; le niveau L, suffisant a l'ecran,
ne l'est pas sur un livre qu'on transporte. Le surcout est une trame un peu
plus dense, pas une perte de lisibilite.

SORTIE : SVG vectoriel (pour l'impression, aucune perte a l'agrandissement) et
PNG a 300 dpi pour les maquettes. Dossier : reports/qr-dette/ (gitignore).

Usage :
  python scripts/generer_qr_dette.py
  python scripts/generer_qr_dette.py --url "https://exemple.fr/page/"
"""
from __future__ import annotations

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

import segno

RACINE = Path(__file__).resolve().parent.parent
DEST = RACINE / "reports" / "qr-dette"

URL_NUE = "https://stephane-lalut.com/cout-de-la-dette-publique/"
URL_MESUREE = URL_NUE + "?src=livre-broche"

# Encre du site : le bleu d'accent, jamais un noir pur — la couverture est deja
# dans cette gamme, et un QR se lit parfaitement des que le contraste depasse
# largement le minimum normatif.
ENCRE = "#1B2A4E"


def produire(url: str, nom: str, encre: str = ENCRE, scale: int = 12,
             cote_cm: float = 2.5) -> None:
    qr = segno.make(url, error="q")
    svg = DEST / (nom + ".svg")
    png = DEST / (nom + ".png")
    # scale=10 + border=4 : la « quiet zone » de 4 modules est normative, un QR
    # colle au bord d'une page devient illisible sans elle.
    qr.save(str(svg), scale=10, border=4, dark=encre, light="#FFFFFF")
    qr.save(str(png), scale=scale, border=4, dark=encre, light="#FFFFFF")
    modules = qr.symbol_size(scale=1, border=4)[0]
    print("  %-22s version %-3s  %d modules  encre %s  %s"
          % (nom, qr.version, modules, encre, url))
    print("     %s + %s (PNG : %d px de cote)"
          % (svg.name, png.name, modules * scale))
    print("     a %.1f cm de cote, un module fait %.2f mm "
          "(0,4 mm est le minimum pratique pour un lecteur de telephone)"
          % (cote_cm, cote_cm * 10 / modules))
    print("     et le PNG y sort a %d dpi (300 est le minimum KDP pour un interieur)"
          % round(modules * scale / (cote_cm / 2.54)))


def main() -> int:
    args = sys.argv[1:]
    DEST.mkdir(parents=True, exist_ok=True)

    def option(nom_court: str, defaut):
        return args[args.index(nom_court) + 1] if nom_court in args else defaut

    # ⛔ Une ENCRE DE COULEUR n'a rien a faire dans un interieur imprime en noir
    # et blanc : KDP convertit en niveaux de gris, le bleu tombe vers un gris
    # moyen et le contraste du QR s'effondre la ou personne ne le verifiera.
    # Pour le LIVRE : --encre "#000000". Pour le SITE : le defaut.
    encre = option("--encre", ENCRE)
    scale = int(option("--scale", 12))
    cote = float(option("--cote-cm", 2.5))

    if "--url" in args:
        produire(option("--url", URL_NUE), option("--nom", "qr-personnalise"),
                 encre, scale, cote)
        return 0
    print("QR du livre Dette Publique -> page du compteur\n")
    produire(URL_MESUREE, "qr-dette-broche", encre, scale, cote)  # recommande : mesurable
    produire(URL_NUE, "qr-dette-url-nue", encre, scale, cote)     # si le parametre n'est pas voulu
    print("\nDossier : %s" % DEST)
    print("RAPPEL : ce QR va dans le LIVRE, jamais dans le contenu A+ Amazon.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
