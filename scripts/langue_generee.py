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

import math

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
    x = float(v)
    # Contre-expertise du 16/10 : rang({"FR": NaN, "BE": 3}) rendait (1, []) -- une donnée invalide classée première.
    if not math.isfinite(x):
        raise ValueError("valeur non finie (%r) : ni s'ecrire, ni se classer, ni se comparer" % (v,))
    return x


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


# --- Rangs et comparaisons publiés (2026-10-16) ------------------------------------------------------------------
# Un rang, un « dépasse », un « plus que » se décident sur la valeur AFFICHÉE, comme les accords ci-dessus : un écart que
# le lecteur ne voit pas ne classe pas. Cas fondateur : intérêts rapportés au PIB, données 2025 (Eurostat, 15/10/2026),
# Belgique 2,2285 % contre France 2,2278 %, toutes deux affichées « 2,23 % » ; la page publiait « huitième rang, cinq
# pays moins endettés la dépassent ». Contrôle : scripts/check-lecture-donnees.py refuse le rang calculé sur valeurs
# brutes (`sorted(...).index(x) + 1`) dans un générateur.

def affichee(v, dec: int = 1) -> float:
    """La valeur telle que le lecteur la lit : même arrondi que nombre()."""
    return float(("{:.%df}" % dec).format(_val(v)))


def depasse(a, b, dec: int = 1) -> bool:
    """a > b À L'AFFICHAGE : faux si les deux s'affichent pareil (« dépasse », « plus que », « paie davantage »)."""
    return affichee(a, dec) > affichee(b, dec)


def rang(valeurs: dict, cle, dec: int = 1, decroissant: bool = True) -> tuple[int, list]:
    """Rang de `cle` parmi `valeurs` ({identifiant: valeur}) à la précision affichée, et les ex aequo.

    Rang = 1 + nombre de valeurs affichées strictement meilleures ; les ex aequo (même valeur affichée) sont rendus
    dans l'ordre d'insertion, pour que la prose les dise (« à égalité avec … ») ou qu'une garde arrête la phrase qui
    ne les prévoit pas."""
    a = {k: affichee(v, dec) for k, v in valeurs.items()}
    if cle not in a:
        raise ValueError("rang : %r absent des valeurs" % (cle,))
    ref = a[cle]
    mieux = sum(1 for k, v in a.items() if k != cle and (v > ref if decroissant else v < ref))
    return 1 + mieux, [k for k, v in a.items() if k != cle and v == ref]


def positions(valeurs, dec: int = 1, maxi: bool = True) -> list[int]:
    """Indices de l'extremum (max si maxi, min sinon) À L'AFFICHAGE, tous les ex aequo compris, dans l'ordre.

    Remplace `liste.index(max(liste))`, qui rend la première occurrence et laisse une phrase nommer une année ou un
    dixième arbitraire quand deux valeurs s'affichent pareil. L'appelant décide : une garde « D7 ou D8 » exige que
    toutes les positions y tombent ; une phrase qui nomme UNE position exige qu'il n'y en ait qu'une."""
    a = [affichee(v, dec) for v in valeurs]
    if not a:
        raise ValueError("positions : liste vide")
    ext = max(a) if maxi else min(a)
    return [i for i, v in enumerate(a) if v == ext]


def position_unique(valeurs, dec: int = 1, maxi: bool = True, quoi: str = "extremum") -> int:
    """Indice de l'extremum quand la prose en nomme UN seul ; ValueError si deux valeurs s'affichent ex aequo."""
    p = positions(valeurs, dec, maxi)
    if len(p) > 1:
        raise ValueError("%s : ex aequo a l'affichage aux positions %s ; la phrase qui en nomme une est a reecrire" % (quoi, p))
    return p[0]


def extremum(elements, cle, dec: int = 1, maxi: bool = True, quoi: str = "extremum"):
    """Remplace `max(elements, key=cle)` / `min(...)` quand l'élément choisi (une année de pic, un pays, un dixième)
    soutient une phrase : ValueError si deux éléments s'affichent ex aequo à la précision `dec` (contre-expertise du
    16/10/2026, point 8 : un sommet « en 2019 » ne se publie pas quand 2019 et 2021 s'affichent pareil)."""
    el = list(elements)
    return el[position_unique([cle(x) for x in el], dec, maxi, quoi)]


def sommets(serie: dict, dec: int = 1, maxi: bool = True) -> list:
    """Clés (années, pays…) dont la valeur s'affiche égale à l'extremum, dans l'ordre croissant des clés : pour une
    phrase qui dit QUAND une série culmine sans choisir arbitrairement entre des années indiscernables à l'affichage
    (« 11,8 % en 2009 et 2013 »). Pour une phrase qui ne peut en nommer qu'une, utiliser extremum()."""
    cles = sorted(serie)
    return [cles[i] for i in positions([serie[k] for k in cles], dec, maxi)]
