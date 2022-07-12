import unittest

from benchmarking.functions import goldstein_price


class TestGoldsteinPrice(unittest.TestCase):

    def test_call(self):

        x = [0, -1]

        self.assertAlmostEqual(goldstein_price.goldstein_price(x[0], x[1]),
                               goldstein_price.goldstein_price_min(), 6)
