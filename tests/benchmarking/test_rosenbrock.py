import unittest

from benchmarking.functions import rosenbrock


class TestRosenbrock(unittest.TestCase):

    def test_minimum_in_different_dimensions(self):

        dim_count = 6 # test in 1-6 dimensional space

        for dim in range(dim_count):
            print("Testing {} dimensions".format(dim))

            xs = [1] * dim

            self.assertAlmostEqual(rosenbrock.rosenbrock(xs),
                                   rosenbrock.rosenbrock_min(), 6)
