import math

def horner_scheme(x: float, coefficients: list[float]) -> float:
    result = coefficients[0]

    for coeff_index in range(1, len(coefficients)):
        result = result * x + coefficients[coeff_index]

    return result

def polynomial_function(x: float, coefficients: list[float]) -> float:
    return horner_scheme(x, coefficients)

def linear_function(x: float, a: float, b: float) -> float:
    return a * x + b

def absolute_value_function(x: float) -> float:
    return abs(x)

def trigonometric_function(x: float, trig_type: str) -> float:
    if trig_type == "sin":
        return math.sin(x)
    elif trig_type == "cos":
        return math.cos(x)
    elif trig_type == "tan":
        return math.tan(x)
    else:
        raise ValueError(f"Nieznana funkcja trigonometryczna: {trig_type}")

def composition_function(x, list):
    current_value = x
    for function in list:
        current_value = function(current_value)
    return current_value