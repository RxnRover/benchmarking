import unittest

from benchmarking.functions import shubert


class TestShubert(unittest.TestCase):

    def test_single_min(self):

        x_1 = -1.4251
        x_2 = -0.8004
        
        self.assertAlmostEqual(shubert.shubert(x_1, x_2),
                               shubert.shubert_min(), 4)
