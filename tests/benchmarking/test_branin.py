import unittest

from benchmarking.functions import branin

class TestBranin(unittest.TestCase):

    def test_call(self):

        x = [9.42478, 2.475]

        self.assertAlmostEqual(branin.branin(x), branin.branin_min(), 6)
