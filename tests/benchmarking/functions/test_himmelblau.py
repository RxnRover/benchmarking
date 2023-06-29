import unittest

from benchmarking.functions import himmelblau


class TestHimmelblau(unittest.TestCase):
    def test_max(self):
        x = [-0.270845, -0.923039]

        self.assertAlmostEqual(
            himmelblau.himmelblau(x), himmelblau.himmelblau_max(), 3
        )

    def test_min_1(self):
        x = [3.0, 2.0]

        self.assertAlmostEqual(
            himmelblau.himmelblau(x), himmelblau.himmelblau_min(), 6
        )

    def test_min_2(self):
        x = [-2.805118, 3.131312]

        self.assertAlmostEqual(
            himmelblau.himmelblau(x), himmelblau.himmelblau_min(), 6
        )

    def test_min_3(self):
        x = [-3.779310, -3.283186]

        self.assertAlmostEqual(
            himmelblau.himmelblau(x), himmelblau.himmelblau_min(), 6
        )

    def test_min_4(self):
        x = [3.584428, -1.848126]

        self.assertAlmostEqual(
            himmelblau.himmelblau(x), himmelblau.himmelblau_min(), 6
        )
