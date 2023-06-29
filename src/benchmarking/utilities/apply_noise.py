import numpy as np


def apply_noise(value, sigma, mean=0, variance=1):
    """Apply noise to the given function values.

    Applies noise of the form \sigma * N to the function value as

    f_bar(x) = f(x) + \sigma * N

    where N is a normally distributed random variable with (by default)
    mean = 0 and variance = 1. \sigma refers to the degree of
    perturbation of the value with \sigma = 0 representing the
    unperturbed problem.
    """

    return value + sigma * np.random.normal(mean, variance)
