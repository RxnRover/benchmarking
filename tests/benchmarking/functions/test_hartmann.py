import unittest

from benchmarking.functions import hartmann


class TestHartmann(unittest.TestCase):
    def test_3d(self):
        xs = [0.114614, 0.555649, 0.852547]

        self.assertAlmostEqual(
            hartmann.hartmann(xs), hartmann.hartmann_min(), 5
        )

    def test_6d(self):
        xs = [0.20169, 0.150011, 0.476874, 0.275332, 0.311652, 0.6573]

        self.assertAlmostEqual(
            hartmann.hartmann(xs), hartmann.hartmann_min(dimensions=6), 5
        )
