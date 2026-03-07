import functions

def bisection_it(it, type,x1,x2):

    for x in range(it):
        resultx0, resultx1, resultx2 = 0, 0, 0
        if type == 1:
            resultx1 = functions.polynomial(x1)
            resultx2 = functions.polynomial(x2)
        elif type == 2:
            resultx1 = functions.exponential(x1)
            resultx2 = functions.exponential(x2)
        elif type == 3:
            resultx1 = functions.trigonometric(x1)
            resultx2 = functions.trigonometric(x2)

        if (resultx0 - resultx1) == 0:
            return x1

        if resultx1 * resultx2 > 0:
            print("nie istnieje")
            return 1

        x0 = (x1 + x2) / 2

        if type == 1:
            resultx0 = functions.polynomial(x0)
        elif type == 2:
            resultx0 = functions.exponential(x0)
        elif type == 3:
            resultx0 = functions.trigonometric(x0)
        x1,x2 = functions.validationBisection(resultx0,resultx1,x1,x2,x0)
    return (x1 + x2)/2

def bisection_stop(eps,type,x1,x2):
    resultx0, resultx1, resultx2 = 0, 0, 0
    it = 0
    while True:
        it += 1
        if type == 1:
            resultx1 = functions.polynomial(x1)
            resultx2 = functions.polynomial(x2)
        elif type == 2:
            resultx1 = functions.exponential(x1)
            resultx2 = functions.exponential(x2)
        elif type == 3:
            resultx1 = functions.trigonometric(x1)
            resultx2 = functions.trigonometric(x2)
        if resultx1 * resultx2 >= 0:
            print("nie istnieje")
            return 1
        x0 = (x1 + x2) / 2
        if type == 1:
            resultx0 = functions.polynomial(x0)
        elif type == 2:
            resultx0 = functions.exponential(x0)
        elif type == 3:
            resultx0 = functions.trigonometric(x0)
        x1,x2 = functions.validationBisection(resultx0,resultx1,x1,x2,x0)

        if abs(resultx0) < eps:
            return x0,it
        if it > 300:
            print("Przekroczono liczbe iteracji")
            return x1,it