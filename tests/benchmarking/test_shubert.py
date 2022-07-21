import unittest

from benchmarking.functions import shubert


class TestShubert(unittest.TestCase):

    def test_single_min(self):

        # These input values were found manually. Since this function is
        # periodic, there should be infinite global minima. Ideally,
        # an analysis of extrema should be performed and multiple minima
        # based on that analysis should be tested.
        x_1 = -1.4251
        x_2 = -0.8004
        
        self.assertAlmostEqual(shubert.shubert(x_1, x_2),
                               shubert.shubert_min(), 4)
