import unittest

from benchmarking.functions import beale


class TestBeale(unittest.TestCase):
    def test_min(self):
        x = [3, 0.5]

        self.assertAlmostEqual(beale.beale(x), beale.beale_min(), 6)
