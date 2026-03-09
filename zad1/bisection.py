import functions

def bisection_it(it, type, x1, x2):

    resultx1, resultx2 = functions.functionType(type, x1, x2,False)

    if resultx1 * resultx2 >= 0:
        return None,None

    for x in range(it):

        x0 = (x1 + x2) / 2

        if type == 1:
            resultx0 = functions.polynomial(x0)
        elif type == 2:
            resultx0 = functions.exponential(x0)
        elif type == 3:
            resultx0 = functions.trigonometric(x0)
        elif type == 4:
            resultx0 = functions.complex_exp_in_poly(x0)
        elif type == 5:
            resultx0 = functions.complex_poly_in_tryg(x0)

        x1,x2 = functions.validationBisection(resultx0,resultx1,x1,x2,x0)

    return (x1 + x2)/2,it
def bisection_stop(eps,type,x1,x2):
    it = 0
    resultx1, resultx2 = functions.functionType(type, x1, x2, False)

    if resultx1 * resultx2 >= 0:
        return None,it

    while True:
        it += 1
        x0 = (x1 + x2) / 2
        if type == 1:
            resultx0 = functions.polynomial(x0)
        elif type == 2:
            resultx0 = functions.exponential(x0)
        elif type == 3:
            resultx0 = functions.trigonometric(x0)
        elif type == 4:
            resultx0 = functions.complex_exp_in_poly(x0)
        elif type == 5:
            resultx0 = functions.complex_poly_in_tryg(x0)

        if abs(resultx0) < eps:
            return x0,it
        if it > 300:
            print("Przekroczono liczbe iteracji")
            return x0,it
        x1,x2 = functions.validationBisection(resultx0,resultx1,x1,x2,x0)
