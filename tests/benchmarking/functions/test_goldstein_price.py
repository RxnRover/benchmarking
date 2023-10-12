import unittest

from benchmarking.functions import goldstein_price


class TestGoldsteinPrice(unittest.TestCase):
    def test_call(self):
        xs = [0, -1]

        foo = goldstein_price.GoldsteinPrice()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)
