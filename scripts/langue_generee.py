"""langue_generee.py -- les mots que les générateurs écrivent autour d'un nombre, en français et en anglais.

Organe commun (industrialisation des ressources, arbitrage OPTIMUM-26 du 2026-10-11, chantier 3). Les fonctions de
format existaient en copies dans treize générateurs, sans aucun test ; la relecture de langue du 11/10/2026 a trouvé
leurs défauts dans le texte servi (« a retiré −15,7 », « 0,4 points », « gagne +7,7 », chiffres et lettres mêlés).
Repris des meilleures copies : update_dette_baisse.py (fr, signe, lettres, enumere), update_dette_dynamique.py
(_abs, _pt), update_dette_monde.py (unite). Tests : scripts/test_langue_generee.py, dans check-all --ci.

Contrats :
- tout se calcule sur la valeur AFFICHÉE (arrondie) : 1,96 affiché « 2,0 » s'accorde au pluriel, −0,04 affiché
  « 0,0 » ne porte pas de signe ;
- une valeur absente (None) lève ValueError : jamais un « 0 » fabriqué pour une donnée manquante ;
- langue inconnue : ValueError.

ADOPTION : générateur par générateur, à sa phase B (et pour les huit ressources refondues, à leur prochaine
intervention), sortie vérifiée identique ou écart expliqué ; jamais par migration en masse (plusieurs générateurs
lisent des API en direct). Une copie locale meurt quand son générateur adopte le module.
"""
from __future__ import annotations

NBSP = " "
MOINS = "−"
LETTRES = {
    "fr": ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze",
           "treize", "quatorze", "quinze", "seize"],
    "en": ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
           "thirteen", "fourteen", "fifteen", "sixteen"],
}


def _lang(lang: str) -> str:
    if lang not in ("fr", "en"):
        raise ValueError("langue inconnue : %r" % (lang,))
    return lang


def _val(v) -> float:
    if v is None:
        raise ValueError("valeur absente : rien ne s'ecrit a la place d'une donnee manquante")
    return float(v)


def nombre(v, dec: int = 1, lang: str = "fr") -> str:
    """3536.14 -> « 3 536,1 » (fr, espace insécable) ou « 3,536.1 » (en) ; moins typographique ; zéro sans signe."""
    lang, v = _lang(lang), _val(v)
    s = ("{:,.%df}" % dec).format(v)
    if float(s.replace(",", "")) == 0:
        s = s.lstrip("-")
    if lang == "fr":
        s = s.replace(",", "\x00").replace(".", ",").replace("\x00", NBSP)
    return s.replace("-", MOINS)


def signe(v, dec: int = 1, lang: str = "fr") -> str:
    """Valeur affichée avec son signe : « +7,7 », « −15,7 » ; une valeur affichée nulle n'en porte pas (« 0,0 »)."""
    s = nombre(v, dec, lang)
    if s.startswith(MOINS) or float(s.replace(NBSP, "").replace(",", ".") if lang == "fr" else s.replace(",", "")) == 0:
        return s
    return "+" + s


def sans_signe(v, dec: int = 1, lang: str = "fr") -> str:
    """Après un verbe qui porte le sens (« a retiré », « gagne », « added ») : « retiré 15,7 », jamais « retiré −15,7 »."""
    return nombre(abs(_val(v)), dec, lang)


def point(v, dec: int = 1, lang: str = "fr") -> str:
    """Accord de « point » sur la valeur AFFICHÉE : singulier sous 2 en français, pluriel sauf exactement 1 en anglais."""
    a = abs(float(sans_signe(v, dec, lang).replace(NBSP, "").replace(",", ".") if lang == "fr"
                  else sans_signe(v, dec, lang).replace(",", "")))
    if lang == "fr":
        return "point" if a < 2 else "points"
    return "point" if a == 1 else "points"


def points(v, dec: int = 1, lang: str = "fr", signe_: bool = False) -> str:
    """Nombre et unité ensemble : « 1,9 point », « 2,0 points », « 0.5 points », « +7,7 points » (fr : insécable)."""
    s = signe(v, dec, lang) if signe_ else nombre(v, dec, lang)
    return s + (NBSP if lang == "fr" else " ") + point(v, dec, lang)


def lettres(n, lang: str = "fr") -> str:
    """Entier de 0 à 16 en lettres (règle typographique) ; au-delà, en chiffres. Un non-entier lève ValueError."""
    lang, v = _lang(lang), _val(n)
    if v != int(v):
        raise ValueError("lettres() attend un entier : %r" % (n,))
    n = int(v)
    return LETTRES[lang][n] if 0 <= n < len(LETTRES[lang]) else nombre(n, 0, lang)


def enumere(items, lang: str = "fr") -> str:
    """« a, b et c » / « a, b and c » (sans virgule de série, usage du site). Liste vide : ValueError."""
    lang, items = _lang(lang), list(items)
    if not items:
        raise ValueError("enumeration vide")
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + (" et " if lang == "fr" else " and ") + items[-1]


def compte(n, mot_sing: str, mot_plur: str, lang: str = "fr") -> str:
    """« un pays », « trois pays », « seventeen countries »… : nombre en lettres jusqu'à seize et accord du nom.
    Français : singulier pour 0 et 1 ; anglais : singulier pour 1 seulement."""
    lang = _lang(lang)
    n = int(_val(n))
    sing = n in (0, 1) if lang == "fr" else n == 1
    return lettres(n, lang) + " " + (mot_sing if sing else mot_plur)
