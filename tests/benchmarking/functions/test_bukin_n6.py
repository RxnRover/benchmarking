import unittest

from benchmarking.functions import bukin_n6


class TestBukinN6(unittest.TestCase):
    def test_min(self):
        x = [-10, 1]

        self.assertAlmostEqual(
            bukin_n6.bukin_n6(x), bukin_n6.bukin_n6_min(), 6
        )
