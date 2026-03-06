def validationBisection(resultx0,resultx1,x1,x2,x0):
    if (resultx0 == 0):
        return x0, x0
    if (resultx1 * resultx0 < 0):
        return x1, x0
    else:
        return x0, x2
def polynomial(a,b,c,d,x):
    resultx = a * (x * x * x) + b * (x * x) + c * x + d
    return resultx

def bisection_it(it, type,x1,x2):
    a = 0.5
    b = -3
    c = 5
    d = 3
    for x in range(it):
        resultx0,resultx1,resultx2 = 0,0,0
        if (type == 1):
            resultx1 = polynomial(a,b,c,d,x1)
            resultx2 = polynomial(a,b,c,d,x2)
        if resultx1 * resultx2 >= 0:
            return 1
        x0 = (x1 + x2) / 2
        if (type == 1):
            resultx0 = polynomial(a,b,c,d,x0)
        x1,x2 = validationBisection(resultx0,resultx1,x1,x2,x0)
    return (x1 + x2)/2

def bisection_stop(eps,type,x1,x2):
    a = 0.5
    b = -3
    c = 5
    d = 3
    resultx0, resultx1, resultx2 = 0, 0, 0
    while True:
        if (type == 1):
            resultx1 = polynomial(a,b,c,d,x1)
            resultx2 = polynomial(a,b,c,d,x2)
        if resultx1 * resultx2 >= 0:
            return 1
        x0 = (x1 + x2) / 2
        if (type == 1):
            resultx0 = polynomial(a,b,c,d,x0)
        x1, x2 = validationBisection(resultx0,resultx1,x1,x2,x0)
        if abs(resultx0) < eps:
            return x0