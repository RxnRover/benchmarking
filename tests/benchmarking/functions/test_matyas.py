import unittest

from benchmarking.functions import matyas


class TestMatyas(unittest.TestCase):
    def test_min(self):
        x = [0, 0]

        self.assertAlmostEqual(matyas.matyas(x), matyas.matyas_min(), 6)
