import unittest

from benchmarking.functions import booth


class TestBooth(unittest.TestCase):
    def test_min(self):
        xs = [1, 3]

        foo = booth.Booth()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)
