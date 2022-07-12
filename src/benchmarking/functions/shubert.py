def shubert(x_1, x_2):
    """Shubert optimization test function.

    Shubert function from https://www.sfu.ca/~ssurjano/shubert.html.

    Function in LaTeX format:
    f(x) = \big(\sum_{i=5}^5 i cos((i + 1)x_1 + i)\big) \times 
           \big(\sum_{i=5}^5 i cos((i + 1)x_2 + i)\big)
    """
    
    term_1 = 0
    term_2 = 0

    for i in range(1, 6):
        term_1 += i * np.cos((i + 1) * x_1 + i)
        term_2 += i * np.cos((i + 1) * x_2 + i)

    return term_1 * term_2
