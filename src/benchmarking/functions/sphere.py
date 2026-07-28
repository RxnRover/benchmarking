from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class Sphere(BenchmarkingFunction):
    def __init__(self, dim: int = 4):
        super().__init__()

        self.set_function(sphere)

        # The global minimum is f(x*) = 0, at x* = (0, ..., 0).
        self.add_minimum([0.0] * dim, 0.0)

        for _ in range(dim):
            self.add_bound([-10, 10])


def sphere(xs: List[float]) -> float:
    """Sphere optimization test function.

    Sphere function from https://www.sfu.ca/~ssurjano/spheref.html.

    Input domain: Hypercube :math:`x_i = [-5.12, 5.12]` for all i=1, ..., d.

    Function in LaTeX format:

    .. math::

        f(x) = \\sum_{i=1}^d x_i^2

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    result = 0.0

    for x in xs:
        result += x**2

    return result
