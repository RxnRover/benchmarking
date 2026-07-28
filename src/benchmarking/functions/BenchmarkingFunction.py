from abc import ABC
from typing import Any, Callable, List, Optional

from benchmarking.functions.Optimum import Optimum


class BenchmarkingFunction(ABC):
    def __init__(self) -> None:
        self._minima: List[Optimum] = []
        self._global_minima: List[Optimum] = []
        self._maxima: List[Optimum] = []
        self._global_maxima: List[Optimum] = []
        self._bounds: List[List[float]] = []
        self._function: Optional[Callable] = None

    def __call__(self, xs: List[float]) -> float:
        if self._function is None:
            raise RuntimeError(
                "Function was not set the benchmarking function."
            )

        return self._function(xs)

    def set_function(self, foo: Callable) -> None:
        self._function = foo

    def add_minimum(
        self, inputs: List[float], outputs: float, local: bool = False
    ) -> None:
        minimum = Optimum(inputs, outputs)
        self._minima.append(minimum)

        if not local:
            self._global_minima.append(minimum)

    def add_maximum(
        self, inputs: List[float], outputs: float, local: bool = False
    ) -> None:
        maximum = Optimum(inputs, outputs)
        self._maxima.append(maximum)

        if not local:
            self._global_maxima.append(maximum)

    def add_bound(self, bound: List[float]) -> None:
        self._bounds.append(bound)

    @property
    def min(self) -> Optional[float]:
        """Get the value of the global minimum. Returns 'None' if there
        are no minima listed for the function.
        """

        if self.nmin == 0:
            return None

        return self.global_minima[0].value

    @property
    def max(self) -> Optional[float]:
        """Get the value of the global maximum. Returns 'None' if there
        are no maxima listed for the function.
        """

        if self.nmax == 0:
            return None

        return self.global_maxima[0].value

    @property
    def global_minima(self) -> List[Optimum]:
        """List of global minima."""
        return self._global_minima

    @property
    def minima(self) -> List[Optimum]:
        """List of all minima."""
        return self._minima

    @property
    def global_maxima(self) -> List[Optimum]:
        """List of global maxima."""
        return self._global_maxima

    @property
    def maxima(self) -> List[Optimum]:
        """List of all maxima."""
        return self._maxima

    @property
    def global_extrema(self) -> List[Optimum]:
        """List of global extrema."""
        return self.global_minima + self.global_maxima

    @property
    def extrema(self) -> List[Optimum]:
        """List of all extrema."""
        return self.minima + self.maxima

    @property
    def nmin(self) -> int:
        """Number of global minima."""
        return len(self.global_minima)

    @property
    def nmax(self) -> int:
        """Number of global maxima."""
        return len(self.global_maxima)

    @property
    def bounds(self) -> List[List[float]]:
        """Suggested boundaries to use."""
        return self._bounds

    @property
    def metadata(self) -> dict:
        """Dictionary containing metadata about benchmarking function."""

        metadata: dict[str, Any] = {}

        metadata["all_minima_count"] = len(self.minima)
        metadata["all_minima_values"] = [f.value for f in self.minima]
        metadata["all_minima_coordinates"] = [
            f.coordinates for f in self.minima
        ]

        metadata["global_minima_count"] = self.nmin
        metadata["global_minima_value"] = self.min
        metadata["global_minima_coordinates"] = [
            f.coordinates for f in self.global_minima
        ]

        metadata["all_maxima_count"] = len(self.maxima)
        metadata["all_maxima_values"] = [f.value for f in self.maxima]
        metadata["all_maxima_coordinates"] = [
            f.coordinates for f in self.maxima
        ]

        metadata["global_maxima_count"] = self.nmin
        metadata["global_maxima_value"] = self.max
        metadata["global_maxima_coordinates"] = [
            f.coordinates for f in self.global_maxima
        ]

        metadata["bounds"] = self.bounds

        return metadata
