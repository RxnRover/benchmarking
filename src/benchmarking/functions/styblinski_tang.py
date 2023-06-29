from typing import List


def styblinski_tang(xs: List[float]) -> float:
    """Styblinski-Tang optimization test function.

    Styblinski-Tang function from https://www.sfu.ca/~ssurjano/stybtang.html.

    Input domain: Hypercube x_i = [-5, 5] for all i=1, ..., d.

    Function in LaTeX format:
    f(x) = \dfrac{1}{2} \sum_{i = 1}^d (x_i^4 - 16 x_i^2 + 5 x_i)

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    result = 0

    for x in xs:
        result += x**4 - 16 * x**2 + 5 * x

    result *= 0.5

    return result


def styblinski_tang_min(dim: int = 2) -> float:
    """Global minimum for the Styblinski-Tang function.

    The global minimum is f(x*) = -39.16599 * d.

    :param dim: Number of dimensions, as the minimum value is dependent on this
                value. Defaults to 2 dimensions.
    :type dim: int, optional

    :return: Global minimum value.
    :rtype: float
    """

    return -39.16599 * dim
