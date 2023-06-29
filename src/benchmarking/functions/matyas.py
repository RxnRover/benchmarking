from typing import List


def matyas(xs: List[float]) -> float:
    """Matyas optimization test function.

    Matyas function from https://www.sfu.ca/~ssurjano/matya.html.

    Input domain: 2D square with bounds [-10, 10].

    Function in LaTeX format:
    f(x) = 0.26 (x_1^2 + x_2^2) - 0.48 x_1 x_2

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = 0.26 * (xs[0] ** 2 + xs[1] ** 2)
    term_2 = 0.48 * xs[0] * xs[1]

    return term_1 - term_2


def matyas_min() -> float:
    """Global minimum for the Matyas function.

    The global minimum is f(0, 0) = 0.

    :return: Global minimum value.
    :rtype: float
    """

    return 0
