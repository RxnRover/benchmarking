import unittest

from benchmarking.functions import three_hump_camel


class TestThreeHumpCamel(unittest.TestCase):
    def test_min(self):
        x = [0, 0]

        self.assertAlmostEqual(
            three_hump_camel.three_hump_camel(x),
            three_hump_camel.three_hump_camel_min(),
            6,
        )
