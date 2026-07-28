from typing import List

import numpy as np

from benchmarking.functions.BenchmarkingFunction import BenchmarkingFunction

supported_dimensions = [3, 6]


class Hartmann3D(BenchmarkingFunction):
    """Hartmann 3-Dimensional Function

    Source: https://www.sfu.ca/~ssurjano/hart3.html
    """

    def __init__(self) -> None:
        super().__init__()

        self.set_function(hartmann)

        # The global minimum is -3.86278 at (0.114614, 0.555649, 0.852547).
        self.add_minimum([0.114614, 0.555649, 0.852547], -3.86278)

        for i in range(3):
            self.add_bound([0, 1])

    def __call__(
        self,
        xs: List[float],
    ) -> float:
        if self._function is None:
            raise RuntimeError(
                "Function was not set the benchmarking function."
            )

        alpha = np.array([1.0, 1.2, 3.0, 3.2])

        A = np.array(
            [[3.0, 10, 30], [0.1, 10, 35], [3.0, 10, 30], [0.1, 10, 35]]
        )

        P = 10 ** (-4) * np.array(
            [
                [3689, 1170, 2673],
                [4699, 4387, 7470],
                [1091, 8732, 5547],
                [381, 5743, 8828],
            ]
        )

        return self._function(xs, alpha, A, P)


class Hartmann6D(BenchmarkingFunction):
    """Hartmann 6-Dimensional Function

    Source: https://www.sfu.ca/~ssurjano/hart6.html
    """

    def __init__(self) -> None:
        super().__init__()

        self.set_function(hartmann)

        # The global minimum is -3.32237 at
        # (0.20169, 0.150011, 0.476874, 0.275332, 0.311652, 0.6573).
        self.add_minimum(
            [0.20169, 0.150011, 0.476874, 0.275332, 0.311652, 0.6573], -3.32237
        )

        for i in range(6):
            self.add_bound([0, 1])

    def __call__(
        self,
        xs: List[float],
    ) -> float:
        if self._function is None:
            raise RuntimeError(
                "Function was not set the benchmarking function."
            )

        alpha = np.array([1.0, 1.2, 3.0, 3.2])

        A = np.array(
            [
                [10, 3, 17, 3.50, 1.7, 8],
                [0.05, 10, 17, 0.1, 8, 14],
                [3, 3.5, 1.7, 10, 17, 8],
                [17, 8, 0.05, 10, 0.1, 14],
            ]
        )

        P = 10 ** (-4) * np.array(
            [
                [1312, 1696, 5569, 124, 8283, 5886],
                [2329, 4135, 8307, 3736, 1004, 9991],
                [2348, 1451, 3522, 2883, 3047, 6650],
                [4047, 8828, 8732, 5743, 1091, 381],
            ]
        )

        return self._function(xs, alpha, A, P)


def hartmann(
    xs: List[float],
    alpha: np.ndarray = None,
    A: np.ndarray = None,
    P: np.ndarray = None,
) -> float:
    """Hartmann n-Dimensional optimization test function. This function
    supports 3 or 6 dimensions, and dimensions are inferred by the length
    of the ``xs`` parameter list.

    Hartmann nD function with (by default) values of :math:`\\alpha`, A, and P
    from https://www.sfu.ca/~ssurjano/hart3.html.

    Function in LaTeX format:

    .. math::

        f(x) = -\\sum_{i=1}^{4} \\alpha_i
               \\exp{\\bigg(-\\sum_{j=1}^n A_{ij}(x_j - P_{ij})^2\\bigg)}

    :param xs: Input parameters
    :type xs: List[float]
    :param alpha: Alpha array, leave as 'None' to get default for given
                  dimension count, defaults to None
    :type alpha: np.ndarray, optional
    :param A: 'A' array, leave as 'None' to get default for given dimension
              count, defaults to None
    :type A: np.ndarray, optional
    :param P: 'P' array, leave as 'None' to get default for given dimension
              count, defaults to None
    :type P: np.ndarray, optional

    :raises ValueError: Invalid dimension count.

    :return: Result of calculation.
    :rtype: float
    """

    # Validate parameters and set proper default
    dimension_count = len(xs)

    # Check dimension count
    if dimension_count not in supported_dimensions:
        raise ValueError("Invalid dimension count.")

    # Check for provided alpha value
    if alpha is None:
        if dimension_count == 3 or dimension_count == 6:
            alpha = np.array([1.0, 1.2, 3.0, 3.2])

    # Check for provided A values
    if A is None:
        if dimension_count == 3:
            A = np.array(
                [[3.0, 10, 30], [0.1, 10, 35], [3.0, 10, 30], [0.1, 10, 35]]
            )
        elif dimension_count == 6:
            A = np.array(
                [
                    [10, 3, 17, 3.50, 1.7, 8],
                    [0.05, 10, 17, 0.1, 8, 14],
                    [3, 3.5, 1.7, 10, 17, 8],
                    [17, 8, 0.05, 10, 0.1, 14],
                ]
            )

    # Check for provided P values
    if P is None:
        if dimension_count == 3:
            P = 10 ** (-4) * np.array(
                [
                    [3689, 1170, 2673],
                    [4699, 4387, 7470],
                    [1091, 8732, 5547],
                    [381, 5743, 8828],
                ]
            )
        elif dimension_count == 6:
            P = 10 ** (-4) * np.array(
                [
                    [1312, 1696, 5569, 124, 8283, 5886],
                    [2329, 4135, 8307, 3736, 1004, 9991],
                    [2348, 1451, 3522, 2883, 3047, 6650],
                    [4047, 8828, 8732, 5743, 1091, 381],
                ]
            )

    # Start the outer sum at zero
    outer_sum = 0

    # Perform the outer sum
    for i in range(4):
        # Start the inner sum at zero
        inner_sum = 0

        # Perform the inner sum
        for j in range(dimension_count):
            inner_sum += A[i][j] * np.square(xs[j] - P[i][j])

        outer_sum += alpha[i] * np.exp(-inner_sum)

    return -outer_sum
