from typing import List


class Optimum:
    def __init__(self, coordinates: List[float], value: float) -> None:
        self._coordinates = coordinates
        self._value = value

    def __str__(self) -> str:
        msg = "{}: {}".format(self.coordinates, self.value)

        return msg

    @property
    def coordinates(self) -> List[float]:
        """Coordinates of the optimum."""
        return self._coordinates

    @property
    def ndim(self) -> int:
        """Number of dimensions (length of coordinates)."""

        return len(self._coordinates)

    @property
    def value(self) -> float:
        """Value of the optimum."""

        return self._value
