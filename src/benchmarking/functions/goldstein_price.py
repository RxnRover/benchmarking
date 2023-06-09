from typing import List


def goldstein_price(xs: List[float]) -> float:
    """Goldstein-Price optimization test function.

    Goldstein-Price function from https://www.sfu.ca/~ssurjano/goldpr.html.

    Function in LaTeX format:
    f(x) = [1 + (x_1 + x_2 + 1)^2 (19 - 14 x_1 + 3 x_1^2 - 14 x_2 + 6 x_1 x_2 + 3 x_2^2)]
           \times [30 + (2 x_1 - 3 x_2)^2 (18 - 32 x_1 + 12 x_1^2 + 48 x_2 - 36 x_1 x_2 + 27 x_2^2)]

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = (xs[0] + xs[1] + 1)**2
    term_1 *= 19 - 14 * xs[0] + 3 * xs[0]**2 - 14 * xs[1] + 6 * xs[0] * xs[1] + 3 * xs[1]**2
    term_1 += 1

    term_2 = (2 * xs[0] - 3 * xs[1])**2
    term_2 *= 18 - 32 * xs[0] + 12 * xs[0]**2 + 48 * xs[1] - 36 * xs[0] * xs[1] + 27 * xs[1]**2
    term_2 += 30

    return term_1 * term_2


def goldstein_price_min() -> float:
    """Global minimum for the Goldstein-Price function.

    The global minimum is f(0, -1) = 3.

    :return: Global minimum value.
    :rtype: float
    """

    return 3
