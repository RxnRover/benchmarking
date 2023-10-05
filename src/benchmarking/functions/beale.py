from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class Beale(BenchmarkingFunction):
    def __init__(self):
        super().__init__()

        self.set_function(beale)

        self.add_minimum([3, 0.5], 0)

        self.add_bound([-4.5, -4.5])
        self.add_bound([-4.5, -4.5])


def beale(xs: List[float]) -> float:
    """Beale optimization test function.

    Beale function from https://www.sfu.ca/~ssurjano/beale.html.

    Input domain: 2D square x_i = [-4.5, 4.5] for all i = 1, 2.

    Function in LaTeX format:
    f(x) = (1.5 - x_1 + x_1 x_2)^2 + (2.25 - x_1 + x_1 x_2^2)^2 +
           (2.625 - x_1 + x_1 x_2^3)^2

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = (1.5 - xs[0] + xs[0] * xs[1]) ** 2
    term_2 = (2.25 - xs[0] + xs[0] * xs[1] ** 2) ** 2
    term_3 = (2.625 - xs[0] + xs[0] * xs[1] ** 3) ** 2

    return term_1 + term_2 + term_3
