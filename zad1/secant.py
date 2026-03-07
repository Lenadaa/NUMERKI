import functions

def secant_it(it, type, x0, x1):
    for x in range(it):
        resultx0, resultx1, resultx2 = 0, 0, 0
        derivedx0,derivedx1 = 0, 0

        if type == 1:
            resultx0 = functions.polynomial(x0)
            resultx1 = functions.polynomial(x1)
            derivedx0 = float(functions.polynomialDeriv(x0))
            derivedx1 = float(functions.polynomialDeriv(x1))
        elif type == 2:
            resultx0 = functions.exponential(x0)
            resultx1 = functions.exponential(x1)
            derivedx0 = float(functions.exponentialDeriv(x0))
            derivedx1 = float(functions.exponentialDeriv(x1))
        elif type == 3:
            resultx0 = functions.trigonometric(x0)
            resultx1 = functions.trigonometric(x1)
            derivedx0 = float(functions.trigometricDeriv(x0))
            derivedx1 = float(functions.trigometricDeriv(x1))
        if (resultx0 - resultx1) == 0:
            return x1

        if(derivedx0 == 0.0 or derivedx1 == 0.0):
            print("nie istnieje")
            return 1

        a = resultx1 * (x1 - x0)
        b = resultx1 - resultx0
        x2 = x1 - a / b
        x0 = x1
        x1 = x2

    return x1
def secant_stop(eps, type, x0, x1):
    it = 0
    while True:
        it +=1
        resultx0, resultx1, resultx2 = 0, 0, 0
        derivedx0,derivedx1 = 0, 0

        if type == 1:
            resultx0 = functions.polynomial(x0)
            resultx1 = functions.polynomial(x1)
            derivedx0 = float(functions.polynomialDeriv(x0))
            derivedx1 = float(functions.polynomialDeriv(x1))
        elif type == 2:
            resultx0 = functions.exponential(x0)
            resultx1 = functions.exponential(x1)
            derivedx0 = float(functions.exponentialDeriv(x0))
            derivedx1 = float(functions.exponentialDeriv(x1))
        elif type == 3:
            resultx0 = functions.trigonometric(x0)
            resultx1 = functions.trigonometric(x1)
            derivedx0 = float(functions.trigometricDeriv(x0))
            derivedx1 = float(functions.trigometricDeriv(x1))

        if (resultx0 - resultx1) == 0:
            return x1,it

        if (derivedx0 == 0.0 or derivedx1 == 0.0):
            print("nie istnieje")
            return 1

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

print(secant_it(60,1,-1,1))
print(secant_stop(0.000000000001,1,-1,1))