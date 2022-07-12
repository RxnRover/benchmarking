import numpy as np

def shekel(xs, m=10,
           C=np.array([[ 4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0 ],
                       [ 4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6 ],
                       [ 4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0 ],
                       [ 4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6 ]]),
           beta=[0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5]
):
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
            inner_sum += (xs[j] - C[j][i])**2 + beta[i]

        outer_sum += 1 / inner_sum

    return -outer_sum
