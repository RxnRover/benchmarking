import math
from typing import List


def eggholder(xs: List[float]) -> float:
    """Eggholder function optimization test function.

    Eggholder function from https://www.sfu.ca/~ssurjano/egg.html.

    Input domain: 2D square x_i = [-512, 512] for all i = 1, 2.

    Function in LaTeX format:
    f(x) = -(x_2 + 47) \sin{(\sqrt{|x_2 + \dfrac{x_1}{2} + 47|})} -
           x_1 \sin{(\sqrt{|x_1 - (x_2 + 47)|})}

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = -(xs[1] + 47) * math.sin(math.sqrt(abs(xs[1] + xs[0] / 2 + 47)))
    term_2 = xs[0] * math.sin(math.sqrt(abs(xs[0] - (xs[1] + 47))))

    return term_1 - term_2


def eggholder_min() -> float:
    """Global minimum for the Eggholder function.

    The global minimum is f(512, 404.2319) = -959.6407.

    :return: Global minimum value.
    :rtype: float
    """

    return -959.6407
