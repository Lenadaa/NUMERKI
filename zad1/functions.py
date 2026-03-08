import math

def polynomial(x):
    resultx = 0.5 * (x ** 3) - 3 * (x ** 2) + 5 * x + 3
    return resultx

def polynomialDeriv(x):
    a = 0.5
    b = -3
    c = 5
    resultx = 3 * a * (x ** 2) + 2 * b * (x ** 1) + c
    return resultx

def exponential(x):
    a = 5
    b = -0.5
    resultx = (a ** x) + b
    return resultx

def exponentialDeriv(x):
    a = 5
    result = (a**x) * math.log(a)
    return result

def trigonometric(x):
    return math.cos(x)

def trigometricDeriv(x):
    return -1 * math.sin(x)

def validationBisection(resultx0,resultx1,x1,x2,x0):
    if (resultx0 == 0):
        return x0, x0
    if (resultx1 * resultx0 < 0):
        return x1, x0
    else:
        return x0, x2
def functionType(type,x1,x2,deriv):
    if deriv == False:
        if type == 1:
            resultx1 = polynomial(x1)
            resultx2 = polynomial(x2)
            return resultx1, resultx2
        elif type == 2:
            resultx1 = exponential(x1)
            resultx2 = exponential(x2)
            return resultx1, resultx2
        elif type == 3:
            resultx1 = trigonometric(x1)
            resultx2 = trigonometric(x2)
            return resultx1, resultx2
    else:
        if type == 1:
            resultx1 = polynomialDeriv(x1)
            resultx2 = polynomialDeriv(x2)
            return resultx1, resultx2
        elif type == 2:
            resultx1 = exponentialDeriv(x1)
            resultx2 = exponentialDeriv(x2)
            return resultx1, resultx2
        elif type == 3:
            resultx1 = trigometricDeriv(x1)
            resultx2 = trigometricDeriv(x2)
            return resultx1, resultx2

