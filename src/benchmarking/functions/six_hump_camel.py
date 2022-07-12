def six_hump_camel(x_1: float, x_2: float) -> float:
    """Six-hump camel optimization test function.

    Six-hump camel function from https://www.sfu.ca/~ssurjano/camel6.html.

    Function in LaTeX format:
    f(x) = (4 - 2.1 x_1^2 + \frac{x_1^4}{3}) x_1^2 + x_1 x_2 + (-4 + 4 x_2^2) x_2^2

    :param x_1: First parameter, 'x_1'
    :type x_1: float
    :param x_2: Second parameter, 'x_2'
    :type x_2: float

    :return: Result of calculation
    :rtype: float
    """

    term_1 = (4 - 2.1 * x_1**2 + x_1**4 / 3) * x_1**2
    term_2 = x_1 * x_2
    term_3 = (-4 + 4 * x_2**2) * x_2**2

    return term_1 + term_2 + term_3

def six_hump_camel_min() -> float:
    """Global minimum of the Six-Hump Camel function.

    Global minimum is -1.0316 at (0.0898, -0.7126) and (-0.0898, 0.7126).
    
    :return: Global minimum
    :rtype: float
    """ 
    
    return -1.0316
