import unittest

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class TestBenchmarkingFunction(unittest.TestCase):
    def test_creation(self):
        # 1D function with various global and local extrema
        def foo(x):
            return x**4 + x**3 - x**2

        corr_bounds = [-2.0, 1.0]

        corr_metadata = {
            "all_minima_count": 2,
            "all_minima_values": [-0.07123, -1.0967],
            "all_minima_coordinates": [[0.42539], [-1.1754]],
            "global_minima_count": 1,
            "global_minima_value": -1.0967,
            "global_minima_coordinates": [[-1.1754]],
            "all_maxima_count": 3,
            "all_maxima_values": [0.0, 1.0, 4.0],
            "all_maxima_coordinates": [[0.0], [1.0], [-2.0]],
            "global_maxima_count": 1,
            "global_maxima_value": 4.0,
            "global_maxima_coordinates": [[-2.0]],
            "bounds": [corr_bounds],
        }

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

        self.assertEqual(bench.metadata, corr_metadata)

    def test_no_extrema(self):
        bench = BenchmarkingFunction()

        corr_metadata = {
            "all_minima_count": 0,
            "all_minima_values": [],
            "all_minima_coordinates": [],
            "global_minima_count": 0,
            "global_minima_value": None,
            "global_minima_coordinates": [],
            "all_maxima_count": 0,
            "all_maxima_values": [],
            "all_maxima_coordinates": [],
            "global_maxima_count": 0,
            "global_maxima_value": None,
            "global_maxima_coordinates": [],
            "bounds": [],
        }

        self.assertIs(bench.min, None)
        self.assertIs(bench.max, None)
        self.assertEqual(bench.nmin, 0)
        self.assertEqual(bench.nmax, 0)
        self.assertEqual(len(bench.extrema), 0)
        self.assertEqual(bench.metadata, corr_metadata)
