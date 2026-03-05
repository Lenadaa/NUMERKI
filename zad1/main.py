def bisection_it():
    it = 31
    x1 = -2
    x2 = 2
    for x in range(it):
        resultx1 = 0.5*(x1*x1*x1)-3*(x1*x1)+5*x1+3
        resultx2 = 0.5*(x2*x2*x2)-3*(x2*x2)+5*x2+3
        if resultx1 * resultx2 >= 0:
            return 1
        x0 = (x1 + x2) / 2
        resultx0 = 0.5*(x0*x0*x0)-3*(x0*x0)+5*x0+3
        if (resultx0 == 0):
            return x0
        if (resultx1 * resultx0 < 0):
            x2 = x0
        else:
            x1 = x0
    return (x1+x2)/2
print(bisection_it())

def bisection_stop():
    x1 = -2
    x2 = 2
    eps = 0.000000001
    it = 0
    while True:
        it += 1
        resultx1 = 0.5 * (x1 * x1 * x1) - 3 * (x1 * x1) + 5 * x1 + 3
        resultx2 = 0.5 * (x2 * x2 * x2) - 3 * (x2 * x2) + 5 * x2 + 3
        if resultx1 * resultx2 >= 0:
            return 1

        x0 = (x1 + x2) / 2

        resultx0 = 0.5 * (x0 * x0 * x0) - 3 * (x0 * x0) + 5 * x0 + 3

        if abs(resultx0) < eps:
            return x0
        if resultx1 * resultx0 < 0:
            x2 = x0
        else:
            x1 = x0
print(bisection_stop())


