from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class SixHumpCamel(BenchmarkingFunction):
    def __init__(self) -> None:
        super().__init__()

        self.set_function(six_hump_camel)

        # Global minimum is -1.0316 at (0.0898, -0.7126) and (-0.0898, 0.7126).
        self.add_minimum([0.0898, -0.7126], -1.0316)
        self.add_minimum([-0.0898, 0.7126], -1.0316)

        self.add_bound([-3, 3])
        self.add_bound([-2, 2])


def six_hump_camel(xs: List[float]) -> float:
    """Six-hump camel optimization test function.

    Six-hump camel function from https://www.sfu.ca/~ssurjano/camel6.html.

    Function in LaTeX format:

    .. math::

        f(x) = (4 - 2.1 x_1^2 + \\frac{x_1^4}{3}) x_1^2 + x_1 x_2 +
               (-4 + 4 x_2^2) x_2^2

    :param xs: Parameter list
    :type xs: float

    :return: Result of calculation
    :rtype: float
    """

    term_1 = (4 - 2.1 * xs[0] ** 2 + xs[0] ** 4 / 3) * xs[0] ** 2
    term_2 = xs[0] * xs[1]
    term_3 = (-4 + 4 * xs[1] ** 2) * xs[1] ** 2

    return term_1 + term_2 + term_3
