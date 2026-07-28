import numpy as np


def apply_noise(
    value: float, sigma: float, mean: float = 0, variance: float = 1
) -> float:
    """Apply noise to the given function values.

    Applies noise of the form :math:`\\sigma * N` to the function value as

    .. math::

        f_bar(x) = f(x) + \\sigma * N

    where N is a normally distributed random variable with (by default)
    mean = 0 and variance = 1. :math:`\\sigma` refers to the degree of
    perturbation of the value with :math:`\\sigma = 0` representing the
    unperturbed problem.
    """

    return value + sigma * np.random.normal(mean, variance)
