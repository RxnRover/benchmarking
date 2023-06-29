import unittest

from benchmarking.functions import styblinski_tang


class TestStyblinskiTang(unittest.TestCase):
    def test_2d(self):
        x = [0, 0]

        self.assertAlmostEqual(
            styblinski_tang.styblinski_tang(x),
            styblinski_tang.styblinski_tang_min(),
            6,
        )

    def test_3d(self):
        x = [0, 0, 0]

        self.assertAlmostEqual(
            styblinski_tang.styblinski_tang(x),
            styblinski_tang.styblinski_tang_min(),
            6,
        )

    def test_4d(self):
        x = [0, 0, 0, 0]

        self.assertAlmostEqual(
            styblinski_tang.styblinski_tang(x),
            styblinski_tang.styblinski_tang_min(),
            6,
        )

    def test_5d(self):
        x = [0, 0, 0, 0, 0]

        self.assertAlmostEqual(
            styblinski_tang.styblinski_tang(x),
            styblinski_tang.styblinski_tang_min(),
            6,
        )
