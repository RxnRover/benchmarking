def rosenbrock(xs):
    """Rosenbrock nD optimization test function.

    Rosenbrock nD function from https://www.sfu.ca/~ssurjano/rosen.html.

    Function in LaTeX format:
    f(x) = \sum_{i=1}^{d-1} [100(x_{i+1} - x_i^2)^2 + (x_i - 1)^2]
    """

    dimensionCount = len(xs)

    sum = 0
    for i in range(dimensionCount - 1):
        term_1 = 100 * (xs[i+1] - xs[i]**2)**2
        term_2 = (xs[i] - 1)**2
        sum += term_1 + term_2

    return sum

def rosenbrock_min() -> float:
    """Rosenbrock global minimum in n-dimensions.

    The global minimum is 0 when all inputs are 1.

    :return: Global minimum.
    :rtype: float
    """

    return 0
