import numpy as np


def generate_box(bounds, numPoints):
    """Generate a box with the given bounds.

    Bounds must be given as a Python 2D list of shape n x 2, where n
    is the number of dimensions of the box, the first column is the
    lower bound, and the second column is the upper bound.
    """

    box = []
    for bound in bounds:
        # Generate the range at the given step size
        box.append(
            np.linspace(bound[0], bound[1], num=numPoints, endpoint=True)
        )

    return box
