import unittest

from benchmarking.functions import schwefel


class TestSchwefel(unittest.TestCase):
    def test_2d(self):
        dim = 2
        xs = [420.9687] * dim

        foo = schwefel.Schwefel(dim=dim)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 3)

    def test_3d(self):
        dim = 3
        xs = [420.9687] * dim

        foo = schwefel.Schwefel(dim=dim)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 3)

    def test_4d(self):
        dim = 4
        xs = [420.9687] * dim

        foo = schwefel.Schwefel(dim=dim)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 3)

    def test_5d(self):
        dim = 5
        xs = [420.9687] * dim

        foo = schwefel.Schwefel(dim=dim)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 3)
