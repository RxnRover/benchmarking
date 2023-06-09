import unittest
from math import pi

from benchmarking.functions import branin

class TestBranin(unittest.TestCase):

    def test_min_1(self):

        x = [-pi, 12.275]

        self.assertAlmostEqual(branin.branin(x), branin.branin_min(), 6)

    def test_min_2(self):

        x = [pi, 2.275]

        self.assertAlmostEqual(branin.branin(x), branin.branin_min(), 6)

    def test_min_3(self):

        x = [9.42478, 2.475]

        self.assertAlmostEqual(branin.branin(x), branin.branin_min(), 6)
