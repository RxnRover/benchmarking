from typing import Any, Dict

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


def function_data(function_name: str) -> Dict[str, Any]:  # pragma: no cover
    """Helper function to retrieve function metadata based on function name.

    :param function_name: Name of the function to use. This must exactly match
                          the actual function name.
    :type function_name: str

    :raises ValueError: Invalid function name was provided.

    :returns:
    :rtype: Dict[str, Any]
    """

    if "beale" in function_name:
        result = Beale().metadata
    elif "booth" in function_name:
        result = Booth().metadata
    elif "branin" in function_name:
        result = Branin().metadata
    elif "bukin_n6" in function_name:
        result = BukinN6().metadata
    elif "eggholder" in function_name:
        result = Eggholder().metadata
    elif "goldstein_price" in function_name:
        result = GoldsteinPrice().metadata
    elif "hartmann_3d" in function_name:
        result = Hartmann3D().metadata
    elif "hartmann_6d" in function_name:
        result = Hartmann6D().metadata
    elif "himmelblau" in function_name:
        result = Himmelblau().metadata
    elif "holder_table" in function_name:
        result = HolderTable().metadata
    elif "matyas" in function_name:
        result = Matyas().metadata
    elif "rosenbrock" in function_name:
        result = Rosenbrock().metadata
    elif "schwefel" in function_name:
        result = Schwefel().metadata
    elif "shekel" in function_name:
        result = Shekel().metadata
    elif "shubert" in function_name:
        result = Shubert().metadata
    elif "six_hump_camel" in function_name:
        result = SixHumpCamel().metadata
    elif "sphere" in function_name:
        result = Sphere().metadata
    elif "styblinski_tang" in function_name:
        result = StyblinskiTang().metadata
    elif "three_hump_camel" in function_name:
        result = ThreeHumpCamel().metadata
    else:
        raise ValueError(
            "Invalid function name given: {}.".format(function_name)
        )

    return result
