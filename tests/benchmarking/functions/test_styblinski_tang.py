import unittest

from benchmarking.functions import styblinski_tang


class TestStyblinskiTang(unittest.TestCase):
    def test_2d(self):
        dim = 2
        xs = [-2.903534] * dim

        foo = styblinski_tang.StyblinskiTang(dim)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 2)

    def test_3d(self):
        dim = 3
        xs = [-2.903534] * dim

        foo = styblinski_tang.StyblinskiTang(dim)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 2)

    def test_4d(self):
        dim = 4
        xs = [-2.903534] * dim

        foo = styblinski_tang.StyblinskiTang(dim)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 2)

    def test_5d(self):
        dim = 5
        xs = [-2.903534] * dim

        foo = styblinski_tang.StyblinskiTang(dim)

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 2)
