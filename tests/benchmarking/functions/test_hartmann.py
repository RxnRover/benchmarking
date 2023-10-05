import unittest

from benchmarking.functions import hartmann


class TestHartmann(unittest.TestCase):
    def test_3d(self):
        xs = [0.114614, 0.555649, 0.852547]

        foo = hartmann.Hartmann3D()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 5)

    def test_6d(self):
        xs = [0.20169, 0.150011, 0.476874, 0.275332, 0.311652, 0.6573]

        foo = hartmann.Hartmann6D()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 5)
