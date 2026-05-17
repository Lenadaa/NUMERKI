from typing import Callable

def simpson_integral_n_subintervals(function_to_integrate: Callable[[float], float], start: float, end: float, n: int) -> float:
    step = (end - start) / n
    total_sum = function_to_integrate(start) + function_to_integrate(end)

    for node in range(1, n):
        current_node = start + step * node
        is_node_even = node % 2 == 0

        if is_node_even:
            total_sum += 2 * function_to_integrate(current_node)
        else:
            total_sum += 4 * function_to_integrate(current_node)

    result = (step / 3) * total_sum

    return result

def simpson_integral(function_to_integrate: Callable[[float], float], start: float, end: float, epsilon: float) -> tuple[float, int, int, int]:
    current_subintervals = 2
    iterations = 1

    evaluated_nodes_cache = {}

    def cached_function_to_integrate(x: float) -> float:
        rounded_x = round(x, 10)

        if rounded_x not in evaluated_nodes_cache:
            evaluated_nodes_cache[rounded_x] = function_to_integrate(x)
        return evaluated_nodes_cache[rounded_x]

    previous_integral_value = simpson_integral_n_subintervals(cached_function_to_integrate, start, end, current_subintervals)

    while True:
        current_subintervals *= 2
        iterations += 1
        current_integral_value = simpson_integral_n_subintervals(cached_function_to_integrate, start, end, current_subintervals)

        if abs(current_integral_value - previous_integral_value) < epsilon:
            total_evaluations = len(evaluated_nodes_cache)
            return current_integral_value, iterations, current_subintervals, total_evaluations

        previous_integral_value = current_integral_value