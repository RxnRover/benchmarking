import unittest

from benchmarking.functions import three_hump_camel


class TestThreeHumpCamel(unittest.TestCase):
    def test_min(self):
        xs = [0, 0]

        foo = three_hump_camel.ThreeHumpCamel()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)
