import math
from typing import List


def schwefel(xs: List[float]) -> float:
    """Schwefel optimization test function.

    Schwefel function from https://www.sfu.ca/~ssurjano/schwef.html.

    Input domain: Hypercube x_i = [-500, 500], for all i=1, ..., d.

    Function in LaTeX format:
    f(x) = 418.9829 d - \sum_{i = 1}^d x_i \sin{(\sqrt{|x_i|})}

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    term_1 = 418.9829 * len(xs)

    term_2 = 0
    for x in xs:
        term_2 += x * math.sin(math.sqrt(abs(x)))

    return term_1 - term_2


def schwefel_min() -> float:
    """Global minimum for the Schwefel function.

    The global minimum is f(x*) = 0, at x* = (420.9687, ..., 420.9687).

    :return: Global minimum value.
    :rtype: float
    """

    return 0
