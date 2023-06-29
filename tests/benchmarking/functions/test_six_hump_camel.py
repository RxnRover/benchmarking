import unittest

from benchmarking.functions import six_hump_camel


class TestSixHumpCamel(unittest.TestCase):
    def test_min_1(self):
        x = [0.0898, -0.7126]

        self.assertAlmostEqual(
            six_hump_camel.six_hump_camel(x),
            six_hump_camel.six_hump_camel_min(),
            4,
        )

    def test_min_2(self):
        x = [-0.0898, 0.7126]

        self.assertAlmostEqual(
            six_hump_camel.six_hump_camel(x),
            six_hump_camel.six_hump_camel_min(),
            4,
        )
