import unittest

from benchmarking.functions.Optimum import Optimum


class TestOptimum(unittest.TestCase):
    def test_creation(self):
        input = [0, 0]
        output = 0

        opt = Optimum(input, output)

        self.assertEqual(opt.coordinates, input)
        self.assertEqual(opt.value, output)
        self.assertEqual(opt.ndim, 2)

    def test_string(self):
        input = [0, 0]
        output = 0

        opt = Optimum(input, output)

        self.assertEqual(str(opt), "[0, 0]: 0")
