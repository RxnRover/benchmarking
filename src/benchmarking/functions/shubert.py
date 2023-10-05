from typing import List

import numpy as np

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class Shubert(BenchmarkingFunction):
    """Shubert Function

    Source: https://www.sfu.ca/~ssurjano/shubert.html
    """

    def __init__(self):
        super().__init__()

        self.set_function(shubert)

        # Global minimum is -186.7309 at ???.
        # This minimum point was found through manual optimization and is
        # an approximation
        self.add_minimum([-1.4251, -0.8004], -186.7309)

        for _ in range(2):
            self.add_bound([-5.12, 5.12])


def shubert(xs: List[float]) -> float:
    """Shubert optimization test function.

    Shubert function from https://www.sfu.ca/~ssurjano/shubert.html.

    Function in LaTeX format:
    f(x) = \big(\sum_{i=5}^5 i cos((i + 1)x_1 + i)\big) \times
           \big(\sum_{i=5}^5 i cos((i + 1)x_2 + i)\big)

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = 0
    term_2 = 0

    for i in range(1, 6):
        term_1 += i * np.cos((i + 1) * xs[0] + i)
        term_2 += i * np.cos((i + 1) * xs[1] + i)

    return term_1 * term_2


def shubert_min() -> float:
    """Global minimum for the Shubert function.

    Global minimum is -186.7309 at ???.

    :return: Global minimum.
    :rtype: float
    """

    return -186.7309
