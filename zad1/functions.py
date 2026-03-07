import math

def polynomial(x):
    a = 0.5
    b = -3
    c = 5
    d = 3
    resultx = a * (x ** 3) + b * (x ** 2) + c * x + d
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