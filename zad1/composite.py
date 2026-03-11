from functions import polynomial_horner, exponential

def composite(number, x):
    if number == 1:
        coefficients = [2, -4]
        return polynomial_horner(coefficients, x)
    elif number == 2:
        coefficients = [1, 0, -9]
        return polynomial_horner(coefficients, x)
    elif number == 3:
        coefficients = [1, -1, -2, 0]
        return polynomial_horner(coefficients, x)
    elif number == 4:
        coefficients = [2, 1, -8]
        return exponential(coefficients, x)
    elif number == 5:
        coefficients = [3, 1, -1]
        return exponential(coefficients, x)
    elif number == 6:
        coefficients = [1 / 2, 1, -4]
        return exponential(coefficients, x)
    else:
        raise TypeError("Nie ma takiej funkcji")


