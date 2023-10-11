import unittest

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class TestBenchmarkingFunction(unittest.TestCase):
    def test_creation(self):
        # 1D function with various global and local extrema
        def foo(x):
            return x**4 + x**3 - x**2

        corr_bounds = [-2.0, 1.0]

        bench = BenchmarkingFunction()

        # Set the function to use
        bench.set_function(foo)

        # Set recommended boundary
        bench.add_bound(corr_bounds)

        # Set the local minimum in the bounds
        bench.add_minimum([0.42539], -0.07123, local=True)

        # Set the global minimum in the bounds
        bench.add_minimum([-1.1754], -1.0967, local=False)

        # Set local maxima in the bounds
        bench.add_maximum([0.0], 0.0, local=True)
        bench.add_maximum([1.0], 1.0, local=True)

        # Set global maximum in the bounds
        bench.add_maximum([-2.0], 4.0, local=False)

        # Test that the minima were set correctly
        self.assertAlmostEqual(bench.min, -1.0967, 4)
        self.assertEqual(bench.nmin, 1)
        self.assertEqual(len(bench.minima), 2)

        # Test that the maxima were set correctly
        self.assertAlmostEqual(bench.max, 4, 4)
        self.assertEqual(bench.nmax, 1)
        self.assertEqual(len(bench.maxima), 3)

        # Test that the extrema were aggregated correctly
        self.assertEqual(len(bench.extrema), 5)
        self.assertEqual(len(bench.global_extrema), 2)

        # Check boundary property
        self.assertEqual(bench.bounds, [corr_bounds])

    def test_no_extrema(self):
        bench = BenchmarkingFunction()

        self.assertIs(bench.min, None)
        self.assertIs(bench.max, None)
        self.assertEqual(bench.nmin, 0)
        self.assertEqual(bench.nmax, 0)
        self.assertEqual(len(bench.extrema), 0)
