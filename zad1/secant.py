from functions import polynomial_derivative, polynomial_horner, exponential, exponential_derivative, trigonometric, trigonometric_derivative,complexFunction,complexFunction_derivative,function_type,derivative_type
def secant(a,b,type,coefficients,typeStop,stopAccuracy):
    result_derivative_a = derivative_type(type,coefficients,a)
    result_derivative_b = derivative_type(type,coefficients,b)

    if result_derivative_a == 0 or result_derivative_b == 0:
        print("(METODA SIECZNYCH) Pochodna równa zero")
        return None, None

    #typeStop = 1 - iteracja
    if typeStop == 1:
        it = int(stopAccuracy)
        for i in range(it):
            result_a = function_type(type, coefficients, a)
            result_b = function_type(type, coefficients, b)

            if result_a - result_b == 0:
                return a, it

            x = result_b * (b - a)
            y = result_b - result_a
            c = b - x / y
            a = b
            b = c

        return b, it
    #typeStop = 2 - dokładność wyniku
    elif typeStop == 2:
        it = 0
        while True:
            it += 1
            result_a = function_type(type, coefficients, a)
            result_b = function_type(type, coefficients, b)

            if result_a - result_b == 0:
                return a, it

            x = result_b * (b - a)
            y = result_b - result_a
            c = b - x / y
            a = b
            b = c

            if abs(result_b) < stopAccuracy:
                return b, it

            if it > 300:
                print("Przekroczono liczbę iteracji")
                return b, it