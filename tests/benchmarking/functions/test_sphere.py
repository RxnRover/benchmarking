import unittest

from benchmarking.functions import sphere


class TestSphere(unittest.TestCase):
    def test_2d(self):
        xs = [0, 0]

        foo = sphere.Sphere()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)

    def test_3d(self):
        xs = [0, 0, 0]

        foo = sphere.Sphere()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)

    def test_4d(self):
        xs = [0, 0, 0, 0]

        foo = sphere.Sphere()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)

    def test_5d(self):
        xs = [0, 0, 0, 0, 0]

        foo = sphere.Sphere()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 6)
