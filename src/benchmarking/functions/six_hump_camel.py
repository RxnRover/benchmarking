def six_hump_camel(x_1, x_2):
    """Six-hump camel optimization test function.

    Six-hump camel function from https://www.sfu.ca/~ssurjano/camel6.html.

    Function in LaTeX format:
    f(x) = (4 - 2.1 x_1^2 + \frac{x_1^4}{3}) x_1^2 + x_1 x_2 + (-4 + 4 x_2^2) x_2^2"""

    term_1 = (4 - 2.1 * x_1**2 + x_1**4 / 3) * x_1**2
    term_2 = x_1 * x_2
    term_3 = (-4 + 4 * x_2**2) * x_2**2

    return term_1 + term_2 + term_3
