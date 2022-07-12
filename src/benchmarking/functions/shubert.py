import numpy as np

def shubert(x_1: float, x_2: float) -> float:
    """Shubert optimization test function.

    Shubert function from https://www.sfu.ca/~ssurjano/shubert.html.

    Function in LaTeX format:
    f(x) = \big(\sum_{i=5}^5 i cos((i + 1)x_1 + i)\big) \times 
           \big(\sum_{i=5}^5 i cos((i + 1)x_2 + i)\big)

    :param x_1: First parameter, 'x_1'
    :type x_1: float
    :param x_2: Second parameter, 'x_2'
    :type x_2: float

    :return: Result of calculation
    :rtype: float
    """
    
    term_1 = 0
    term_2 = 0

    for i in range(1, 6):
        term_1 += i * np.cos((i + 1) * x_1 + i)
        term_2 += i * np.cos((i + 1) * x_2 + i)

    return term_1 * term_2

def shubert_min() -> float:
    """Global minimum for the Shubert function.

    Global minimum is -186.7309 at ???.

    :return: Global minimum.
    :rtype: float
    """

    return -186.7309
