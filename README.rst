.. image:: https://img.shields.io/badge/Documentation-grey
    :alt: Documentation link
    :target: https://rxnrover.github.io/benchmarking/

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

########################
 benchmarking functions
########################

    A collection of benchmarking functions for use with optimization algorithms.

This package provides a collection of standard test functions used to benchmark
the performance of optimization algorithms. Each function exposes its callable
form along with metadata such as its known global (and, where applicable, local)
minima/maxima and suggested input bounds, making it easy to score an optimizer's
results against ground truth.

The original 10 functions (Branin, Goldstein-Price, Hartmann 3D, Hartmann 6D,
Rosenbrock, Shekel 5, Shekel 7, Shekel 10, Shubert, and Six-Hump Camel) match
the set used to benchmark the CyRxnOpt optimizer and are the same functions used
in the SNOBFIT paper for its own benchmarking.

This repository is intended to grow beyond that original set of 10 test
problems. It currently also includes Beale, Booth, Bukin N.6, Eggholder,
Himmelblau, Holder Table, Matyas, Schwefel, Sphere, Styblinski-Tang, and
Three-Hump Camel, with more functions expected to be added over time.

**************
 Installation
**************

Clone the repository and install it with pip:

.. code-block:: bash

    git clone https://github.com/RxnRover/benchmarking.git
    cd benchmarking
    pip install .

*******
 Usage
*******

Each benchmarking function is implemented as a class that can be called directly
with a list of input coordinates. For example, to evaluate the Branin function
and inspect its metadata:

.. code-block:: python

    from benchmarking.functions.branin import Branin

    branin = Branin()

    # Evaluate the function at a point.
    result = branin([-3.14, 12.275])

    # Metadata about the function: known minima/maxima, bounds, etc.
    print(branin.metadata)

    # Convenience accessors are also available.
    print(branin.min)  # value of the global minimum
    print(branin.bounds)  # suggested input bounds

Functions can also be looked up by name, which is useful when the specific
function to benchmark against is chosen dynamically (e.g. from a config file or
command-line argument):

.. code-block:: python

    from benchmarking.evaluate import evaluate
    from benchmarking.function_data import function_data

    result = evaluate("branin", [-3.14, 12.275])
    metadata = function_data("branin")

The full list of valid function names is available in
``benchmarking.function_ids.function_ids``.

*******************************
 Making Changes & Contributing
*******************************

This project uses pre-commit_, please make sure to install it before making any
changes:

.. code-block:: bash

    # After cloning the repository
    pip install pre-commit
    cd benchmarking
    pre-commit install

.. _pre-commit: https://pre-commit.com/
