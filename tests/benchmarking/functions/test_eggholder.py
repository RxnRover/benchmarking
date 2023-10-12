import unittest

from benchmarking.functions import eggholder


class TestEggholder(unittest.TestCase):
    def test_min(self):
        xs = [512, 404.2319]

        foo = eggholder.Eggholder()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 4)
