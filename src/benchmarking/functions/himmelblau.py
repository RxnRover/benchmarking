from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class Himmelblau(BenchmarkingFunction):
    def __init__(self):
        super().__init__()

        self.set_function(himmelblau)

        self.add_minimum([3.0, 2.0], 0.0)
        self.add_minimum([-2.805118, 3.131312], 0.0)
        self.add_minimum([-3.779310, -3.283186], 0.0)
        self.add_minimum([3.584428, -1.848126], 0.0)

        self.add_maximum([-0.270845, -0.923039], 181.617)

        # Recommended bounds from Supplemental Information in:
        # S. Soritz, D. Moser, and H. Gruber-Wölfler, “Comparison of
        #     Derivative-Free Algorithms for their Applicability in
        #     Self-Optimization of Chemical Processes,” Chemistry–Methods,
        #     vol. 2, no. 5, p. e202100091, 2022,
        #     doi: 10.1002/cmtd.202100091.
        for _ in range(2):
            self.add_bound([-5, 5])


def himmelblau(xs: List[float]) -> float:
    """Himmelblau's optimization test function.

    Himmelblau's function from
    https://en.wikipedia.org/wiki/Himmelblau's_function.

    Input domain: Unknown.

    Function in LaTeX format:
    f(x) = (x_1^2 + x_2 - 11)^2 + (x_1 + x_2^2 - 7)^2

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = (xs[0] ** 2 + xs[1] - 11) ** 2
    term_2 = (xs[0] + xs[1] ** 2 - 7) ** 2

    return term_1 + term_2


def himmelblau_max() -> float:
    """Global maximum for Himmelblau's function.

    The global maximum is f(-0.270845, -0.923039) = 181.617.

    :return: Global maximum value.
    :rtype: float
    """

    return 181.617


def himmelblau_min() -> float:
    """Global minima for Himmelblau's function.

    There are four local minima which all yield a value of zero. These are:
    - f(3, 2) = 0.
    - f(-2.805118, 3.131312) = 0.
    - f(-3.779310, -3.283186) = 0.
    - f(3.584428, -1.848126) = 0.

    :return: Global minimum value.
    :rtype: float
    """

    return 0
