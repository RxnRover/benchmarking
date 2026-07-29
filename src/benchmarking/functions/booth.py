from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class Booth(BenchmarkingFunction):
    def __init__(self) -> None:
        super().__init__()

        self.set_function(booth)

        # The global minimum is f(1, 3) = 0.
        self.add_minimum([1, 3], 0.0)

        for _ in range(2):
            self.add_bound([-10, 10])


def booth(xs: List[float]) -> float:
    """Booth optimization test function.

    Booth function from https://www.sfu.ca/~ssurjano/booth.html.

    Input domain: 2D square with bounds [-10, 10].

    Function in LaTeX format:

    .. math::

        f(x) = (x_1 + 2x_2 - 7)^2 + (2x_1 + x_2 - 5)^2

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = (xs[0] + 2 * xs[1] - 7) ** 2
    term_2 = (2 * xs[0] + xs[1] - 5) ** 2

    return term_1 + term_2
