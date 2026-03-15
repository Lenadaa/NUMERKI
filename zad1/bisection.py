from functions import validation_bisection, polynomial_horner, exponential, trigonometric,complexFunction,function_type

def bisection(a,b,type,coeff,stopType,stopAccuracy):
    result_a = function_type(type,coeff,a)
    result_b = function_type(type,coeff,b)

    if result_a * result_b >= 0:
        print("(METODA BISEKCJI) Funkcja w podanym przedziale nie zmienia znaku, miejsce zerowe nie istnieje")
        return None, None
    #stopType = 1 - iteracja
    if stopType == 1:
        it = int(stopAccuracy)
        for x in range(it):
            x0 = (a + b) / 2
            result_x0 = function_type(type, coeff, x0)
            a, b = validation_bisection(result_x0, result_a, a, b, x0)
        return x0, it
    #stopType = 1 - dokładność
    elif stopType == 2:
        it = 0
        while True:
            it += 1
            x0 = (a + b) / 2
            result_x0 = function_type(type, coeff, x0)
            if abs(result_x0) < stopAccuracy:
                return x0, it
            if it > 300:
                print("Przekroczono liczbę iteracji")
                return x0, it
            a, b = validation_bisection(result_x0, result_a, a, b, x0)

