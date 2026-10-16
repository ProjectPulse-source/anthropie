"""test_langue_generee.py -- cas limites de scripts/langue_generee.py (chantier 3, arbitrage OPTIMUM-26 du 2026-10-11).

    python scripts/test_langue_generee.py        (dans check-all --ci)

Chaque cas vient d'un défaut vu dans le texte servi ou d'une frontière d'accord : zéro, un, 1,9, 2, négatif, −0,04
arrondi à zéro, absent, 16/17, grands nombres, changement de langue. Témoin positif : `--temoin` casse l'accord de
« point » dans une copie du module chargée en mémoire ; au moins un test doit échouer (sortie 1 sinon).
Sortie console ASCII pur.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import langue_generee as L  # noqa: E402

S, M = L.NBSP, L.MOINS


class Nombre(unittest.TestCase):
    def test_fr_en(self):
        self.assertEqual(L.nombre(3536.14), "3" + S + "536,1")
        self.assertEqual(L.nombre(3536.14, lang="en"), "3,536.1")
        self.assertEqual(L.nombre(1234567, 0), "1" + S + "234" + S + "567")

    def test_negatif_et_zero(self):
        self.assertEqual(L.nombre(-1.2), M + "1,2")
        self.assertEqual(L.nombre(-0.04), "0,0")          # arrondi à zéro : pas de « −0,0 »
        self.assertEqual(L.nombre(-0.04, lang="en"), "0.0")
        self.assertEqual(L.nombre(0, 0), "0")

    def test_absent_et_langue(self):
        with self.assertRaises(ValueError):
            L.nombre(None)
        with self.assertRaises(ValueError):
            L.nombre(1, lang="de")


class Signe(unittest.TestCase):
    def test_signe(self):
        self.assertEqual(L.signe(7.71), "+7,7")
        self.assertEqual(L.signe(-15.7), M + "15,7")
        self.assertEqual(L.signe(-0.04), "0,0")
        self.assertEqual(L.signe(0.04, lang="en"), "0.0")
        self.assertEqual(L.signe(6.1, lang="en"), "+6.1")
        self.assertEqual(L.signe(1234.5, lang="en"), "+1,234.5")

    def test_sans_signe(self):
        self.assertEqual(L.sans_signe(-15.7), "15,7")       # « a retiré 15,7 », jamais « retiré −15,7 »
        self.assertEqual(L.sans_signe(7.7, lang="en"), "7.7")
        with self.assertRaises(ValueError):
            L.sans_signe(None)


class Point(unittest.TestCase):
    def test_fr(self):
        for v, mot in ((0, "point"), (1, "point"), (1.9, "point"), (1.94, "point"), (1.96, "points"), (2, "points"),
                       (-1.2, "point"), (-2.4, "points"), (-0.04, "point"), (32.7, "points")):
            self.assertEqual(L.point(v), mot, v)

    def test_en(self):
        for v, mot in ((1, "point"), (1.0, "point"), (-1, "point"), (0, "points"), (0.1, "points"), (0.5, "points"),
                       (1.9, "points"), (2, "points"), (0.96, "point")):   # 0.96 affiché « 1.0 »
            self.assertEqual(L.point(v, lang="en"), mot, v)

    def test_points(self):
        self.assertEqual(L.points(1.9), "1,9" + S + "point")
        self.assertEqual(L.points(7.71, signe_=True), "+7,7" + S + "points")
        self.assertEqual(L.points(0.11, 2, "en"), "0.11 points")


class Lettres(unittest.TestCase):
    def test_bornes(self):
        self.assertEqual(L.lettres(0), "zéro")
        self.assertEqual(L.lettres(1), "un")
        self.assertEqual(L.lettres(16), "seize")
        self.assertEqual(L.lettres(17), "17")
        self.assertEqual(L.lettres(16, "en"), "sixteen")
        self.assertEqual(L.lettres(17, "en"), "17")
        self.assertEqual(L.lettres(1234, "fr"), "1" + S + "234")
        with self.assertRaises(ValueError):
            L.lettres(2.5)
        with self.assertRaises(ValueError):
            L.lettres(None)

    def test_compte(self):
        self.assertEqual(L.compte(0, "pays", "pays"), "zéro pays")
        self.assertEqual(L.compte(1, "pays", "pays"), "un pays")
        self.assertEqual(L.compte(3, "année", "années"), "trois années")
        self.assertEqual(L.compte(0, "country", "countries", "en"), "zero countries")
        self.assertEqual(L.compte(1, "country", "countries", "en"), "one country")
        self.assertEqual(L.compte(17, "country", "countries", "en"), "17 countries")


class Enumere(unittest.TestCase):
    def test(self):
        self.assertEqual(L.enumere(["la Grèce"]), "la Grèce")
        self.assertEqual(L.enumere(["Chypre", "le Portugal"]), "Chypre et le Portugal")
        self.assertEqual(L.enumere(["a", "b", "c"]), "a, b et c")
        self.assertEqual(L.enumere(["a", "b", "c"], "en"), "a, b and c")
        with self.assertRaises(ValueError):
            L.enumere([])


class RangEtComparaison(unittest.TestCase):
    """Cas fondateur du 16/10/2026 : 2,2285 et 2,2278 s'affichent « 2,23 » -- ni rang distinct, ni « dépasse »."""
    def test_egalite_a_l_affichage(self):
        v = {"IT": 3.85, "BE": 2.2285, "FR": 2.2278, "PT": 1.93}
        self.assertEqual(L.rang(v, "FR", 2), (2, ["BE"]))
        self.assertFalse(L.depasse(2.2285, 2.2278, 2))
        self.assertTrue(L.depasse(2.2285, 2.2278, 4))

    def test_sens_croissant_et_sans_egalite(self):
        v = {"a": 1.04, "b": 2.0, "c": 3.0}
        self.assertEqual(L.rang(v, "c", 1), (1, []))
        self.assertEqual(L.rang(v, "a", 1, decroissant=False), (1, []))
        self.assertEqual(L.rang(v, "c", 0, decroissant=False), (3, []))

    def test_positions_ex_aequo(self):
        self.assertEqual(L.positions([1.42, 1.38, 1.9], 1, maxi=False), [0, 1])     # 1,4 et 1,4
        self.assertEqual(L.position_unique([1.2, 1.9, 1.5], 1), 1)
        with self.assertRaises(ValueError):
            L.position_unique([1.42, 1.38, 1.0], 1)

    def test_absent(self):
        with self.assertRaises(ValueError):
            L.rang({"a": 1.0}, "z")
        with self.assertRaises(ValueError):
            L.depasse(None, 1.0)


