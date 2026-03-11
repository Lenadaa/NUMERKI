import math

def polynomial_horner(coefficients, x):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result = result * x + coefficients[i]
    return result

def polynomial_derivative(coefficients):
    amount = len(coefficients)
    it = 0
    derivative_coefficients = []
    while amount > 1:
        amount -= 1
        derivative_coefficients.append(coefficients[it] * amount)
        it += 1
    return derivative_coefficients

def exponential(coefficients, x):
    a = coefficients[0]
    c = coefficients[1]
    d = coefficients[2]
    result = a ** x * c + d
    return result

def exponential_derivative(coefficients, x):
    a = coefficients[0]
    c = coefficients[1]
    result = (a ** x) * c * math.log(a)
    return result

def trigonometric(trig_type, x):
    if trig_type == 1:
        return math.sin(x)
    elif trig_type == 2:
        return math.cos(x)
    elif trig_type == 3:
        return math.tan(x)
    else:
        raise TypeError("Funkcja trygonometryczna nie istnieje")

def trigonometric_derivative(trig_type, x):
    if trig_type == 1:
        return math.cos(x)
    elif trig_type == 2:
        return -1 * math.sin(x)
    elif trig_type == 3:
        return math.cos(x) * math.cos(x)
    else:
        raise TypeError("Funkcja trygonometryczna nie istnieje")

def validation_bisection(result_x0, result_a, a, b, x0):
    if result_x0 == 0:
        return x0, x0
    elif result_a * result_x0 < 0:
        return a, x0
    else:
        return x0, b

def polynomial(coefficient, x):
    result = coefficient[0]
    for i in range(1, len(coefficient)):
        result = result * x + coefficient[i]
    return result
