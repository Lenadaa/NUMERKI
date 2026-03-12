import math

def derivative_type(type, coefficients, x):
    if type == 1:
        deriv = polynomial_derivative(coefficients)
        if not deriv:
            return 0.0
        return polynomial_horner(deriv, x)
    elif type == 2:
        return exponential_derivative(coefficients,x)
    elif type == 3:
        return trigonometric_derivative(coefficients[0],x)
    else:
        return None

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
        return 1 / (math.cos(x) * math.cos(x))
    else:
        raise TypeError("Funkcja trygonometryczna nie istnieje")

def validation_bisection(result_x0, result_a, a, b, x0):
    if result_x0 == 0:
        return x0, x0
    elif result_a * result_x0 < 0:
        return a, x0
    else:
        return x0, b

def function_type(type,coefficients,x):
    if type == 1:
        result = polynomial_horner(coefficients, x)
        return result
    elif type == 2:
        result = exponential(coefficients, x)
        return result
    elif type == 3:
        if isinstance(coefficients,list): #Tutaj to jest do sprawdzanie dlaczego tak działa
            trig_type = int(coefficients[0])
        else:
            trig_type = int(coefficients)
        result = trigonometric(trig_type, x)
        return result

def complexFunction(operations, x):
    result = x
    for f_type, coeffs in operations:
        result = function_type(f_type, coeffs, result)
    return result
def complexFunction_derivative(operations, x):
    total = 1.0
    values = [x]
    for f_type, coeffs in operations:
        x = function_type(f_type, coeffs, x)
        values.append(x)

    for i in range(len(operations)):
        f_type, coeffs = operations[i]
        point = values[i]
        derv = derivative_type(f_type, coeffs, point)

        total *= derv
    return total