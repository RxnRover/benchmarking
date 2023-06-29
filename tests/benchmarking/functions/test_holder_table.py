import unittest

from benchmarking.functions import holder_table


class TestHolderTable(unittest.TestCase):
    def test_min_1(self):
        x = [8.05502, 9.66459]

        self.assertAlmostEqual(
            holder_table.holder_table(x), holder_table.holder_table_min(), 4
        )

    def test_min_2(self):
        x = [8.05502, -9.66459]

        self.assertAlmostEqual(
            holder_table.holder_table(x), holder_table.holder_table_min(), 4
        )

    def test_min_3(self):
        x = [-8.05502, 9.66459]

        self.assertAlmostEqual(
            holder_table.holder_table(x), holder_table.holder_table_min(), 4
        )

    def test_min_4(self):
        x = [-8.05502, -9.66459]

        self.assertAlmostEqual(
            holder_table.holder_table(x), holder_table.holder_table_min(), 4
        )
