import math
from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class HolderTable(BenchmarkingFunction):
    def __init__(self):
        super().__init__()

        self.set_function(holder_table)

        # The global minima are:
        # - f(8.05502, 9.66459) = -19.2085.
        # - f(8.05502, -9.66459) = -19.2085.
        # - f(-8.05502, 9.66459) = -19.2085.
        # - f(-8.05502, -9.66459) = -19.2085.
        self.add_minimum([8.05502, 9.66459], -19.2085)
        self.add_minimum([8.05502, -9.66459], -19.2085)
        self.add_minimum([-8.05502, 9.66459], -19.2085)
        self.add_minimum([-8.05502, -9.66459], -19.2085)

        for _ in range(2):
            self.add_bound([-10, 10])


def holder_table(xs: List[float]) -> float:
    """Holder Table function optimization test function.

    Holder Table function from https://www.sfu.ca/~ssurjano/holder.html.

    Input domain: 2D square x_i = [-10, 10] for all i = 1, 2.

    Function in LaTeX format:
    f(x) = -|\sin{(x_1)} \cos{(x_2)}
             \exp{(|1 - \frac{\sqrt{x_1^2 + x_2^2}}{\pi}|)}|

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    result = math.sin(xs[0]) * math.cos(xs[1])
    result *= math.exp(abs(1 - math.sqrt(xs[0] ** 2 + xs[1] ** 2) / math.pi))

    return -abs(result)
