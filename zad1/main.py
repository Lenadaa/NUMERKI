def bisection_it():
    it = 31
    x1 = -2
    x2 = 2
    a = 0.5
    b = -3
    c = 5
    d = 3
    for x in range(it):
        resultx1 = a * (x1 * x1 * x1) + b * (x1 * x1) + c * x1 + d
        resultx2 = a * (x2 * x2 * x2) + b * (x2 * x2) + c * x2 + d
        if resultx1 * resultx2 >= 0:
            return 1
        x0 = (x1 + x2) / 2
        resultx0 = a * (x0 * x0 * x0) + b * (x0 * x0) + c * x0 + d
        if (resultx0 == 0):
            return x0
        if (resultx1 * resultx0 < 0):
            x2 = x0
        else:
            x1 = x0
    return (x1 + x2)/2
print(bisection_it())

def bisection_stop():
    x1 = -2
    x2 = 2
    a = 0.5
    b = -3
    c = 5
    d = 3
    eps = 0.000000001
    while True:
        resultx1 = a * (x1 * x1 * x1) + b * (x1 * x1) + c * x1 + d
        resultx2 = a * (x2 * x2 * x2) + b * (x2 * x2) + c * x2 + d
        if resultx1 * resultx2 >= 0:
            return 1

        x0 = (x1 + x2) / 2

        resultx0 = a * (x0 * x0 * x0) + b * (x0 * x0) + c * x0 + d

        if abs(resultx0) < eps:
            return x0
        if resultx1 * resultx0 < 0:
            x2 = x0
        else:
            x1 = x0
print(bisection_stop())


