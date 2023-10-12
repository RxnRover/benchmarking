import unittest

from benchmarking.functions import bukin_n6


class TestBukinN6(unittest.TestCase):
    def test_min(self):
        xs = [-10, 1]

        foo = bukin_n6.BukinN6()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)
