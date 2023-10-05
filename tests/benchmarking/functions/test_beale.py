import unittest

from benchmarking.functions import beale


class TestBeale(unittest.TestCase):
    def test_min(self):
        xs = [3, 0.5]

        foo = beale.Beale()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)
