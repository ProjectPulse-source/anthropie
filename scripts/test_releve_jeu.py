"""test_releve_jeu.py -- releve_jeu.normalise (né le 2026-10-19).

    python scripts/test_releve_jeu.py            (dans check-all --ci)
    python scripts/test_releve_jeu.py --temoin   témoin positif

Un générateur compare le jeu qu'il vient de calculer à celui en place et n'écrit rien s'ils sont identiques. Comparés
exactement, deux calculs du même jeu différaient au 15e chiffre (ordre de sommation, autre machine) : trois commits du
robot sur treize, du 25/09 au 18/10, ne portaient que ce bruit, avec leurs figures et leurs PNG. Les cas de bruit
ci-dessous sont repris des commits 4b74633 (dette_generations) et 0583ef0 (dette_baisse).
Témoin : `--temoin` remplace normalise() par l'identité ; au moins un test doit échouer (sortie 1 sinon).
Sortie console ASCII pur.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import releve_jeu as R  # noqa: E402


class Bruit(unittest.TestCase):
    def test_bruit_reel_ignore(self):
        for a, b in ((81.73406701860014, 81.73406701860016), (18.467822240006335, 18.46782224000633),
                     (22.967377287238314, 22.96737728723832), (2643912.0999999996, 2643912.1)):
            self.assertEqual(R.normalise(a), R.normalise(b), (a, b))

    def test_profondeur(self):
        x = {"a": [{"v": 0.1 + 0.2}], "b": {"c": [1.0000000000000002]}}
        y = {"a": [{"v": 0.3}], "b": {"c": [1.0]}}
        self.assertEqual(R.normalise(x), R.normalise(y))


class VraieDonnee(unittest.TestCase):
    def test_variation_au_onzieme_chiffre_conservee(self):
        self.assertNotEqual(R.normalise(73.9408345880), R.normalise(73.9408345890))

    def test_revision_ordinaire_conservee(self):
        self.assertNotEqual(R.normalise({"dette": 115.6}), R.normalise({"dette": 115.7}))
        self.assertNotEqual(R.normalise([0.0]), R.normalise([1e-9]))

    def test_types_non_flottants_intacts(self):
        x = {"n": 3, "s": "2,9 points", "b": True, "z": None, "l": [2025, "T2 2026"]}
        self.assertEqual(R.normalise(x), x)
        self.assertIs(type(R.normalise(True)), bool)


class Ecriture(unittest.TestCase):
    def test_relu_identique(self):
        """Écrit puis relu, un jeu normalisé reste identique à lui-même : la comparaison suivante ne voit rien."""
        x = R.normalise({"a": [73.94083458807205, -0.000123456789012345, 1e-320, 6.02e23]})
        self.assertEqual(R.normalise(json.loads(json.dumps(x, ensure_ascii=False, indent=1))), x)


def lancer() -> unittest.TestResult:
    suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    return unittest.TextTestRunner(stream=open("nul" if sys.platform == "win32" else "/dev/null", "w"), verbosity=0).run(suite)


def main() -> int:
    if "--temoin" in sys.argv:
        vraie = R.normalise
        R.normalise = lambda x: x
        r = lancer()
        R.normalise = vraie
        mord = bool(r.failures or r.errors)
        print("Temoin (normalisation desactivee) : %s." % ("%d test(s) en echec, le test mord" % len(r.failures + r.errors) if mord else "AUCUN test en echec"))
        return 0 if mord else 1
    r = lancer()
    n = r.testsRun
    if r.failures or r.errors:
        for _, tb in r.failures + r.errors:
            print(tb.encode("ascii", "replace").decode())
        print("Releve des jeux : %d test(s), %d en echec. ECHEC" % (n, len(r.failures + r.errors)))
        return 1
    print("Releve des jeux : %d test(s), tous passes. OK" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
