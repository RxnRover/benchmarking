import numpy as np

def branin(x, a=1, b=5.1/(4*np.pi**2), c=5/np.pi, r=6, s=10, t=1/(8*np.pi)):
    """Branin, or Branin-Hoo, optimization test function.

    Branin function with (by default) values of a, b, c, r, s, t:
    a = 1, b = 5.1 / (4 * pi^2), c = 5 / pi, r = 6, s = 10 and t = 1 / (8 * pi)
    from https://www.sfu.ca/~ssurjano/branin.html.

    Function in LaTeX format:
    f(x) = a(x_2 - bx_1^2 + cx_1 - r)^2 + s(1-t)cos(x_1) + s
    """

    term_1 = a * (x[1] - b * x[0]**2 + c * x[0] - r)**2
    term_2 = s * (1 - t) * np.cos(x[0])
    
    return term_1 + term_2 + s

def branin_min() -> float:
    """Branin function global minimum value.

    Global minimum of 0.397887 is found at (-pi, 12.275), (pi, 2.275) and
    (9.42478, 2.475).

    :return: Global minimum.
    :rtype: float
    """

    return 0.397887
