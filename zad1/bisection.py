from functions import validation_bisection, polynomial_horner, exponential, trigonometric

def bisection_it (a, b, type, coefficients, it):

    result_a, result_b, result_x0, x0  = 0, 0, 0, 0

    if type == 1:
        result_a = polynomial_horner(coefficients, a)
        result_b = polynomial_horner(coefficients, b)
    if type == 2:
        result_a = exponential(coefficients, a)
        result_b = exponential(coefficients, b)
    if type == 3:
        result_a = trigonometric(coefficients[0], a)
        result_b = trigonometric(coefficients[0], b)

    if result_a * result_b >= 0:
        raise TypeError("Funkcja w podanym przedziale nie zmienia znaku, miejsce zerowe nie istnieje")

    for x in range(it):

        x0 = (a + b) / 2

        if type == 1:
            result_x0 = polynomial_horner(coefficients, x0)
        if type == 2:
            result_x0 = exponential(coefficients, x0)
        if type == 3:
            result_x0 = trigonometric(coefficients[0], x0)

        a, b = validation_bisection(result_x0, result_a, a, b, x0)

    return x0, it

def bisection_stop (a, b, type, coefficients, eps):

    it = 0

    result_a, result_b, result_x0 = 0, 0, 0

    if type == 1:
        result_a = polynomial_horner(coefficients, a)
        result_b = polynomial_horner(coefficients, b)

    if type == 2:
        result_a = exponential(coefficients, a)
        result_b = exponential(coefficients, b)

    if type == 3:
        result_a = trigonometric(coefficients[0], a)
        result_b = trigonometric(coefficients[0], b)

    if result_a * result_b >= 0:
        raise TypeError("Funkcja w podanym przedziale nie zmienia znaku, miejsce zerowe nie istnieje")

    while True:

        it += 1

        x0 = (a + b) / 2

        if type == 1:
            result_x0 = polynomial_horner(coefficients, x0)
        if type == 2:
            result_x0 = exponential(coefficients, x0)
        if type == 3:
            result_x0 = trigonometric(coefficients[0], x0)

        if abs(result_x0) < eps:
            return x0, it

        if it > 300:
            print("Przekroczono liczbę iteracji")
            return x0, it

        a, b = validation_bisection(result_x0, result_a, a, b, x0)
