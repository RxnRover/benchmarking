from benchmarking.functions.beale import Beale
from benchmarking.functions.booth import Booth
from benchmarking.functions.branin import Branin
from benchmarking.functions.bukin_n6 import BukinN6
from benchmarking.functions.eggholder import Eggholder
from benchmarking.functions.goldstein_price import GoldsteinPrice
from benchmarking.functions.hartmann import Hartmann3D, Hartmann6D
from benchmarking.functions.himmelblau import Himmelblau
from benchmarking.functions.holder_table import HolderTable
from benchmarking.functions.matyas import Matyas
from benchmarking.functions.rosenbrock import Rosenbrock
from benchmarking.functions.schwefel import Schwefel
from benchmarking.functions.shekel import Shekel
from benchmarking.functions.shubert import Shubert
from benchmarking.functions.six_hump_camel import SixHumpCamel
from benchmarking.functions.sphere import Sphere
from benchmarking.functions.styblinski_tang import StyblinskiTang
from benchmarking.functions.three_hump_camel import ThreeHumpCamel


def evaluate(function_name: str, *args, **kwargs):  # pragma: no cover
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
        result = Beale()(*args, **kwargs)
    elif "booth" in function_name:
        result = Booth()(*args, **kwargs)
    elif "branin" in function_name:
        result = Branin()(*args, **kwargs)
    elif "bukin_n6" in function_name:
        result = BukinN6()(*args, **kwargs)
    elif "eggholder" in function_name:
        result = Eggholder()(*args, **kwargs)
    elif "goldstein_price" in function_name:
        result = GoldsteinPrice()(*args, **kwargs)
    elif "hartmann_3d" in function_name:
        result = Hartmann3D()(*args, **kwargs)
    elif "hartmann_6d" in function_name:
        result = Hartmann6D()(*args, **kwargs)
    elif "himmelblau" in function_name:
        result = Himmelblau()(*args, **kwargs)
    elif "holder_table" in function_name:
        result = HolderTable()(*args, **kwargs)
    elif "matyas" in function_name:
        result = Matyas()(*args, **kwargs)
    elif "rosenbrock" in function_name:
        result = Rosenbrock()(*args, **kwargs)
    elif "schwefel" in function_name:
        result = Schwefel()(*args, **kwargs)
    elif "shekel" in function_name:
        result = Shekel()(*args, **kwargs)
    elif "shubert" in function_name:
        result = Shubert()(*args, **kwargs)
    elif "six_hump_camel" in function_name:
        result = SixHumpCamel()(*args, **kwargs)
    elif "sphere" in function_name:
        result = Sphere()(*args, **kwargs)
    elif "styblinski_tang" in function_name:
        result = StyblinskiTang()(*args, **kwargs)
    elif "three_hump_camel" in function_name:
        result = ThreeHumpCamel()(*args, **kwargs)
    else:
        raise ValueError(
            "Invalid function name given: {}.".format(function_name)
        )

    return result