def lancer() -> unittest.TestResult:
    suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    return unittest.TextTestRunner(stream=open("nul" if sys.platform == "win32" else "/dev/null", "w"), verbosity=0).run(suite)


def main() -> int:
    if "--temoin" in sys.argv:
        vrai = L.point
        L.point = lambda v, dec=1, lang="fr": "points" if lang == "fr" and abs(v) >= 1 else vrai(v, dec, lang)
        r = lancer()
        L.point = vrai
        # Second témoin (16/10/2026) : un rang calculé sur la valeur BRUTE doit faire échouer un test.
        vraie = L.affichee
        L.affichee = lambda v, dec=1: L._val(v)
        r2 = lancer()
        L.affichee = vraie
        if not (r2.failures or r2.errors):
            print("Temoin (rang sur valeur brute) : AUCUN test en echec.")
            return 1
        mord = bool(r.failures or r.errors)
        print("Temoin (accord de point casse) : %s." % ("%d test(s) en echec, le test mord" % len(r.failures + r.errors) if mord else "AUCUN test en echec"))
        return 0 if mord else 1
    r = lancer()
    for t, tb in r.failures + r.errors:
        print("  ECHEC  %s : %s" % (t.id(), tb.strip().splitlines()[-1].encode("ascii", "backslashreplace").decode("ascii")))
    if r.failures or r.errors:
        print("Langue generee : %d test(s) en echec sur %d." % (len(r.failures) + len(r.errors), r.testsRun))
        return 1
    print("Langue generee : %d test(s), tous passes. OK" % r.testsRun)
    return 0


if __name__ == "__main__":
    sys.exit(main())
