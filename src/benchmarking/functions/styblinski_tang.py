from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class StyblinskiTang(BenchmarkingFunction):
    def __init__(self, dim: int = 4):
        super().__init__()

        self.set_function(styblinski_tang)

        # The global minimum is f(x*) = -39.16599 * d, for
        # x* = (-2.903534, ... , -2.903534).
        self.add_minimum([-2.903634] * dim, -39.16599 * dim)

        for _ in range(dim):
            self.add_bound([-5, 5])


def styblinski_tang(xs: List[float]) -> float:
    """Styblinski-Tang optimization test function.

    Styblinski-Tang function from https://www.sfu.ca/~ssurjano/stybtang.html.

    Input domain: Hypercube :math:`x_i = [-5, 5]` for all i=1, ..., d.

    Function in LaTeX format:

    .. math::

        f(x) = \\dfrac{1}{2} \\sum_{i = 1}^d (x_i^4 - 16 x_i^2 + 5 x_i)

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    result = 0.0

    for x in xs:
        result += x**4 - 16.0 * x**2 + 5.0 * x

    result *= 0.5

    return result
