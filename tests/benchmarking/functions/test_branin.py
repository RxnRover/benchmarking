import unittest
from math import pi

from benchmarking.functions import branin


class TestBranin(unittest.TestCase):
    def test_min_1(self):
        xs = [-pi, 12.275]

        foo = branin.Branin()

        self.assertAlmostEqual(foo(xs), foo.minima[0].value, 6)

    def test_min_2(self):
        xs = [pi, 2.275]

        foo = branin.Branin()

        self.assertAlmostEqual(foo(xs), foo.minima[1].value, 6)

    def test_min_3(self):
        xs = [9.42478, 2.475]

        foo = branin.Branin()

        self.assertAlmostEqual(foo(xs), foo.minima[2].value, 6)
