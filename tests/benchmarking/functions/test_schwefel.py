import unittest

from benchmarking.functions import schwefel


class TestSchwefel(unittest.TestCase):
    def test_2d(self):
        dim = 2
        x = [420.9687] * dim

        self.assertAlmostEqual(
            schwefel.schwefel(x), schwefel.schwefel_min(), 3
        )

    def test_3d(self):
        dim = 3
        x = [420.9687] * dim

        self.assertAlmostEqual(
            schwefel.schwefel(x), schwefel.schwefel_min(), 3
        )

    def test_4d(self):
        dim = 4
        x = [420.9687] * dim

        self.assertAlmostEqual(
            schwefel.schwefel(x), schwefel.schwefel_min(), 3
        )

    def test_5d(self):
        dim = 5
        x = [420.9687] * dim

        self.assertAlmostEqual(
            schwefel.schwefel(x), schwefel.schwefel_min(), 3
        )
