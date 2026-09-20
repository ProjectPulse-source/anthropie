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


def produire(url: str, nom: str) -> None:
    qr = segno.make(url, error="q")
    svg = DEST / (nom + ".svg")
    png = DEST / (nom + ".png")
    # scale=10 + border=4 : la « quiet zone » de 4 modules est normative, un QR
    # colle au bord d'une page devient illisible sans elle.
    qr.save(str(svg), scale=10, border=4, dark=ENCRE, light="#FFFFFF")
    qr.save(str(png), scale=12, border=4, dark=ENCRE, light="#FFFFFF")
    cote_cm = 2.5
    modules = qr.symbol_size(scale=1, border=4)[0]
    print("  %-22s version %-3s  %d modules  %s"
          % (nom, qr.version, modules, url))
    print("     %s + %s" % (svg.name, png.name))
    print("     a %.1f cm de cote, un module fait %.2f mm "
          "(0,4 mm est le minimum pratique pour un lecteur de telephone)"
          % (cote_cm, cote_cm * 10 / modules))


def main() -> int:
    args = sys.argv[1:]
    DEST.mkdir(parents=True, exist_ok=True)
    if "--url" in args:
        produire(args[args.index("--url") + 1], "qr-personnalise")
        return 0
    print("QR du livre Dette Publique -> page du compteur\n")
    produire(URL_MESUREE, "qr-dette-broche")     # recommande : mesurable
    produire(URL_NUE, "qr-dette-url-nue")        # si le parametre n'est pas voulu
    print("\nDossier : %s" % DEST)
    print("RAPPEL : ce QR va dans le LIVRE, jamais dans le contenu A+ Amazon.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
