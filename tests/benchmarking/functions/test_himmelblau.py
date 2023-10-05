import unittest

from benchmarking.functions import himmelblau


class TestHimmelblau(unittest.TestCase):
    def test_max(self):
        xs = [-0.270845, -0.923039]

        foo = himmelblau.Himmelblau()

        self.assertAlmostEqual(foo(xs), foo.maxima[0].value, 3)

    def test_min_1(self):
        xs = [3.0, 2.0]

        foo = himmelblau.Himmelblau()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)

    def test_min_2(self):
        xs = [-2.805118, 3.131312]

        foo = himmelblau.Himmelblau()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)

    def test_min_3(self):
        xs = [-3.779310, -3.283186]

        foo = himmelblau.Himmelblau()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)

    def test_min_4(self):
        xs = [3.584428, -1.848126]

        foo = himmelblau.Himmelblau()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)
