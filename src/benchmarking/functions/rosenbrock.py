from typing import List

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction


class Rosenbrock(BenchmarkingFunction):
    def __init__(self, dim: int = 4):
        super().__init__()

        self.set_function(rosenbrock)

        self.add_minimum([1] * dim, 0)

        for i in range(dim):
            self.add_bound([-5, 10])


def rosenbrock(xs: List[float]) -> float:
    """Rosenbrock nD optimization test function. Dimensions are inferred
    from the length of the input paremeter list, ``xs``.

    Rosenbrock nD function from https://www.sfu.ca/~ssurjano/rosen.html.

    Function in LaTeX format:
    f(x) = \sum_{i=1}^{d-1} [100(x_{i+1} - x_i^2)^2 + (x_i - 1)^2]

    :param xs: List of input parameters
    :type xs: List[float]
    :return: Result of calculation
    :rtype: float
    """

    dimension_count = len(xs)

    sum = 0
    for i in range(dimension_count - 1):
        term_1 = 100 * (xs[i + 1] - xs[i] ** 2) ** 2
        term_2 = (xs[i] - 1) ** 2
        sum += term_1 + term_2

    return sum


def rosenbrock_min() -> float:
    """Rosenbrock global minimum in n-dimensions.

    The global minimum is 0 when all inputs are 1.

    :return: Global minimum.
    :rtype: float
    """

    return 0
