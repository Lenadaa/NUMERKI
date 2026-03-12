from functions import polynomial_derivative, polynomial_horner, exponential, exponential_derivative, trigonometric, trigonometric_derivative,complexFunction,complexFunction_derivative
def secant_it(a, b, type, coefficients, it):
    result_derivative_a, result_derivative_b, result_a, result_b = 0, 0, 0, 0

    if type == 1:
        result_a = polynomial_horner(coefficients, a)
        result_b = polynomial_horner(coefficients, b)

        derivative_coefficients = polynomial_derivative(coefficients)
        result_derivative_a = polynomial_horner(derivative_coefficients, a)
        result_derivative_b = polynomial_horner(derivative_coefficients, b)

    if type == 2:
        result_a = exponential(coefficients, a)
        result_b = exponential(coefficients, b)

        result_derivative_a = exponential_derivative(coefficients, a)
        result_derivative_b = exponential_derivative(coefficients, b)

    if type == 3:
        result_a = trigonometric(coefficients[0], a)
        result_b = trigonometric(coefficients[0], b)

        result_derivative_a = trigonometric_derivative(coefficients[0], a)
        result_derivative_b = trigonometric_derivative(coefficients[0], b)
    if type == 4:
        result_a = complexFunction(coefficients, a)
        result_b = complexFunction(coefficients, b)

        result_derivative_a = complexFunction_derivative(coefficients, a)
        result_derivative_b = complexFunction_derivative(coefficients, b)

    if result_derivative_a == 0 or result_derivative_b == 0:
        raise TypeError("Pochodna równa zero, miejsce zerowe nie istnieje")

    if result_a * result_b >= 0:
        raise TypeError("Funkcja w podanym przedziale nie zmienia znaku, miejsce zerowe nie istnieje")

    for x in range(it):

        if type == 1:
            result_a = polynomial_horner(coefficients, a)
            result_b = polynomial_horner(coefficients, b)

        if type == 2:
            result_a = exponential(coefficients, a)
            result_b = exponential(coefficients, b)

        if type == 3:
            result_a = trigonometric(coefficients[0], a)
            result_b = trigonometric(coefficients[0], b)
        if type == 4:
            result_a = complexFunction(coefficients, a)
            result_b = complexFunction(coefficients, b)
        if result_a - result_b == 0:
            return a, it

        x = result_b * (b - a)
        y = result_b - result_a
        c = b - x / y
        a = b
        b = c

    return b, it

def secant_stop(a, b, type, coefficients, eps):

    it = 0

    if type == 1:
        result_a = polynomial_horner(coefficients, a)
        result_b = polynomial_horner(coefficients, b)

        derivative_coefficients = polynomial_derivative(coefficients)
        result_derivative_a = polynomial_horner(derivative_coefficients, a)
        result_derivative_b = polynomial_horner(derivative_coefficients, b)

    if type == 2:
        result_a = exponential(coefficients, a)
        result_b = exponential(coefficients, b)

        result_derivative_a = exponential_derivative(coefficients, a)
        result_derivative_b = exponential_derivative(coefficients, b)

    if type == 3:
        result_a = trigonometric(coefficients[0], a)
        result_b = trigonometric(coefficients[0], b)

        result_derivative_a = trigonometric_derivative(coefficients[0], a)
        result_derivative_b = trigonometric_derivative(coefficients[0], b)
    if type == 4:
        result_a = complexFunction(coefficients, a)
        result_b = complexFunction(coefficients, b)

        result_derivative_a = complexFunction_derivative(coefficients, a)
        result_derivative_b = complexFunction_derivative(coefficients, b)
    if result_derivative_a == 0 or result_derivative_b == 0:
        raise TypeError("Pochodna równa zero, miejsce zerowe nie istnieje")

    if result_a * result_b >= 0:
        raise TypeError("Funkcja w podanym przedziale nie zmienia znaku, miejsce zerowe nie istnieje")

    while True:

        it += 1

        if type == 1:
            result_a = polynomial_horner(coefficients, a)
            result_b = polynomial_horner(coefficients, b)

        if type == 2:
            result_a = exponential(coefficients, a)
            result_b = exponential(coefficients, b)

        if type == 3:
            result_a = trigonometric(coefficients[0], a)
            result_b = trigonometric(coefficients[0], b)
        if type == 4:
            result_a = complexFunction(coefficients, a)
            result_b = complexFunction(coefficients, b)
        if result_a - result_b == 0:
            return a, it

        x = result_b * (b - a)
        y = result_b - result_a
        c = b - x / y
        a = b
        b = c

        if abs(result_b) < eps:
            return b, it

        if it > 300:
            print("Przekroczono liczbę iteracji")
            return b, it