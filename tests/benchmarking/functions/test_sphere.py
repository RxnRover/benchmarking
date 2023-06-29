import unittest

from benchmarking.functions import sphere


class TestSphere(unittest.TestCase):
    def test_2d(self):
        x = [0, 0]

        self.assertAlmostEqual(sphere.sphere(x), sphere.sphere_min(), 6)

    def test_3d(self):
        x = [0, 0, 0]

        self.assertAlmostEqual(sphere.sphere(x), sphere.sphere_min(), 6)

    def test_4d(self):
        x = [0, 0, 0, 0]

        self.assertAlmostEqual(sphere.sphere(x), sphere.sphere_min(), 6)

    def test_5d(self):
        x = [0, 0, 0, 0, 0]

        self.assertAlmostEqual(sphere.sphere(x), sphere.sphere_min(), 6)
