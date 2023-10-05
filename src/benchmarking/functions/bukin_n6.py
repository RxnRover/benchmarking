import math
from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class BukinN6(BenchmarkingFunction):
    def __init__(self):
        super().__init__()

        self.set_function(bukin_n6)

        self.add_minimum([-10, 1], 0)

        self.add_bound([-15, -5])
        self.add_bound([-3, 3])


def bukin_n6(xs: List[float]) -> float:
    """Sixth Bukin function optimization test function.

    Sixth Bukin function from https://www.sfu.ca/~ssurjano/bukin6.html.

    Input domain: 2D rectangle x_1 = [-15, -5], x_2 = [-3, 3].

    Function in LaTeX format:
    f(x) = 100 \sqrt{|x_2 - 0.01 x_1^2|} + 0.01 |x_1 + 10|

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = 100 * math.sqrt(abs(xs[1] - 0.01 * xs[0] ** 2))
    term_2 = 0.01 * abs(xs[0] + 10)

    return term_1 + term_2


def bukin_n6_min() -> float:
    """Global minimum for the Sixth Bukin function.

    The global minimum is f(-10, 1) = 0.

    :return: Global minimum value.
    :rtype: float
    """

    return 0
