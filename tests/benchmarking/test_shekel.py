import unittest

from benchmarking.functions import shekel


class TestShekel(unittest.TestCase):

    def test_m5(self):

        xs = [4, 4, 4, 4]
        m = 5
        
        self.assertAlmostEqual(shekel.shekel(xs, m),
                               shekel.shekel_min(m), 3)

    def test_m7(self):

        xs = [4, 4, 4, 4]
        m = 7
        
        self.assertAlmostEqual(shekel.shekel(xs, m),
                               shekel.shekel_min(m), 3)

    def test_m10(self):

        xs = [4, 4, 4, 4]
        m = 10
        
        self.assertAlmostEqual(shekel.shekel(xs, m),
                               shekel.shekel_min(m), 3)
