from abc import ABC
from typing import List

from benchmarking.functions.Optimum import Optimum


class BenchmarkingFunction(ABC):
    def __init__(self):
        self._minima = []
        self._bounds = []
        self._function = None

    def __call__(self, xs: List[float]) -> float:
        return self._function(xs)

    def set_function(self, foo):
        self._function = foo

    def add_minimum(self, inputs, outputs):
        minimum = Optimum(inputs, outputs)
        self._minima.append(minimum)

    def add_bound(self, bound):
        self._bounds.append(bound)

    @property
    def min(self):
        """Get the value of the global minimum. Returns 'None' if there
        are no minima listed for the function.
        """

        if self.nmin == 0:
            return None

        return self.minima[0].value()

    @property
    def minima(self):
        """List of global minima."""
        return self._minima

    @property
    def nmin(self):
        """Number of global minima."""
        return len(self._minima)

    @property
    def bounds(self):
        """Suggested boundaries to use."""
        return self._bounds
