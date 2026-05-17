import math
from typing import Callable

# ========== WIELOMIAN ==========

def horner_scheme(x: float, coefficients: list[float]) -> float:
    result = coefficients[0]
    for coeff_index in range(1, len(coefficients)):
        result = result * x + coefficients[coeff_index]
    return result

def polynomial_function(coefficients: list[float]) -> Callable[[float], float]:
    def wrapper(x: float) -> float:
        return horner_scheme(x, coefficients)
    return wrapper


# ========== F. LINIOWA ==========

def linear(x: float, a: float, b: float) -> float:
    return a * x + b

def linear_function(a: float, b: float) -> Callable[[float], float]:
    def wrapper(x: float) -> float:
        return linear(x, a, b)
    return wrapper


# ========== MODUŁ ==========

def absolute_value(x: float) -> float:
    return abs(x)

def absolute_value_function() -> Callable[[float], float]:
    def wrapper(x: float) -> float:
        return absolute_value(x)
    return wrapper

# ========== F. TRYGONOMETRYCZNA ==========

def trigonometric(x: float, trig_type: str) -> float:
    if trig_type == "sin":
        return math.sin(x)
    elif trig_type == "cos":
        return math.cos(x)
    elif trig_type == "tan":
        return math.tan(x)
    else:
        raise ValueError(f"Nieznana funkcja trigonometryczna: {trig_type}")

def trigonometric_function(trig_type: str) -> Callable[[float], float]:
    def wrapper(x: float) -> float:
        return trigonometric(x, trig_type)
    return wrapper


# ========== ZŁOŻENIA ==========

def composition(x: float, functions_list: list[Callable[[float], float]]) -> float:
    current_value = x
    for function in functions_list:
        current_value = function(current_value)
    return current_value

def composition_function(functions_list: list[Callable[[float], float]]) -> Callable[[float], float]:
    def wrapper(x: float) -> float:
        return composition(x, functions_list)
    return wrapper