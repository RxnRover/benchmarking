from typing import List

import numpy as np


def shekel(xs: List[float],
           m: int = 10,
           C: np.ndarray = np.array(
               [[4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0],
                [4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6],
                [4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0],
                [4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6]]),
           beta: List[float] = [
               0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5
           ]):
    """Sheckel 4D optimization test function.

    Sheckel 4D function with (by default) values of \beta and C
    from https://www.sfu.ca/~ssurjano/shekel.html. Does not support
    m > 10 without a new C provided.

    Function in LaTeX format:
    f(x) = -\sum_{i=1}^m \bigg(\sum_{j=1}^4(x_j - C_{ji})^2 + \beta_i\bigg)^-1
    """

    outer_sum = 0

    for i in range(m):
        inner_sum = 0

        for j in range(4):
            inner_sum += (xs[j] - C[j][i])**2

        outer_sum += 1 / (inner_sum + beta[i])

    return -outer_sum


def shekel_min(m: int = 10) -> float:
    """Shekel function global minimum. This function only supports 'm' values
    of 5, 7, or 10.

    Global minimum at

    * m = 5 is -10.1532 for (4, 4, 4, 4)
    * m = 7 is -10.4029 for (4, 4, 4, 4)
    * m = 10 is -10.5364 for (4, 4, 4, 4)

    :param m: _description_, defaults to 10
    :type m: int, optional
    :raises ValueError: _description_
    :return: _description_
    :rtype: float
    """

    if (m == 5):
        return -10.1532
    elif (m == 7):
        return -10.4029
    elif (m == 10):
        return -10.5364
    else:
        raise ValueError("Invalid 'm' value.")
