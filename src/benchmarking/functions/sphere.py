from typing import List


def sphere(xs: List[float]) -> float:
    """Sphere optimization test function.

    Sphere function from https://www.sfu.ca/~ssurjano/spheref.html.

    Input domain: Hypercube x_i = [-5.12, 5.12] for all i=1, ..., d.

    Function in LaTeX format:
    f(x) = \sum_{i=1}^d x_i^2

    :param xs: Parameter list
    :type xs: List[float]

    :return: Result of calculation
    :rtype: float
    """

    result = 0

    for x in xs:
        result += x**2

    return result


def sphere_min() -> float:
    """Global minimum for the Sphere function.

    The global minimum is f(x*) = 0, at x* = (0, ..., 0).

    :return: Global minimum value.
    :rtype: float
    """

    return 0
