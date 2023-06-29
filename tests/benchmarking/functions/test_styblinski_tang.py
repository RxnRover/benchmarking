import unittest

from benchmarking.functions import styblinski_tang


class TestStyblinskiTang(unittest.TestCase):
    def test_2d(self):
        dim = 2
        x = [-2.903534] * dim

        self.assertAlmostEqual(
            styblinski_tang.styblinski_tang(x),
            styblinski_tang.styblinski_tang_min(dim),
            2,
        )

    def test_3d(self):
        dim = 3
        x = [-2.903534] * dim

        self.assertAlmostEqual(
            styblinski_tang.styblinski_tang(x),
            styblinski_tang.styblinski_tang_min(dim),
            2,
        )

    def test_4d(self):
        dim = 4
        x = [-2.903534] * dim

        self.assertAlmostEqual(
            styblinski_tang.styblinski_tang(x),
            styblinski_tang.styblinski_tang_min(dim),
            2,
        )

    def test_5d(self):
        dim = 5
        x = [-2.903534] * dim

        self.assertAlmostEqual(
            styblinski_tang.styblinski_tang(x),
            styblinski_tang.styblinski_tang_min(dim),
            2,
        )
