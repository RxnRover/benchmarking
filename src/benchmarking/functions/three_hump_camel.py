from typing import List


def three_hump_camel(xs: List[float]) -> float:
    """Three-hump camel optimization test function.

    Three-hump camel function from https://www.sfu.ca/~ssurjano/camel3.html.

    Input domain: 2D square x_i = [-5, 5] for all i = 1, 2.

    Function in LaTeX format:
    f(x) = 2 x_1^2 - 1.05 x_1^4 + \dfrac{x_1^6}{6} + x_1 x_2 + x_2^2

    :param xs: Parameter list
    :type xs: float

    :return: Result of calculation
    :rtype: float
    """

    result = 2 * xs[0] ** 2
    result -= 1.05 * xs[0] ** 4
    result += xs[0] ** 6 / 6
    result += xs[0] * xs[1]
    result += xs[1] ** 2

    return result


def three_hump_camel_min() -> float:
    """Global minimum of the Three-Hump Camel function.

    Global minimum is f(0, 0) = 0.

    :return: Global minimum
    :rtype: float
    """

    return 0
