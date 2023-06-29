import unittest

from benchmarking.functions import eggholder


class TestEggholder(unittest.TestCase):
    def test_min(self):
        x = [512, 404.2319]

        self.assertAlmostEqual(
            eggholder.eggholder(x), eggholder.eggholder_min(), 4
        )
