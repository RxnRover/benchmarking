import unittest

from benchmarking.evaluate import evaluate
from benchmarking.functions import beale


class TestEvaluate(unittest.TestCase):
    def test_beale(self):
        x = [3, 0.5]

        eval_result = evaluate("beale", x)

        self.assertAlmostEqual(eval_result, beale.beale(x), 6)

    def test_invalid_function(self):
        x = [3, 0.5]

        self.assertRaises(ValueError, evaluate, "invalid", x)
