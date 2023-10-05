import unittest

from benchmarking.functions import six_hump_camel


class TestSixHumpCamel(unittest.TestCase):
    def test_min_1(self):
        xs = [0.0898, -0.7126]

        foo = six_hump_camel.SixHumpCamel()

        self.assertAlmostEqual(foo(xs), foo.minima[0].value, 4)

    def test_min_2(self):
        xs = [-0.0898, 0.7126]

        foo = six_hump_camel.SixHumpCamel()

        self.assertAlmostEqual(foo(xs), foo.minima[0].value, 4)
