from typing import Callable
from numpy.polynomial.legendre import leggauss

def gauss_legendre_integral(function_to_integrate: Callable[[float], float], start: float, end: float, nodes_count: int) -> float:
    nodes, weights = leggauss(nodes_count)
    total_sum = 0.0

    for i in range(nodes_count):
        current_node = nodes[i]
        current_weight = weights[i]

        transformed = 0.5 * ((end - start) * current_node + start + end)

        total_sum += current_weight * function_to_integrate(float(transformed))

    result = 0.5 * (end - start) * total_sum

    return float(result)