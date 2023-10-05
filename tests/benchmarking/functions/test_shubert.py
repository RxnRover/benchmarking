import unittest

import numpy as np

from benchmarking.functions import shubert


class TestShubert(unittest.TestCase):
    def test_single_min(self):
        # This minimum point was found through manual optimization
        xs = [-1.4251, -0.8004]

        foo = shubert.Shubert()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 4)

    def test_multiple_mins(self):
        """The Shubert function has a period of 2 * pi. This can be used
        to test multiple minima and make sure the period is correct in the
        implementation.
        """

        foo = shubert.Shubert()

        # Shubert function has a period of 2 * pi
        period = 2 * np.pi

        # This minimum point was found through manual optimization
        xs = [-1.4251, -0.8004]

        # Create a 5x5 grid around the initial point. To get a grid centered
        # on the initial point, this should always be an odd number.
        grid_length = 5

        # Initialize to the lowest value in the grid
        # For example, grid_length = 5 would be
        #   x_i = x_1 - 2 * period, or x_i = x_1 - 4 * pi
        x_i = xs[0] - grid_length // 2 * period
        for i in range(grid_length):
            x_i += period

            # Initialize to the lowest value in the grid
            x_j = xs[1] - grid_length // 2 * period
            for j in range(grid_length):
                x_j += period

                self.assertAlmostEqual(
                    foo([x_i, x_j]), foo.global_minima[0].value, 4
                )

                self.assertAlmostEqual(
                    foo([x_j, x_i]), foo.global_minima[0].value, 4
                )
