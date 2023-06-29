import unittest

from benchmarking.functions import booth


class TestBooth(unittest.TestCase):
    def test_min(self):
        x = [1, 3]

        self.assertAlmostEqual(booth.booth(x), booth.booth_min(), 6)
