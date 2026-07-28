from typing import List

import numpy as np

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class Branin(BenchmarkingFunction):
    def __init__(self) -> None:
        super().__init__()

        self.set_function(branin)

        # Global minimum of 0.397887 is found at (-pi, 12.275), (pi, 2.275) and
        # (9.42478, 2.475).
        self.add_minimum([-np.pi, 12.275], 0.397887)
        self.add_minimum([np.pi, 2.275], 0.397887)
        self.add_minimum([9.42478, 2.475], 0.397887)

        self.add_bound([-5, 10])
        self.add_bound([0, 15])


def branin(
    xs: List[float],
    a: float = 1,
    b: float = 5.1 / (4 * np.pi**2),
    c: float = 5 / np.pi,
    r: float = 6,
    s: float = 10,
    t: float = 1 / (8 * np.pi),
) -> float:
    """Branin, or Branin-Hoo, optimization test function.

    Branin function with (by default) values of a, b, c, r, s, t:
    a = 1, b = 5.1 / (4 * pi^2), c = 5 / pi, r = 6, s = 10 and t = 1 / (8 * pi)
    from https://www.sfu.ca/~ssurjano/branin.html.

    Function in LaTeX format:

    .. math::

        f(x) = a(x_2 - bx_1^2 + cx_1 - r)^2 + s(1-t)cos(x_1) + s

    :param xs: Input 'x' values.
    :type xs: List[float]
    :param a: 'a' parameter, defaults to 1
    :type a: float, optional
    :param b: 'b' parameter, defaults to 5.1/(4 * np.pi**2)
    :type b: float, optional
    :param c: 'c' parameter, defaults to 5/np.pi
    :type c: float, optional
    :param r: 'r' parameter, defaults to 6
    :type r: float, optional
    :param s: 's' parameter, defaults to 10
    :type s: float, optional
    :param t: 't' parameter, defaults to 1/(8 * np.pi)
    :type t: float, optional

    :return: Result of calculation.
    :rtype: float
    """

    term_1 = a * (xs[1] - b * xs[0] ** 2 + c * xs[0] - r) ** 2
    term_2 = s * (1 - t) * np.cos(xs[0])

    return term_1 + term_2 + s
