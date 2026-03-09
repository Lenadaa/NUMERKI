import functions

def secant_it(it, type, x0, x1):

    derivedx0, derivedx1 = functions.functionType(type, x0, x1, True)
    resultx0, resultx1 = functions.functionType(type, x0, x1, False)

    if (derivedx0 == 0 or derivedx1 == 0):
        return None, None
    if resultx0 * resultx1 >= 0:
        return None, None

    for x in range(it):
        resultx0, resultx1 = functions.functionType(type, x0, x1, False)
        if (resultx0 - resultx1) == 0:
            return x1,it
        a = resultx1 * (x1 - x0)
        b = resultx1 - resultx0
        x2 = x1 - a / b
        x0 = x1
        x1 = x2
    return x1,it

def secant_stop(eps, type, x0, x1):
    it = 0

    derivedx0, derivedx1 = functions.functionType(type, x0, x1, True)
    resultx0, resultx1 = functions.functionType(type, x0, x1, False)

    if (derivedx0 == 0 or derivedx1 == 0):
        return None, None
    if resultx0 * resultx1 >= 0:
        return None, None

    while True:
        it += 1
        resultx0, resultx1 = functions.functionType(type, x0, x1, False)
        if (resultx0 - resultx1) == 0:
            return x1,it

        a = resultx1*(x1-x0)
        b = resultx1-resultx0

        x2 = x1 - a/b
        x0 = x1
        x1 = x2

        if abs(resultx1) < eps:
            return x1,it
        if it > 300:
            print("Przekroczono liczbe iteracji")
            return x1,it
