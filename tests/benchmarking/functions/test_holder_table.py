import unittest

from benchmarking.functions import holder_table


class TestHolderTable(unittest.TestCase):
    def test_min_1(self):
        xs = [8.05502, 9.66459]

        foo = holder_table.HolderTable()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 4)

    def test_min_2(self):
        xs = [8.05502, -9.66459]

        foo = holder_table.HolderTable()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 4)

    def test_min_3(self):
        xs = [-8.05502, 9.66459]

        foo = holder_table.HolderTable()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 4)

    def test_min_4(self):
        xs = [-8.05502, -9.66459]

        foo = holder_table.HolderTable()

        self.assertAlmostEqual(foo(xs), foo.global_minima[0].value, 4)
