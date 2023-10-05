import unittest

from benchmarking.functions import matyas


class TestMatyas(unittest.TestCase):
    def test_min(self):
        xs = [0, 0]

        foo = matyas.Matyas()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)
