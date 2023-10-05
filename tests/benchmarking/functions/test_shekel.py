import unittest

from benchmarking.functions import shekel


class TestShekel(unittest.TestCase):
    def test_m5(self):
        xs = [4, 4, 4, 4]
        m = 5

        foo = shekel.Shekel(m=m)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 3)

    def test_m7(self):
        xs = [4, 4, 4, 4]
        m = 7

        foo = shekel.Shekel(m=m)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 3)

    def test_m10(self):
        xs = [4, 4, 4, 4]
        m = 10

        foo = shekel.Shekel(m=m)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 3)
