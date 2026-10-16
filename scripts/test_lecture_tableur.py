"""test_lecture_tableur.py -- cas limites de scripts/lecture_tableur.py (né le 2026-10-16).

    python scripts/test_lecture_tableur.py            (dans check-all --ci)
    python scripts/test_lecture_tableur.py --temoin   témoin positif

Chaque cas vient d'une forme réellement servie par une source : année en texte (Insee Première n° 2130), colonnes
vides en queue d'en-tête, espace insécable dans un libellé, nombre au format français, code d'absence « /// ».
Témoin : `--temoin` remplace annee() par l'ancien filtre (`isinstance(v, (int, float))`) ; au moins un test doit
échouer (sortie 1 sinon). Sortie console ASCII pur.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lecture_tableur as T  # noqa: E402


class Annee(unittest.TestCase):
    def test_nombre_et_texte(self):
        self.assertEqual(T.annee(1990), 1990)
        self.assertEqual(T.annee(1990.0), 1990)
        self.assertEqual(T.annee("1990"), 1990)            # Insee Première n° 2130, tableau complémentaire 2
        self.assertEqual(T.annee(" 2025 (p)"), 2025)
        self.assertEqual(T.annee("2024p"), 2024)

    def test_pas_une_annee(self):
        for v in (None, "", "Lecture : En 2025, ...", "Champ : France", 12, 1990.5, True, "19900"):
            self.assertIsNone(T.annee(v), v)


class Nombre(unittest.TestCase):
    def test_formes(self):
        self.assertEqual(T.nombre(705528), 705528.0)
        self.assertEqual(T.nombre("1 234,5"), 1234.5)
        self.assertEqual(T.nombre("1 234,5"), 1234.5)
        self.assertEqual(T.nombre("12,3 %"), 12.3)
        self.assertEqual(T.nombre("−4,2"), -4.2)
        self.assertEqual(T.nombre("10.1"), 10.1)

    def test_absent_n_est_pas_zero(self):
        for v in (None, "", "///", "nd", "s", "texte libre", True):
            self.assertIsNone(T.nombre(v), v)
        self.assertEqual(T.nombre(0), 0.0)                 # un vrai zéro reste un zéro

    def test_valeur_garde_le_type(self):
        self.assertIsInstance(T.valeur(-6400), int)
        self.assertEqual(T.valeur("-6 400"), -6400.0)
        self.assertIsNone(T.valeur("///"))


class ContreExpertise(unittest.TestCase):
    """Contre-exemples de la contre-expertise anthropie-site-20261016-154235, devenus permanents."""

    def test_ambiguite_refusee(self):
        for v in ("1.234", "1,234", "12,345", "-1.500"):
            self.assertIsNone(T.nombre(v), v)
        self.assertEqual(T.nombre("1.234", decimal="."), 1.234)
        self.assertEqual(T.nombre("1.234", decimal=","), 1234.0)
        self.assertEqual(T.nombre("0,354"), 0.354)          # partie entière nulle : pas de milliers possibles
        self.assertEqual(T.nombre("10.1"), 10.1)

    def test_formes_mal_formees_refusees(self):
        for v in ("1 2,3", "12%%", "1 23 456", "1,2,3", "--4"):
            self.assertIsNone(T.nombre(v), v)
        self.assertEqual(T.nombre("1 234 567"), 1234567.0)

    def test_non_finis_refuses(self):
        for v in (float("nan"), float("inf"), float("-inf"), "nan", "inf"):
            self.assertIsNone(T.nombre(v), v)
            self.assertIsNone(T.valeur(v), v)

    def test_entier_exige(self):
        self.assertEqual(T.entier(12.0), 12)
        self.assertEqual(T.entier("1 234"), 1234)
        self.assertIsNone(T.entier(12.5))
        self.assertIsNone(T.entier("12,5"))

    def test_none_ne_fait_pas_glisser_les_colonnes(self):
        entete = [None, 2024, 2021, "Ensemble"]
        i24, i21 = T.colonnes(entete, [2024, 2021])
        with self.assertRaises(ValueError):                  # r = ["Champ", None, 50, 40] : 2024 absent, on arrête
            T.cellules(["Champ", None, 50, 40], [i24, i21])
        self.assertEqual(T.cellules(["Champ", 60, 50, 40], [i24, i21]), [60, 50])
        with self.assertRaises(ValueError):
            T.colonnes([None, 2024, 2024], [2024])           # colonne en double : ambigu

    def test_serie_vide_interne_arrete_vide_de_queue_tolere(self):
        with self.assertRaises(ValueError):
            T.serie(["D", 1, None, 3, 4])                    # None entre deux déciles
        self.assertEqual(T.serie(["D", 1, 2, 3, None, None]), [1, 2, 3])   # None après « Ensemble »

    def test_annee_manquante_arrete(self):
        self.assertEqual(T.annees_continues([1990, 1991, 1992], 1990, 1992), [1990, 1991, 1992])
        with self.assertRaises(ValueError):
            T.annees_continues([1990, 1992])                 # 1991 écartée en silence
        with self.assertRaises(ValueError):
            T.annees_continues([1990, 1991, 1991])
        with self.assertRaises(ValueError):
            T.annees_continues([1990, 1991], derniere=1992)


class Entetes(unittest.TestCase):
    def test_queue_vide_et_insecables(self):
        brut = ["Année", "Émissions directes  des ménages", "Empreinte totale"] + [None] * 52
        self.assertEqual(T.entetes(brut), ["Année", "Émissions directes des ménages", "Empreinte totale"])

    def test_ligne_garde_les_positions(self):
        self.assertEqual(T.ligne(["Toutes disciplines", None, 3, None]), ["Toutes disciplines", None, 3, None])

    def test_ordre_et_trous_gardes(self):
        self.assertEqual(T.entetes(["a", None, "b", None]), ["a", None, "b"])


def lancer() -> unittest.TestResult:
    suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    return unittest.TextTestRunner(stream=open("nul" if sys.platform == "win32" else "/dev/null", "w"), verbosity=0).run(suite)


def main() -> int:
    if "--temoin" in sys.argv:
        vraie = T.annee
        T.annee = lambda v: int(v) if isinstance(v, (int, float)) else None
        r = lancer()
        T.annee = vraie
        mord = bool(r.failures or r.errors)
        print("Temoin (ancien filtre d'annee) : %s." % ("%d test(s) en echec, le test mord" % len(r.failures + r.errors) if mord else "AUCUN test en echec"))
        return 0 if mord else 1
    r = lancer()
    n = r.testsRun
    if r.failures or r.errors:
        for _, tb in r.failures + r.errors:
            print(tb.encode("ascii", "replace").decode())
        print("Lecture des tableurs : %d test(s), %d en echec. ECHEC" % (n, len(r.failures + r.errors)))
        return 1
    print("Lecture des tableurs : %d test(s), tous passes. OK" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
