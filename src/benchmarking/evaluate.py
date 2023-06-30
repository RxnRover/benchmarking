from benchmarking.functions.beale import beale
from benchmarking.functions.booth import booth
from benchmarking.functions.branin import branin
from benchmarking.functions.bukin_n6 import bukin_n6
from benchmarking.functions.eggholder import eggholder
from benchmarking.functions.goldstein_price import goldstein_price
from benchmarking.functions.hartmann import hartmann
from benchmarking.functions.himmelblau import himmelblau
from benchmarking.functions.holder_table import holder_table
from benchmarking.functions.matyas import matyas
from benchmarking.functions.rosenbrock import rosenbrock
from benchmarking.functions.schwefel import schwefel
from benchmarking.functions.shekel import shekel
from benchmarking.functions.shubert import shubert
from benchmarking.functions.six_hump_camel import six_hump_camel
from benchmarking.functions.sphere import sphere
from benchmarking.functions.styblinski_tang import styblinski_tang
from benchmarking.functions.three_hump_camel import three_hump_camel


def evaluate(function_name: str, *args, **kwargs):
    """Helper function to evaluate different benchmarking functions given
    the function name. This helps to not have to put this large if-elif
    statement everywhere that multiple functions are possible.

    :param function_name: Name of the function to use. This must exactly match
                          the actual function name.
    :type function_name: str
    :param \*args: Positional arguments to be passed to the benchmarking
                   function.
    :param \*\*kwargs: Keyword arguments to be passed to the benchmarking
                       function.

    :raises ValueError: Invalid function name was provided.
    """

    if "beale" in function_name:
        result = beale(*args, **kwargs)
    elif "booth" in function_name:
        result = booth(*args, **kwargs)
    elif "branin" in function_name:
        result = branin(*args, **kwargs)
    elif "bukin_n6" in function_name:
        result = bukin_n6(*args, **kwargs)
    elif "eggholder" in function_name:
        result = eggholder(*args, **kwargs)
    elif "goldstein_price" in function_name:
        result = goldstein_price(*args, **kwargs)
    elif "hartmann" in function_name:
        result = hartmann(*args, **kwargs)
    elif "himmelblau" in function_name:
        result = himmelblau(*args, **kwargs)
    elif "holder_table" in function_name:
        result = holder_table(*args, **kwargs)
    elif "matyas" in function_name:
        result = matyas(*args, **kwargs)
    elif "rosenbrock" in function_name:
        result = rosenbrock(*args, **kwargs)
    elif "schwefel" in function_name:
        result = schwefel(*args, **kwargs)
    elif "shekel" in function_name:
        result = shekel(*args, **kwargs)
    elif "shubert" in function_name:
        result = shubert(*args, **kwargs)
    elif "six_hump_camel" in function_name:
        result = six_hump_camel(*args, **kwargs)
    elif "sphere" in function_name:
        result = sphere(*args, **kwargs)
    elif "styblinski_tang" in function_name:
        result = styblinski_tang(*args, **kwargs)
    elif "three_hump_camel" in function_name:
        result = three_hump_camel(*args, **kwargs)
    else:
        raise ValueError(
            "Invalid function name given: {}.".format(function_name)
        )

    return result
